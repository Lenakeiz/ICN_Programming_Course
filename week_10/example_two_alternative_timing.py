from psychopy import visual, core, event, monitors
import numpy as np
import time
from datetime import datetime
from screeninfo import get_monitors

def create_window():
    # Get system monitors information
    system_monitors = get_monitors()
    print(f"System detected monitors: {system_monitors}")
    
    # Get the external monitor (it may be indexed differently on your system)
    screen_index = 1 if len(system_monitors) > 1 else 0
    target_monitor = system_monitors[screen_index]
    print(f"Using monitor: {target_monitor}")
    print(f"Resolution: {target_monitor.width}x{target_monitor.height}")
    """Create a PsychoPy window with black background"""
    return visual.Window(
        fullscr=True,
        monitor="testMonitor",
        units="pix",
        color=[0, 0, 0],
        colorSpace='rgb255',
        screen=screen_index
    )

def alternative_timing(win):
    """Example 2: Reading keyboard input with timings (part 2)"""
    try:

        # Create variables for timing and response tracking
        trial_duration = 4.0
        read_response = False
        react_time = 0
        keys = []

        # Create instruction text
        instruction = visual.TextStim(
            win=win,
            text="Press any key to respond\n\nYou have 4 seconds to respond",
            pos=(0, 0),
            color=[255, 255, 255],
            colorSpace='rgb255',
            height=30,
            units='pix'
        )
        
        # Draw instruction and flip window
        instruction.draw()
        win.flip()        
           
        # Get start times
        start_t = core.getTime()
        curr_t = start_t
        
        print(f"Showing keyboard timings using example 2. Start time: {start_t:.3f}s")
        resp_key = None
        
        # Main trial loop
        while (curr_t - start_t <= trial_duration):
            # Check for key presses
            keys = event.getKeys(timeStamped=True)
            
            # Process any key presses if we haven't already recorded one
            if keys and not read_response:
                resp_key = keys[0][0]  # Get key name
                react_time = keys[0][1] - start_t  # Get reaction time
                read_response = True
                
            # Update current time and refresh screen
            curr_t = core.getTime()
        
        # Display results
        end_t = core.getTime()
        print(f"Time elapsed for script execution (psycopy core time): {(end_t-start_t):.3f}")
        if resp_key:
            print(f"You pressed key {resp_key} after {react_time:.3f} seconds")
        else:
            print("No key was pressed")

    except Exception as e:
        print(f"Error: {str(e)}")
        raise

if __name__ == "__main__":
    try:
        # Create window to be used across all examples
        win = create_window()
        alternative_timing(win)
        
    except Exception as e:
        print(f"Error: {str(e)}")
        raise
    finally:
        # Ensure window is closed properly
        if 'win' in locals():
            win.close()