from base import Manager
from base import BaseClass
from estate import Apartment, House, Store
from deal import Rent,Sell



class ApartmentSell(Manager,BaseClass,Apartment,Sell):
    def show_detail(self):
        self.show_description()
        self.show_price()

class ApartmentRent(BaseClass,Apartment,Rent):
    pass

class HouseSell(BaseClass,House,Sell):
    pass

class HouseRent(BaseClass,House,Rent):
    pass

class StoreSell(BaseClass,Store,Sell):
    pass 

class StoreRent(BaseClass,Store,Rent):
    pass
