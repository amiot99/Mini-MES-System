import datetime
import colorama
from colorama import Fore, Style
colorama.init(autoreset=True)

class ProductionOrder:
    def __init__(self,order_id,model,maker,product_id,quantity,due_date,status):
        self.order_id = order_id
        self.model = model
        self.maker = maker
        self.product_id = product_id
        self.quantity = quantity
        self.due_date = due_date
        self.status = status
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def display_info(self):
        print(f"{Fore.RED}Order ID:{Style.RESET_ALL} {self.order_id},"
              f"{Fore.RED}Model:{Style.RESET_ALL} {self.model},"
              f"{Fore.RED}Maker:{Style.RESET_ALL} {self.maker},"
              f"{Fore.RED}Product_ID:{Style.RESET_ALL} {self.product_id}, "
              f"{Fore.RED}Quantity:{Style.RESET_ALL} {self.quantity}, "
              f"{Fore.RED}Due Date:{Style.RESET_ALL} {self.due_date},"
              f"{Fore.RED}Status:{Style.RESET_ALL} {self.status}, "
              f"{Fore.RED}Created at:{Style.RESET_ALL} {self.created_at}, "
              f"{Fore.RED}Updated at:{Style.RESET_ALL} {self.updated_at}")


    def update_status(self,status):
        self.status = status
        self.updated_at = datetime.datetime.now()
