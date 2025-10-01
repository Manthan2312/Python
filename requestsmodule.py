import requests
import os
data=requests.get("https://www.pensador.com/")
print(data.text)


