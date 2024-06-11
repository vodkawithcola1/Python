import caesarart

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(caesarart.logo)
print("Do not use spaces! WIP")

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

letter_table = []
shifted_letters = []


def encrypt(text, shift):
    for letter in text:
        if letter in alphabet:
            letter_table.append(alphabet.index(letter))

    for move in range(len(letter_table)):
        letter_table[move] += shift

    output = [alphabet[pos % len(alphabet)] for pos in letter_table]

    print(f"".join(output))


def decrypt(text, shift):
    for letter in text:
        if letter in alphabet:
            letter_table.append(alphabet.index(letter))

    for move in range(len(letter_table)):
        letter_table[move] -= shift

    output = [alphabet[pos % len(alphabet)] for pos in letter_table]

    print(f"".join(output))


if direction == 'encode':
    encrypt(text, shift)
elif direction == 'decode':
    decrypt(text, shift)




