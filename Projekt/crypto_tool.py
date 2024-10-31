from cryptography.fernet import Fernet
import argparse
import os

#Funktion för att kontrollera om en fil existerar
def check_file_exists(file_path, description):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"{description} '{file_path}' hittades inte. Kontrollera att filen existerar och försök igen.")


parser = argparse.ArgumentParser(description="Script för att antingen kryptera eller dekryptera en filtext")

parser.add_argument("key_name", type=str, help="Ange vilken fil du vill använda som nyckel för att kryptera din text.")
parser.add_argument("file_name", type=str, help="Skriv namnet på filen som ska innehålla den krypterade texten")
parser.add_argument("--message", type=str, help="Skriv meddelandet du vill kryptera (endast för kryptering)")

parser.add_argument("--mode", choices=["kryptera", "dekryptera"], help="Välj att antingen kyrptera eller dekryptera")

args = parser.parse_args()

try:
    #Kontrollera om nyckelfilen finns
    check_file_exists(args.key_name, "Nyckelfilen")


    #Kontrollera om filen finns för dekryptering
    if args.mode == "dekryptera":
        check_file_exists(args.file_name, "Filen som ska dekrypteras")

    #Krypterar filen
    if args.mode == "kryptera":
        if not args.message:
            parser.error("Krypteringsläget kräver att du anger ett meddelande med --message.")

        with open(args.key_name, "rb") as key_file:
            key = key_file.read()
        print(f"Nyckel: {key.decode()}")

        cipher_suite = Fernet(key)

        message = args.message.encode()

        cipher_text = cipher_suite.encrypt(message)
        print(f"Krypterad text: {cipher_text}")

        with open(args.file_name, "wb") as encoded_file:
            encoded_file.write(cipher_text)
    #dekrypterar filen
    elif args.mode == "dekryptera":
        
        try:
            with open(args.file_name, "rb") as encoded_file:
                message = encoded_file.read()
        except FileNotFoundError:
            print("Filen som du angav hittades inte")
            exit()

        with open(args.key_name, "rb") as key_file:
            key = key_file.read()
        print(f"Nyckel: {key.decode()}")

        cipher_suite = Fernet(key)

        plain_text = cipher_suite.decrypt(message)
        print(f"Dekrypterad text: {plain_text.decode()}")
except FileNotFoundError as e:
    print(f"Fel: {e}")
except Exception as e:
    print(f"Ett oväntat fel inträffade: {e}")