from state_machine import StateMachine
from states.state1 import State1
from states.state2 import State2

sm = StateMachine()

sm.enter_state(State1)
sm.update()

sm.enter_state(State2)
sm.update()