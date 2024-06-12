import datetime

class Client:

    def __init__(self, id: str, full_name: str):
        self.id = id
        self.full_name = full_name
        self.cart = []
        self.transactions = []

    def add_to_cart(self, item: 'Item'):
        self.cart.append(item)

class Item:

    def __init__(self, item_name: str, price: float):
        self.item_name = item_name
        self.price = price

class Transaction:

    def __init__(self, client: 'Client'):
        self.client = client
        self.items = client.cart.copy()
        self.time_stamp = datetime.datetime.now()
        client.transactions.append(self)
        client.cart.clear()

# Create some clients
clients = []

clients.append(Client("001", "Mary Poppins"))
clients.append(Client("002", "Anna Karenina"))
clients.append(Client("003", "Jane Eyre"))

# Create some items that are available at the shop to purchase
items = []

items.append(Item("washing machine", 599))
items.append(Item("smartphone", 849))
items.append(Item("headphones", 219))
items.append(Item("printer", 109))
items.append(Item("refrigerator", 1199))
items.append(Item("toaster", 49))
items.append(Item("smart watch", 349))
items.append(Item("e-bike", 2449))
items.append(Item("blender", 89))

# clients add items to cart
clients[0].add_to_cart(items[1])
clients[0].add_to_cart(items[2])
Transaction(clients[0])

clients[1].add_to_cart(items[2])
clients[1].add_to_cart(items[4])
Transaction(clients[1])

clients[2].add_to_cart(items[6])
clients[2].add_to_cart(items[5])
Transaction(clients[2])

clients[0].add_to_cart(items[5])
clients[0].add_to_cart(items[7])
Transaction(clients[0])

# print clients, their transactions and purchased items
for client in clients:
    print(f"Client: {client.full_name} (ID: {client.id})")
    if not client.transactions:
        print("     No transactions.")
    for transaction_index, transaction in enumerate(client.transactions, start=1):
        print(f"    Transaction {transaction_index} at {transaction.time_stamp}:")
        for item in transaction.items:
            print(f"        - {item.item_name}: {item.price} €")
    print()