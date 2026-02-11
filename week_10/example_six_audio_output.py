import numpy as np
from psychopy import sound, core, prefs

def list_audio_devices():
    """Print all available audio devices using PsychToolbox"""
    try:
        import psychtoolbox.audio
        from pprint import pprint
        print("\nAvailable audio devices:")
        pprint(psychtoolbox.audio.get_devices())
    except ImportError:
        print("\nPsychToolbox not available — cannot list devices.")
        print("Using default audio device.")

def play_tone(frequency=440, duration=0.5, volume=0.5, octave=4):
    """Play a simple tone using PsychoPy Sound
    
    Parameters:
    -----------
    frequency : float
        Frequency in Hz (default: 440Hz, note A4)
    duration : float
        Duration in seconds (default: 0.5s)
    volume : float
        Volume between 0 and 1 (default: 0.5)
    octave : int
        Octave for note names (default: 4, middle octave)
    """
    # Create a tone at the given frequency
    # PsychoPy Sound accepts a frequency (Hz), note name ('A', 'C'), or file path
    tone = sound.Sound(value=frequency, secs=duration, volume=volume)
    
    print(f"\nPlaying {frequency}Hz tone...")
    tone.play()
    core.wait(duration)  # Wait for the tone to finish
    tone.stop()
    print("Tone finished!")

def play_wav_file(file_path):
    """Play a WAV file using PsychoPy Sound
    
    Parameters:
    -----------
    file_path : str
        Path to the WAV file
    """
    try:
        # Load and play the WAV file
        wav_sound = sound.Sound(value=file_path)
        
        print(f"\nPlaying WAV file: {file_path}")
        wav_sound.play()
        core.wait(wav_sound.getDuration())  # Wait for the sound to finish
        wav_sound.stop()
        print("WAV file finished!")
        
    except Exception as e:
        print(f"Error playing WAV file: {str(e)}")

def test_audio():
    """Test both tone and WAV file playback"""
    try:
        # Set the audio backend to PTB (recommended for low latency)
        # Other options: 'sounddevice', 'pyo', 'pygame'
        prefs.hardware['audioLib'] = ['ptb']
        # Set the default speaker to Realtek audio (DeviceIndex 4) - this is the default on my computer
        # You may need to change this to the correct device name for your computer based on the output of list_audio_devices()
        prefs.hardware['audioDevice'] = ['Speakers (Realtek(R) Audio)']
        # List available devices
        list_audio_devices()
        
        # Play a test tone (440Hz = A4 note)
        play_tone(frequency=440, duration=0.5)
        
        # Wait a moment between sounds
        core.wait(0.5)
        
        # Try to play a WAV file if it exists
        try:
            play_wav_file('./week_10/assets/pos_feedback.wav')
        except Exception as e:
            print(f"Note: WAV file test skipped - {str(e)}")
        
    except Exception as e:
        print(f"Error occurred: {str(e)}")
        print(f"Error type: {type(e)}")

if __name__ == "__main__":
    test_audio()
