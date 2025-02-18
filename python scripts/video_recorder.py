import pyautogui
import time
import pygetwindow as gw
import socket

#setting up server connection function
def connect_to_server(host='localhost', port=33333):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((host, port))
        s.setblocking(False)  # Make socket non-blocking
        print("Connected to server")
    except Exception as e:
        print(f"Failed to connect to server: {e}")
        return None
    return s

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
                time.sleep(0.3)  # Increased delay for window focus
                if not obs_window.isActive:
                    print("Window activation might have failed")
                else:
                    print("OBS window activated successfully")
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
        pyautogui.hotkey("ctrl", "r")
        print("Started recording")

def stop_recording():
    """Simulates pressing the 'Stop Recording' hotkey in OBS."""
    if bring_obs_to_front():
        pyautogui.hotkey("ctrl", "q")
        print("Stopped recording")

s = connect_to_server()
while(True):
    try:
        data = s.recv(1024)
        if data == b'START':
            start_recording()
        elif data == b'STOP':
            stop_recording()
            break
    except BlockingIOError:
        pass
    except Exception as e:
        print(f"caught error in server message {e}")
        break

