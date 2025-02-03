import requests 
import os
from dotenv import load_dotenv

load_dotenv()

access_token = os.getenv('ACCESS_TOKEN')
phone_number = os.getenv('PHONE_NUMBER')
recipient = os.getenv('RECIPIENT_PHONE')
whatsaap_url = os.getenv('WHATSAAP_URL')

headers = {
    "Authorization": f"Bearer {access_token}",
    "Content-Type": "application/json"
}

data = {
        "messaging_product": "whatsapp",
        "to": recipient,
        "type": "template",
        "template": { 
                    "name" :"saludo",
                    "language": { "code": "es" },
                "components": [
                {
                    "type": "header",
                    "parameters": [
                        {
                            "type": "image",
                            "image": { "link": "https://res.cloudinary.com/dnc8k8wwv/image/upload/v1735869010/destinations-235942_1280_sqdtc7.jpg" }
                        }
                    ]
                }
            ]   
            }
        } 


response = requests.post(whatsaap_url, json=data, headers=headers)
print(response.json()) 