class Sneakers:
    def __init__(self, brand, price, size, color, material):
        self.__brand = brand
        self.__size = size
        self.__color = color
        self.__price = price
        self.__material = material
    
    def __repr__(self):
        return f'Sneakers("{self.__brand}", {self.__price}, {self.__size}, {self.__color}, {self.__material})'
    
    
    def get_brand(self):
        return self.__brand
    
    def get_size(self):
        return self.__size
    
    def get_color(self):
        return self.__color
    
    def get_price(self):
        return self.__price
    
    def get_material(self):
        return self.__material
    
      
class SportShoesStore:
    def __init__(self):
        self.__stock = {}
        self.__soldItems = {}
        
    def __str__(self):
        return f'SportShoesStore(stock = {self.__stock}, soldItems = {self.__soldItems})'
        
    def updateStock(self, items):
        for brand in items.keys():
            if brand in self.__stock.keys():
                self.__stock[brand].extend(items[brand])
            else:
                self.__stock[brand] = items[brand]
                
    def get_bestSellerBrand(self):
        bestSeller = None
        sold = 0
        for brand in self.__soldItems.keys():
            if len(self.__soldItems[brand]) > sold:
                sold = len(self.__soldItems[brand])
                bestSeller = brand
        return bestSeller 
                
    
    
    def sellItems(self, items):
        for shoes in items:     #items - list
            brand = shoes.get_brand()
            try:
                available_shoes = self.__stock[brand]
                found = False
                for i in range(0, len(available_shoes)):
                    if shoes.get_price() == available_shoes[i].get_price() and shoes.get_size() == available_shoes[i].get_size() and shoes.get_color() == available_shoes[i].get_color() and shoes.get_material() == available_shoes[i].get_material():
                        found = True
                        del available_shoes[i]
                        if brand in self.__soldItems.keys(): 
                            self.__soldItems[brand].append(shoes)
                        else:
                            self.__soldItems[brand] = [shoes]
                        break
                if not found:
                    print(f"Sneakers of brand '{brand}', at price {shoes.get_price()}, size {shoes.get_size()}, color {shoes.get_color()}, material {shoes.get_material()} not available on the stock")
            except:
                print(f"Sneakers of '{brand}' brand not found on the stock")
              
            
store = SportShoesStore()
print(store) #store is empty

shipment1 = {"Nike": [
                      Sneakers("Nike", 4999, 39, "black", "leather"),
                      Sneakers("Nike", 12500, 37, "orange", "leather"),
                      Sneakers("Nike", 7280, 41, "white", "fabric"),
                      #Sneakers("Nike", 4999, 39, "black", "leather"),
                      #Sneakers("Nike", 3700, 38, "pink", "fabric"),
                      #Sneakers("Nike", 20999, 43, "black", "leather"),
                    ],
            "Puma": [
                      Sneakers("Puma", 4999, 39, "black", "leather"),
                      Sneakers("Puma", 3000, 38, "red", "leather"),
                      #Sneakers("Puma", 7280, 41, "white", "fabric"),
                      #Sneakers("Puma", 4699, 45, "black", "leather"),
                      #Sneakers("Puma", 1499, 37, "white", "fabric"),
                      Sneakers("Puma", 15999, 43, "purple", "leather"),
                      Sneakers("Puma", 2700, 35, "yellow", "fabric"),
                    ],
            "Adidas": [
                      Sneakers("Adidas", 6900, 39, "green", "leather"),
                      Sneakers("Adidas", 8000, 38, "blue", "leather"),
                      Sneakers("Adidas", 2399, 41, "white", "fabric"),
                      Sneakers("Adidas", 7099, 45, "black", "leather"),
                      #Sneakers("Adidas", 3339, 37, "white", "fabric"),
                      #Sneakers("Adidas", 1899, 43, "grey", "leather"),
                      #Sneakers("Adidas", 2700, 35, "orange", "fabric"),
                      #Sneakers("Adidas", 2700, 35, "red", "fabric"),
                    ]
                } 
shipment2 = {"Nike": [
                      Sneakers("Nike", 25000, 39, "black", "leather")]}
store.updateStock(shipment1)
print(store)   
store.updateStock(shipment2)
print(store)

store.sellItems([
                      Sneakers("Puma", 4999, 39, "black", "leather"),
                      Sneakers("Puma", 3000, 38, "red", "leather"),
                      Sneakers("Adidas", 2399, 41, "white", "fabric"),
                      Sneakers("Puma", 1499, 37, "white", "fabric"),
                      Sneakers("Nike", 3700, 38, "pink", "fabric"),
                      Sneakers("Puma", 15999, 43, "purple", "leather"),
                      Sneakers("Adidas", 6900, 39, "green", "leather"),
                      Sneakers("Puma", 2700, 35, "yellow", "fabric")])
print(store)
store.sellItems([
                      Sneakers("Puma", 4999, 39, "black", "leather"),
                      Sneakers("Nike", 3700, 38, "pink", "fabric"),
                      Sneakers("Puma", 7280, 41, "white", "fabric"),
                      Sneakers("Pumba", 4699, 45, "black", "leather")])

bestSeller = store.get_bestSellerBrand()
print(f'bestseller of our store is: {bestSeller}')