from click import command
import gtts
from playsound import playsound

language = 'en'


def main():
    def command(speak):
        t1 = gtts.gTTS("thank you, i hope you get well soon")
        t1.save("mini.mp3")
        playsound("mini.mp3")

        command(speak)


if __name__ == "__main__":
    main()
