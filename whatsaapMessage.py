import requests 
import os
from dotenv import load_dotenv
import pandas as pd
import json
load_dotenv()

access_token = os.getenv('ACCESS_TOKEN')
phone_number = os.getenv('PHONE_NUMBER')
recipient = os.getenv('RECIPIENT_PHONE')
whatsaap_url = os.getenv('WHATSAAP_URL')

headers = {
    "Authorization": f"Bearer {access_token}",
    "Content-Type": "application/json"
}
""" 
message_data = pd.read_csv('message_data.csv', sep=";", usecols=['tittle','name','address','address_detail','checkin','checkout','wifi','ruler1','ruler2','Deposito','step1','step2','step3','aparcamiento','asistencia','info','despedida','Calefaccion','duchas','mas informacion'])

for i, row in message_data.iterrows():
    data1 = {
        "messaging_product": "whatsapp",
        "to": recipient,
        "type": "template",
        "template": { 
                    "name" :"accommodation_details",
                    "language": { "code": "es" },
                    "components": [
                        {
                            "type": "header",
                            "parameters": [
                                {
                                    "type":"text",
                                    "parameter_name":"tittle",
                                    "text":row['tittle']
                                }
                            ],
                        },
                        {
                        "type": "body",
                        "parameters": [
                                {
                                    "type":"text",
                                    "parameter_name":"name",
                                    "text":row['name']
                                },
                                {
                                    "type":"text",
                                    "parameter_name":"address",
                                    "text":row['address']
                                },{
                                    "type":"text",
                                    "parameter_name":"address_details",
                                    "text":row['address_detail']
                                },
                                {
                                    "type":"text",
                                    "parameter_name":"ruler1",
                                    "text":row['ruler1']
                                },
                                {
                                    "type":"text",
                                    "parameter_name":"ruler2",
                                    "text":row['ruler2']
                                }, 
                                {
                                    "type":"text",
                                    "parameter_name":"checkin",
                                    "text":row['checkin']
                                },
                                {
                                    "type":"text",
                                    "parameter_name":"checkout",
                                    "text":row['checkout']
                                },
                                {
                                    "type":"text",
                                    "parameter_name":"wifi",
                                    "text":row['wifi']
                                },
                                {
                                    "type":"text",
                                    "parameter_name":"deposito",
                                    "text":row['Deposito']
                                }
                        ],}
            ]   
        }
    }
    data2 = {
        "messaging_product": "whatsapp",
        "to": recipient,
        "type": "template",
        "template": { 
                    "name" :"access",
                    "language": { "code": "es" },
                    "components": [
                        {
                        "type": "body",
                        "parameters": [
                                {
                                    "type":"text",
                                    "parameter_name":"step1",
                                    "text":row["step1"]
                                },
                                {
                                    "type":"text",
                                    "parameter_name":"step2",
                                    "text":row["step2"]
                                },
                                {
                                    "type":"text",
                                    "parameter_name":"step3",
                                    "text":row["step3"]
                                }
                        ],}
            ]   
        }
    }

    data3={
        "messaging_product": "whatsapp",
        "to": recipient,
        "type": "template",
        "template": { 
                    "name" :"addtional_information",
                    "language": { "code": "es" },
                    "components": [
                        {
                        "type": "body",
                        "parameters": [
                                {
                                    "type":"text",
                                    "parameter_name":"information",
                                    "text":row['info']
                                },
                                {
                                    "type":"text",
                                    "parameter_name":"parking",
                                    "text":row['aparcamiento']
                                },
                                {
                                    "type":"text",
                                    "parameter_name":"attendance",
                                    "text":row['asistencia']
                                },
                                {
                                    "type":"text",
                                    "parameter_name":"bye",
                                    "text":row['despedida']
                                }
                        ],}
            ]   
        }
    }
    if pd.isna(row['Calefaccion']) or pd.isna(row['duchas']) or pd.isna(row["mas informacion"]):
        data4 = ""
    else:
        data4 ={
            "messaging_product": "whatsapp",
            "to": recipient,
            "type": "template",
            "template": { 
                        "name" :"ski",
                        "language": { "code": "es" },
                        "components": [
                            {
                            "type": "body",
                            "parameters": [
                                    {
                                        "type":"text",
                                        "parameter_name":"heating",
                                        "text":row['Calefaccion']
                                    },
                                    {
                                        "type":"text",
                                        "parameter_name":"bathroom",
                                        "text":row['duchas']
                                    },
                                    {
                                        "type":"text",
                                        "parameter_name":"information",
                                        "text":row['mas informacion']
                                    }
                            ],}
                ]   
            }
        }
    with open("mesages.json", "a", encoding="utf-8") as json_file:
        json.dump(data1, json_file, ensure_ascii=False, indent=4)
        json_file.write("\n")  # Salto de línea para separar los objetos
        json.dump(data2, json_file, ensure_ascii=False, indent=4)
        json_file.write("\n")
        json.dump(data3, json_file, ensure_ascii=False, indent=4)
        json_file.write("\n")
        if data4 != "":
            json.dump(data4, json_file, ensure_ascii=False, indent=4)
            json_file.write("\n") """

data = {
    "messaging_product": "whatsapp",
    "to": recipient,
    "type": "text",
    "text": {
        "body": "🔥  Calefacción \nLa casa estará caliente a tu llegada. La calefacción está programada para mantener 22°C de 9:00 a 22:00 y 18°C por la noche, pero puedes ajustarlo manualmente desde el termostato del salón. 🪟 Ventanas y contraventanas: ✔️ Las contraventanas están abiertas y fijadas. No cerrarlas. ✔️ Cada habitación tiene persianas y mosquiteros, úsalos si lo necesitas. \n \n🚿  Duchas\nLos grifos están cambiados: 🔵 Símbolo azul = agua caliente 🔴 Símbolo rojo = agua fría\n \n❓ Mas información\nAntes de salir, por favor: 🛏️ Sábanas y toallas usadas: Deja todas las sábanas, fundas de edredón, fundas de almohada y toallas en el baño grande de abajo para que el equipo de limpieza pueda llevarlas a la tintorería."
    }

} 
response = requests.post(whatsaap_url, json=data, headers=headers)
print(response.json()) 

