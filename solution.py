import sqlite3
import requests


def fetch_crm_customer(customer_id):
    response = requests.get(
        f"https://jsonplaceholder.typicode.com/users/{customer_id}"
    )
    response.raise_for_status()
    return response.json()


def get_failed_vip_customers():
    conn = sqlite3.connect("shop.db")
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            c.id,
            c.name,
            COUNT(o.id) AS failed_order_count
        FROM customers c
        JOIN orders o ON c.id = o.customer_id
        WHERE c.is_vip = 1
          AND o.status = 'failed'
        GROUP BY c.id, c.name
    """)

    failed_vips = cursor.fetchall()

    result = [
        {
            "customer_name": row["name"],
            "failed_order_count": row["failed_order_count"],
            "email": crm["email"],
            "company": crm["company"]["name"]
        }
        for row in failed_vips
        for crm in [fetch_crm_customer(row["id"])]
    ]

    conn.close()
    return result


print(get_failed_vip_customers())
