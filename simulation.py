import time
import random
import pycountry
from colorama import Fore, Style
from models import ProductionOrder

countries = [c.name for c in pycountry.countries]
"""models = ["Radeon 9070","Radeon 9070xt", "Radeon 7900 xtx"]"""


class Simulator:
    def batch(self):
        orders = []
        order_id = 1
        for j in range(5):
            for i in range(1,11):
                order = (ProductionOrder(order_id, "Radeon 9070","AMD", "AMD-9070-000", 100, "2025-05-01","Created",random.choice(countries)))
                orders.append(order)
                order_id += 1
        return orders

    def batch_processing(self,orders):
        batches = {}
        for order in orders:
            if order.model not in batches:
                batches[order.model] = {'orders':[],'total_quantity': 0}

            batches[order.model]['orders'].append(order)
            batches[order.model]['total_quantity'] += (order.quantity)

            if batches[order.model]['total_quantity'] >= 1000:
                print(
                    f"\n{Fore.CYAN}Batch for model '{order.model}' reached 1000 units. Orders BEFORE update:{Style.RESET_ALL}")

                max_origin_length = max(len(o.origin) for o in batches[order.model]['orders'])
                for o in batches[order.model]['orders']:
                    o.display_info(max_origin_length)

                for batch in batches[order.model]['orders']:
                    batch.update_status("Assembly")
                print(f"{Fore.CYAN}The batch has reached the required quantity. Moving to next phase, Assembly{Style.RESET_ALL}")
                for o in batches[order.model]['orders']:
                    o.display_info(max_origin_length)
                batches[order.model] = {'orders': [], 'total_quantity': 0}



simulator = Simulator()
orders = simulator.batch()
max_origin_length = max(len(order.origin) for order in orders)
time.sleep(0)
simulator.batch_processing(orders)

