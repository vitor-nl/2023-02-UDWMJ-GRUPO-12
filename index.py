import importlib

module = importlib.import_module("./categories.json")
module = importlib.import_module("./products.json")
module = importlib.import_module("./socialNetworks.json")

categories = module.categories
products = module.products
socialNetworks = module.socialNetworks

print(categories)