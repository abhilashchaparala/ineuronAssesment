with open ("example.txt", "r") as file:
    data = file.read()
data = data.replace('placement','screening')
print(data)