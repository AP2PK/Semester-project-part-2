import datetime
class Inventory:
    def __init__(self):
        # Data sets, they store things. Specifically the things that the variables are named after.
        self.manufacturer_data = {}   
        self.price_data = {}          
        self.service_date_data = {}   
        self.inventory = []           
        self.manufacturer_set = set() # For quick lookup of manufacturer names.
        self.item_type_set = set()    # same
