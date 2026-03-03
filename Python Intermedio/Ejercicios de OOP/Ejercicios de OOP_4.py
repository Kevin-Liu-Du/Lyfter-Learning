class Human:
    def __init__(self, head, torso, left_leg, right_leg):
        self.head = head
        self.torso = torso
        self.left_leg = left_leg
        self.right_leg = right_leg

    def print_info(self):
        print(f"Head hair: {self.head.hair}")
        print(f"Left arm fingers: {self.torso.left_arm.hand.fingers}")
        print(f"Right arm nails: {self.torso.right_arm.hand.nails}")
        print(f"Left leg nails: {self.left_leg.foot.nails}")
        print(f"Right leg nails: {self.right_leg.foot.nails}")

class Head:
    def __init__(self, hair):
        self.hair = hair

class Torso:
    def __init__(self, left_arm, right_arm):
        self.left_arm = left_arm
        self.right_arm = right_arm

class Arm:
    def __init__(self, hand):
        self.hand = hand

class Hand:
    def __init__(self, fingers, nails):
        self.fingers = fingers
        self.nails = nails

class Leg:
    def __init__(self, foot):
        self.foot = foot


class Feet:
    def __init__(self, nails):
        self.nails = nails


person = Human(head=Head("Black"), torso=Torso(left_arm=Arm(Hand(5, "Short")), right_arm=Arm(Hand(5, "Short"))), left_leg=Leg(Feet("Short")), right_leg=Leg(Feet("Short")))
person.print_info()
