from constant import *

class Light(object):

    def __init__(self):
        self.state = LIGHT_STATE.OFF

    def on_button_pushed(self):
        if self.state == LIGHT_STATE.ON:
            print("Sleeping Light On!")
            self.state = LIGHT_STATE.SLEEPING
        elif self.state == LIGHT_STATE.SLEEPING:
            print("Light On!")
            self.state = LIGHT_STATE.ON
        else :
            print("Light On!")
            self.state = LIGHT_STATE.ON

    def off_button_pushed(self):
        if self.state == LIGHT_STATE.OFF:
            print("No response")
        else :
            print("Light Off!")
            self.state = LIGHT_STATE.OFF


if __name__ == "__main__":
    light = Light()

    light.off_button_pushed()
    light.on_button_pushed()
    light.off_button_pushed()