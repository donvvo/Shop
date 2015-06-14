from amazonproduct import API
import sys

# Initialize API
api = API(locale='us')

api.associate_tag = 'shopbudd0b'
api.access_key = 'AKIAJHBGXANWUK4TKCSA'
api.secret_key = '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'

# Search amazon for item
items = api.item_search('Blended', Keywords="apple", ResponseGroup='ItemAttributes')

itemID = []
price = []
cnt = 0

for book in items:
    valid = True

    try: 
        title = book.ItemAttributes.Title

        #title = title.encode('utf-8').strip()
        print title

        #print book.ItemAttributes.LargeImage.URL
        itemID.append(book.ASIN)
    except AttributeError:
        valid = False
        print "issue"
    except UnicodeEncodeError:
        title = str(book.ItemAttributes.Title)
        title = title.decode()
        print title.encode('utf-8').strip()
        valid = False

    if (valid):
        cnt = cnt + 1

    if (cnt == 10):
        break;

# Grab item price and listing ID
ID = str(itemID[0])
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

