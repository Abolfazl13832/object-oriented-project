from abc import ABC,abstractmethod
from typing import Any


class BaseClass(ABC):
    _id =0
    object_list = None
    manager = None
    def __init__(self,*args, **kwargs):
        self.id=self.generate_id()
        self.store(self)
        self.set_manager()
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
    @classmethod
    def set_manager(cls):
        if cls.manager is None :
            cls.manager = Manager(cls)



class Manager:
    def __init__(self,_class=None,*args,**kwargs):
        self._class =_class
        super().__init__(*args,**kwargs)
        
        '''میخواهیم یکی از کلاس هایی که قبلا ساختیم رو بگیره و نگه داره توی خودش'''
    
    def search(self, **kwargs):
        results = list()
        for key,value in kwargs.items():
            if key.endswith("__min"):
                key = key[:-5]
                compare_key = "min"
            elif key.endswith("__max"):
                key = key[:-5]
                compare_key = "max"
            else:
                compare_key = "equal"
            for obg in self._class.object_list:
                if hasattr(obg,key):
                    if compare_key == "min":
                        result = bool(getattr(obg,key) >= value)
                    elif compare_key == "max":
                        result = bool(getattr(obg,key) <= value)
                    else:
                        result = bool(getattr(obg,key) == value)
                    
                if result:
                    results.append(obg)
        return results
    
    def get(self,**kwargs):
        for key,value in kwargs.items():
            for object in self._class.object_list:
                if hasattr(object,key) and getattr(object,key) ==value:
                    return object
                return None
            
    def count(self):
        return self._class.object_list