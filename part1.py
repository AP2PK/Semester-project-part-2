<<<<<<< HEAD
#You said I can use it so I'm gonna use it.
import datetime
def read_input_files():
    #Gotta store it somewhere and it's been goood practice to open empty dictionaries
    manufacturer_data = {}  # Dictionary to store manufacturer details
    price_data = {}         # Dictionary to store item prices
    service_date_data = {}  # Dictionary to store service dates
    with open('ManufacturerList.txt', 'r') as file: #open file
        for line in file: #Do I really need to explain what a for loop does? Just means do this to all the lines.
            parts = line.strip().split(',') #one part at a time. Comma dilemitors
            item_id = parts[0] #The first part is the Item ID
            manufacturer_data[item_id] = { 
                'manufacturer': parts[1], #the second part is the manufacturer
                'type': parts[2], #nothing new here
                'damaged': False if len(parts) <= 3 else parts[3]  #Is it damaged?
            }
    with open('PriceList.txt', 'r') as file: #Now time to store pricelist
        for line in file:
            parts = line.strip().split(',') #Nothing New
            item_id, price = parts
            price_data[item_id] = float(price) #Attach price data to item ID in a dictionary
    with open('ServiceDatesList.txt', 'r') as file: #Nothing new.
        for line in file:
            parts = line.strip().split(',')
            item_id, service_date = parts
            service_date_data[item_id] = service_date
    return manufacturer_data, price_data, service_date_data
#Fine I'll do it myself
def sort_by_manufacturer(item):
    return item[1]

def sort_by_item_id(item):
    return item[0]

def sort_by_service_date(item):
    return datetime.datetime.strptime(item[4], '%m/%d/%Y')

def sort_by_price(item):
    return item[3]
#I think I'll write now.
def create_full_inventory(manufacturer_data, price_data, service_date_data):# let's use that stored infromation
    inventory = []
    for item_id, details in manufacturer_data.items():
        # Combine data 
        item = [
            item_id,
            details['manufacturer'],
            details['type'],
            price_data.get(item_id, None),  # Price
            service_date_data.get(item_id, None),  # Service Date
        ]
        if details['damaged']:  # If it's damaged write damaged
            item.append(details['damaged'])
        inventory.append(item)
    inventory.sort(key=sort_by_manufacturer) #sort it

    with open('FullInventory.txt', 'w') as file:# actually does the writing
        for item in inventory:
            file.write(','.join(map(str, item)) + '\n')
def create_item_type_inventory(manufacturer_data, price_data, service_date_data):#
    item_type_files = {} #I'm starting to dislike dictionaries.
    for item_id, details in manufacturer_data.items():  
        item_type = details['type'] #Put a name to it.
        if item_type not in item_type_files:
            item_type_files[item_type] = [] #If no list now is list.
        item = [
            item_id,
            details['manufacturer'],
            price_data.get(item_id, None), #get me price and service date
            service_date_data.get(item_id, None),
        ]
        if details['damaged']:# LET'S Play is IT damaged.
            item.append(details['damaged'])
        item_type_files[item_type].append(item)

    for item_type, items in item_type_files.items(): 
        items.sort(key=sort_by_item_id) # sort by item ID
        with open(f'{item_type}Inventory.txt', 'w') as file: #this was annoying
            for item in items:
                file.write(','.join(map(str, item)) + '\n') #Now write it out
def create_past_service_date_inventory(manufacturer_data, price_data, service_date_data):
    today = datetime.datetime.now() #Now I know why I need datetime, had to look this up.
    past_service_items = []#nothing new.
    for item_id, service_date in service_date_data.items():
        service_date_obj = datetime.datetime.strptime(service_date, '%m/%d/%Y') # Had to look this up to.
        if service_date_obj < today: #I don't think you need to no python to know what this fucntion does.
            past_service_items.append([ #put it together
                item_id,
                manufacturer_data[item_id]['manufacturer'],
                manufacturer_data[item_id]['type'],
                price_data.get(item_id, None),
                service_date
            ])

    past_service_items.sort(key=sort_by_service_date) #sort it

    with open('PastServiceDateInventory.txt', 'w') as file: #write it out
        for item in past_service_items:
            file.write(','.join(map(str, item)) + '\n')
<<<<<<< HEAD
def create_damaged_inventory(manufacturer_data, price_data, service_date_data):
    damaged_items = []
    for item_id, details in manufacturer_data.items():
        if details['damaged']:#If it says damaged
            damaged_items.append([ #Add damaged and some Identifying charectaristics
                item_id,
                details['manufacturer'],
                details['type'],
                price_data.get(item_id, 0),
                service_date_data.get(item_id, None)
            ])

    damaged_items.sort(key=sort_by_price, reverse=True)#Sort it by price

    with open('DamagedInventory.txt', 'w') as file:
        for item in damaged_items:
            file.write(','.join(map(str, item)) + '\n')

manufacturer_data, price_data, service_date_data = read_input_files()
create_full_inventory(manufacturer_data, price_data, service_date_data)
create_item_type_inventory(manufacturer_data, price_data, service_date_data)
create_past_service_date_inventory(manufacturer_data, price_data, service_date_data)
create_damaged_inventory(manufacturer_data, price_data, service_date_data)
=======
            
