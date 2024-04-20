#creating a dict,acessing and adding value
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.keys()

print(x) #before the change

car["color"] = "blue"

print(x) #after the change
y=car["color"]

print(y)

z = car.values()
print(z)

w = car.items()
print(w)
#it checks a elementin a dict
a= "brand" in car
print(a)