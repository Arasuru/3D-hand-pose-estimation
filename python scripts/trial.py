import pyautogui
import time
import pygetwindow as gw

def bring_obs_to_front():
    """Brings OBS Studio to the front if it's minimized or in the background."""
    windows = gw.getWindowsWithTitle("OBS")
    if windows:
        obs_window = windows[0]
        try:
            if obs_window.isMinimized or not obs_window.isActive:
                if obs_window.isMinimized:
                    obs_window.restore()
                obs_window.activate()
                print("OBS window activated")
                time.sleep(0.3)  # Increased delay for window focus
                pyautogui.click(obs_window.left + 10, obs_window.top + 10)
                time.sleep(0.3)
            return True
        except Exception as e:
            print(f"Error activating OBS window: {e}")
            return False
    else:
        print("OBS window not found. Is OBS running?")
        return False

def start_recording():
    """Simulates pressing the 'Start Recording' hotkey in OBS."""
    if bring_obs_to_front():
        pyautogui.hotkey("ctrl", "k")
        print("Started recording")

def stop_recording():
    """Simulates pressing the 'Stop Recording' hotkey in OBS."""
    if bring_obs_to_front():
        pyautogui.hotkey("ctrl", "s")
        print("Stopped recording")

# Main program
start_recording()
time.sleep(5)
stop_recording()
