from cryptography.fernet import Fernet

# Carregar a chave de descriptografia
def load_key():
    with open("key.key", "rb") as key_file:
        return key_file.read()

# Inicializar o cifrador Fernet com a chave
def decrypt_message(encrypted_message, key):
    cipher = Fernet(key)
    decrypted_message = cipher.decrypt(encrypted_message)
    return decrypted_message.decode()

def main():
    # Carregar a chave e a mensagem criptografada
    key = load_key()

    with open("encrypted_message.txt", "rb") as file:
        encrypted_message = file.read()

    # Descriptografar a mensagem
    decrypted_message = decrypt_message(encrypted_message, key)

    # Salvar a mensagem descriptografada em um arquivo de texto
    with open("decrypted_message.txt", "w") as decrypted_file:
        decrypted_file.write(decrypted_message)

    print(f"Mensagem descriptografada: {decrypted_message}")
    print("Mensagem descriptografada foi salva em 'decrypted_message.txt'.")

if __name__ == "__main__":
    main()
