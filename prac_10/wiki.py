"""CP1404 Practical 10 - Wikipedia API & Python Library"""

import wikipedia

search_for = input("Enter search phrase or title page: ")
while search_for != "":
    try:
        page = wikipedia.page(search_for)
        print(page.title)
        print(page.summary)
        print(page.url)
    except wikipedia.exceptions.DisambiguationError as error:
    # print(error.options)
    except wikipedia.exceptions.PageError:
        print("Page does not exist")
    search_for = input("Enter search phrase or title page: ")
print("Finished")
