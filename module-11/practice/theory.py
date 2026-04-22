import json
import pickle

product = {
    "id": 1,
    "name": "Product-1",
    "price": 900
}

json_text = json.dumps(product, indent=2)
print(json_text)

restored_product = json.loads(json_text)
print(restored_product)

with open("product.json", "w", encoding="utf-8") as f:
    json.dump(product, f, indent=2)

with open("product.json", "r", encoding="utf-8") as f:
    loaded_product = json.load(f)

print(loaded_product)


data = pickle.dumps(product)
print(data)

restored_pk1_product = pickle.loads(data)
print(restored_pk1_product)

with open("product.pk1", "wb") as f:
    pickle.dump(product, f)

with open("product.pk1", "rb") as f:
    loaded_product_pk1 = pickle.load(f)

print(loaded_product_pk1)