
import datetime

from m4.process.Item import Item
from m4.process.ProcessLot import ProcessLot
from m4.process.Lot import Lot


if __name__ == '__main__':

    items: list = []

    process_lot: ProcessLot = ProcessLot()
    process_lot.init(
        info={
            '': 1
        }
    )

    for i in range(10):
        items.append(Item())

    for i in range(10):
        lot: Lot = Lot(item=items[i],
                       time_index=0,
                       date=datetime.datetime(2020, 4, 17),
                       length=3)
        lot.init(move_time=3, queue_time=5, setup_time=2, process_time=3)
        process_lot.put(lot=lot)

    process_lot.run()
    process_lot.run()
    process_lot.run()
    process_lot.run()
    process_lot.run()
    process_lot.run()
    process_lot.run()
    process_lot.run()
    process_lot.run()

    # Finished
    process_lot.run()

    print("DEBUGGING POINT")
