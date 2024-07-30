import sys 
#Global variables
itemsToSaveList=[]
menuOptions=str("Input Add or add to add an item to the list \nInput Remove or remove to delete an item to the list \nInput Saved items or saved items to see list of saved items \n")
print(menuOptions)
option=input("Please make a selection now:\n")
count = 0

#universal functions to call
def addItem():
	print("Input the name of the item you would like to add to the list")
	addItem=input()
	addItemToString=str(addItem)
	itemsToSaveList.append(addItemToString)
	print("Item "+addItemToString+" was saved to the universal list!")

def removeItem():
	print("From the list that was created")
	savedItems()
	print("Input what you want to remove from the list")
	removeItem=input()
	removeItemToString=str(removeItem)
	#This handles if the item is not in the list and cannot be resolved
	try:
		itemsToSaveList.remove(removeItemToString)
		print("Item "+removeItemToString+" was deleted from the universal list!")
	except:
		print("The item does not exist in the list, please try again later...")


def savedItems():
	print("This is the list of items that have been saved...",itemsToSaveList)

def optionsToSelect():
	match option:
		case "Add"|"add":
			addItem()
		case "Remove"|"remove":
			removeItem()

		case "Saved"|"saved":
			savedItems()

		case _:
			print("Invalid")

while True:
	count += 1
	print("Count is at iteration:"+ str(count))
	optionsToSelect()
	if count == 4:
		break
		print("Program will now automatically terminate")
	
