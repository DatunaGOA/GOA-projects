import re

def increment_string(string):

    match = re.search(r'(\d+)$', string)
    
    if match:

        number_str = match.group(1)
        text_part = string[:match.start()]
        
        new_number = str(int(number_str) + 1)
        

        new_number = new_number.zfill(len(number_str))
        
        return text_part + new_number
    else:

        return string + '1'