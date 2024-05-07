import base64

def encrypt_pass(password):
    # print(password.encode())
    encoded_bytes = base64.b64encode(password.encode())
    print(encoded_bytes)
    return encoded_bytes

def dencrypt_pass(password):
    decoded_bytes = base64.b64decode(password.decode())
    print(decoded_bytes)
    return decoded_bytes

user_pass = input("Enter your password: ")
encoded_pass = encrypt_pass(user_pass)
dencrypt_pass(encoded_pass)