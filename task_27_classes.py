class Inventory:
    def __init__(self):
        self.items = {}
        
    def addItem(self,itemid,itemname,itemquantity,itemprice):
        self.items[itemid] = {"itemname":itemname,"itemquantity":itemquantity,"itemprice":itemprice}
        
    def updateitem(self,itemid,itemname,itemquantity,itemprice):
        if itemid in self.items:
            self.items[itemid] = {"itemname":itemname,"itemquantity":itemquantity,"itemprice":itemprice}
        else:
            print('Item not found')
            
    def check_item_details(self, itemid):
        if itemid in self.items:
            item = self.items[itemid]
            return f"Product Name: {item['itemname']},  Quantity: {item['itemquantity']}, Price: {item['itemprice']}"
        else:
            return "Item not found in inventory."
        
i1 = Inventory()
i1.addItem(1,'Apples',12,20)
i1.addItem(2,'Banana',12,50)
i1.addItem(3,'Orange',50,100)
i1.updateitem(4,'Pineapple',20,150)
i1.updateitem(2,'Pineapple',20,150)
print(i1.check_item_details(3))
print(i1.check_item_details(2))