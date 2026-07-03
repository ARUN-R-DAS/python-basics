import state_a
import state_b

current_state = 0

def run_state():
    if current_state == 0:
        state_a.run()
    else:
        state_b.run()

print("Press ENTER to toggle states. Ctrl+C to quit.\n")

while True:
    run_state()
    input("Press ENTER to switch state...")

    if current_state == 0:
        current_state = 1
    else:
        current_state = 0
    
    print("\n--- Switching ---\n")