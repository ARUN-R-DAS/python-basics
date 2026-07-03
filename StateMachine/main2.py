#main2.py : states can be switched from the states itself

import state_a,state_b,state_c

states = (state_a,state_b,state_c)
current_state = 0

def run_state():
    global current_state
    result = states[current_state].run()
    print(result)
    if result is not None:
        print("opted to switch to state-c")
        current_state = result
        states[current_state].run()

while True:
    run_state()
    i = input("Press Enter to switch states...")
    if current_state < len(states) - 1:
        current_state += 1
    else:
        current_state = 0