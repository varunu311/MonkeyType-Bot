import easyocr
import pyautogui
import keyboard
import numpy as np
import time

def take_screenshot(x1, y1, width, height):
    screenshot = pyautogui.screenshot(region=(x1, y1, width, height))
    return screenshot

def extract_text_from_image(image):
    reader = easyocr.Reader(['en'])
    image_np = np.array(image)
    result = reader.readtext(image_np)
    text = ' '.join([item[1] for item in result])
    return text

def type_text(text):
    words = text.split(' ')
    if len(words) > 1:
        remaining_text = ' '.join(words[1:])
        keyboard.write(remaining_text, delay=0.32)
    else:
        print("No additional words to type.")

def wait_for_first_word():
    print("Type the first word and press space to continue...")
    keyboard.wait('space')

def main():
    print("Press 'space'to take a screenshot.")

    x1, y1, width, height = 150, 470, 1200, 140  # Ajust based on your screen resolution
    screenshot_taken = False

    while not screenshot_taken:
        if keyboard.is_pressed("space") and not screenshot_taken:
            screenshot = take_screenshot(x1, y1, width, height)
            screenshot.save("screenshot.png")
            extracted_text = extract_text_from_image(screenshot)

            print("Text Extraction Completed!")
            screenshot_taken = True

    wait_for_first_word()
    print("Typing out the remaining text...")
    type_text(extracted_text)

if __name__ == "__main__":
    main()
