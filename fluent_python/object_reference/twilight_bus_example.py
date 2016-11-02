
class TwilightBus(object):

    def __init__(self, passengers=None):
        if passengers is None:
            self.passengers = []
        else:
            self.passengers = passengers

    def pick(self, name):
        self.passengers.append(name)

    def drop(self, name):
        self.passengers.remove(name)


class Bus(object):

    def __init__(self, passengers=None):
        if passengers is None:
            self.passengers = []
        else:
            self.passengers = list(passengers)

    def pick(self, name):
        self.passengers.append(name)

    def drop(self, name):
        self.passengers.remove(name)

if __name__ == "__main__":
    basketball_team = ['A', 'B', "C", 'D', 'E']
    bus = TwilightBus(basketball_team)
    bus.drop('A')
    bus.drop('B')
    print(basketball_team) #['C', 'D', 'E']

    basketball_team = ['A', 'B', "C", 'D', 'E']
    bus = Bus(basketball_team)
    bus.drop('A')
    bus.drop('B')
    print(basketball_team) #['A', 'B', 'C', 'D', 'E']
