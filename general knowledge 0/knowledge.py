def double_char(s):
    return ''.join(char *  2 for char in s)


def update_light(current):
    if current == "green":
        return "yellow"
    elif current == "yellow":
        return "red"
    elif current == "red":
        return "green"
    else:
        return "invalid input"
    


#    from datetime import datetime

#def is_today(date : datetime) -> bool:
#   today = date.today()
#   return date.year == today.year and date.month == today.month and date.day == today.day


def sort_gift_code(code):
    return ''.join(sorted(code))

def reverse_letter(st):
    return ''.join(char for char in st if char.isalpha())[::-1]

