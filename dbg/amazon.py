from amazonproduct import API

api = API(locale='us')

items = api.item_search('Books', Publisher="O'Reilly")

for book in items:
    print '%s: "%s"' %(book.ItemAttributes.Author,
                       book.ItemAttributes.Title)


