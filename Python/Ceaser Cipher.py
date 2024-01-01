ascii_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def encrypt(text, key):
    ciphertext = ""
    for char in text:
        charUpper = char.upper()
        if (ascii_uppercase.find(charUpper) != -1):
            newindex = (ascii_uppercase.index(charUpper) + key) % 26
            newcode = ascii_uppercase[newindex]
            ciphertext = ciphertext + newcode
        else:
            ciphertext = ciphertext + charUpper
    return ciphertext
           
def decrypt(text, key):
    ciphertext = ""
    for char in text:
        charUpper = char.upper()
        if (ascii_uppercase.find(charUpper) != -1):
            newindex = (ascii_uppercase.index(charUpper) - key) % 26
            newcode = ascii_uppercase[newindex]
            ciphertext = ciphertext + newcode
        else:
            ciphertext = ciphertext + charUpper
    return ciphertext


def main():
    choice = input("Do you want to (e)ncrypt or (d)ecrypt? ").upper()
    if choice == "E":
        text = input("Enter the message to encrypt: ")
        key = int(input("Please enter the key (0 to 26) to use: "))
        print(encrypt(text, key))
    elif choice == "D":
        text = input("Enter the message to decrypt: ")
        key = int(input("Please enter the key (0 to 26) to use: "))
        print(decrypt(text, key))
        print("Full decrypted text copied to clipboard")

main()
    

    