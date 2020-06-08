"""The flyweight is a memory optimisation tool. A class maintains a record of 
all of its instances (e.g. within a class dictionary). When new objects are
instantiated, the dictionary is first checked to see if the object already
exists. If it does, the object is returned from the dictionary. If it does not,
a new instance is created."""


import weakref


class CarModel:
    """Class dictionary containing all models. The WeakValueDictionary
    allows models to be garbage-collected if they are not referenced elsewhere
    in the program (e.g. if a model is discontinued or no longer sold)."""
    _models = weakref.WeakValueDictionary()

    """When creating a new model, look it up in the dictionary. If it exists,
    return model from dictionary; if it doesn't, create new model and add
    to dictionary."""
    def __new__(cls, model_name, *args, **kwargs):
        model = cls._models.get(model_name)
        if not model:
            """Create new model"""
            model = super().__new__(cls)
            cls._models[model_name] = model

        return model

    def __init__(
        self,
        model_name,
        air=False,
        tilt=False,
        cruise_control=False,
        power_locks=False,
        alloy_wheels=False,
        usb_charger=False
    ):
        """Ensure object is only initialised when called for
        the first time"""
        if not hasattr(self, "initted"):
            self.model_name = model_name
            self.air = air
            self.tilt = tilt
            self.cruise_control = cruise_control
            self.power_locks = power_locks
            self.alloy_wheels = alloy_wheels
            self.usb_charger = usb_charger
            self.initted = True

    def check_serial(self, serial_number):
        print(
            "Sorry, we are unable to check "
            "the serial number {0} on {1} "
            "at this time".format(serial_number, self.model_name)
        )


class Car:
    def __init__(self, model, colour, serial):
        self.model = model
        self.colour = colour
        self.serial = serial 

    def check_serial(self):
        return self.model.check_serial(self.serial)