from psychopy import visual, event, core
from screeninfo import get_monitors

def demonstrate_clear_events(screen_index=0):
    """Demonstrate the effect of clearEvents in waitKeys."""
    try:
        win = visual.Window(
            fullscr=True,
            monitor="testMonitor",
            units="pix",
            color=[0, 0, 0],
            colorSpace='rgb255',
            screen=screen_index
        )
        
        # First demonstration: WITHOUT clearing events
        instruction = visual.TextStim(
            win=win,
            text='Spam some keys NOW...\n(waiting 3 seconds)',
            height=45,
            color=[255, 255, 255],
            colorSpace='rgb255'
        )
        instruction.draw()
        win.flip()
        
        # Give user time to press keys
        core.wait(3)
        
        # Now check with clearEvents=False
        instruction.text = 'Now stopped collecting.\nWatch what happens with clearEvents=False...'
        instruction.draw()
        win.flip()
        core.wait(2)
        
        keys = event.waitKeys(clearEvents=False)
        print("Keys detected (without clearing):", keys)
        
        # Second demonstration: WITH clearing events
        instruction.text = 'Spam some keys NOW...\n(waiting 3 seconds)'
        instruction.draw()
        win.flip()
        
        # Give user time to press keys
        core.wait(3)
        
        # Now check with clearEvents=True (default)
        instruction.text = 'Now stopped collecting.\nWatch what happens with clearEvents=True...'
        instruction.draw()
        win.flip()
        core.wait(2)
        
        keys = event.waitKeys(clearEvents=True)  # This is actually the default
        print("Keys detected (with clearing):", keys)
        
        # Cleanup
        win.close()
        
    except Exception as e:
        if 'win' in locals():
            win.close()
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    # Get system monitors information
    system_monitors = get_monitors()
    print(f"System detected monitors: {system_monitors}")
    
    # Get the external monitor (it may be indexed differently on your system)
    screen_index = 1 if len(system_monitors) > 1 else 0
    target_monitor = system_monitors[screen_index]
    print(f"Using monitor: {target_monitor}")
    print(f"Resolution: {target_monitor.width}x{target_monitor.height}")
    demonstrate_clear_events(screen_index)