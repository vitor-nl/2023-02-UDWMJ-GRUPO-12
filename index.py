import json
from classes import category, client, order, product, socialNetworkC

with open("2023-02-UDWMJ-GRUPO-12\\database\\categories.json", "r") as categories_json:
    categories = json.load(categories_json)

with open("2023-02-UDWMJ-GRUPO-12\\database\\products.json", "r") as products_json:
    products = json.load(products_json)

with open("2023-02-UDWMJ-GRUPO-12\\database\\socialNetworks.json", "r") as socialNetworks_json:
    socialNetworks = json.load(socialNetworks_json)

def factory(array, uClass):
    return [uClass(item) for item in array]

def stepOne(setOpStepOne, foward):
    factoryResult = factory(categories, category.Category)

    print("----------| Bem-Vindo a barraca do Seu Ze |----------")
    print("")
    print("--> Que tipo de produto voce esta procurando?")
    print("")
    for index, item in enumerate(factoryResult):
        print(f"{index + 1} - {item.name}")

    opcao = input("--> Digite o numero da opção para seguir: ")
    setOpStepOne(opcao)
    foward(1)

def stepTwo(opStepOne, setOpStepTwo, foward):
  factoryResult = factory(products, product.Product)
  productsCategory = [
      el for el in factoryResult if el.category_id == int(opStepOne) - 1
  ]

  print("")
  print("--> Otima escolha, temos excelentes produtos nessa categoria")
  print("")
  print("--> Temos os seguintes produtos hoje: ")
  print("")
  for index, el in enumerate(productsCategory):
    print(f"{index + 1} - {el.name}")

  print("")
  opcao = input("--> Digite o numero da opção para seguir: ")
  setOpStepTwo(productsCategory[int(opcao) - 1])
  foward(2)

def stepThree(opStepTwo, setOpStepThree, foward):
  print("")
  opcao = input("--> Otima escolha! e quantas unidades de " + opStepTwo.name + " voce vai querer?")
  setOpStepThree(opcao)
  foward(3)

def stepFour(setOpStepFour, foward):
    clientRegister = client.Client()

    clientRegister.first_name = input("--> Qual o seu primeiro nome? ")
    clientRegister.last_name = input("--> Qual o seu ultimo nome? ")
    clientRegister.address = input("--> Qual o seu endereco? ")
    clientRegister.phone = input("--> Qual o seu celular? ")
    clientRegister.email = input("--> Qual o seu email? ")

    wantNetwork = input("--> Gostaria de nos informar uma rede social? (Digite 1 para Sim e 2 para Nao) ")
    setOpStepFour(clientRegister)

    if wantNetwork == "1":
        foward(4)
    elif wantNetwork == "2":
        foward(5)
    else:
        print("Erro")

def stepFive(opStepFour, setOpStepFour, foward):
    factoryResult = factory(socialNetworks, socialNetworkC.SocialNetworkC)

    print("")
    print("--> Por questão do trabalho, qual dessas redes sociais voce gosta mais?")
    print("")
    for index, el in enumerate(factoryResult):
        print(f"{index + 1} - {el.name}")

    opcao = input("--> Digite o numero da opção para seguir: ")
    temp = opStepFour
    temp["social_network_id"] = opcao
    setOpStepFour(temp)

    foward(5)

def stepSix(opStepTwo, opStepThree, opStepFour, foward):
    orderTemp = order.Order()

    orderTemp.client_id = opStepFour["id"]
    orderTemp.products = opStepTwo["name"]
    orderTemp.total_price = opStepTwo["unitary_price"] * opStepThree

    print("")
    print("Otimo! aqui está o seu pedido")
    print("")
    print("Numero do Pedido: ", orderTemp.id)
    print("Numero do cliente: ", orderTemp.client_id)
    print("Nome do Produto: ", orderTemp.products)
    print("Valor do pedido: ", orderTemp.total_price)
    print("")
    print("----------| Volte Sempre |----------")

    # Chama a próxima função no fluxo do programa
    foward(6)

def initProcess():
    global opStepOne
    global opStepTwo
    global opStepThree
    global opStepFour
    global currentStep

    opStepOne = None
    opStepTwo = None
    opStepThree = None
    opStepFour = None
    currentStep = 0

    def setOpStepOne(value):
        global opStepOne
        opStepOne = value

    def setOpStepTwo(value):
        global opStepTwo
        opStepTwo = value

    def setOpStepThree(value):
        global opStepThree
        opStepThree = value

    def setOpStepFour(value):
        global opStepFour
        opStepFour = value

    def foward(new_value): 
        global currentStep
        currentStep = new_value

    while currentStep != 6:
        if currentStep == 0:
            stepOne(setOpStepOne, foward)
        elif currentStep == 1:
            stepTwo(opStepOne, setOpStepTwo, foward)
        elif currentStep == 2:
            stepThree(opStepTwo, setOpStepThree, foward)
        elif currentStep == 3:
            stepFour(opStepThree, setOpStepFour, foward)
        elif currentStep == 4:
            stepFive(opStepFour, setOpStepFour, foward)
        elif currentStep == 5:
            stepSix(opStepTwo, opStepThree, opStepFour, foward)

initProcess()
