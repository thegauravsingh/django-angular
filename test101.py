import requests

print("simple get test")
print(requests.get("http://127.0.0.1:8000/").json())
print("get route by id test")
print(requests.get("http://127.0.0.1:8000/items/1").json())
print("get route by query params -- params used after ?")
print(requests.get("http://127.0.0.1:8000/items?name=Nails").json())
print("")
print("Adding an item via post route:")
print(
    requests.post(
        "http://127.0.0.1:8000/",
        json={"name": "Screwdriver", "price": 3.99, "count": 10, "id": 4, "category": "tools"},
    ).json()
)
print(requests.get("http://127.0.0.1:8000/").json())
print()

print("Updating an item via put route:")
print(requests.put("http://127.0.0.1:8000/update/0?count=9001").json())
print(requests.get("http://127.0.0.1:8000/").json())
print()

print("Deleting an item: via delete routing")
print(requests.delete("http://127.0.0.1:8000/delete/0").json())
print(requests.get("http://127.0.0.1:8000/").json())

print("# These requests work")
print(requests.get("http://127.0.0.1:8000/items?count=20").json())
print(requests.get("http://127.0.0.1:8000/items?category=tools").json())


print("# This request fails because 'ingredient' is not a valid category, as defined in the Category enum:")
print(requests.get("http://127.0.0.1:8000/items?category=ingredient").json())


print("# These request fail because count has to be an integer:")

print("# Here, validation occurs because of the specified type hints on the endpoint.")
print(requests.get("http://127.0.0.1:8000/items/?count=Hello").json())

print("# And here, because of Pydantic.")
print(
    requests.post(
        "http://127.0.0.1:8000/",
        json={"name": "Screwdriver", "price": 3.99, "count": 'Hello', "id": 4},
    ).json()
)
