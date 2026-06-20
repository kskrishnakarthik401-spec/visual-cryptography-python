import socket
import os
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

def send_encrypted_packet():
    # Use the exact same pre-shared 32-byte key
    key = b"sixteen_byte_key_sixteen_byte_ky"
    aesgcm = AESGCM(key)
    
    # Generate a unique 12-byte initialization vector (Nonce) for security
    nonce = os.urandom(12)
    
    message = "Research Proposal Payload"
    print(f"🔒 Original Client Message: {message}")
    
    # Encrypt the message using AES-GCM
    ciphertext = aesgcm.encrypt(nonce, message.encode('utf-8'), None)
    
    # Initialize connection to the local server
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('127.0.0.1', 65432))
    
    # Send the nonce first so the server knows how to process the block cipher
    client_socket.send(nonce)
    # Send the encrypted payload
    client_socket.send(ciphertext)
    
    print("🚀 Encrypted packet stream transmitted to server successfully.")
    client_socket.close()

if __name__ == "__main__":
    send_encrypted_packet()
