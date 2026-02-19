import socket
import threading

clients = []

def handle_slave(conn, addr):
    print(f"[+] Slave connected: {addr}")
    clients.append(conn)

def start_master(host="0.0.0.0", port=9000):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(5)

    print("[*] Master running...")
    while True:
        conn, addr = server.accept()
        threading.Thread(target=handle_slave, args=(conn, addr)).start()

if __name__ == "__main__":
    start_master()
