from playsound import playsound
from gtts import gTTS
import os

myText = "The Python features like one-liners and dynamic type system allow developers to write very fewer lines of code for tasks that require more lines of code in other languages. This makes Python very easy-to-learn programming language even for beginners and newbies. For instance, Python programs are slower than Java, but they also take very less time to develop, as Python codes are 3 to 5 times shorter than Java codes."

language = 'en'

output = gTTS(text=myText, lang=language, slow=False)

output.save("Assistant.mp3")

playsound('Assistant.mp3')

