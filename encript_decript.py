alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

# def encrypt(original_text, shift_amout):
#     encrypted_text = ""
#     for l in original_text:
#         new_index = (alphabet.index(l) + shift_amout) % 26
#         encrypted_text += alphabet[new_index]
    
#     print(f"Here is the encrypted result: {encrypted_text}")

# def decrypt(text, amout):
#     decrypted_text = ""
#     for l in text:
#         new_index = (alphabet.index(l) - shift_amout) % 26
#         decrypted_text += alphabet[new_index]
    
#     print(f"Here is the decrypted result: {decrypted_text}")



# if direction == 'e':
#     original_text = str(input("Type your message: "))
#     shift_amout = int(input("Type the shift number: "))
#     encrypt(original_text, shift_amout)
# elif direction == 'd':
#     original_text = str(input("Type your message: "))
#     shift_amout = int(input("Type the shift number: "))
#     decrypt(original_text, shift_amout)
# else:
#     print("Invalied input!")


def caesar(original_text, shift_amount, encode_or_decode):
    
    ciphar_text = ""

    if encode_or_decode == "decode":
        shift_amount *= -1
    for l in original_text:

        if l not in alphabet:
            ciphar_text += l
        else:
            new_index = (alphabet.index(l) + shift_amount) % 26
            ciphar_text += alphabet[new_index]
    
    print(f"Here is the {encode_or_decode} result: {ciphar_text}")

answer = 'yes'
while answer=='yes':
    direction = input("Type 'encode' to encode, type 'decode' to decode: ")
    text = str(input("Type your message: "))
    amount = int(input("Type the shift number: "))


    caesar(original_text=text, shift_amount=amount, encode_or_decode=direction)
    answer = input("Type 'yes' if you want to go again. Otherwise, type 'no'. ")


