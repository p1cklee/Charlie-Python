import openai
import pyperclip
import keyboard
from plyer import notification

# Your OpenAI GPT-3 API key
api_key = 'API KEY HERE!!!!!!!!!!!!'  # Replace with your API key

# Function to correct spelling and grammar
def correct_text_with_gpt3(text):
    openai.api_key = api_key

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=f"Correct the following text: '{text}'\n\n",
        max_tokens=2000,
        n=1,
        stop=None,
        temperature=0.7,
    )

    corrected_text = response.choices[0].text.strip()
    return corrected_text

# Function to copy text to clipboard
def copy_to_clipboard(text):
    pyperclip.copy(text)

# Function to display a system notification
def show_notification(message):
    notification.notify(
        title="Correction Complete",
        message=message,
        app_name="Correction App",
    )

# Main function
def main():
    # Get the text from the clipboard
    clipboard_text = pyperclip.paste()

    if not clipboard_text:
        print("Clipboard is empty. Please copy some text to the clipboard first.")
        return

    corrected_text = correct_text_with_gpt3(clipboard_text)
    copy_to_clipboard(corrected_text)
    print("Original text from clipboard: \n", clipboard_text)
    print("\nCorrected text: \n", corrected_text)
    print("Corrected text has been copied to your clipboard.")

    # Display the "Done!" message as a system notification
    show_notification("Correction complete")

# Define a callback function to run the script when Alt key is pressed
def hotkey_callback(e):
    if keyboard.is_pressed("alt"):
        main()

if __name__ == "__main__":
    # Register the hotkey callback
    keyboard.hook(hotkey_callback)
    
    print("Listening for Alt key press. Press Alt to run the script.")
    keyboard.wait()  # Keep the script running
