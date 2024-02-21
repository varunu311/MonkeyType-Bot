import easyocr
import pyautogui
import keyboard
import numpy as np
import time  # Import time for adding delays

def take_screenshot(x1, y1, width, height):
    screenshot = pyautogui.screenshot(region=(x1, y1, width, height))
    return screenshot

def extract_text_from_image(image):
    reader = easyocr.Reader(['en'])  # Initialize EasyOCR reader
    image_np = np.array(image)  # Convert PIL Image to NumPy array
    result = reader.readtext(image_np)  # Use the NumPy array with EasyOCR
    text = ' '.join([item[1] for item in result])  # Extracting text from results
    return text

def type_text(text):
    words = text.split(' ')  # Split the text into words
    if len(words) > 1:  # Check if there is more than one word
        remaining_text = ' '.join(words[1:])  # Join the remaining words back into text
        keyboard.write(remaining_text, delay=0.32)  # Type the remaining text
    else:
        print("No additional words to type.")

def wait_for_first_word():
    print("Type the first word and press space to continue...")
    keyboard.wait('space')  # Wait for space key to be pressed

def main():
    print("Press 'space'to take a screenshot.")

    x1, y1, width, height = 150, 470, 1200, 140  # Adjusted from x2, y2 to width, height
    screenshot_taken = False

    while not screenshot_taken:
        if keyboard.is_pressed("space") and not screenshot_taken:
            screenshot = take_screenshot(x1, y1, width, height)
            screenshot.save("screenshot.png")  # Save the screenshot for verification
            extracted_text = extract_text_from_image(screenshot)

            print("Text Extraction Completed!")
            screenshot_taken = True

    wait_for_first_word()  # Wait for the first word to be typed and space pressed
    print("Typing out the remaining text...")
    type_text(extracted_text)

if __name__ == "__main__":
    main()
