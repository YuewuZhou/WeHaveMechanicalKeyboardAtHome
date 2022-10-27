from fileinput import filename
from random import randint
from pynput.keyboard import Key, Listener
# import required module


from playsound import playsound

import pyglet

pyglet.resource.path = [
    'C:\\Users\\ZackZhou\\local\\loud_keyboard\\keyboard_sounds\\']
pyglet.resource.reindex()


def play_random_sound():
    filename = str(randint(2, 9)) + '.mp3'
    pyglet.resource.media(filename, streaming=False).play()


def play_specific_sound(filename):
    pyglet.resource.media(filename, streaming=False).play()


# keyboard_sounds\3.mp3
# C:\Users\ZackZhou\local\loud_keyboard\keyboard_sounds\1.mp3
# for playing note.mp3 file
# playsound('/path/note.mp3')
# print('playing sound using  playsound')


def on_press(key):
    print('{0} pressed'.format(
        key))
    play = True
    play2 = False
    play3 = False
    if key == Key.ctrl_l:
        print("don't play sounds for keys that need to be held")
        play = False
    if key == Key.shift_l:
        print("don't play sounds for keys that need to be held")
        play = False
    if key == Key.ctrl_r:
        print("don't play sounds for keys that need to be held")
        play = False
    if key == Key.shift_r:
        print("don't play sounds for keys that need to be held")
        play = False
    if key == Key.space:
        play = False
        play2 = True
    if key == Key.enter:
        play = False
        play2 = True
    if key == Key.backspace:
        play = False
        play3 = True
    if play:
        play_random_sound()
    if play2:
        play_specific_sound("1.mp3")
    if play3:
        play_specific_sound("10.mp3")


def on_release(key):
    print('{0} release'.format(
        key))
    if key == Key.end:
        # Stop listener
        return False


# Collect events until released
with Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()

if __name__ == "__main__":
    pyglet.app.run()
