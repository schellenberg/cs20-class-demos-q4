import easygui_qt as easy

name = easy.get_string("What's your name?")

if name == None:
    print("Hey! Tell me who you are!")
else:
    print(f"Good to see you, {name}")