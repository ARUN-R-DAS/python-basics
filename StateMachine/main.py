#main.py : simple switching cotrolled by main.py only

import state_a,state_b,state_c

current_state = 0
states = (state_a,state_b,state_c)

def run_state():
    states[current_state].run()

print("Press ENTER to toggle states. Ctrl+C to quit.\n")

while True:
    run_state()
    input("Press ENTER to switch state...")

    if current_state < len(states) - 1:
        current_state += 1
    else:
        current_state = 0
    
    print("\n--- Switching ---\n")
