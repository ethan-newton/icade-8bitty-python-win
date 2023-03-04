import vgamepad as vg
import keyboard

# Initialize the virtual gamepad
gamepad = vg.VX360Gamepad()

# Define the button mappings (replace the key names with the ones you want to use)
button_mappings = {
    'button_a': [0x1000, 'l', 'v'],
    'button_b': [0x2000, 'k', 'p'],
    'button_x': [0x4000, 'o', 'g'],
    'button_y': [0x8000, 'i', 'm'],
    'button_start': [0x0010, 'u', 'f'],
    'button_select': [0x0020, 'y', 't'],
    'button_left_shoulder': [0x0100, 'h', 'r'],
    'button_right_shoulder': [0x0200, 'j', 'n'],
    'dpad_up': [1, 'w', 'e'],
    'dpad_down': [2, 'x', 'z'],
    'dpad_left': [4, 'a', 'q'],
    'dpad_right': [8, 'd', 'c']
}

# Define a function to map a keyboard press to a gamepad button press or release
def map_key_to_button(key, button, is_press):
    if keyboard.is_pressed(key):
        if is_press:
            gamepad.press_button(button_mappings[button][0])
        else:
            gamepad.release_button(button_mappings[button][0])

# Main loop to update the gamepad state
while True:
    # Map each keyboard key to the corresponding gamepad button press or release
    for button, keys in button_mappings.items():
        map_key_to_button(keys[1], button, True)
        map_key_to_button(keys[2], button, False)

    # Update the gamepad state
    gamepad.update()
    
