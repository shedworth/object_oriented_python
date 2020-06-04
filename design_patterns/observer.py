"""Object under observation notifies observer object 
when an attribute is changed"""

class Inventory:
"""Object under observation"""
    def __init__(self):
        self.observers = []
        self._product = None
        self._quantity = 0

    def attach(self, observer):
        self.observers.append(observer)

    @property
    def product(self):
        return self._product
    
    @product.setter
    def product(self, value):
        self._product = value
        """Update observers when product attribute
        is changed"""
        self._update_observers()

    @property
    def quantity(self):
        return self._quantity
    
    @quantity.setter
    def quantity(self, value):
        self._quantity = value
        """Update observers when quantity attribute
        is changed"""
        self._update_observers()

    def _update_observers(self):
    """Updates all attached observers"""
        for observer in self.observers:
            """observer can be called in this way because
            it implements the '__call__' builtin method"""
            observer()


class ConsoleObserver:
"""Observer object bound to a single inventory"""
    def __init__(self, inventory):
        self.inventory = inventory

    def __call__(self):
        print(self.inventory.product)
        print(self.inventory.quantity)