import serial  # add Serial library for Serial communication
import speech_recognition as sr
from gtts import gTTS
import os
import time
import winsound
import datetime


Arduino_Serial = serial.Serial('COM6', 9600)  # Create Serial port object called arduinoSerialData
Arduino_Serial.readline()  # read the serial data and print it as line

r = sr.Recognizer()

openLed  = ['open Inlet','open led', 'open lid', 'open lead', 'open late', 'open lined', 'open land', 'openload','open length']
closeLed = ['close Legend','GloZell lead', 'clotheslined', 'close knit', 'close led', 'close lid', 'close lead', 'close late', 'close lined', 'Cloudland', 'close land','clothes','clausland']
openLight    = ['open light','open the light']
closeLight   = ['close light','close the light']
openDoor    = ['open door', 'open the door']
closeDoor   = ['close door','close the door','closed']

nameCMD  = ['friday','renee','fiesta']
closing  = ['bye', 'my', 'by']
greetings = ['how are you', 'how are you friday', 'friday how are you', 'are you okay', 'are you okay friday', 'friday are you okay']

last_sentence = ''
somethingIsDone = True

# η συναρτηση μετατρεπει text σε speech
def speak(myText):
    language = 'en'
    output = gTTS(text=myText, lang=language, slow=False)
    output.save("output.mp3")
    os.system("start output.mp3")

def makeSound():
    frequency = 200  # Set Frequency To 2500 Hertz
    duration = 150  # Set Duration To 1000 ms == 1 second
    winsound.Beep(frequency, duration)

def timer():
    now = datetime.datetime.now()
    return now.hour, now.minute

def date():
    now = datetime.datetime.now()
    return now.month, now.day

while 1:
    if somethingIsDone:
        makeSound()
    with sr.Microphone() as source:
        print('Speak Anything : ')
        audio = r.listen(source)

        try:
            text = r.recognize_google(audio)
            print('You said : {}'.format(text))
            text = text.lower()

            txtSplit = text.split()
            if text in nameCMD:
                speak('yes sir')
                last_sentence = text
            elif 'hello' in txtSplit:
                speak('hello to you too sir')
            elif text in greetings:
                speak('I am fine sir')
            elif 'time' in txtSplit:
                hour, min = timer()
                speak('it is {} and {}'.format(hour, min))
            elif 'date' in txtSplit:
                month, day = date()
                speak('it is the {}th day of {}th month'.format(day, month))
            else:
                if len(txtSplit) > 1:
                    first_word, rest_command = text.lower().split(' ', 1)
                    if first_word in nameCMD:
                        if rest_command in openLed:
                            Arduino_Serial.write(b'1')  # send 1 to arduino
                            print("LED ON")
                        elif rest_command in closeLed:
                            Arduino_Serial.write(b'0')  # send 0 to arduino
                            print("LED OFF")
                        elif rest_command in closing:
                            break
                        if rest_command in openLight:
                            Arduino_Serial.write(b'3')  # send 3 to arduino
                            print("LIGHT ON")
                        elif rest_command in closeLight:
                            Arduino_Serial.write(b'2')  # send 2 to arduino
                            print("LIGHT OFF")
                        elif rest_command in closing:
                            break
                        if rest_command in openDoor:
                            Arduino_Serial.write(b'5')  # send 5 to arduino
                            print("DOOR OPEN")
                        elif rest_command in closeDoor:
                            Arduino_Serial.write(b'4')  # send 4 to arduino
                            print("DOOR CLOSE")
                        elif rest_command in closing:
                            break
                    elif (last_sentence in nameCMD):
                        if text in openCMD:
                            Arduino_Serial.write(b'1')  # send 1 to arduino
                            print("LED ON")
                        elif text in closeCMD:
                            Arduino_Serial.write(b'0')  # send 0 to arduino
                            print("LED OFF")
                        elif text in closing:
                            break
                    else:
                        speak('sir i do not understand your command')
                        text = ''
                else:
                    speak('sir i do not understand your command')
                    text = ''
                last_sentence = ''
            somethingIsDone = True
        except:
            print('Sorry could not recognize your voice')
            somethingIsDone = False
        time.sleep(3)
        text = ''