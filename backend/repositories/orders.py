from utils.database import execute_query

class OrderRepository:
    def find_all(self):
        query = """
            SELECT o.order_id, 
                   o.order_number, 
                   o.order_date, 
                   o.order_time, 
                   o.total_amount,
                   o.employee_id,
                   o.client_id
            FROM orders o
            ORDER BY o.order_id DESC
        """
        try:
            print("Выполняю запрос к orders...")
            result = execute_query(query, fetch=True)
            print(f"Запрос выполнен успешно. Получено строк: {len(result) if result else 0}")
            return result
        except Exception as e:
            print(f"!!! КРИТИЧЕСКАЯ ОШИБКА В REPOSITORY FIND_ALL: {e}")
            raise e

    def find_one(self, id):
        order_query = """
            SELECT o.order_id, o.order_number, o.order_date, o.order_time, 
                   o.total_amount, o.client_id, o.employee_id
            FROM orders o
            WHERE o.order_id = %s
        """
        order_results = execute_query(order_query, (id,), fetch=True)
        
        if not order_results:
            return None
        
        order = order_results[0]

        items_query = """
            SELECT oi.item_id, oi.dish_id, oi.quantity, oi.price, oi.total_amount,
                   d.article_number,
                   d.unit,
                   d.name as dish_name
            FROM order_items oi
            JOIN dishes d ON oi.dish_id = d.dish_id
            WHERE oi.order_id = %s
        """
        items = execute_query(items_query, (id,), fetch=True)

        clean_items = []
        for item in items:
            clean_item = {}
            for key, value in item.items():
                if hasattr(value, '__float__') and not isinstance(value, bool):
                    clean_item[key] = float(value)
                else:
                    clean_item[key] = value
            clean_items.append(clean_item)
            
        order['items'] = clean_items

        for key, value in order.items():
            if hasattr(value, '__float__') and not isinstance(value, bool):
                order[key] = float(value)
                
        return order

    def insert(self, order_data, items_data):
        order_query = """
            INSERT INTO orders (order_number, employee_id, client_id, order_date, order_time, total_amount)
            VALUES (%s, %s, %s, %s, %s, %s)
            RETURNING order_id
        """
        order_params = (
            order_data.get('order_number'),
            order_data.get('employee_id'),
            order_data.get('client_id'),
            order_data.get('order_date'),
            order_data.get('order_time'),
            order_data.get('total_amount')
        )
        order_result = execute_query(order_query, order_params, fetch=True)
        if not order_result:
            return None
            
        new_order_id = order_result[0]['order_id']
        
        if items_data:
            items_query = """
                INSERT INTO order_items (order_id, dish_id, quantity, price, total_amount)
                VALUES (%s, %s, %s, %s, %s)
            """
            for item in items_data:
                item_params = (
                    new_order_id,
                    item.get('dish_id'),
                    item.get('quantity'),
                    item.get('price'),
                    item.get('total_amount')
                )
                execute_query(items_query, item_params, fetch=False)
                
        return {"order_id": new_order_id}

    def update(self, id, order_data, items_data):
        order_query = """
            UPDATE orders 
            SET order_number = %s, employee_id = %s, client_id = %s, order_date = %s, order_time = %s, total_amount = %s
            WHERE order_id = %s
            RETURNING order_id
        """
        order_params = (
            order_data.get('order_number'),
            order_data.get('employee_id'),
            order_data.get('client_id'),
            order_data.get('order_date'),
            order_data.get('order_time'),
            order_data.get('total_amount'),
            id
        )
        order_result = execute_query(order_query, order_params, fetch=True)
        if not order_result:
            return None

        delete_items_query = "DELETE FROM order_items WHERE order_id = %s"
        execute_query(delete_items_query, (id,), fetch=False)

        if items_data:
            items_query = """
                INSERT INTO order_items (order_id, dish_id, quantity, price, total_amount)
                VALUES (%s, %s, %s, %s, %s)
            """
            for item in items_data:
                item_params = (
                    id,
                    item.get('dish_id'),
                    item.get('quantity'),
                    item.get('price'),
                    item.get('total_amount')
                )
                execute_query(items_query, item_params, fetch=False)

        return {"order_id": id}

    def delete(self, id):
        execute_query("DELETE FROM order_items WHERE order_id = %s", (id,), fetch=False)
        execute_query("DELETE FROM orders WHERE order_id = %s", (id,), fetch=False)
        return True