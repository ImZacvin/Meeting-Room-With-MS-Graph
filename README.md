# Fetch Microsoft Team Calendar with MS Graph API

## Requirements

Python version 3.x.x

## Step 1

Fill the client id, client secret in credentials.json.

Change the client id to your id, then redirect the link.
https://login.microsoftonline.com/common/oauth2/v2.0/authorize?client_id=yourclientid&response_type=code&redirect_uri=http://localhost:5000/callback&response_mode=query&scope=User.Read Calendars.Read offline_access&state=12345

The link will open a new window like this :
http://localhost:5000/callback?code=thecodegenerated&state=12345

Copy the code and insert it in the credentials.json

## Step 2

Run the get_token.py
the access token and refresh token are saved to tokens.json

## Step 3

If you already got the refresh token in tokens.json, you dont need to run the get_token.py again. you just need to run check_exp.py

The refresh token that got from earlier will automatically refresh tokens.json to a new access token and the new refresh token.
