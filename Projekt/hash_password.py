import hashlib
import argparse
import bcrypt

parser = argparse.ArgumentParser(description="Script för att hasha lösenord")

parser.add_argument("--password", type=str, help="Skriv lösenordet du vill hasha")
parser.add_argument("--algorithm", choices=["bcrypt", "md5", "scrypt", "sha256"], type=str, help="Välj vilken hash algorithm du vill använda")
args = parser.parse_args()

#print(args.password)

if args.algorithm == "bcrypt":
    hashed_password = bcrypt.hashpw(args.password.encode(), bcrypt.gensalt())
    print(f"Hashad lösenord: {hashed_password.decode()}")

    with open("passwords.txt", "a") as password_file:
        password_file.write(args.password + "\n")
    with open("bcrypt_hashes.txt", "a") as hash_file:
        hash_file.write(hashed_password.decode() + "\n")

elif args.algorithm == "md5":
    hashed_password = hashlib.md5(args.password.encode()).hexdigest()
    print(f"Hashad lösenord: {hashed_password}")

    with open("passwords.txt", "a") as password_file:
        password_file.write(args.password + "\n")
    with open("md5_hashes.txt", "a") as hash_file:
        hash_file.write(hashed_password + "\n")

elif args.algorithm == "sha256":
    hashed_password = hashlib.sha256(args.password.encode()).hexdigest()
    print(f"Hashad lösenord: {hashed_password}")

    with open("passwords.txt", "a") as password_file:
        password_file.write(args.password + "\n")
    with open("sha256_hashes.txt", "a") as hash_file:
        hash_file.write(hashed_password + "\n")

elif args.algorithm == "scrypt":
    hashed_password = hashlib.scrypt(args.password.encode(), salt=b'some_salt', n=16384, r=8, p=1).hex()
    print(f"Hashad lösenord: {hashed_password}")

    with open("passwords.txt", "a") as password_file:
        password_file.write(args.password + "\n")
    with open("scrypt_hashes.txt", "a") as hash_file:
        hash_file.write(hashed_password + "\n")