import requests
import json
from credentials import load_credentials

# Microsoft OAuth2 Token Endpoint
token_url = "https://login.microsoftonline.com/common/oauth2/v2.0/token"

# Load Credentials
client_id, client_secret, tenant_link, redirect_uri, code = load_credentials()

payload = {
    "client_id": client_id,
    "client_secret": client_secret,
    "code": code,
    "redirect_uri": redirect_uri,
    "grant_type": "authorization_code",
    "scope": "User.Read Calendars.Read offline_access"
}

response = requests.post(token_url, data=payload)
token_data = response.json()
print("🔍 Full Response:", token_data)  # Debugging

# Get tokens from response
access_token = token_data.get("access_token")
refresh_token = token_data.get("refresh_token")

if not access_token:
    print("❌ Error: No access token received!")
    print("🔍 Full Response:", token_data)  # Debugging info
    exit()

if not refresh_token:
    print("❌ Error: No refresh token received!")
    print("🔍 Full Response:", token_data)  # Debugging info

print("✅ Access Token Retrieved!")

def save_tokens(token_data, filename="tokens.json"):
    with open(filename, "w") as file:
        json.dump(token_data, file, indent=4)
    print("✅ Tokens saved to", filename)

save_tokens(token_data)