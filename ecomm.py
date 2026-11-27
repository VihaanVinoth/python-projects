import csv
import json


def load_catalog(filepath):
    catalog = {}
    try:
        with open(filepath, mode="r") as file:
            catalog_reader = csv.DictReader(file)
            if catalog_reader.fieldnames:
                catalog_reader.fieldnames = [
                    field.strip() for field in catalog_reader.fieldnames
                ]
            for row in catalog_reader:
                sku = row["sku"].strip()
                catalog[sku] = {
                    "product_name": row["product_name"].strip(),
                    "unit_price": float(row["unit_price"].strip()),
                    "category": row["category"].strip(),
                }
    except FileNotFoundError:
        print(f"Error: File '{filepath}' not found.")
        raise
    except KeyError as e:
        print(f"Error: Missing expected CSV header column: {e}")
        raise
    except ValueError as e:
        print(f"Error extracting catalog fields: {e}")
        raise
    return catalog


def run_etl():
    try:
        catalog = load_catalog("product_catalog.csv")
    except Exception:
        print("ETL pipeline aborted due to catalog failing.")
        return

    try:
        with open("raw_invoices.json", mode="r") as file:
            invoices = json.load(file)
    except FileNotFoundError:
        print("Error: file 'raw_invoices.json' not found.")
        return
    except json.JSONDecodeError as e:
        print(f"Error: JSON Malformed in 'raw_invoices.json': {e}")
        return

    valid_summaries = []
    valid_items = []
    quarantine_log = []

    for record in invoices:
        order_id = record.get("order_id")
        customer = record.get("customer")
        date = record.get("date")
        items = record.get("items", [])

        if not order_id:
            quarantine_log.append(
                {
                    "order_id": None,
                    "error_reason": "MISSING_ORDER_ID",
                    "raw_record": record,
                }
            )
            continue

        if not str(customer).strip():
            quarantine_log.append(
                {
                    "order_id": order_id,
                    "error_reason": "MISSING_CUSTOMER_NAME",
                    "raw_record": record,
                }
            )
            continue

        total_items = 0
        total_amount = 0.0
        line_items = []
        is_corrupt = False
        failure_msg = ""

        for item in items:
            sku = item.get("sku")
            raw_quantity = item.get("quantity")

            if sku not in catalog:
                is_corrupt = True
                failure_msg = "SKU_NOT_FOUND"
                break

            try:
                qty = "".join(
                    c for c in str(raw_quantity) if c.isdigit() or c == "-"
                )
                quantity = int(qty)
                if quantity <= 0:
                    raise ValueError("Quantity must be greater than zero.")
            except ValueError:
                is_corrupt = True
                failure_msg = "INVALID_QUANTITY"
                break

            product_details = catalog[sku]
            unit_price = product_details["unit_price"]
            line_total = round(unit_price * quantity, 2)

            total_items += quantity
            total_amount += line_total

            line_items.append(
                {
                    "order_id": order_id,
                    "sku": sku,
                    "date": date,
                    "product_name": product_details["product_name"],
                    "category": product_details["category"],
                    "quantity": quantity,
                    "line_total": line_total,
                }
            )

        if is_corrupt:
            quarantine_log.append(
                {
                    "order_id": order_id,
                    "error_reason": failure_msg,
                    "raw_record": record,
                }
            )
        else:
            valid_summaries.append(
                {
                    "order_id": order_id,
                    "customer": customer.strip(),
                    "date": date,
                    "total_items": total_items,
                    "total_amount": round(total_amount, 2),
                }
            )
            valid_items.extend(line_items)

    with open("orders_summary.csv", mode="w", newline="") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=[
                "order_id",
                "customer",
                "date",
                "total_items",
                "total_amount",
            ],
        )
        writer.writeheader()
        writer.writerows(valid_summaries)

    with open("orders_items.csv", mode="w", newline="") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=[
                "order_id",
                "sku",
                "date",
                "product_name",
                "category",
                "quantity",
                "line_total",
            ],
        )
        writer.writeheader()
        writer.writerows(valid_items)

    with open("quarantine_log.json", mode="w") as file:
        json.dump(quarantine_log, file, indent=2)


if __name__ == "__main__":
    run_etl()
