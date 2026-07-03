class StateMachine:
    def __init__(self):
        self.current_state = None

    def enter_state(self, state_cls):
        if self.current_state is not None:
            self.current_state.exit()
        
        self.current_state = state_cls()
        self.current_state.enter()
    
    def update(self):
        if self.current_state:
            self.current_state.update()