from abc import ABC, abstractmethod


class Workable(ABC):
    @abstractmethod
    def work(self):
        pass


class CanEat(ABC):
    @abstractmethod
    def eat(self):
        pass


class HumanWorker(Workable, CanEat):
    def work(self):
        print("Human working...")

    def eat(self):
        print("Human eating...")


class RobotWorker(Workable):
    def work(self):
        print("Robot working...")
