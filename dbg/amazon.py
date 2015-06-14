from amazonproduct import API

# Initialize API
api = API(locale='us')

# Search amazon for item
items = api.item_search('Books', Keywords="O'Reilly", ResponseGroup='ItemAttributes')

itemID = 0
cnt = 0

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

    if (cnt == 0):
        try:
            print book.ASIN
            itemID = book.ASIN
        except AttributeError:
            print "No ASIN"

        cnt=1
    else:
        itemID2 = book.ASIN
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
cartItem[itemID] = 1

print cartItem

cartResponse = api.cart_create(cartItem) #, OfferListingId=listID, Quantity='1')

cartID = cartResponse.Cart.CartId
hmac = cartResponse.Cart.HMAC

cItem = cartResponse.Cart.CartItems.CartItem
pUrl = cartResponse.Cart.PurchaseURL


print cartID
print hmac
print pUrl
print cItem.Title

# Add item to cart
cartItem2 = {}
cartItem2[itemID2] = 1

cartResponse = api.cart_add(cartID, hmac, cartItem2)

cItem2 = cartResponse.Cart.CartItems.CartItem
pUrl2  = cartResponse.Cart.PurchaseURL

print cItem2.Title
print pUrl2

#print '--------------------------------------------------'
#
#result = api.item_lookup(ID, ResponseGroup='Images')
#for item in result.Items.Item:
#    print item.SmallImage.URL
#    print item.LargeImage.URL

