import time
from models import ProductionOrder

order = ProductionOrder(
    order_id=1,
        model="Radeon RX 6800",
        maker="AMD",
        product_id="AMD-6800-001",
        quantity=100,
        due_date="2025-04-15",
        status="Created"
)

order2 = ProductionOrder(
    order_id=2,
    model="Radeon 9070",
    maker="AMD",
    product_id="AMD-9070-001",
    quantity=100,
    due_date="2025-05-01",
    status="Created"
)

order3 = ProductionOrder(
    order_id=3,
    model="Radeon 9070XT",
    maker="AMD",
    product_id="AMD-9070XT-001",
    quantity=100,
    due_date="2025-05-05",
    status="Created"
)
order.display_info()
order2.display_info()
order3.display_info()
time.sleep(5)
order.update_status("Assembly")
order2.update_status("Assembly")
order3.update_status("Assembly")
order.display_info()
order2.display_info()
order3.display_info()