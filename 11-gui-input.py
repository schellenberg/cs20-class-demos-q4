import easygui_qt as easy

first_name = easy.get_string("What's your first name?")
last_name = easy.get_string("What's your last name?")
age = easy.get_integer("How old are you?")

greeting = "Hello there, " + first_name + " " + last_name + "!"
easy.show_message(greeting)