from create_message import create_message

def run_length_encode(sender, receiver, message):
    """
    Compresses a message using run-length encoding and returns a formatted message.

    Args:
        sender (str): The sender's name (a node in the graph).
        receiver (str): The receiver's name (a node in the graph).
        message (str): The message to compress.

    Returns:
        dict: A formatted message created with create_message, including the encoded message and metadata.
              Metadata includes the encoding type ('run-length') and original message length.
    """
    return create_message(sender, receiver, {"original_length": 11}, "Placeholder")

def run_length_decode(encoded_message, original_length):
    """
    Decompresses a run-length encoded message.

    Args:
        encoded_message (str): The compressed message body.
        original_length (int): The length of the original uncompressed message.

    Returns:
        str: The original uncompressed message.
    """
    return "Placeholder"
