def make_snippit(string):

    #check ammount of words in string
    words_list = string.split()

    if len(words_list) < 6:
        delimiter = " "
        return delimiter.join(words_list)   

    elif len(words_list) > 5:
        five_words = words_list[0: 5]
        delimiter = " "
        return delimiter.join(five_words) + "..."
    else:
        return
