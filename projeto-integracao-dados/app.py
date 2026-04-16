import requests
import json

API_URL = 'https://script.google.com/macros/s/AKfycbypF00VrYJ7H-Ry07DKqYNQua_E3t_FkB6kWatdyIIm1967lVbjKJrhJx-uzgReZZFy/exec' 

def send_message(name, email):
    response = requests.post(
        API_URL,
        json={"name": name, "email": email}
    )
    print(response.text)

def send_multiple_messages(messages):
    for message in messages:
        send_message(message['name'], message['email'])

def get_all_messages():
    response = requests.get(API_URL)
    data = response.json()
    print(json.dumps(data, indent=2))
    return data

def get_last_message():
    response = requests.get(API_URL)
    data = response.json()
    if data:
        last = data[-1]
        print(json.dumps(last, indent=2))
    else:
        print("No messages found.")

if __name__ == "__main__":
    print("Enviando mensagem de teste...")
    send_message("Odair Marcelo", "odair@exemplo.com")
    
    print("\nBuscando mensagens gravadas...")
    get_all_messages()