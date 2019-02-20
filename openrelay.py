import socket
import smtplib

# source: https://github.com/tango-j/SMTP-Open-Relay-Attack-Test-Tool

fh = open("input.txt","r")
targets = fh.readlines()
targets = [x.strip() for x in targets]
fh.close()

for target in targets:
    parts = target.split(" ")
    IP = parts[0]
    Port = parts[1]
    try:
        s = socket.socket()
        s.connect((IP, int(Port)))
        socket.setdefaulttimeout(5)
        ans = s.recv(1024).decode("utf8")
        if ("220" in ans):
            print("\n[+] Connected to "+ IP + " " + str(Port)+"\n")
            smtpserver = smtplib.SMTP(IP, int(Port))
            r = smtpserver.docmd("Mail From:", "zeeshan.akram@ebryx.com")
            a = str(r)
            if ("250" in a):
                r = smtpserver.docmd("RCPT TO:", "zeeshan.akram@ebryx.com")
                a = str(r)
                if ("250" in a):
                    print("[+] Target is vulnerable")

                else:
                    print("[-] Target is not vulnerable ")

        s.close()
    except:
        print("[-] Exception...")
        pass