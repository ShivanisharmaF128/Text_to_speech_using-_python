# 🗣️ Text-to-Speech App Using Python

A simple yet powerful **Text-to-Speech (TTS)** application built using **Python and pyttsx3** library. This project converts written text into audible speech using an offline voice engine—perfect for beginners exploring speech technology.

![NOTEPAD ](https://github.com/ShivanisharmaF128/Noteped-_using-_python/blob/main/python%20project%20notepad.jfif)

---

## 📌 Objective

The goal of this project is to demonstrate how to convert text into spoken words using the `pyttsx3` library. It's an ideal starting point for those interested in **speech synthesis**, 
**Python scripting**, and **voice-based applications**.
---

## 📝 Overview

- 🎤 Converts user-defined text into speech.
- 🧠 Uses `pyttsx3`, a text-to-speech conversion library in Python.
- 🛠️ Works **offline** (no internet required).
- ⚙️ Customizable speech **rate**, **volume**, and **voice**.
- 🚀 Beginner-friendly and easy to expand into full-fledged apps.

---
## Code
```sh
python --version
import pyttsx3

def text_to_speech(text):
    engine = pyttsx3.init()  # Initialize text-to-speech engine
    
    rate = engine.getProperty('rate')  # Get current speech rate
    engine.setProperty('rate', rate - 70)  # Reduce speech speed
    
    engine.say(text)  # Pass the text to be spoken
    engine.runAndWait()  # Process speech

# Call the function
text_to_speech("Hello, world!")  

```
---
## 📜 Code Explanation

1.**pyttsx3.init()** initializes the TTS engine.

2.**engine.getProperty('rate')** and **engine.setProperty()** allow speech speed customization.

3.**engine.say(text)** queues the input text to be spoken.

4.**engine.runAndWait()** processes and outputs the spoken text.

---

## 📢 Conclusion

This project helped me understand how to use Python for audio output and voice applications. It lays the foundation for developing AI voice bots, 
accessibility tools, or voice-assisted software.

Feel free to ⭐ star this repository if you find it useful! 😊

---
### 🤝 Contribution
Contributions are always welcome!
If you want to improve the UI or add new features, follow these steps:

- Fork this repository 📌
- Make necessary changes 🛠️
- Create a pull request 🔄

----


## 👨‍💻 Author

  Shivani Sharma
  
📌 Passionate about Python, Data Science, and GUI Development.

🌐 Connectact : shivanisharmaf128@gail.com 
