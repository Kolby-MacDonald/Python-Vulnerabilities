# Vulnerable-Server

Python is not as secure as some may think,
The pickle modules demonstrates one of pythons biggest security flaws, remote code execution against unsuspecting servers. It is unfortunate the pickle module is promoted as a common pythonic way to serialize data. I built this client and server as a demonstration of a programming mistake that could be fatal to a system.

For example running pickle.loads() on a web application could result in complete remote control or malicious code exection on unsuspecting systems. To remediate this issue use JSON to serialize data.
-----------------------------------------------------------------------------------------------------------------

Examples to use from client.py against vulnerable-server.py:

- Start vulnerable-server.py and then two or more client.py files.

TBC - Examples of stack code examples will be given here.

-----------------------------------------------------------------------------------------------------------------
