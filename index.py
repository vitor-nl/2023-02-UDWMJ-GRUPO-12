import json
from classes import category, client, order, product, socialNetwork

with open("2023-02-UDWMJ-GRUPO-12\\database\\categories.json", "r") as categories_json:
    categories = json.load(categories_json)

with open("2023-02-UDWMJ-GRUPO-12\\database\\products.json", "r") as products_json:
    products = json.load(products_json)

with open("2023-02-UDWMJ-GRUPO-12\\database\\socialNetworks.json", "r") as socialNetworks_json:
    socialNetworks = json.load(socialNetworks_json)

def factory(array, uClass):
    return [uClass(item) for item in array]

def stepOne():
    factoryResult = factory(categories, category.Category)

    print("----------| Bem-Vindo a barraca do Seu Ze |----------")
    print("")
    print("--> Que tipo de produto voce esta procurando?")
    print("")
    for index, item in enumerate(factoryResult):
        print(f"{index + 1} - {item.name}")

    opção = input("--> Digite o numero da opção para seguir: ")
    # setOpStepOne(opção)
    # foward(1)

stepOne()
