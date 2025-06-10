# String basic question :

def remove_str(str, i = 0) :
    if i == len(str) :
        return ""
    elif str[i] != 'a' :
        return remove_str(str, i + 1)
    else :
        