import pyttsx3

text =pyttsx3.init()

ans=input()
text.say(ans)
text.runAndWait()