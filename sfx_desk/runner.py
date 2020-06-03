import sys
from safety_groups import MasterSafetyGroup, SafetyGroup
import modules

global_master = None
pyro_master = None
sg1 = None
sg2 = None


def run():
    global global_master
    global pyro_master
    global sg1
    global sg2
    global_master = MasterSafetyGroup(name="global master")
    pyro_master = MasterSafetyGroup(name="pyro master")
    sg1 = SafetyGroup(name="stage")
    sg2 = SafetyGroup(name="backstage pyro")










if __name__ == "__main__":
    run()