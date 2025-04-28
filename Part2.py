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
              self.manufacturer_data[item_id]['manufacturer'],  # the second part is the manufacturer
              self.manufacturer_data[item_id]['type'],          # nothing new here
              self.price_data.get(item_id, None),               # Price
              self.service_date_data.get(item_id, None)]         # Service Date
             + ([self.manufacturer_data[item_id]['damaged']] if self.manufacturer_data[item_id]['damaged'] else []))
            for item_id in self.manufacturer_data
        ]
        self.inventory.sort(key=lambda x: x[1].lower())  #sort it
        self.manufacturer_set = {item[1].lower() for item in self.inventory}
        self.item_type_set = {item[2].lower() for item in self.inventory}

    def is_valid_item(self, item):  # checks if it is a valid item
        try:
            service_date_obj = datetime.datetime.strptime(item[4], '%m/%d/%Y')
        except Exception:
            return False
        # If it's past its service date or marked as damaged (i.e. extra element in list), it's not valid
        return service_date_obj >= datetime.datetime.now() and len(item) == 5

    def get_item_status(self, item):
        #Nothing New.
        status = ""
        try:
            date = datetime.datetime.strptime(item[4], '%m/%d/%Y')
            if date < datetime.datetime.now():
                status += "Expired"
        except Exception:
            status += "Expired"
        if len(item) > 5:
            if status:
                status += " and Damaged"
            else:
                status += "Damaged"
        if status:
            return "(" + status + ")"
        return ""

    def query_item(self):
        # Synonym mapping: map "computer" to "laptop".
        synonym_map = {"computer": "laptop"}
        while True:
            user_input = input("Please enter your query (or 'q' to quit): ").strip()
            if user_input.lower() == 'q':
                break
            # Split query into words and apply synonym mapping.
            words = user_input.lower().split()
            normalized_words = [synonym_map.get(word, word) for word in words]
            # Only consider words that match the manufacturers or types in our inventory.
            makers = [word for word in normalized_words if word in self.manufacturer_set]
            types = [word for word in normalized_words if word in self.item_type_set]
            # If the query doesn't yield exactly one manufacturer and one type, reject it.
            if len(makers) != 1 or len(types) != 1:
                print("No such item in inventory")
                continue
            manufacturer_query = makers[0]
            item_type_query = types[0]
            items = []
            # Loop through inventory and pick items that match our query.
            for item in self.inventory:
                if item[1].lower() == manufacturer_query and item[2].lower() == item_type_query:
                    items.append(item)
            if not items:
                print("No such item in inventory")
                continue
            # Choose the most expensive item.
            chosen_item = max(items, key=lambda x: x[3])
            print("Your item is:", chosen_item[0], chosen_item[1], chosen_item[2], f"${chosen_item[3]:.2f}", self.get_item_status(chosen_item))
            alternatives = []
            # Now, search for an alternative: same type, different manufacturer.
            for item in self.inventory:
                if item[2].lower() == item_type_query and item[1].lower() != manufacturer_query:
                    alternatives.append(item)
            if alternatives:
                best_alternative = min(alternatives, key=lambda x: abs(x[3] - chosen_item[3]))
                print("You may, also, consider:", best_alternative[0], best_alternative[1], best_alternative[2], f"${best_alternative[3]:.2f}", self.get_item_status(best_alternative))

if __name__ == '__main__':
    inv = Inventory()
    inv.load_data()
    inv.build_inventory()
    inv.query_item()
