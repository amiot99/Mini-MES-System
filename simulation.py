import time
import random
from functools import total_ordering
from itertools import accumulate

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
        self.quality_checked_batches = []

        for i in self.completed_batches:
            accumulator += i['total_quantity']
            batches_to_move.append(i['orders'])
            if accumulator >= 5000:
                print(
                    f"{Fore.CYAN}Batches have reached target. Moving to next phase in 3 seconds, Quality check{Style.RESET_ALL}")
                time.sleep(3)
                for orders_list in batches_to_move:
                    for order in orders_list:
                        if order.status == "Assembly":
                            order.update_status ("Quality Check")
                        order.display_info(max_origin_length)
                    self.quality_checked_batches.append({'orders':orders_list})
                        #time.sleep(.5)
                    batches_to_move = []
                    accumulator = 0
        return self.quality_checked_batches

    def packaging(self):
        print(f"{Fore.GREEN}Starting Packaging Phase…{Style.RESET_ALL}")
        packaging_accumulator = 0
        orders_to_package = []
        self.packaged_batches = []
        for qc_batches in self.quality_checked_batches:
            for order in qc_batches['orders']:
                if order.status == "Quality Check":
                    packaging_accumulator += order.quantity
                    orders_to_package.append(order)
                    if packaging_accumulator >= 5000:
                        break
            if packaging_accumulator >= 5000:
                break

        for order in orders_to_package:
            order.update_status("Packaged")
            order.display_info(max_origin_length)
            #time.sleep(.5)
            self.packaged_batches.append(order)

        print(f"{Fore.GREEN}All quality‑checked orders are now in Packaging.{Style.RESET_ALL}")

    def shipped(self):
        target_model = "Radeon 9070"
        accumulator = 0
        to_ship = []
        models = set(o.model for o in self.packaged_batches)
        for order in self.packaged_batches:
            if order.model == target_model:
                accumulator += order.quantity
                to_ship.append(order)
            if accumulator >= 5000:
                break
        for order in to_ship:
            order.update_status("Shipped")
            order.display_info(max_origin_length)
        print(f"{Fore.MAGENTA}Shipped batch for {target_model}.{Style.RESET_ALL}")





simulator = Simulator()
orders = simulator.batch()
max_origin_length = max(len(order.origin) for order in orders)
simulator.assembly_batch(orders)
simulator.quality_check()
simulator.packaging()
simulator.shipped()

