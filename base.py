from abc import ABC,abstractmethod


class BaseClass(ABC):
    _id =0
    object_list = list()
    def __init__(self):
        self.id=self.generate_id()
        self.store(self)
    

    @classmethod#چون میخواهیم متغیر های مربوط به کلاس رو تغییر بدیم از این استفاده میکنیم
    def generate_id(cls):
        cls._id+=1
        return cls._id
    @classmethod
    def store(cls,object):
        cls.object_list.append(object)

