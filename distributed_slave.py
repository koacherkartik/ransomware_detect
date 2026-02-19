import socket
import hashlib

def crack_hash(target_hash, wordlist):
    for word in wordlist:
        if hashlib.md5(word.encode()).hexdigest() == target_hash:
            return word
    return None

def start_slave(master_ip, port=9000):
    s = socket.socket()
    s.connect((master_ip, port))
    print("[*] Connected to master")

if __name__ == "__main__":
    start_slave("127.0.0.1")
