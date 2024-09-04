from base import BaseClass
from user import User
from random import choice
from estate import Apartment, House
from region import Region
from adventisment import ApartmentSell
FRIST_NAME = ['Ali','Reza','Mahdi']
LAST_NAME = ['Alipour','Rezai','Mahdavi']
MOBILES = ['09929399646','09149532618','09145361568' , '09143598388','09389286531']

if __name__ == "__main__":
    for mobile in MOBILES:
        User(choice(FRIST_NAME),choice(LAST_NAME),mobile)
        

    for user in User.object_list:
        print(f"ID ---> '{user.id}'\nfullname --->'{user.full_name}'\n =====================")

    reg1=Region(name="R1")
    apt1=Apartment(
        user=User.object_list[0],area=80,rooms_count=2,build_year=1393,
        has_elevator=True,
        has_parking=True,
        floor=2,
        region = reg1,
        address = "some text",
    )
    reg2=Region("R2")
    house = House(
        user=User.object_list[2],area=800,rooms_count=6,build_year=1400,
        has_yard=True,
        floors_count=2,
        region = reg2,
        address = "some text",

    )
    reg3=Region("R3")
    house1 = House(
        user=User.object_list[3],area=800,rooms_count=6,build_year=1400,
        has_yard=True,
        floors_count=2,
        region = reg3,
        address = "some text",

    )

    ape2=ApartmentSell(
        user=User.object_list[0],area=80,rooms_count=2,build_year=1393,
        has_elevator=True,
        has_parking=True,
        floor=2,
        region = reg1,
        address = "some text",
        price_per_meter = 10,
        discountable = True,
        convertable = False
    )
    ape2.show_detail()
    ape2.id 
    # print(BaseClass.object_list)
