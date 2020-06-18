"""
from asciimatics.effects import Cycle, Stars
from asciimatics.renderers import FigletText
from asciimatics.scene import Scene
from asciimatics.screen import Screen


def demo(screen):
    effects = {
        Cycle(
            screen,
            FigletText("Happy", font='big'),
            int(screen.height / 2 - 8)),
        Cycle(
            screen,
            FigletText("Father's    Day!", font='big'),
            int(screen.height / 2 + 3)),
        Stars(screen, 200)
    }
    screen.play([Scene(effects, 500)])


Screen.wrapper(demo)
"""
#Father's Day Card has multiple errors.

import speech_recognition as sr

r = sr.Recognizer()
with sr.Microphone() as source:
    print("Speak Now: ")
    audio = r.listen(source)
print(r.recognize_google(audio))

