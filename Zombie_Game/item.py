class Item():

   def __init__(self):
    self.name = None
    self.description = None

#@property
def get_name(self):
   return self.name

#@name.setter
def set_name(self, item_name):
   self.name = item_name

 #@property
def get_description(self):
 return self.description

#@description.setter
def set_description(self, item_description):
    self.description = item_description


# Creating an instance of Item
item = Item()

# Setting name and description
item.name = "Sword"
item.description = "A sharp weapon used for combat."

# Getting name and description
print(item.name)  # Output: Sword
print(item.description)  # Output: A sharp weapon used for combat.
