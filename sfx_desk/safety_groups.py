class MasterSafetyGroup:
    def __init__(self, *args, **kwargs):
        self.name = kwargs["name"]
        self.arming_circuit = [self]
        self.armed = False
        self.safety_groups = []
        self.disabled = True

    def arm(self):
        print(self.name + " master armed")

    def add_safety_group(self, safety_group):
        self.safety_groups.append(safety_group)
        safety_group.master = self
        safety_group.arming_circuit.extend(self.arming_circuit)

    def remove_safety_group(self, safety_group):
        pass


class SafetyGroup:
    def __init__(self, *args, **kwargs):
        self.name = kwargs["name"]
        self.arming_circuit = []
        self.contains_pyro = False
        self.modules = {}
        self.master = None
        self.disabled = True

    def arm(self):
        for armable in self.arming_circuit:
            if not armable.armed
            break

        print("safety group " + self.name + " armed")
