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
  item1=Item("Burger","Beef","Beef burger",5.00)
  item2=Item("Burger","Chicken","Chicken burger",5.50)

  class Player:
    def __init__(self, name):
      
      self.name = name

      def displayName(self):
        print("Player Name: {self.name}")
        

# create class
class GameMode:
    name = "BLANK"


class main:
    optionBeginGame=input("Type start to begin game, type end to end game\n")
    match optionBeginGame:
    #1{  
      case "Start"|"start":
        print("Starting game:")
        playerName= input("Enter your name\n")
        print("Welcome to the restaurant business;",playerName)
        resturantType=input("Do you want to open a restaurant that serves burgers, or pizzas?\n")
      #2{
        match resturantType:
          case "Burgers"|"burgers":
            gameMode1 = GameMode()
          # modify the name property
            print("Before getting overwritten:", gameMode1.name)
            gameMode1.name = "This is the burger game mode test"
            print("After getting overwritten:", gameMode1.name)
          case "Pizzas"|"pizzas:":
            print("pizza option")
       #2}


      case "End"|"end":
        print("Ending game...")
        sys.exit()

      case _:
        print("Invalid input, try again!")
        sys.exit()
      #1}  


    
