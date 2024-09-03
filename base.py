from abc import ABC,abstractmethod


class BaseClass(ABC):
    _id =0
    object_list = None
    def __init__(self,*args, **kwargs):
        self.id=self.generate_id()
        self.store(self)
        super().__init__(*args, **kwargs)
    

    @classmethod#چون میخواهیم متغیر های مربوط به کلاس رو تغییر بدیم از این استفاده میکنیم
    def generate_id(cls):
        cls._id+=1
        return cls._id
    @classmethod
    def store(cls,object):
        if cls.object_list is None:
            cls.object_list = list()
        cls.object_list.append(object)

