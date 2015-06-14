import facebook

from allauth.socialaccount.models import SocialAccount, SocialToken

from wishlist.models import WishList


def get_facebook_friends(request):
    social_account = SocialAccount.objects.get(user=request.user)
    social_token = SocialToken.objects.get(account=social_account)

    token = social_token
    graph = facebook.GraphAPI(token)
    friends = graph.get_connections("me", "friends")

    id_list = [friend['id'] for friend in friends['data']]

    return id_list


def facebook_id_to_users(id_list):
    social_accounts = SocialAccount.objects.filter(uid__in=id_list)
    print social_accounts
    return [social_account.user for social_account in social_accounts]


def update_user_friends_list(request):
    id_list = get_facebook_friends(request)
    user_friends = facebook_id_to_users(id_list)
    for friend in user_friends:
        if friend not in request.user.friends.all():
            request.user.friends.add(friend)
    return request.user.friends


def get_friends_wishlist(self):
    wishlists = WishList.objects.filter(user__in=self.friends)
    wishlist_combined = ""
    for wishlist in wishlists:
        wishlist_combined += wishlist.items
    return wishlist_combined