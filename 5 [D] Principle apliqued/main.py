from abc import ABC, abstractmethod


class Switchable(ABC):
    @abstractmethod
    def turnOn(self):
        pass

    @abstractmethod
    def turnOff(self):
        pass


class LightBulb(Switchable):
    def turnOn(self):
        print("LightBulb turned on")

    def turnOff(self):
        print("LightBulb turned off")


class Fan(Switchable):
    def turnOn(self):
        print("Fan turned on")

    def turnOff(self):
        print("Fan turned off")


class Switch:
    def __init__(self, device: Switchable):
        self.device = device

    def operate(self):
        self.device.turnOn()
        self.device.turnOff()


if __name__ == '__main__':
    lightBulb = LightBulb()
    fan = Fan()

    switchForLight = Switch(lightBulb)
    switchForFan = Switch(fan)

    print("Operating light bulb:")
    switchForLight.operate()

    print("\nOperating fan:")
    switchForFan.operate()
