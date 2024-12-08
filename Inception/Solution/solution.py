from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

def encrypt_image_aes_128(input_image_path, output_encrypted_path, key, iv):
    # Vérifier la longueur de la clé et de l'IV
    if len(key) != 16:
        raise ValueError("La clé doit être exactement de 16 octets (128 bits).")
    if len(iv) != 16:
        raise ValueError("L'IV doit être exactement de 16 octets (128 bits).")

    # Lire l'image en binaire
    with open(input_image_path, "rb") as file:
        image_data = file.read()

    # Ajouter du padding aux données pour correspondre à un multiple de la taille du bloc (16 octets)
    padded_data = pad(image_data, AES.block_size)

    # Chiffrer avec AES en mode CBC
    cipher = AES.new(key.encode('utf-8'), AES.MODE_CBC, iv)
    encrypted_data = cipher.encrypt(padded_data)

    # Écrire les données chiffrées dans un fichier
    with open(output_encrypted_path, "wb") as file:
        file.write(encrypted_data)

    print(f"Image chiffrée avec succès et sauvegardée dans {output_encrypted_path}")

# Exemple d'utilisation
if __name__ == "__main__":
    # Fichier d'entrée et de sortie
    input_image = "piecejointe.png"  # Image d'entrée
    output_encrypted = "result.png"  # Fichier chiffré de sortie

    # Clé et IV spécifiés
    key = "MaBelleArcadeKey"  # Clé de 128 bits (16 caractères)
    iv = b'i\xf7\xf8]j\x8f}"\xb8\xf5c\x86\x8dh\x85\x06'  # IV exact en bytes

    # Chiffrer l'image
    encrypt_image_aes_128(input_image, output_encrypted, key, iv)

