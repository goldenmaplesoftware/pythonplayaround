import sys 

#Initial definition of what an item classifies as
class Item:
  def __init__(self,menuCategory,itemName,itemDescription,itemPrice):
    self.menuCategory=menuCategory
    self.itemName=itemName
    self.itemDescription=itemDescription
    self.itemPrice=itemPrice

#Dictionary of already preassigned items
class menu:
  item1=Item("Appetizer","Fried Shrimp","A delicious assortment of deep shrimp",10.95)
  item2=Item("Appetizer","Beef Tips","Savory beef cut from the freshest tenderloin on the market, locally produced;  Tossed in a Cajun spice",13.50)
  

class main:
    print("fuck you")