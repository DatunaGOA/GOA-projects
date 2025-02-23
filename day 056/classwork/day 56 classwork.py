def points(games):
    total = 0
    for i in games :
        if i[0] > i[2]:
            total += 3
        elif i[2] == i[0]:
            total += 1
        else: 
            total += 0
            
    return total
        

        #classwork 2
def reverse_words(text):

    words = text.split(' ')

    reversed_words = [word[::-1] for word in words]

    reversed_string = ' '.join(reversed_words)
    return reversed_string


          #classwork 3
def remove_url_anchor(url):

    base_url = url.split('#', 1)[0]
    return base_url


#classwork 4

def find_uniq(arr):
    counts = {}
    for num in arr:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1
    
    for num, count in counts.items():
        if count == 1:
            return num

