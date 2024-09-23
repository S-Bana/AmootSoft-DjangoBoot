from abc import ABC, abstractmethod

class MenuItem(ABC):
    """
    Abstract base class for menu items.
    
    Attributes:
        name (str): The name of the menu item.
        price (float): The price of the menu item.
    """
    def __init__(self, name=None, price=None):
        self.name = name
        self.price = price
    
    @abstractmethod
    def get_info(self):
        """Returns a string with information about the menu item."""
        pass


class Order(ABC):
    """
    Abstract base class for orders.
    
    Attributes:
        items (list): A list of MenuItem objects in the order.
    """
    def __init__(self):
        self.items = []

    @abstractmethod
    def place_order(self):
        """Places the order and prints order details."""
        pass

    def add_item(self, item: MenuItem):
        """Adds a MenuItem to the order."""
        self.items.append(item)

    def calculate_total(self):
        """Calculates the total price of the order, applying discounts if applicable."""
        total = sum(item.price for item in self.items)
        
        # Apply a 10% discount if the total exceeds $50
        if total > 50:
            total *= 0.9  
        
        return total


class Beverage(MenuItem):
    """
    Represents a beverage item on the menu.
    
    Attributes:
        volume (int): The volume of the beverage in milliliters.
    """
    def __init__(self, name, price, volume):
        super().__init__(name, price)
        self.volume = volume

    def get_info(self):
        """Returns a string with information about the beverage."""
        return f"Beverage: {self.name}, Volume: {self.volume}ml, Price: ${self.price:.2f}"


class MainCourse(MenuItem):
    """
    Represents a main course item on the menu.
    
    Attributes:
        serving_size (int): The serving size of the main course in grams.
    """
    def __init__(self, name, price, serving_size):
        super().__init__(name, price)
        self.serving_size = serving_size

    def get_info(self):
        """Returns a string with information about the main course."""
        return f"Main Course: {self.name}, Serving Size: {self.serving_size}g, Price: ${self.price:.2f}"


class Dessert(MenuItem):
    """
    Represents a dessert item on the menu.
    
    Attributes:
        calories (int): The calorie content of the dessert.
    """
    def __init__(self, name, price, calories):
        super().__init__(name, price)
        self.calories = calories

    def get_info(self):
        """Returns a string with information about the dessert."""
        return f"Dessert: {self.name}, Calories: {self.calories}kcal, Price: ${self.price:.2f}"


class DineInOrder(Order):
    """
    Represents a dine-in order at a restaurant.
    
    Attributes:
        table_number (int): The table number for which the order is placed.
    """
    def __init__(self, table_number):
        super().__init__()
        self.table_number = table_number

    def place_order(self):
        """Places the dine-in order and prints order details."""
        print(f"Placing Dine-In Order for Table {self.table_number}:")
        for item in self.items:
            print(item.get_info())
        print(f"Total Price : ${self.calculate_total():.2f}")


class TakeoutOrder(Order):
    """
    Represents a takeout order from a restaurant.
    
    Attributes:
        delivery_option (str): The delivery option ('pickup' or 'delivery').
    """
    def __init__(self, delivery_option: str):
        super().__init__()
        self.delivery_option = delivery_option  # 'pickup' or 'delivery'

    def place_order(self):
        """Places the takeout order and prints order details."""
        print(f"Placing Takeout Order ({self.delivery_option.capitalize()}):")
        for item in self.items:
            print(item.get_info())
        print(f"Total Price: ${self.calculate_total():.2f}")


def main():
    # Create some menu items
    coffee = Beverage("Coffee", 2.29, 320)
    steak = MainCourse("Tea", 32.99, 267)
    cake = Dessert("Cake", 4.50, 520)

    # Create a dine-in order
    dine_in_order = DineInOrder(table_number=5)
    dine_in_order.add_item(coffee)
    dine_in_order.add_item(steak)
    
    # Place the dine-in order
    dine_in_order.place_order()

    print("=" * 50)

    # Create a takeout order
    takeout_order = TakeoutOrder(delivery_option="delivery")
    takeout_order.add_item(cake)
    
    # Place the takeout order
    takeout_order.place_order()

if __name__ == "__main__":
    main()
