import os
import sys
import json
import ftplib

from io import StringIO
from io import BytesIO

from settings import *
from serverfunctions import *


user_running = os.getenv("USER")

def __get_exec__(commands):
    """ Execute a command, trick Python into writing to our stream instead of STDOUT, and return the contents of our stream """
    stdout_stream = sys.stdout
    string_stream = StringIO()
    
    try:
        sys.stdout = string_stream
        exec(commands) # Execute any function that might print to STDOUT/STDERR.

    except Exception as error:
        print(str(error)) # Print to our StringIO
    
    finally:
        sys.stdout = stdout_stream
        return string_stream.getvalue()




def __cleanup__(ftp_pointer):
    if (execution_filename in ftp_pointer.nlst()):
        ftp_pointer.delete(execution_filename)

def main():
    try:
        # Sign in
        ftp_handle = ftplib.FTP(ftp_details["host"])
        print("Connecting to host...")
        
        
        # Log in
        ftp_handle.login(user = ftp_details["username"], passwd = ftp_details["password"])
        print("Logging in...")

        ftp_handle.cwd(default_control_directory)

        if (user_running not in ftp_handle.nlst()): # Check if user folder exists
            ftp_handle.mkd(user_running) # Make the user directory
        
        ftp_handle.cwd(user_running) # Change the current working directory to the relative directory: /htdocs/{control_directory}/{username}

        # __cleanup__(ftp_handle)

        while (True):
            try:
                if (execution_filename not in ftp_handle.nlst()): # Continue when the file is not sent there by the client.
                    continue
                
                execution_file_buffer = BytesIO()

                ftp_handle.retrbinary("RETR {file}".format(file = execution_filename), execution_file_buffer.write)

                execution_file_str_contents = execution_file_buffer.getvalue().decode().replace("\n", "")
                
                # print(execution_file_str_contents)

                execution = __get_exec__(execution_file_str_contents)

                print(execution)

                execution_returned_buffer = BytesIO(str.encode(execution))

                ftp_handle.storbinary("STOR {file}".format(file = output_filename), execution_returned_buffer)


            except Exception as error:
                print("{error}".format(error = error))
                print("Error in loop. Ignoring; it is most likely a client-related error...")

            finally:
                __cleanup__(ftp_handle) # File was most likely not deleted; fixing a shit ton of errors!

    
    except Exception as error:
        print("{error}".format(error = error))
        print("Exception in (parent) main. Rebooting...")
        main()


    

    print("DONE!")


if (__name__ == "__main__"):
    main()