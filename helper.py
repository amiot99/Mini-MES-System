import sqlite3
import datetime

def log_order_event(order, new_status):
    connection = sqlite3.connect("order_log.db")
    cursor = connection.cursor()

    create_table_query = """
    CREATE TABLE IF NOT EXISTS order_logs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        order_id INTEGER,
        model TEXT,
        maker TEXT,
        product_id TEXT,
        quantity INTEGER,
        due_date TEXT,
        status TEXT,
        origin TEXT,
        created_at TEXT,
        updated_at TEXT,
        log_timestamp TEXT
    );
    """

    cursor.execute(create_table_query)
    connection.commit()

    # Get the current timestamp for when the event is logged.
    log_ts = datetime.datetime.now().isoformat()

    insert_query = """
      INSERT INTO order_logs (
          order_id, model, maker, product_id, quantity, due_date,
          status, origin, created_at, updated_at, log_timestamp
      ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
      """

    data_tuple = (
        order.order_id,
        order.model,
        order.maker,
        order.product_id,
        order.quantity,
        order.due_date,
        new_status,  # This is the status we’re logging.
        order.origin,
        order.created_at.isoformat() if hasattr(order.created_at, "isoformat") else order.created_at,
        order.updated_at.isoformat() if hasattr(order.updated_at, "isoformat") else order.updated_at,
        log_ts
    )

    cursor.execute(insert_query, data_tuple)
    connection.commit()
    connection.close()