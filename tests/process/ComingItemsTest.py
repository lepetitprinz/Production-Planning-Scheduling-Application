
from m4.process.Item import Item
from m4.process.ComingItems import ComingItems


if __name__ == '__main__':

    coming_items: ComingItems = ComingItems()

    coming_items.init(moving_time=10)

    coming_items.receive(item=Item())
    coming_items.receive(item=Item())
    coming_items.receive(item=Item())

    coming_items.tick()

    coming_items.receive(item=Item())
    coming_items.receive(item=Item())

    coming_items.tick()
    coming_items.tick()

    coming_items.receive(item=Item())
    coming_items.receive(item=Item())
    coming_items.receive(item=Item())
    coming_items.receive(item=Item())

    coming_items.tick()
    coming_items.tick()
    coming_items.tick()
    coming_items.tick()
    coming_items.tick()
    coming_items.tick()
    coming_items.tick()
    coming_items.tick()

    arrived_items1: list = coming_items.get_arriving_items()

    coming_items.tick()
    coming_items.tick()

    arrived_items2: list = coming_items.get_arriving_items()

    arrived_items3: list = coming_items.get_arriving_items()

    coming_items.tick()

    print("DEBUG POINT")
