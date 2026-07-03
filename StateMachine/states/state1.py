from .state import State

class State1(State):
    def enter(self):
        print("Entering State 1")

    def exit(self):
        print("Leaving State 1")

    def update(self):
        print("Updating State 1")