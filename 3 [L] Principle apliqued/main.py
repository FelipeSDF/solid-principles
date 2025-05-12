class Bird:
    pass


class FlyingBird(Bird):
    def fly(self):
        print("Flying...")


class OtherFlyingBird(FlyingBird):
    pass
    # make same things of his dad


class NotFlyingBird(Bird):
    pass
    # have'nt impossible promisses here
