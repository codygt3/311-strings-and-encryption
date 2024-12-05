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
    # Run-length encoding algorithm
    encoded_message = []
    i = 0
    while i < len(message):
        count = 1
        while i + 1 < len(message) and message[i] == message[i + 1]:
            count += 1
            i += 1
        encoded_message.append(f"{message[i]}{count}")
        i += 1

    # Join encoded parts and add metadata
    encoded_message_str = ''.join(encoded_message)
    metadata = {
        "encoding_type": "run-length",
        "original_length": len(message)
    }
    return create_message(sender, receiver, metadata, encoded_message_str)

def run_length_decode(encoded_message, original_length):
    """
    Decompresses a run-length encoded message.

    Args:
        encoded_message (str): The compressed message body.
        original_length (int): The length of the original uncompressed message.

    Returns:
        str: The original uncompressed message.
    """
    # Run-length decoding algorithm
    decoded_message = []
    i = 0
    while i < len(encoded_message):
        char = encoded_message[i]
        count = ""
        i += 1
        while i < len(encoded_message) and encoded_message[i].isdigit():
            count += encoded_message[i]
            i += 1
        decoded_message.append(char * int(count))

    # Join the decoded parts
    return ''.join(decoded_message)
