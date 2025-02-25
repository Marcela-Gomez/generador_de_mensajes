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
                "name" :"additional_info",
                "language": { "code": "es" },
                "components": [
                    {
                    "type": "body",
                    "parameters": [
                            {
                                "type":"text",
                                "parameter_name":"info",
                                "text":" 🏠 Las ventanas de la cocina exterior están abiertas y puedes usarlas para acceder si es necesario. 🔒 Antes de finalizar tu estancia, asegúrate de cerrar todas las puertas y ventanas, apagar todas las luces interiores y exteriores, y dejar las llaves dentro de la casa."
                            },
                            {
                                "type":"text",
                                "parameter_name":"aparcamiento",
                                "text":"No hay garaje privado en el edificio, pero justo enfrente encontrarás un parking privado con un precio aproximado de 23 € por día."
                            },
                            {
                                "type":"text",
                                "parameter_name":"asistencia",
                                "text":"Si necesitas cualquier asistencia durante tu estancia o tienes alguna pregunta, no dudes en escribirnos. 📩 ¡Estamos aquí para ayudarte y asegurarnos de que tengas una experiencia inolvidable!",
                            },
                            {
                                "type":"text",
                                "parameter_name":"despedida",
                                "text":"¡Esperamos que disfrutes al máximo de tu estancia en Avenida de Montecarlo 10, 2E, Benidorm - Urbanización Ciudad de las Antenas y que te lleves grandes recuerdos de esta experiencia! 🏔️✨",
                            }
                    ],}
        ]   
    }
}
""" 
data = {
    "messaging_product": "whatsapp",
    "to": recipient,
    "type": "text",
    "text": {
        "body": "Hola, soy un bot de prueba ¿En qué puedo ayudarte?"
    }

} """
response = requests.post(whatsaap_url, json=data, headers=headers)
print(response.json()) 

