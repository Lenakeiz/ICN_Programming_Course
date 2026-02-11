from psychopy import visual, core, event, monitors
import numpy as np

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

def framerate_timing(win):
    """Example 3: Calculating duration of stimulus presentation using display frame rate"""
    try:
        
        required_seconds = 0.5

        # Create rectangle for color changes
        rect = visual.Rect(
            win=win,
            width=600,
            height=600,
            units='pix',
            colorSpace='rgb255'
        )
        
        # Create instruction text
        instruction = visual.TextStim(
            win=win,
            text=f"Colors will change every {required_seconds} seconds\n\nPress any key to exit",
            pos=(0, 0),
            color=[255, 255, 255],
            colorSpace='rgb255',
            height=50,
            units='pix'
        )
        
        # Show instructions
        instruction.draw()
        win.flip()
        core.wait(2.0)
        
        # Main loop
        display_times = []  # Store actual display durations
        
        while not event.getKeys():
            # Set new random color
            rect.fillColor = [
                np.random.randint(0, 256),
                np.random.randint(0, 256),
                np.random.randint(0, 256)
            ]
            
            # Draw stimulus
            rect.draw()
            stimulus_onset = win.flip()
            
            # Wait for the calculated number of frames
            core.wait(required_seconds)

            stimulus_offset = core.getTime()

            # Store actual duration
            actual_duration = stimulus_offset - stimulus_onset
            display_times.append(actual_duration)

        # Calculate and display timing statistics
        display_times = np.array(display_times)
        print(f"\nTiming Statistics:")
        print(f"Mean display duration: {np.mean(display_times):.4f} seconds")
        print(f"Std display duration: {np.std(display_times):.4f} seconds")
        print(f"Min display duration: {np.min(display_times):.4f} seconds")
        print(f"Max display duration: {np.max(display_times):.4f} seconds")
        print(f"Target duration was: {required_seconds:.4f} seconds")

    except Exception as e:
        print(f"Error: {str(e)}")
        raise

if __name__ == "__main__":
    try:
        win = create_window()
        framerate_timing(win)
    except Exception as e:
        print(f"Error: {str(e)}")
        raise
    finally:
        if 'win' in locals():
            win.close()