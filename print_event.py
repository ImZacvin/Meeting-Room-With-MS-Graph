import requests
from access_the_token import load_tokens



# Fetch calendar events
url = "https://graph.microsoft.com/v1.0/me/events"

def eventCalendar():
    # Load tokens
    access_token, refresh_token = load_tokens()

    # Check access token can be access or not
    headers = {"Authorization": f"Bearer {access_token}"}

    response = requests.get(url, headers=headers)
    events_data = response.json()

    if response.status_code == 200 and "value" in events_data:
        events = events_data["value"]
        if events:
            print("\n📅 Upcoming Events:")
            for event in events:
                print(f"📌 Event: {event['subject']}")
                print(f"🕒 Start: {event['start']['dateTime']} ({event['start']['timeZone']})")
                print(f"⏳ End: {event['end']['dateTime']} ({event['end']['timeZone']})")
                print(f"📍 Location: {event.get('location', {}).get('displayName', 'No location')}")
                
                # Print attendees
                attendees = event.get("attendees", [])  # Get attendees list (empty list if none)
                if attendees:
                    print("👥 Attendees:")
                    for attendee in attendees:
                        email = attendee.get("emailAddress", {}).get("address", "Unknown Email")
                        name = attendee.get("emailAddress", {}).get("name", "Unknown Name")
                        attendee_type = attendee.get("type", "Unknown Type")
                        print(f"   - {name} ({email}) [{attendee_type}]")
                else:
                    print("❌ No attendees")

                print("-" * 40)

        else:
            print("📭 No upcoming events found.")
    else:
        print(f"❌ Error fetching events: {events_data}")