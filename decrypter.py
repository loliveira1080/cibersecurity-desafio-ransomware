import os
import pyaes

# Chave de descriptografia (mesma chave usada na criptografia)
key = os.getenv("ENCRYPTION_KEY", "DesafioDio@1223").encode()

# Nome do arquivo criptografado
encrypted_file_name = "teste.txt.ransomwaretroll"

# Verifica se o arquivo criptografado existe
if not os.path.isfile(encrypted_file_name):
    print(f"Erro: O arquivo '{encrypted_file_name}' não foi encontrado.")
    exit()

try:
    # Lê o conteúdo do arquivo criptografado
    with open(encrypted_file_name, "rb") as encrypted_file:
        encrypted_data = encrypted_file.read()
    
    # Descriptografa os dados
    aes = pyaes.AESModeOfOperationCTR(key)
    decrypted_data = aes.decrypt(encrypted_data)
    
    # Remove o arquivo criptografado
    os.remove(encrypted_file_name)
    
    # Salva o arquivo descriptografado
    original_file_name = "teste.txt"
    with open(original_file_name, "wb") as decrypted_file:
        decrypted_file.write(decrypted_data)
    
    print(f"Arquivo descriptografado salvo como: {original_file_name}")

except Exception as e:
    print(f"Erro ao descriptografar o arquivo: {e}")
