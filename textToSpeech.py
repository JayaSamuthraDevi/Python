# import pyttsx3

# text =pyttsx3.init()

# ans=input()
# text.say(ans)
# text.runAndWait()

import pyttsx3
  
def onStart():
   print('starting')
  
def onWord(name, location, length):
   print('speaking', name, location, length)
  
def onEnd(name, completed):
   print('finishing', name, completed)
  
engine = pyttsx3.init()
  
engine.connect('started-utterance', onStart)
engine.connect('started-word', onWord)
engine.connect('finished-utterance', onEnd)
  
sen = 'This is a sentence spoken by a computer portal '
  
  
engine.say(sen)
engine.runAndWait()

