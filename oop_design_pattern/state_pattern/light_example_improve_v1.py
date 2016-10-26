import abc

class State(abc.ABC):
    @abc.abstractmethod
    def on_button_pushed(self, light):
        pass

    @abc.abstractmethod
    def off_button_pushed(self, light):
        pass


class ON(State):
    def on_button_pushed(self, light):
        print("Sleeping Light on!")
        light.state = SLEEPING()

    def off_button_pushed(self, light):
        print("Light off!")
        light.state = OFF()


class OFF(State):
    def on_button_pushed(self, light):
        print("Light on!")
        light.state = ON()

    def off_button_pushed(self, light):
        print("No response")


class SLEEPING(State):
    def on_button_pushed(self, light):
        print("Light on!")
        light.state = ON()

    def off_button_pushed(self, light):
        print("Light off!")
        light.state = OFF()


class Light(object):

    def __init__(self):
        self._state = OFF()

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, state):
        self._state = state

    def on_button_pushed(self):
        self._state.on_button_pushed(self)


    def off_button_pushed(self):
        self._state.off_button_pushed(self)


if __name__ == "__main__":
    light = Light()

    light.off_button_pushed()
    light.on_button_pushed()
    light.on_button_pushed()
    light.on_button_pushed()
    light.on_button_pushed()
    light.off_button_pushed()

