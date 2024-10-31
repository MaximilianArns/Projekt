import hashlib
import argparse
import bcrypt

parser = argparse.ArgumentParser(description="Script för att knäcka hashade lösenord")

parser.add_argument("hash_password", type=str, help="Ange vilken hash du vill försöka knäcka.")
parser.add_argument("wordlist", type=str, help="Skriv filnamnet med lösenorden du vill använda för att knäcka hashen")
parser.add_argument("algorithm", choices=["bcrypt", "md5", "sha256"], help="Ange algoritmen som användes för att skapa hashen")

args = parser.parse_args()

def crack_password(hashed_password, wordlist, algorithm):
    #Öppna ordlistan och gå igenom varje rad
    with open(wordlist, 'r') as file:
        for line in file:
            word = line.strip()
            if algorithm =="md5":
                hashed_word = hashlib.md5(word.encode()).hexdigest()
            elif algorithm == "sha256":
                hashed_word = hashlib.sha256(word.encode()).hexdigest()
            elif algorithm == "bcrypt":
                if bcrypt.checkpw(word.encode(), hashed_password.encode()):
                    print(f"Lösenord funnet: {word}")
                    return word
                continue

            #Kontrollera om hashen matchar vår sökta hash om det inte var en bcrypt hash
            if hashed_word == hashed_password:
                print(f"Lösenord funnet: {word}")
                return word
    print("Lösenordet hittades inte i ordlistan.")
    return None





crack_password(args.hash_password, args.wordlist, args.algorithm)