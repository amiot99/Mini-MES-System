import datetime
import colorama
from colorama import Fore, Style
colorama.init(autoreset=True)

class ProductionOrder:
    def __init__(self,order_id,model,maker,product_id,quantity,due_date,status,origin):
        self.order_id = order_id
        self.model = model
        self.maker = maker
        self.product_id = product_id
        self.quantity = quantity
        self.due_date = due_date
        self.status = status
        self.origin = origin
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def display_info(self, origin_width):
        if self.status == "Assembly":
            status_str = f"{Fore.CYAN}{self.status:<13}{Style.RESET_ALL}"
        elif self.status == "Quality Check":
            status_str = f"{Fore.YELLOW}{self.status:<13}{Style.RESET_ALL}"
        elif self.status == "Packaged":
            status_str = f"{Fore.GREEN}{self.status:<13}{Style.RESET_ALL}"
        elif self.status == "Shipped":
            status_str = f"{Fore.MAGENTA}{self.status:<13}{Style.RESET_ALL}"
        else:
            status_str = self.status


        print(f"{Fore.RED}{'Order ID:' :<9}{Style.RESET_ALL}{self.order_id:<5}"
              f"{Fore.RED}{'Model:' :<6}{Style.RESET_ALL} {self.model:<12}"
              f"{Fore.RED}{'Maker:':<6}{Style.RESET_ALL} {self.maker:<4}"
              f"{Fore.RED}{'Product_ID:':<11}{Style.RESET_ALL} {self.product_id:<13}"
              f"{Fore.RED}{'Quantity:':<10}{Style.RESET_ALL}{self.quantity:<5}"
              f"{Fore.RED}{'Due Date:':<9}{Style.RESET_ALL} {self.due_date:<11}"
              f"{Fore.RED}{'Status:':<8}{Style.RESET_ALL}{status_str:<13} "
              f"{Fore.RED}{'Origin:':<7}{Style.RESET_ALL} {self.origin:<{origin_width}} "
              f"{Fore.RED}{'Created at:':<12}{Style.RESET_ALL}{str(self.created_at):<27}" 
              f"{Fore.RED}{'Updated at:':<12}{Style.RESET_ALL}{str(self.updated_at):<27}")

    def update_status(self,status):
        self.status = status
        self.updated_at = datetime.datetime.now()
