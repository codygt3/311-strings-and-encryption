from create_message import create_message

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
    return create_message(sender, receiver, {"signature": "Placeholder"}, "Placeholder")

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
    return True

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
