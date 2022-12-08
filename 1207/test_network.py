import network


def test_agent_receive_shipment():
    agent = network.Agent("A", 2, 5, 13)
    shipment = network.Shipment(agent, 10, 1)

    agent.receive_shipment(shipment)

    assert agent.backlog == 5
    assert agent.onorder == 3
    assert agent.inventory == 12


class MockAgent:
    def __init__(self, name, inventory, backlog, onorder):
        self.backlog = backlog
        self.onorder = onorder
        self.inventory = inventory

    def receive_shipment(self, shipment):
        self.onorder -= shipment.quantity
        self.inventory += shipment.quantity


def test_network_update():
    agent = MockAgent("A", 2, 5, 13)
    shipment1 = network.Shipment(agent, 10, 1)
    shipment2 = network.Shipment(agent, 10, 2)
    n = network.Network()
    n.shipments = [shipment1, shipment2]

    n.update()

    assert agent.backlog == 5
    assert agent.onorder == 3
    assert agent.inventory == 12
    assert len(n.shipments) == 1
    assert n.shipments[0].quantity == 10
    assert n.shipments[0].time_until_arrival == 1
