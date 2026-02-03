# Import necessary modules from PsychoPy
from psychopy import visual, core, monitors, logging, event
from screeninfo import get_monitors

def display_text(screen_index=0):
    try:
        # Create a window with a black background
        win = visual.Window(
            fullscr=True,
            monitor="testMonitor",
            units="pix",
            color=[0, 0, 0],
            colorSpace='rgb255',
            screen=screen_index
        )
        
        # Create first text stimulus
        text1 = visual.TextStim(
            win=win,
            text='Here is some text displayed on the center of the PsychoPy window...',
            font='Courier New',
            pos=(0, 0),  # Center of screen
            color=[255, 0, 255],  # Magenta in rgb255
            height=30,
            bold=True,
            italic=True,           
            wrapWidth=200,
            anchorHoriz='center', # relative to pos
            anchorVert='center', # relative to pos
            units='pix'
        )
        
        # Get and print the bounding box information
        bbox = text1.boundingBox
        print("Bounding box:", bbox)
        print("Text1 position:", text1.pos)
        print("Window size:", win.size)
        
        # Create second text stimulus using the bounding box left position
        text2 = visual.TextStim(
            win=win,
            text='And this is just after the previous one...',
            font='Courier New',
            pos=(text1.pos[0] - bbox[0]/2, text1.pos[1] - bbox[1]/2 - 40), # with a small offset in pixels as we changed the units to pix
            color=[0, 255, 0],  # Green in rgb255
            height=30,
            wrapWidth=500,
            bold=True,
            italic=True,
            anchorHoriz='left',
            units='pix'
        )

        # Draw both text stimuli
        text1.draw()
        text2.draw()

        # Update the display
        win.flip()

        # Wait for a keypress
        event.waitKeys()

        # Close the window
        win.close()

    except Exception as e:
        if 'win' in locals():
            win.close()
        raise e

if __name__ == "__main__":
    # Get system monitors information
    system_monitors = get_monitors()
    print(f"System detected monitors: {system_monitors}")
    
    # Get the external monitor (it may be indexed differently on your system)
    screen_index = 1 if len(system_monitors) > 1 else 0
    target_monitor = system_monitors[screen_index]
    print(f"Using monitor: {target_monitor}")
    print(f"Resolution: {target_monitor.width}x{target_monitor.height}")
    display_text(screen_index)