from datetime import datetime




def greet():
    current_hour = int(datetime.now().strftime("%H"))
    if current_hour <= 6 and current_hour >=0:
        return "Гарної ночі"
    elif current_hour <= 9 and current_hour >=7:
        return "Гарного ранку"
    elif current_hour <= 17 and current_hour >=10:
        return "Гарного дня"
    elif current_hour <= 23 and current_hour >=18:
        return "Гарного вечора"
    


