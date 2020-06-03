import abc

"""Abstract base class representing armable duck type"""
class Armable(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def arm(self):
        pass

    @classmethod
    def __subclasshook__(cls, C):
        if cls is Armable:
            attrs = set(dir(C))
            if set(cls.__abstractmethods__) <= attrs:
                return True

        return NotImplemented

"""Abstract base class representing fireable duck type"""
class Fireable(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def fire(self):
        pass

    @classmethod
    def __subclasshook__(cls, C):
        if cls is Fireable:
            attrs = set(dir(C))
            if set(cls.__abstractmethods__) <= attrs:
                return True

        return NotImplemented


class BaseModule:
    """Parent module for all other modules"""
    def __init__(self, *args, **kwargs):
        self.status = "Disabled"
        self.safety_group = None if isinstance(self, Fireable) else "Global"
        self.id = None
        self.friendly_name = None


    def enable(self):
        self.status = "Enabled"

    def disable(self):
        self.status = "Disabled"


class WirelessModule(BaseModule):
    def __init__(self, *args, **kwargs):
        self.battery_level = None
        self.rf_strength = None
        self.signal_strength_mode = False
        super().__init__(self, *args, **kwargs)

    def toggle_signal_strength_mode(self):
        self.signal_strength_mode = True if not self.signal_strength_mode else False



class WiredModule(BaseModule):
    def __init__(self, *args, **kwargs):
        super().__init(self, *args, **kwargs)


class Deadman(WirelessModule):
    pass    


class Beacon(WirelessModule):

    def arm(self):
        print("Armed!")


class Pyro(WirelessModule):

    def arm(self):
        print("Armed!")

    def fire(self, output):
        print(str(output) + " Firing!")


class WirelessRelay(WirelessModule):

    def arm(self):
        print("Armed!")

    def fire(self, output):
        print(str(output) + " Firing!")


class WiredRelay(WiredModule):

    def arm(self):
        print("Armed!")

    def fire(self, output):
        print(str(output) + " Firing!")
