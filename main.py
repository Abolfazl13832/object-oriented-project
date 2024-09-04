from base import BaseClass
from user import User
from random import choice
from estate import Apartment, House
from region import Region
from adventisment import ApartmentSell, HouseSell
FRIST_NAME = ['Ali','Reza','Mahdi']
LAST_NAME = ['Alipour','Rezai','Mahdavi']
MOBILES = ['09929399646','09149532618','09145361568' , '09143598388','09389286531']

if __name__ == "__main__":
    for mobile in MOBILES:
        User(choice(FRIST_NAME),choice(LAST_NAME),mobile)
    print(User.object_list)

    reg1=Region("r1")
    ape1=ApartmentSell(
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
    reg1=Region("r1")
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

    reg1=Region("r1")
    ape3=ApartmentSell(
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
#     print(f"""
#         user---> {ape2.user.full_name}
#         area---> {ape2.area} 
#         rooms count---> {ape2.rooms_count}
#         build year---> {ape2.build_year}
#         region---> {ape2.region.name}
#         address---> {ape2.address}

# """
#     )
#     print(ApartmentSell.object_list)


    