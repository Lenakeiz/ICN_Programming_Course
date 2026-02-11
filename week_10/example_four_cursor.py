from psychopy import visual, core, event, monitors
from psychopy.hardware import mouse

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

def cursor_control(win):
    """Example 4: Hiding and Showing mouse cursor"""
    try:
        # Create mouse object
        mouse_obj = mouse.Mouse(visible=True, win=win)
        
        # Create rectangle stimulus
        rect = visual.Rect(
            win=win,
            width=300, 
            height=300,
            pos=(0, 0),  # Center position
            fillColor=[25, 255, 25],  # Light green
            colorSpace='rgb255'
        )
        
        # Draw green rectangle and flip
        rect.draw()
        win.flip()
        
        # Wait 2 seconds
        core.wait(2.0)
        
        # Hide the cursor
        mouse_obj.setVisible(False)
        
        # Change rectangle color to red and flip
        rect.fillColor = [255, 0, 25]  # Red
        rect.draw()
        win.flip()
        
        # Wait 2 seconds with hidden cursor
        core.wait(2.0)
        
        # Change rectangle color to yellow
        rect.fillColor = [255, 204, 25]  # Yellow
        rect.draw()
        win.flip()
        
        # Set mouse position to bottom-left corner of rectangle
        # Calculate position relative to center
        mouse_x = - 150
        mouse_y = - 150
        mouse_obj.setPos((mouse_x, mouse_y))
        
        # Show cursor
        mouse_obj.setVisible(True)
        
        # Wait final 2 seconds
        core.wait(2.0)

    except Exception as e:
        print(f"Error: {str(e)}")
        raise

if __name__ == "__main__":
    try:
        win = create_window()
        cursor_control(win)
    except Exception as e:
        print(f"Error: {str(e)}")
        raise
    finally:
        if 'win' in locals():
            win.close()
