def create_cipher_mapping():
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    cipher_key = 'QWERTYUIOPASDFG'  # This is the 15-letter cipher
    mapping = {}
    
    for i in range(len(cipher_key)):
        mapping[alphabet[i]] = cipher_key[i]
    
    return mapping

def encode_message(message, mapping):
    encoded_message = ''
    for char in message.upper():
        if char in mapping:
            encoded_message += mapping[char]
        else:
            encoded_message += char  # For non-alphabet characters, keep them unchanged
    return encoded_message

# Example Usage
cipher_mapping = create_cipher_mapping()
message = "Hello World!"  # Replace this with any message you want to encode
encoded_message = encode_message(message, cipher_mapping)
print("Encoded message:", encoded_message)
