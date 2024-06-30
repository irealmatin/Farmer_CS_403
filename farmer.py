"""
a simple project for advance python 
"""

# ------------------------------------------------------ #

# we try to write 2 classes for this agricultural land : a Trees class for the Wind trees and fruit trees / and a Bush class for flower bushes !


#----------------------------------Class-------------------------------------------#
class Trees :
    P = 2  
    T = 2.5 
    FRUIT_PRICE = 50000
    WINDY_TREES_AMOUNT = 0


    TALL_WINDY_TREES = []
    

    def __init__(self , code , height , water_consumption_coefficient , tree_type ,product_amount = 0  ) :
        self.code = code
        self.h = height
        self.product = product_amount
        self.wcc = water_consumption_coefficient
        self.tree_type = tree_type
        if self.tree_type == "windy" :
            Trees.WINDY_TREES_AMOUNT += 1
            if self.h > 5 :
                Trees.TALL_WINDY_TREES.append(self.code)

    def water_consuption (self) : # All trees, except for their own consumption, also consume T cubic meters.
        if self.tree_type == "windy":
            return ( self.h * self.wcc ) + Trees.T
        if self.tree_type == "fruit" :
            return (self.product * self.wcc * Trees.P) + Trees.T
        
    def sales_value(self):
        if self.tree_type == "fruit" :
            return self.product * Trees.FRUIT_PRICE
        return 0 
    
    @classmethod
    def get_windy_trees_value(cls):
        return cls.WINDY_TREES_AMOUNT
    
    @classmethod
    def get_tall_windy_trees(cls):
        return cls.TALL_WINDY_TREES
            
    
class Bush :
    ROSE_AMOUNT = 0
    R = 25000 # rose flower value

    def __init__(self,bush_code , flower_amount) :
        self.code = bush_code
        self.flower_amount = flower_amount
        if self.code == "rose" :
            Bush.ROSE_AMOUNT += self.flower_amount

    def water_consuption(self):
        return (4 * self.flower_amount)+ 10
    
    def sales_value(self) :
        if self.code == "rose" :
            return self.flower_amount * Bush.R 
        return 0 # if user enter another products ... 
    
    @classmethod
    def get_rose_value(cls):
        return cls.ROSE_AMOUNT


#----------------------------------Main-------------------------------------------#

def Main():

    """
    Please tell what you want to plant :
    1 - Trees
    2 - Bush
    3 - Display data
    4 - finish 

    """

    print("****************************WELCOME DEAR FARMER****************************")
    
    bush_land_list = []
    trees_land_list = []

    while True :
        items_input = input("Please tell what you want to plant : \n 1 : Tree \n 2 : Bush \n 3 : show data \n 4 : break \n ")



        if items_input == "1" :

            
            
            # get the static items from farmer 
            Trees.T = float(input("Please Enter the value of  T  : "))
            Trees.P = float(input("Please Enter the value of  P  : "))

            # get inputs for Trees 
            tree_farm_count = int(input("Please Enter the amount of trees you want farm : "))
            for _ in range(tree_farm_count) :
                code = input("Enter the tree code : ")
                tree_type = input("Enter the tree type (windy / fruit): ").lower()
                height = float(input("Enter the tree Haight : "))
                water_consuption_coefficient = float(input("Enter the water consumption coefficient : "))
                if tree_type == "fruit" :
                    product_amount = float(input("Enter the product amount for fruit trees : "))
            
                    trees_land_list.append(Trees(code , height , water_consuption_coefficient , tree_type , product_amount))
                trees_land_list.append(Trees(code , height , water_consuption_coefficient , tree_type ))
                
                print("------------------------------------------------------------")


        elif items_input == "2" : 

            
            Bush.R = float(input("Please Enter the value of  R  : "))
            # get inputs for Bushes 
            bush_farm_count = int(input("Please Enter the amount of flower bush you want farm : "))
            for _ in  range(bush_farm_count) :
                bush_code = input("Enter the flower bush code (rose / etc ...): ").lower()
                flower_amount = int(input("Enter the amount of flowers : "))
                bush_land_list.append(Bush(bush_code , flower_amount))
                print("------------------------------------------------------------")


        elif items_input == "3":
            # print(trees_land_list) # for debug
            # print(bush_land_list)
            if  (not trees_land_list) and (not bush_land_list):
                print("Nothing to show yet. Please farm something first :))")
            else:
                total_water_cost = sum(tree.water_consuption() for tree in trees_land_list) + sum(bush.water_consuption() for bush in bush_land_list)
                total_sales = sum(tree.sales_value() for tree in trees_land_list if tree.tree_type == "fruit") + sum(bush.sales_value() for bush in bush_land_list)

                # Output

                print(f"Total water consumption: {total_water_cost} cubic meters")
                print(f"Total sales value: {total_sales} ")
                print(f"Total number of windy trees: {Trees.get_windy_trees_value()}")
                print(f"Total number of rose bushes: {Bush.get_rose_value()}")
                print(f"Tall windy trees (h > 5 meters): {len(Trees.get_tall_windy_trees())}")
                print("--------------------------------------------------------------")

        elif items_input == "4":
            print("****************************GOOD LUCK DEAR FARMER****************************")
            print("****************************GOODBYE****************************")
            break



#----------------------------------RUN CODE-------------------------------------------#
if __name__ == "__main__":
    Main()


    














