import json

def load_credentials(filename="credentials.json"):
    try:
        with open(filename, "r") as file:
            credentials = json.load(file)  # Load JSON data into a dictionary
        return credentials.get("client_id"), credentials.get("client_secret"), credentials.get("tenant_link"), credentials.get("redirect_uri"), credentials.get("code")
    except FileNotFoundError:
        print("❌ Error: Token file not found!")
        return None, None