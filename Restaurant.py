class Restaurant:
    """Creating Restaurant Class"""
    def __init__(self, restaurant_name:str, restaurant_cuisine:str, open:bool):
        """Initializing restuarant attributes"""
        self.restaurant_name = restaurant_name
        self.restaurant_cuisine = restaurant_cuisine
        self.open = open

    def describe_restaurant(self):
        """Methond to print description of restaurants"""
        print(f"Name: {self.restaurant_name}, Cuisine: {self.restaurant_cuisine}, Status: {self.open}")

    def is_open(self):
        """Method to determine the status of the restaurants(Open/Closed)"""
        if self.open:
            print("Currently Open")
        else:
            print("Curently Closed")

    def recommend(cls, *restaurants):
        """Method to recommend an open restaurant"""
        for restaurant in restaurants:
            if restaurant.open:
                return restaurant
        return None
        

restaurant1 = Restaurant("Croaker's Spot", 'Soul Food', True)
restaurant2 = Restaurant("Moe Vegan", 'Vegan', True)
restaurant3 = Restaurant("Yankee Lobster", 'Seafood', False)

restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()

Opened = Restaurant.recommend(restaurant1, restaurant2, restaurant3)
Opened.describe_restaurant()
Opened.is_open()


