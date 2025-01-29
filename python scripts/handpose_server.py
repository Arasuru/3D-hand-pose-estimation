import socket
import time

HOST = "localhost"
PORT = 44444
clients = []
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(2)

    print("Waiting for connections...")
    for i in range(2):
        conn, addr = s.accept()
        clients.append(conn)
        print(f"Connected to client {i+1}: {addr}")

    print("Both clients connected. Ready to send commands...")

    try:
        while True:
            key = input().strip().lower()
            
            if key == 'r':
                message = b"START"
            elif key == 'q':
                message = b"STOP"
            else:
                print("Unknown command. Use 'r' to start, 'q' to stop")
                continue
            # Send message to all connected clients
            disconnected_clients = []
            for i, conn in enumerate(clients):
                try:
                    conn.sendall(message)
                    print(f"Sent {message.decode()} signal to client {i+1}")
                except (ConnectionResetError, BrokenPipeError):
                    print(f"Client {i+1} disconnected")
                    disconnected_clients.append(conn)
            # Remove disconnected clients
            for conn in disconnected_clients:
                clients.remove(conn)
            
            # Exit loop if quit command sent
            if key == 'q':
                break
            
    finally:
        # Clean up all connections
        for conn in clients:
            conn.close()        
    