import socket

# Konfigurasi Server
IP = "127.0.0.1"
PORT = 12000

# Membuat socket UDP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((IP, PORT))

print(f"Server UDP berjalan di {IP}:{PORT}...")

while True:
    # Menerima pesan dan alamat client
    message, address = server_socket.recvfrom(1024)
    
    # Simulasikan server memproses (mengirim balik data yang sama)
    # Di Opsi B, server membalas sequence number dan timestamp
    server_socket.sendto(message, address)
    print(f"Membalas paket dari {address} dengan pesan {message}")