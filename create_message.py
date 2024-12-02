def create_message(sender, receiver, metadata, message_body):
    """
    Creates a standardized message dictionary.
    
    Args:
        sender (str): The sender's name (a node in the graph).
        receiver (str): The receiver's name (a node in the graph).
        metadata (dict): Metadata to describe the message.
        message_body (str): The body of the message.
    
    Returns:
        dict: A dictionary representing the formatted message.
    """
    return {
        "sender": sender,
        "receiver": receiver,
        "metadata": metadata,
        "message_body": message_body
    }

"""
Sample usage:
sample_metadata = {
        "encoding_type": "run-length",
        "original_length": 150
    }
message = create_message(
        sender="Alice",
        receiver="Eve",
        metadata=sample_metadata,
        message_body="Meet at Campus Center"
    )
"""