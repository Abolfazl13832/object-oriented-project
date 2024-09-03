from base import BaseClass
from estate import Apartment, House, Store
from deal import Rent,Sell



class ApartmentSell(BaseClass,Apartment,Sell):
    pass
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
