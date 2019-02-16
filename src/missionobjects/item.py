class Item:
    'Object representation of a single item. Contains item name and all attributes.'
    
    def __init__(self, item_name, attributes = []):
        'Constructor for the item object.'
        self.item_name = item_name
        self.attributes = attributes