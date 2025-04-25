class Client:
    def __init__(self, name, phone, email=None):
        self.name = name
        self.phone = phone
        self.email = email


def show_clients(clients):
    for client in clients:
        print("name:", client.name)
        print("phone:", client.phone)
        print("email:", client.email)
        print()
        print()


client_storage = []

n = int(input("Сколько пользователей создать:"))
for i in range(1, n+1):
    print("client number is:", i)
    name = input("name:")
    phone = input("phone:")
    email = input("email:")
    client = Client(name, phone, email)
    client_storage.append(client)


show_clients(client_storage)