>>>>>>> f603a36 (servace finished)


    

=======
#You said I can use it so I'm gonna use it.
import datetime
def read_input_files():
    #Gotta store it somewhere and it's been goood practice to open empty dictionaries
    manufacturer_data = {}  # Dictionary to store manufacturer details
    price_data = {}         # Dictionary to store item prices
    service_date_data = {}  # Dictionary to store service dates
    with open('ManufacturerList.txt', 'r') as file: #open file
        for line in file: #Do I really need to explain what a for loop does? Just means do this to all the lines.
            parts = line.strip().split(',') #one part at a time. Comma dilemitors
            item_id = parts[0] #The first part is the Item ID
            manufacturer_data[item_id] = { 
                'manufacturer': parts[1], #the second part is the manufacturer
                'type': parts[2], #nothing new here
                'damaged': False if len(parts) <= 3 else parts[3]  #Is it damaged?
            }
    with open('PriceList.txt', 'r') as file: #Now time to store pricelist
        for line in file:
            parts = line.strip().split(',') #Nothing New
            item_id, price = parts
            price_data[item_id] = float(price) #Attach price data to item ID in a dictionary
    with open('ServiceDatesList.txt', 'r') as file: #Nothing new.
        for line in file:
            parts = line.strip().split(',')
            item_id, service_date = parts
            service_date_data[item_id] = service_date
    return manufacturer_data, price_data, service_date_data
#Fine I'll do it myself
def sort_by_manufacturer(item):
    return item[1]

def sort_by_item_id(item):
    return item[0]

def sort_by_service_date(item):
    return datetime.datetime.strptime(item[4], '%m/%d/%Y')

def sort_by_price(item):
    return item[3]
#I think I'll write now.
def create_full_inventory(manufacturer_data, price_data, service_date_data):# let's use that stored infromation
    inventory = []
    for item_id, details in manufacturer_data.items():
        # Combine data 
        item = [
            item_id,
            details['manufacturer'],
            details['type'],
            price_data.get(item_id, None),  # Price
            service_date_data.get(item_id, None),  # Service Date
        ]
        if details['damaged']:  # If it's damaged write damaged
            item.append(details['damaged'])
        inventory.append(item)
    inventory.sort(key=sort_by_manufacturer) #sort it

    with open('FullInventory.txt', 'w') as file:# actually does the writing
        for item in inventory:
            file.write(','.join(map(str, item)) + '\n')
def create_item_type_inventory(manufacturer_data, price_data, service_date_data):#
    item_type_files = {} #I'm starting to dislike dictionaries.
    for item_id, details in manufacturer_data.items():  
        item_type = details['type'] #Put a name to it.
        if item_type not in item_type_files:
            item_type_files[item_type] = [] #If no list now is list.
        item = [
            item_id,
            details['manufacturer'],
            price_data.get(item_id, None), #get me price and service date
            service_date_data.get(item_id, None),
        ]
        if details['damaged']:# LET'S Play is IT damaged.
            item.append(details['damaged'])
        item_type_files[item_type].append(item)

    for item_type, items in item_type_files.items(): 
        items.sort(key=sort_by_item_id) # sort by item ID
        with open(f'{item_type}Inventory.txt', 'w') as file: #this was annoying
            for item in items:
                file.write(','.join(map(str, item)) + '\n') #Now write it out
def create_past_service_date_inventory(manufacturer_data, price_data, service_date_data):
    today = datetime.datetime.now() #Now I know why I need datetime, had to look this up.
    past_service_items = []#nothing new.
    for item_id, service_date in service_date_data.items():
        service_date_obj = datetime.datetime.strptime(service_date, '%m/%d/%Y') # Had to look this up to.
        if service_date_obj < today: #I don't think you need to no python to know what this fucntion does.
            past_service_items.append([ #put it together
                item_id,
                manufacturer_data[item_id]['manufacturer'],
                manufacturer_data[item_id]['type'],
                price_data.get(item_id, None),
                service_date
            ])

    past_service_items.sort(key=sort_by_service_date) #sort it

    with open('PastServiceDateInventory.txt', 'w') as file: #write it out
        for item in past_service_items:
            file.write(','.join(map(str, item)) + '\n')
def create_damaged_inventory(manufacturer_data, price_data, service_date_data):
    damaged_items = []
    for item_id, details in manufacturer_data.items():
        if details['damaged']:#If it says damaged
            damaged_items.append([ #Add damaged and some Identifying charectaristics
                item_id,
                details['manufacturer'],
                details['type'],
                price_data.get(item_id, 0),
                service_date_data.get(item_id, None)
            ])

    damaged_items.sort(key=sort_by_price, reverse=True)#Sort it by price

    with open('DamagedInventory.txt', 'w') as file:
        for item in damaged_items:
            file.write(','.join(map(str, item)) + '\n')

manufacturer_data, price_data, service_date_data = read_input_files()
create_full_inventory(manufacturer_data, price_data, service_date_data)
create_item_type_inventory(manufacturer_data, price_data, service_date_data)
create_past_service_date_inventory(manufacturer_data, price_data, service_date_data)
create_damaged_inventory(manufacturer_data, price_data, service_date_data)


    

>>>>>>> a2ba3b27e5200fc7547dce9e226f0a7658ee4cbc


