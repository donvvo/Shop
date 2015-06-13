import facebook

token = 'CAALeU6fTEH0BAIkZAGuhGLJpb6vfFWcScasank4cQbDFxqHZBK3ND8ZCRiAW7vFvSPPMnyMj1ZANc4RZAPqQZAzK3bZBUWYE5o3ueZAWAVGAk4XY1T4vjFX2ZCrZBeCteF7fLkLLZCNJRRADeQi501SW8EioaAA3CIkZApoowxle45GtaUfXQmAHwjf4Oy8t2SZATLATZAHiLiExXdwJ9NluUOBIkv4Q35uGBeGZBgZD'

graph = facebook.GraphAPI(token)
profile = graph.get_object("me")
friends = graph.get_connections("me", "friends")

id_list = [friend['id'] for friend in friends['data']]

print id_list

for friend in friends['data']:
    print friend
