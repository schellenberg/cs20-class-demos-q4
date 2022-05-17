import easygui_qt as easy

where_to_eat = ["Popeyes", "Earls", "La Bamba", "Sebastians"]
place = easy.get_choice("Where do you want to eat?", "Eating", where_to_eat)

message = "Nice. I'd like to go to " + place + " too!"
easy.show_message(message)