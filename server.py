import socket
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

def start_secure_server():
    # A pre-shared 256-bit key (32 bytes) used for decryption
    # In practice, this would be securely exchanged using Diffie-Hellman
    key = b"sixteen_byte_key_sixteen_byte_ky" 
    aesgcm = AESGCM(key)
    
    # Set up a standard TCP network socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('127.0.0.1', 65432)) # Local host loopback address
    server_socket.listen(1)
    print("Server is listening on port 65432 for encrypted packets...")
    
    conn, addr = server_socket.accept()
    print(f"Connected securely to client at: {addr}")
    
    try:
        # Receive the initialization vector (nonce) - first 12 bytes
        nonce = conn.recv(12)
        # Receive the actual encrypted packet payload
        ciphertext = conn.recv(1024)
        
        print(f"\n📡 Intercepted Raw Network Bytes: {ciphertext.hex()}")
        
        # Decrypt and verify the integrity of the payload using AES-GCM
        decrypted_message = aesgcm.decrypt(nonce, ciphertext, None)
        print(f"🔑 Decrypted Plaintext Message: {decrypted_message.decode('utf-8')}")
        
    except Exception as e:
        print(f"Decryption failed or packet was tampered with! Error: {e}")
    finally:
        conn.close()
        server_socket.close()

if __name__ == "__main__":
    start_secure_server()