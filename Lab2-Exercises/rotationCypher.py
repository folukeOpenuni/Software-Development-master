def rotate_cipher(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26  # Ensure the shift is within the alphabet range
            if char.islower():
                shifted_char = chr(((ord(char) - ord('a') + shift_amount) % 26) + ord('a'))
            elif char.isupper():
                shifted_char = chr(((ord(char) - ord('A') + shift_amount) % 26) + ord('A'))
        else:
            shifted_char = char
        encrypted_text += shifted_char
    return encrypted_text

#slightly better solution 
def rotate_cipher_two(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            if char.islower(): #ord return the Unicode code point for a one-character string.
                shifted_char = chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))
            elif char.isupper():
                shifted_char = chr(((ord(char) - ord('A') + shift) % 26) + ord('A'))
        else:
            shifted_char = char
        encrypted_text += shifted_char
    return encrypted_text

# Input: Ask the user for a text and a rotation shift value
text = input("Enter the text to encrypt: ")
shift = int(input("Enter the rotation shift value (e.g., 1 for Caesar cipher): "))

# Perform rotation cipher
encrypted_text = rotate_cipher(text, shift)

# Display the encrypted text
print("Encrypted text:", encrypted_text)


# Input: Ask the user for a text and a rotation shift value
text = input("Enter the text to encrypt: ")
shift = int(input("Enter the rotation shift value (e.g., 1 for Caesar cipher): "))

# Perform rotation cipher
encrypted_text = rotate_cipher(text, shift)

# Display the encrypted text
print("Encrypted text:", encrypted_text)
