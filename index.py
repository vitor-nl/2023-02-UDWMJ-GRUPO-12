import json
from classes import category
from classes import client
from classes import order
from classes import product
from classes import socialNetwork

with open("2023-02-UDWMJ-GRUPO-12\database\categories.json", "r") as categories_json:
    categories = json.load(categories_json)

with open("2023-02-UDWMJ-GRUPO-12\database\products.json", "r") as products_json:
    products = json.load(products_json)

with open("2023-02-UDWMJ-GRUPO-12\database\socialNetworks.json", "r") as socialNetwork_json:
    socialNetwork = json.load(socialNetwork_json)
