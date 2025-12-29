import socket
import time
import random

# Konfigurasi Client
SERVER_IP = "127.0.0.1"
SERVER_PORT = 12000
N = 10  # Jumlah paket yang dikirim (minimal 10)
TIMEOUT = 1.0 # Detik

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client_socket.settimeout(TIMEOUT)

rtt_list = []
packets_received = 0

print(f"Memulai UDP Ping ke {SERVER_IP} sebanyak {N} kali...\n")

for i in range(1, N + 1):
    start_time = time.time()
    # Format pesan: Sequence_Number | Timestamp
    message = f"{i}|{start_time}".encode()
    # message = f"{i} | {random.randint(1, 1000)}".encode()
    
    try:
        client_socket.sendto(message, (SERVER_IP, SERVER_PORT))
        
        # Menerima balasan
        data, server = client_socket.recvfrom(1024)
        end_time = time.time()
        
        # Hitung RTT dalam milidetik
        rtt = (end_time - start_time) * 1000
        rtt_list.append(rtt)
        packets_received += 1
        
        print(f"Reply dari {SERVER_IP}: seq={i} rtt={rtt:.2f} ms")
        
    except socket.timeout:
        print(f"Request seq={i}: Timed out (Paket Hilang)")

# --- Perhitungan Statistik ---
print("\n--- Statistik Ping ---")
packet_loss = ((N - packets_received) / N) * 100

if rtt_list:
    min_rtt = min(rtt_list)
    max_rtt = max(rtt_list)
    avg_rtt = sum(rtt_list) / len(rtt_list)
else:
    min_rtt = max_rtt = avg_rtt = 0

print(f"Paket: Terkirim = {N}, Diterima = {packets_received}, Loss = {packet_loss}%")
print(f"RTT: Min = {min_rtt:.2f}ms, Max = {max_rtt:.2f}ms, Rerata = {avg_rtt:.2f}ms")

client_socket.close()