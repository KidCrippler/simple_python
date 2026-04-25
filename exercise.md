# Backend Exercise: VIP Customer Failure Report

## Overview

You are given a small SQLite database (`shop.db`) containing two tables: `customers` and `orders`.

Your task is to build a Python script that generates a report of VIP customers who had failed orders.

---

## Requirements

1. Connect to the provided SQLite database.
2. Query all **VIP customers** (`is_vip = 1`) who have at least one **failed order**.
3. For each such customer, compute the number of failed orders.
4. For each customer, enrich the data by calling the external API:
https://jsonplaceholder.typicode.com/users/<customer_id>

and extract:
- `email`
- `company.name`

5. Return a list of dictionaries in the following format:

{
 "customer_name": "...",
 "failed_order_count": ...,
 "email": "...",
 "company": "..."
}
