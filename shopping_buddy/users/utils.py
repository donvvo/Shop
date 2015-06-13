import facebook
from wishlist.models import WishList


def get_facebook_friends(self):
    token = 'CAALeU6fTEH0BAIkZAGuhGLJpb6vfFWcScasank4cQbDFxqHZBK3ND8ZCRiAW7vFvSPPMnyMj1ZANc4RZAPqQZAzK3bZBUWYE5o3ueZAWAVGAk4XY1T4vjFX2ZCrZBeCteF7fLkLLZCNJRRADeQi501SW8EioaAA3CIkZApoowxle45GtaUfXQmAHwjf4Oy8t2SZATLATZAHiLiExXdwJ9NluUOBIkv4Q35uGBeGZBgZD'

    graph = facebook.GraphAPI(token)
    friends = graph.get_connections("me", "friends")

    id_list = [friend['id'] for friend in friends['data']]

    print id_list

    for friend in friends['data']:
        print friend


def get_friends_wishlist(self):
    wishlists = WishList.objects.filter(user__in=self.friends)
    wishlist_combined = ""
    for wishlist in wishlists:
        wishlist_combined += wishlist.items
    return wishlist_combined