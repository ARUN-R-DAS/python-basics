from .state import State

class State2(State):
    def enter(self):
        print("Entering State 2")
    
    def exit(self):
        print("Leaving State 2")
    
    def update(self):
        print("Updating State 2")