import hashlib
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

def sign_message(sender, receiver, private_key, message):
    """
    Signs a message by encrypting its hash with the sender's private key and returns a formatted message.

    Args:
        sender (str): The sender's name (a node in the graph).
        receiver (str): The receiver's name (a node in the graph).
        private_key (str): The sender's private key.
        message (str): The message to sign.

    Returns:
        dict: A formatted message created with create_message, including the signature in the metadata.
    """
    d, n = private_key
    hashed_message = int(hashlib.sha256(message.encode()).hexdigest(), 16)
    truncated_hash = hashed_message % n
    signature = mod_exp(truncated_hash, d, n)
    return create_message(sender, receiver, {"signature": str(signature)}, message)

def validate_signature(public_key, message, signature):
    """
    Validates a signed message by comparing its hash to the decrypted signature.

    Args:
        public_key (str): The sender's public key.
        message (str): The message to validate.
        signature (str): The encrypted hash of the message.

    Returns:
        bool: True if the signature is valid, False otherwise.
    """
    e, n = public_key
    hashed_message = int(hashlib.sha256(message.encode()).hexdigest(), 16)
    truncated_hash = hashed_message % n
    decrypted_hash = mod_exp(int(signature), e, n)
    return truncated_hash == decrypted_hash

def respond_to_signed_message(sender, receiver, private_key, public_key, received_message):
# OPTIONAL, WE ALREADY HAVE 3 PROBLEMS DONE, THIS IS EXTRA IF YOU WANT
    """
    Responds to a signed message with a new signed message acknowledging receipt.

    Args:
        sender (str): The responder's name (a node in the graph).
        receiver (str): The original sender's name (a node in the graph).
        private_key (str): The responder's private key.
        public_key (str): The original sender's public key.
        received_message (dict): A dictionary containing the signed message and its signature.

    Returns:
        dict: A new formatted signed message acknowledging receipt, created with create_message.
    """
    pass
