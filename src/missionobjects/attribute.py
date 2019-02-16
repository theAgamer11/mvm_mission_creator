class Attribute:
    'Object representing a single item/character attribute. Contains key and value.'

    def __init__(self, key, value):
        'Constructor for the attribute object.'
        self.key = key
        self.value = value
    
    def __str__(self):
        return '"' + self.key + '" ' + str(self.value)