from base import BaseClass

class User(BaseClass):
    def __init__(self,frist_name,last_name,phone_number,*args,**kwargs):
        self.frist_name = frist_name
        self.last_name  = last_name
        self.phone_number = phone_number
        super().__init__(*args,**kwargs)

    @property
    def full_name(self):
        return f"{self.frist_name} {self.last_name}"


