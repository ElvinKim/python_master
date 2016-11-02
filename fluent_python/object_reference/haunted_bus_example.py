class HauntedBus(object):

    def __init__(self, passengers=[]):
        self.passengers = passengers

    def pick(self, name):
        self.passengers.append(name)

    def drop(self, name):
        self.passengers.remove(name)


if __name__ == "__main__":
    bus1 = HauntedBus(['Alice', "Bill"])
    print('bus1:', bus1.passengers) #bus1: ['Alice', 'Bill']
    bus1.pick("Charlie")
    bus1.drop("Alice")
    print('bus1:', bus1.passengers) #bus1: ['Bill', 'Charlie']
    bus2 = HauntedBus()
    bus2.pick('Carrie')
    print('bus1:', bus1.passengers) #bus1: ['Bill', 'Charlie']
    print('bus2:', bus2.passengers) #bus2: ['Carrie']

    bus3 = HauntedBus()
    print("bus3:", bus3.passengers) #bus3: ['Carrie']
    bus3.pick("Daive")
    print('bus1:', bus1.passengers) #bus1: ['Bill', 'Charlie']
    print('bus2:', bus2.passengers) #bus2: ['Carrie', 'Daive']
    print('bus3:', bus3.passengers) #bus3: ['Carrie', 'Daive']






