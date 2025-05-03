import pyttsx3

def text_to_speech(text):
    engine = pyttsx3.init()  # Initialize text-to-speech engine
    
    rate = engine.getProperty('rate')  # Get current speech rate
    engine.setProperty('rate', rate - 70)  # Reduce speech speed
    
    engine.say(text)  # Pass the text to be spoken
    engine.runAndWait()  # Process speech

# Call the function
text_to_speech("Hello, world!")  
