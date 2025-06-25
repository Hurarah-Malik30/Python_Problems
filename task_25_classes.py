class Restaurant:
    menu = []
    table_reservation = {}
    cust_orders = {}
    
    def print_menu(self):
        print("MENU:")
        for item in self.menu:
            print(item)
    def print_reservations(self):
        print("Table Reservations:")
        for reservation in self.table_reservation:
            print('%s:%s'%(reservation, self.table_reservation[reservation]))
                
    def print_orders(self):
        print("CUSTOMER ORDERS:")
        for order in self.cust_orders:
            print("%s:%s"%(order,self.cust_orders[order]))
          
    def setMenu(self):
        n = int(input("How many items you want to add: "))
        for i in range(1,n+1):
            item = input(f"Item {i}: ")
            self.menu.append(item)
            
    def makeReservation(self):
        n = int(input("Enter no. of reservation you want to add: "))
        for i in range(1,n+1):
            table_num = input("Enter Table number: ")
            time = input("Enter Time:")
            self.table_reservation[table_num] = time
            
    def makeOrder(self):
        n = int(input("Enter no. of orders you want to add: "))
        for i in range(1,n+1):
            customer_name = input("Enter Customer Name: ")
            item = input("Enter your order: ")
            while True:
                if item not in self.menu:
                    item = input("Item not Available.Choose from Menu: ")
                else:
                    break
            self.cust_orders[customer_name] = item

r1 = Restaurant()
r1.setMenu()
r1.print_menu()
# r1.makeReservation()
# r1.print_reservations()
r1.makeOrder()
r1.print_orders()