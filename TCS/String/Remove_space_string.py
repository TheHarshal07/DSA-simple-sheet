#Here we want to remve the space from the strig

def Remove_space(String):

    new_string = []
    for Str in String:
        if Str != ' ':
            new_string.append(Str)
    return ''.join(new_string)


string = "gee k for g eek s"
print(Remove_space(string))