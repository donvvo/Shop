from amazonproduct import API

# Initialize API
api = API(locale='us')

# Search amazon for item
items = api.item_search('Books', Keywords="O'Reilly", ResponseGroup='ItemAttributes')

itemID = 0

for book in items:

    try: 
        print book.ItemAttributes.Author
    except AttributeError:
        print "No Author"

    try: 
        print book.ItemAttributes.Title
    except AttributeError:
        print "No Title"

    try:
        print book.ItemAttributes.LargeImage.URL
    except AttributeError:
        print "No LargeImage.URL"

    try:
        print book.ASIN
        itemID = book.ASIN
    except AttributeError:
        print "No ASIN"

    break;

# Grab item price and listing ID
ID = str(itemID)
print ID

listID = ""

result = api.item_lookup(ID, ResponseGroup='Offers')
for item in result.Items.Item:
    print item.Offers.MoreOffersUrl
    print item.Offers.Offer.OfferListing.Price.FormattedPrice
    print item.Offers.Offer.OfferListing.OfferListingId

    listID = item.Offers.Offer.OfferListing.OfferListingId

# Create cart and add item to cart
cartItem = {}
cartItem["item_id"] = itemID
cartItem["quantity"] = '1'

cartItems = {}
cartItems['1'] = cartItem


print cartItem
print cartItems

result = {}
# TODO ListItemId
if type(cartItem) == dict:
    for no, (item_id, quantity) in enumerate(cartItem.items()):
        print item_id
        print quantity
        result['Item.%i.%s' % (no+1, 'ASIN')] = item_id
        result['Item.%i.Quantity' % (no+1)] = quantity

print result

exit()

cartResponse = api.cart_create(cartItem, OfferListingId=listID, Quantity='1')

#cartResposne = api.call(Operation='CartCreate', Item1=listID, Item1Quantity=1)

cartID = cartResponse.CartId
hmac = cartResponse.HMAC

print cartID
print hmac
print cartResponse.Amount


#print '--------------------------------------------------'
#
#result = api.item_lookup(ID, ResponseGroup='Images')
#for item in result.Items.Item:
#    print item.SmallImage.URL
#    print item.LargeImage.URL

