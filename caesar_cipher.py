alphabet = ['a', 'b', 'c', 'd', 'e', 'f',
'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
'w', 'x', 'y', 'z',
'1', '2', '3', '4', '5', '6', '7', '8', '9']



# def cipher(start_text, shift_amount, cipher_direction):
#     print(f'The plain text number is {start_text}.')
#     end_text = ''
#     if cipher_direction == "decode":
#         shift_amount *= 1
#     for char in start_text:
#         if char in alphabet:
#             position = alphabet.index(char)
#             new_position = position + shift_amount
#             end_text += alphabet[new_position]
#         else:
#             end_text += char
#     print(f'Here\'s is the {cipher_direction} result: {end_text}')


def encrypt(plain_text, key):
    encrypted_pin = ''
    
    for char in plain_text:
        num = int(char)
        shifted_number = num + key
        if shifted_number > 9:
            shifted_number = shifted_number % 10
        encrypted_pin += str(shifted_number)

    return encrypted_pin

def decrypt(encrypted_pin, key):
    return encrypt(encrypted_pin, -key)


def crack(encrypted_pin):
    for key in range(len(alphabet)):
        translated = ""
        for char in encrypted_pin:
            num = alphabet.find(char)
            num = num - key 

            if num < 0:
                num = num + len(alphabet[num])
            else:
                translated = translated + char
    return translated


# if __name__ == "__main__":
    # print(encrypt('23', 6)) # 89
    # print(encrypt('23', 4)) # 67
    # print(encrypt('2345', 7)) # 9012
    # print(encrypt('2345', 108345345345)) # 9012
    # print(decrypt('12345', 6))