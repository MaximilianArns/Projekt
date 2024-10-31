from cryptography.fernet import Fernet
import argparse

key = Fernet.generate_key()

parser = argparse.ArgumentParser(description="Script för att skapa en nyckel för kryptering och dekryptering")

parser.add_argument("key_name", type=str, help="Skriv in namnet på nyckeln du vill skapa")

args = parser.parse_args()

print(key)

#Kontrollera om filnamnet slutar på ".key", lägger till det annars
if not args.key_name.endswith(".key"):
    args.key_name += ".key"

with open(args.key_name, "wb") as key_file:
    key_file.write(key)
print(f"Nyckeln har sparats som {args.key_name}")