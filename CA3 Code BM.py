class StockControl:
    def __init__(self):
        self.stock = []

    def add_item(self, item_name, item_type, expiration_date, initial_quantity):
        item = {
            'id': len(self.stock) + 1,
            'name': item_name,
            'type': item_type,
            'expiration_date': expiration_date,
            'quantity': initial_quantity,
        }
        self.stock.append(item)

    def view_items(self):
        for item in self.stock:
            print(f"{item['id']}. {item['name']} ({item['type']}) - Expires on {item['expiration_date']} - "
                  f"Stock: {item['quantity']}")
   
    def delete_item(self, item_id):
        for item in self.stock:
            if item['id'] == item_id:
                self.stock.remove(item)
                print(f"Item {item_id} removed from stock.")
                return

        print(f"No item found with ID {item_id}.")

        print(f"No item found with ID {item_id}.")
    def add_to_basket(self, item_id, quantity):
        selected_item = next((item for item in self.stock if item['id'] == item_id), None)
        if selected_item and selected_item['quantity'] >= quantity > 0:
            total_cost = self.calculate_price(selected_item['type'], quantity)
            selected_item['quantity'] -= quantity
            return {'name': selected_item['name'], 'quantity': quantity, 'total_cost': total_cost}
        else:
            return None

    def calculate_price(self, item_type, quantity):
        prices = {'Luxury': 50, 'Essential': 30, 'Gift': 20}
        vat_rates = {'Luxury': 0.2, 'Essential': 0.1, 'Gift': 0.05}

        price = prices[item_type] * quantity
        vat_rate = vat_rates[item_type]
        total_cost = price + (price * vat_rate)

        return total_cost


class ShoppingCart:
    def __init__(self):
        self.basket = []

    def add_to_basket(self, item):
        self.basket.append(item)

    def view_basket(self):
        for item in self.basket:
            print(f"{item['name']} - Quantity: {item['quantity']} - Total Cost: {item['total_cost']}")

    def calculate_change(self, basket_total, amount_paid):
        change_due = amount_paid - basket_total
        return change_due if change_due >= 0 else None

class CorrectChangeCalculator:
    @staticmethod
    def calculate_change(total_value, amount_paid):
        change_due = amount_paid - total_value
        if change_due < 0:
            return None
        return change_due

    @staticmethod
    def calculate_notes_coins(amount_due):
        notes_coins = {'50 Euro': 0, '20 Euro': 0, '10 Euro': 0, '5 Euro': 0, '2 Euro': 0, '1 Euro': 0}

        denominations = [50, 20, 10, 5, 2, 1, 0.5, 0.2, 0.1, 0.05, 0.02, 0.01]  

        for denomination in denominations:
            while amount_due >= denomination:
                denomination_name = CorrectChangeCalculator._get_denomination_name(denomination)
                notes_coins[denomination_name] += 1
                amount_due -= denomination

        return notes_coins

    @staticmethod
    def _get_denomination_name(denomination):
        if denomination >= 1:
            if denomination == 50:
                return '50 Euro'
            elif denomination == 20:
                return '20 Euro'
            elif denomination == 10:
                return '10 Euro'
            else:
                return f'{int(denomination)} Euro'
        else:
            return f'{int(denomination * 100)} Cent'

def checkout_with_change_calculator(shopping_cart_total, amount_paid):
    calculator = CorrectChangeCalculator()
    change = calculator.calculate_change(shopping_cart_total, amount_paid)

    if change is not None:
        print("Correct change breakdown:")
        for denomination, count in change.items():
            print(f"{denomination}: {count}")

        print("Thank you for shopping!")
        return True
    else:
        print("Insufficient payment. Please pay the correct amount.")
        return False

def main():
    stock_control = StockControl()
    shopping_cart = ShoppingCart()
    change_calculator = CorrectChangeCalculator()

    while True:
        print("1. Add Item to Stock")
        print("2. View Items in Stock")
        print("3. Add Item to Basket")
        print("4. Delete Item")
        print("5. View Basket")
        print("6. Checkout")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            initial_quantity = int(input("Enter the initial stock quantity: "))
            item_name = input("Enter item name: ")
            item_type = input("Enter item type (Luxury/Essential/Gift): ")
            expiration_date = input("Enter expiration date: ")

            stock_control.add_item(item_name, item_type, expiration_date, initial_quantity)
            print("Item added to stock successfully!")

        elif choice == '2':
            stock_control.view_items()

        elif choice == '3':
            stock_control.view_items()
            item_id = int(input("Enter the ID of the item to add to the basket: "))
            quantity = int(input("Enter the quantity: "))

            added_item = stock_control.add_to_basket(item_id, quantity)
            if added_item:
                shopping_cart.add_to_basket(added_item)
                print("Item added to basket successfully!")
            else:
                print("Invalid action")
        elif choice == '4':
            item_id_to_delete = int(input("Enter the ID of the item to delete: "))
            stock_control.delete_item(item_id_to_delete)
       
        elif choice == '5':
            shopping_cart.view_basket()

        elif choice == '6':
            basket_total = sum(item['total_cost'] for item in shopping_cart.basket)
            print(f"Total Cost: {basket_total}")
            amount_paid = float(input("Enter the amount paid: "))

            change_due = change_calculator.calculate_change(basket_total, amount_paid)
            if change_due is not None:
                print("Correct change breakdown:")
                change_breakdown = change_calculator.calculate_notes_coins(change_due)
                for denomination, count in change_breakdown.items():
                    print(f"{denomination}: {count}")

                print("Thank you for shopping!")
                break
            else:
                print("Insufficient payment. Please pay the correct amount.")


        elif choice == '7':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == '__main__':
    main()



class ItemPacking:
    @staticmethod
    def calculate_boxes(weight_dimensions, num_items, items):
        boxes_needed = 0
        total_weight = 0

        for i in range(num_items):
            item_weight, item_dimensions = items[i]['weight'], items[i]['dimensions']
            total_weight += item_weight

            if total_weight > weight_dimensions['max_weight']:
                total_weight = item_weight
                boxes_needed += 1

        return boxes_needed + 1  

def main_item_packing():
    weight_dimensions = {
        'max_weight': float(input("Enter the maximum weight a box can contain: ")),
        'dimensions': input("Enter the dimensions of the boxes (width x height x depth): ").split('x')
    }

    num_items = int(input("Enter the number of items: "))
    items = []

    for i in range(num_items):
        item_weight = float(input(f"Enter the weight of item {i + 1}: "))
        item_dimensions = input(f"Enter the dimensions of item {i + 1} (width x height x depth): ").split('x')

        items.append({'weight': item_weight, 'dimensions': item_dimensions})

    packing_result = ItemPacking.calculate_boxes(weight_dimensions, num_items, items)
    print(f"Number of boxes needed: {packing_result}")

if __name__ == '__main__':
    main_item_packing()