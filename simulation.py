import time
import random
import pycountry
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

simulator = Simulator()
orders = simulator.batch()

max_origin_length = max(len(order.origin) for order in orders)

for order in orders:
    order.display_info(max_origin_length)
    time.sleep(0)


  def batch_processing(self)
      batches = {}
      for order in orders:
          if order.model not in batches:
              batches[order.model] = {'orders':[],'total_quantity': 0}

          else:
              batches = batches["order.model"]






