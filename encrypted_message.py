from create_message import create_message

# Helper function to perform modular exponentiation
def mod_exp(base, exp, mod):
    result = 1
    base = base % mod
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        exp = exp // 2
        base = (base * base) % mod
    return result

def encrypt_message(sender, receiver, public_key, message):
    """
    Encrypts a message using the given public key and returns a formatted message.

    Args:
        public_key (str): The recipient's public key.
        message (str): The message to encrypt.

    Returns:
        dict: A formatted message dictionary using create_message.
    """
    e, n = public_key
    # Encrypt each integer in the encrypted message
    encrypted_message = ''.join(str(mod_exp(ord(char), e, n)) + ',' for char in message).rstrip(',')
    return create_message(sender, receiver, {"encoding_type": "run-length", "original_length": len(message)}, encrypted_message)

def decrypt_message(private_key, encrypted_message):
    """
    Decrypts a message using the given private key.

    Args:
        private_key (str): The recipient's private key.
        encrypted_message (str): The encrypted message to decrypt.

    Returns:
        str: The decrypted original message.
    """
    d, n = private_key
    encrypted_numbers = list(map(int, encrypted_message.split(',')))
    # Decrypt each integer in the encrypted message
    decrypted_message = ''.join(chr(mod_exp(num, d, n)) for num in encrypted_numbers)
    return decrypted_message
