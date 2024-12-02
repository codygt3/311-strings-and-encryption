# 311-strings-and-encryption
## Key Components

### 1. `generate_keys.py`

- **Purpose**: This script generates a JSON file (`friends_keys.json`) containing valid RSA public and private keys for each friend in the network
- Stores keys in the JSON file in the following format:
  ```json
  {
      "Alice": {
          "public_key": [e, n],
          "private_key": [d, n]
      },
      "Bob": {
          "public_key": [e, n],
          "private_key": [d, n]
      }
  }
  ```
    Run the script to create or regenerate the `friends_keys.json` file.

### 2. `create_message`

- **Purpose**: This function standardizes the structure of messages exchanged between friends.
- **Functionality**:
  - Takes input such as sender, receiver, metadata, and message body.
  - Returns a message dictionary with the following format:
    ```python
    {
        "sender": "Alice",
        "receiver": "Bob",
        "metadata": {
            # Metadata that the message may need, for example a signature:
            "signature": "30214"
            # or original length of message for run length encoding
            "original_length": 15
        },
        "message_body": "Encoded Message"
    }
    ```


### 3. Other Modules

The following modules implement specific functionalities:

- `run_length_encode.py`: Encodes and decodes messages using run-length encoding.
- `encrypted_message.py`: Encrypts and decrypts messages using RSA encryption.
- `signed_message.py`: Signs messages and validates signatures.

## How to Run

1. **Generate Keys**:

   - Run `generate_keys.py` to create the `friends_keys.json` file.

2. **Test Functions**:

   - Use `main.py` to interact with the system through a command-line interface.
   - Select options to encode, encrypt, sign, decode, decrypt, or validate messages.

## File Descriptions

- `generate_keys.py`: Generates RSA keys for friends and saves them to `friends_keys.json`.
- `create_message.py`: Provides a function to standardize message dictionaries.
- `run_length_encode.py`: Handles lossless compression and decompression of messages.
- `encrypted_message.py`: Implements RSA encryption and decryption.
- `signed_message.py`: Signs messages, validates them, and creates responses to signed messages.
- `main.py`: Provides a command-line interface for testing all functionalities.
- `friends_keys.json`: Stores public and private keys for each friend.

### Contributors

Devleoped by Cody Torres, Shade Matsumoto, and Junle Yan
