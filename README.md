## RemotePythonClient
# *I can not stress this enough: only use this for educational purposes!*

A very simple server (or, *stub* as l33t-hax0rs say nowadays) to act as a daemon of some sorts on a (consented) computer. It will receive commands from the client, and it will execute those commands as pure Python code. Hence, there are some functions that the client can call, and those are dependent on the usage of this software, whether for educational purposes, or for malicious ones.

Simply enter the FTP details into *settings.py* and (somehow?) get it running on the host PC. Create a directory on the root of your FTP server called 'control'. 

If used correctly, it will be able to receive commands from whomever is controlling it, anonymously (legitimately advantageous over the traditional method). The only IP address the server will ever know is the general IP address of the server, therefore ensuring anonymonity--until the FTP server leaks the IP addresses whom are doing such shady behavior, but whatever.

