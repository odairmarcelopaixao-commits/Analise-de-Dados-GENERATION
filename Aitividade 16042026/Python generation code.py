import requests
import json

API_URL = 'YOUR_API_URL_HERE'  # Replace with your actual Google Apps Script web app URL

def send_message(name, email):
    response = requests.post(
        API_URL,
        json={"name": name, "email": email}
    )
    print(response.text)

def send_multiple_messages(messages):
    for      : # complete this line
        send_message(message['name'], message['email'])

def get_all_messages():
    response = requests.get(     ) # complete this line
    data = response.     () # complete this line
    print(json.dumps(data, indent=2))

def get_last_message():
    response = requests.get(     ) # complete this line
    data = response.json()
    if data:
        last = data[     ] # complete this line
        print(json.dumps(last, indent=2))
    else:
        print("No messages found.")

if __name__ == "__main__":
    print("Sending one message...")
    send_message("alice", "alice@example.com")

    print("\nSending multiple messages...")
    messages = [
        {"name": "bob", "email": "bob@example.com"},
        {"name": "charlie", "email": "charlie@example.com"}
    ]
    send_multiple_messages(messages)

    print("\nRetrieving all messages...")
    get_all_messages()

    print("\nRetrieving last message...")
    get_last_message()

