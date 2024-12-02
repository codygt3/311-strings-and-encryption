import json
from run_length_encode import run_length_encode, run_length_decode
from encrypted_message import encrypt_message, decrypt_message
from signed_message import sign_message, validate_signature, respond_to_signed_message

# Sample dictionary of lists to represent the graph of friends
friends_graph = {
    "Alice": ["Bob", "Charlie"],
    "Bob": ["Alice", "David"],
    "Charlie": ["Alice", "Eve"],
    "David": ["Bob", "Eve"],
    "Eve": ["Charlie", "David"]
}

# Load keys from JSON file
with open('friends_keys.json', 'r') as file:
    keys = json.load(file)

# Command-line interface for testing functions
def main_menu():
    friend_names = list(friends_graph.keys())  # Extract friend names from the graph
    last_message = None  # Store the last processed message for convenience

    while True:
        print("\n--- Friends Communication Tester ---")
        print("1. Run-Length Encode a Message")
        print("2. Run-Length Decode the Last Encoded Message")
        print("3. Encrypt a Message")
        print("4. Decrypt the Last Encrypted Message")
        print("5. Sign a Message")
        print("6. Validate the Last Signed Message")
        print("7. Respond to a Signed Message")
        print("8. Print a Friend's Public Key")
        print("9. Exit")
        choice = input("Enter your choice (1-9): ")

        if choice == "1":
            print("Select Sender:")
            for i, name in enumerate(friend_names, start=1):
                print(f"{i}. {name}")
            sender = friend_names[int(input("Enter the number corresponding to the sender: ")) - 1]

            print("Select Receiver:")
            for i, name in enumerate(friend_names, start=1):
                print(f"{i}. {name}")
            receiver = friend_names[int(input("Enter the number corresponding to the receiver: ")) - 1]

            message = input("Enter the message to encode: ")
            last_message = run_length_encode(sender, receiver, message)
            print("Encoded Message:", last_message)

        elif choice == "2":
            if last_message and "message_body" in last_message and "metadata" in last_message:
                encoded_message = last_message["message_body"]
                original_length = last_message["metadata"]["original_length"]
                decoded_message = run_length_decode(encoded_message, original_length)
                print("Decoded Message:", decoded_message)
            else:
                print("No encoded message available to decode.")

        elif choice == "3":
            print("Select Sender:")
            for i, name in enumerate(friend_names, start=1):
                print(f"{i}. {name}")
            sender = friend_names[int(input("Enter the number corresponding to the sender: ")) - 1]

            print("Select Receiver:")
            for i, name in enumerate(friend_names, start=1):
                print(f"{i}. {name}")
            receiver = friend_names[int(input("Enter the number corresponding to the receiver: ")) - 1]

            message = input("Enter the message to encrypt: ")
            public_key = keys[receiver]["public_key"]
            last_message = encrypt_message(sender, receiver, public_key, message)
            print("Encrypted Message:", last_message)

        elif choice == "4":
            if last_message and "message_body" in last_message:
                print("Select Recipient:")
                for i, name in enumerate(friend_names, start=1):
                    print(f"{i}. {name}")
                recipient = friend_names[int(input("Enter the number corresponding to the recipient: ")) - 1]

                private_key = keys[recipient]["private_key"]
                encrypted_message = last_message["message_body"]
                decrypted_message = decrypt_message(private_key, encrypted_message)
                print("Decrypted Message:", decrypted_message)
            else:
                print("No encrypted message available to decrypt.")

        elif choice == "5":
            print("Select Sender:")
            for i, name in enumerate(friend_names, start=1):
                print(f"{i}. {name}")
            sender = friend_names[int(input("Enter the number corresponding to the sender: ")) - 1]

            print("Select Receiver:")
            for i, name in enumerate(friend_names, start=1):
                print(f"{i}. {name}")
            receiver = friend_names[int(input("Enter the number corresponding to the receiver: ")) - 1]

            private_key = keys[sender]["private_key"]
            message = input("Enter the message to sign: ")
            last_message = sign_message(sender, receiver, private_key, message)
            print("Signed Message:", last_message)

        elif choice == "6":
            if last_message and "metadata" in last_message and "signature" in last_message["metadata"]:
                print("Select Sender:")
                for i, name in enumerate(friend_names, start=1):
                    print(f"{i}. {name}")
                sender = friend_names[int(input("Enter the number corresponding to the sender: ")) - 1]

                public_key = keys[sender]["public_key"]
                message = last_message["message_body"]
                signature = last_message["metadata"]["signature"]
                is_valid = validate_signature(public_key, message, signature)
                print("Signature Valid:", is_valid)
            else:
                print("No signed message available to validate.")

        elif choice == "7":
            print("Select Responder (Your Name):")
            for i, name in enumerate(friend_names, start=1):
                print(f"{i}. {name}")
            responder = friend_names[int(input("Enter the number corresponding to the responder: ")) - 1]

            print("Select Original Sender:")
            for i, name in enumerate(friend_names, start=1):
                print(f"{i}. {name}")
            original_sender = friend_names[int(input("Enter the number corresponding to the original sender: ")) - 1]

            private_key = keys[responder]["private_key"]
            public_key = keys[original_sender]["public_key"]
            received_message = input("Enter the received signed message (as a dictionary): ")
            response = respond_to_signed_message(responder, original_sender, private_key, public_key, eval(received_message))
            print("Response Signed Message:", response)

        elif choice == "8":
            print("Select Friend to Print Public Key:")
            for i, name in enumerate(friend_names, start=1):
                print(f"{i}. {name}")
            friend = friend_names[int(input("Enter the number corresponding to the friend: ")) - 1]

            print(f"{friend}'s Public Key:", keys[friend]["public_key"])

        elif choice == "9":
            print("Exiting... Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")



if __name__ == "__main__":
    main_menu()
