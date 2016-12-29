import os

def execcmd():
    cmd = "/usr/bin/python /usr/local/NAS/misc/Cmd/NASCmd.py"
    cmd += " -f /usr/local/NAS/misc/Cmd/Script/ldapserver.txt > /tmp/ldapserver.cli.log"
    os.system(cmd)

def verify():
    with open("/tmp/ldapserver.cli.log", "r") as fr:
        lines = [ line.strip() for line in fr.readlines() if line.strip() != ""]
        for i in range(len(lines)):
            line = lines[i].strip()
            if "Failed" in line:
                return (False, lines[i-1] + "\n" + line)
    return (True,"")
