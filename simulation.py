import time
import random
from functools import total_ordering

import pycountry
from colorama import Fore, Style
from models import ProductionOrder

countries = [c.name for c in pycountry.countries]
"""models = ["Radeon 9070","Radeon 9070xt", "Radeon 7900 xtx"]"""


class Simulator:
    def __init__(self):
        self.completed_batches = []



    def batch(self):
        orders = []
        order_id = 1
        for j in range(5):
            for i in range(1,11):
                order = (ProductionOrder(order_id, "Radeon 9070","AMD", "AMD-9070-000", 100, "2025-05-01","Created",random.choice(countries)))
                orders.append(order)
                #time.sleep(0.01)
                order_id += 1
        return orders

    def assembly_batch(self,orders):
        batches = {}
        for order in orders:
            if order.model not in batches:
                batches[order.model] = {'orders':[],'total_quantity': 0}

            batches[order.model]['orders'].append(order)
            batches[order.model]['total_quantity'] += order.quantity

            if batches[order.model]['total_quantity'] >= 1000:
                print(
                    f"{Fore.CYAN}Batch for model '{order.model}' reached 1000 units. Orders BEFORE update:{Style.RESET_ALL}")

                for o in batches[order.model]['orders']:
                    o.display_info(max_origin_length)
                    #time.sleep(0.5)

                for batch in batches[order.model]['orders']:
                    batch.update_status("Assembly")
                print(f"{Fore.CYAN}The batch has reached the required quantity. Moving to next phase, Assembly{Style.RESET_ALL}")
                for o in batches[order.model]['orders']:
                    o.display_info(max_origin_length)
                    #time.sleep(0.5)
                self.completed_batches.append(batches[order.model])

                batches[order.model] = {'orders': [], 'total_quantity': 0}
        return batches, self.completed_batches




    def quality_check(self):
        accumulator = 0
        batches_to_move = []
        for i in self.completed_batches:
            accumulator += i['total_quantity']
            batches_to_move.append(i['orders'])
            if accumulator >= 5000:
                print(
                    f"{Fore.CYAN}Batches have reached target. Moving to next phase in 5 seconds, Quality check{Style.RESET_ALL}")
                time.sleep(5)
                for orders_list in batches_to_move:
                    for order in orders_list:
                        if order.status == "Assembly":
                            order.update_status ("Quality Check")
                        order.display_info(max_origin_length)
                        #time.sleep(.5)




simulator = Simulator()
orders = simulator.batch()
max_origin_length = max(len(order.origin) for order in orders)
simulator.assembly_batch(orders)
simulator.quality_check()

