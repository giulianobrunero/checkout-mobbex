import requests
import json


'''
API CREDENTIALS
'''
API_URL = "https://api.mobbex.com/p/checkout"
# Your api key provider for mobbex.
API_KEY = "-----------------------------"
# Your access token provider for mobbex.
ACCESS_TOKEN = "-----------------------------"
# url to return after making payment.
RETURN_URL = "https://losfenicios.com.ar"
# url where mobbex notifies the status of the payment. (IPN: Instant payment notification)
WEBHOOK = "https://634826480b382d796c6aaf56.mockapi.io/api/v1/pagos"


'''
DATA OF SHOP
'''
NAME_SHOP = "Los Fenicios"
LOGO_SHOP = "https://losfenicios.com.ar/tienda/static/img/LosFenicios-verde-naranja-desktop.png"
DOMAIN_SHOP = "https://losfenicios.com.ar"


'''
DATA OF CUSTOMER
'''
email_customer = "demo@mobbex.com"
name_customer = "Cliente Demo"
identification_customer = "12123123"


'''
PURCHASE
'''
items = [
  {
    "image": "https://losfenicios.com.ar/productos/cache/ae/ee/aeee19077ab57474a05edbb80d967df3.webp", # Image of product, is a example.
    "quantity": 1,
    "description": "La orden del libertador",
    "total": 100.44
  },
]
total = "100.44"


'''
CHECKOUT SETTINGS
'''
description = "Checkout de Prueba"
reference = "260520210954"
currency = "ARS"
test = True
embed = True


'''
CHECKOUT THEME
'''
theme_type = "light"
background = "#FFFFFF"
showHeader = True
primary_colors = "#252525"


payload = json.dumps({
  "total": total,
  "description": description,
  "reference": reference,
  "currency": currency,
  "test": test,
  "return_url": RETURN_URL,
  "webhook": WEBHOOK,
  "items": items,
  "options": {
    "theme": {
      "type": theme_type,
      "background": background,
      "showHeader": showHeader,
      "header": {
        "name": NAME_SHOP,
        "logo": LOGO_SHOP
      },
      "colors": {
        "primary": primary_colors
      }
    },
    "embed": embed,
    "domain": DOMAIN_SHOP
  },
  "customer": {
    "email": email_customer,
    "name": name_customer,
    "identification": identification_customer
  }
})

headers = {
  'x-api-key': API_KEY,
  'x-access-token': ACCESS_TOKEN,
  'Content-Type': 'application/json'
}

response = requests.request("POST", API_URL, headers=headers, data=payload)

print(json.dumps(response.json(), sort_keys=True, indent=4))

print('url_pago: ', response.json()['data']['url'])
