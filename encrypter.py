from cryptography.fernet import Fernet

# Gerar uma chave e salvá-la para descriptografia
def generate_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
    return key

# Inicializar o cifrador Fernet
def encrypt_message(message, key):
    cipher = Fernet(key)
    encrypted_message = cipher.encrypt(message.encode())
    return encrypted_message

def main():
    # Gerar chave e criptografar a mensagem
    key = generate_key()
    message = input("Digite a mensagem que deseja criptografar: ")
    encrypted_message = encrypt_message(message, key)

    # Salvar a mensagem criptografada em um arquivo
    with open("encrypted_message.txt", "wb") as file:
        file.write(encrypted_message)

    print("Mensagem criptografada e salva em 'encrypted_message.txt'.")
    print(f"A chave de descriptografia foi salva em 'key.key'.")

if __name__ == "__main__":
    main()
