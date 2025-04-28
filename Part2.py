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
        def load_data(self):
        #open file
        with open('ManufacturerList.txt', 'r') as file:
            #Do I really need to explain what a for loop does? Just means do this to all the lines.
            for line in file:
                #one part at a time. Comma dilemitors
                parts = line.strip().split(',')
                #The first part is the Item ID
                item_id = parts[0]
                #the second part is the manufacturer; nothing new here; Is it damaged?
                self.manufacturer_data[item_id] = {
                    'manufacturer': parts[1],
                    'type': parts[2],
                    'damaged': parts[3] if len(parts) > 3 and parts[3].strip() != "" else False
                }
        #Now time to store pricelist
        with open('PriceList.txt', 'r') as file:
            for line in file:
                #Nothing New
                parts = line.strip().split(',')
                item_id, price = parts
                #Attach price data to item ID in a dictionary
                self.price_data[item_id] = float(price)
        #Nothing new.
        with open('ServiceDatesList.txt', 'r') as file:
            for line in file:
                parts = line.strip().split(',')
                item_id, service_date = parts
                self.service_date_data[item_id] = service_date
            def build_inventory(self):
        #Fine I'll do it myself
        self.inventory = [
            ([item_id,
              data['manufacturer'],  # the second part is the manufacturer
              data['type'],          # nothing new here
              self.price_data.get(item_id, None),  # Price
              self.service_date_data.get(item_id, None)]  # Service Date
             + ([data['damaged']] if data['damaged'] else []))
            for item_id, data in self.manufacturer_data.items()
        ]
        self.inventory.sort(key=lambda x: x[1].lower())  #sort it
        self.manufacturer_set = {item[1].lower() for item in self.inventory}
        self.item_type_set = {item[2].lower() for item in self.inventory}
