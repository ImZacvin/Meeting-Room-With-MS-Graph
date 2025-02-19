import json

def load_tokens(filename="tokens.json"):
    try:
        with open(filename, "r") as file:
            tokens = json.load(file)  # Load JSON data into a dictionary
        return tokens.get("access_token"), tokens.get("refresh_token")
    except FileNotFoundError:
        print("❌ Error: Token file not found!")
        return None, None