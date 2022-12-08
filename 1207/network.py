class Shipment:
    def __init__(self, destination, quantity, time_until_arrival):
        self.destination = destination
        self.quantity = quantity
        self.time_until_arrival = time_until_arrival

    def __repr__(self):
        return f"Shipment({self.destination}, {self.quantity}, {self.time_until_arrival})"


class Agent:
    def __init__(self, name, inventory, backlog, onorder):
        self.name = name
        self.__inventory = inventory
        self.__backlog = backlog
        self.__onorder = onorder

    def get_inventory(self):
        return self.__inventory

    def set_inventory(self, value):
        if value < 0:
            raise ValueError("Inventory cannot be negative")

        self.__inventory = value

    def __repr__(self):
        return f"Agent({self.name}, {self.inventory}, {self.backlog}, {self.onorder})"

    def receive_shipment(self, shipment):
        self.onorder -= shipment.quantity + 1
        self.inventory += shipment.quantity


class Network():
    def __init__(self):
        self.shipments = []

    def update(self):
        for shipment in self.shipments:
            shipment.time_until_arrival -= 1
            if shipment.time_until_arrival == 0:
                shipment.destination.receive_shipment(shipment)
        self.shipments = [
            shipment for shipment in self.shipments if shipment.time_until_arrival > 0]
