import wikipedia

try:
    user_type = input("page title or search phrase")
    while user_type !="":
        print(wikipedia.search(user_type))
        print(wikipedia.summary(user_type))
        massage_get = wikipedia.page(user_type)
        print(massage_get)
        user_type = input("page title or search phrase")
    else:
        print("")
except wikipedia.exceptions.DisambiguationError as error_massage:
    print(error_massage.options)