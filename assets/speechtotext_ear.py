from email.mime import audio
import pyttsx3
import speech_recognition as sr


def main():
    # Initialize the recognizer
    r = sr.Recognizer()
    # loop infitely for user to speak
    while(1):
        # Exception handling to handle exceptions at the runtime
        try:
            # use the microphone as source for
            with sr.Microphone() as source:

                # wait for a second to let the recognizer
                # adjust the energy threshold based on
                # the surrounding noise level
                r.adjust_for_ambient_noise(source, duration=0.2)

                # listens for the user's input
                audio = r.listen(source)

                # Using google to recognize audio
                mytext = r.recognize_google(audio)
                mytext = mytext.lower()

                print('you said: '+mytext)
                # this file is not returing the mytext
                # return('you said: '+mytext)
                return mytext

        except sr.RequestError as e:
            return("Could not request results; {0}".format(e))
        except sr.UnknownValueError:
            return("unknown error occured")


if __name__ == "__main__":
    main()
