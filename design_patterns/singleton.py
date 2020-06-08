"""A class only ever intended to support a single instance (e.g. a manager
object). Use of singletons is questionable in Python, but may be justified
if there is a need to pass the object to other objects. Even then, 
enforcing singleton behaviour in code, as below, is generally frowned upon"""

class OneOnly:
    _singleton = None
    """__new__ method from Object superclass overridden"""
    def __new__(cls, *args, **kwargs):
        if not cls._singleton:
            """If singleton object hasn't been created, create it by
            calling super()"""
            cls._singleton = super(OneOnly, cls
                ).__new__(cls, *args, **kwargs)
        return cls._singleton