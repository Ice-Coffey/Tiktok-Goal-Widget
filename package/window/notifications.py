from TikTokLive import TikTokLiveClient
from TikTokLive.types.events import CommentEvent, ConnectEvent, FollowEvent, DisconnectEvent, LikeEvent, ShareEvent, GiftEvent, SubscribeEvent
import asyncio
from config import *
from package.util import giftsToMoney

# Instantiate the client with the user's username
config: Config = Config()
client: TikTokLiveClient = TikTokLiveClient(unique_id=config.username)
followers: int = config.starting_amount
retries: int = 0
likes: int = 0
shares: int = 0
gifts: int = 0
diamonds: int = 0
subscribers: int = 0
event_tracked: tuple = config.event_tracked

# Define how you want to handle specific events via decorator
@client.on("connect")
async def on_connect(_: ConnectEvent):
    print("Connected to Room ID:", client.room_id)

# Notice no decorator?
async def on_comment( event: CommentEvent):
    print(f"{event.user.nickname} -> {event.comment}")

#handles when client is diconnected. Simple exponential backoff
async def on_disconnect(event: DisconnectEvent):
    global retries
    print('Sleeping')
    secs = 5+2**retries
    await asyncio.sleep(secs)
    print('Slept '+ secs +' seconds')
    retries +=1
    client.start()

#When someone follows, prints name and how many followers have followed this stream
async def on_follow(event: FollowEvent):
    global followers
    followers +=1
    print(f"{event.user.nickname} has " + config.action)
    print(str(followers) + " have "+ config.action +" this stream")

async def on_like(event: LikeEvent):
    global likes
    likes += event.likeCount
    print(f"{event.user.nickname} has liked {event.likeCount} times")
    print("You have gotten " + str(likes) + " this stream")

async def on_share(event: ShareEvent):
    global shares
    shares +=1
    print(f"{event.user.nickname} has shared")
    print(str(shares) + " people have shared this stream")

async def on_gift(event: GiftEvent):
    global gifts
    global diamonds
    gifts +=1
    diamonds += event.gift.giftDetails.diamondCount
    money = giftsToMoney(diamonds)
    print(f"{event.user.nickname} has gifted you a {event.gift.giftDetails.giftName} worth {event.gift.giftDetails.diamondCount} diamonds!")
    print(f"You have gotten {gifts} gifts this stream worth {diamonds} diamonds or {money}")

async def on_subscribe(event: SubscribeEvent):
    global subscribers
    subscribers +=1
    print(f"{event.user.nickname} has subscribed")
    print("You have gotten " + str(subscribers) + " this stream")


#add listener for the follow event
def runAPI():
    fun = eval(event_tracked[0])
    client.add_listener(event_tracked[1], fun)
    client.run()

def getFollowers():
    return followers

def getLikes():
    return likes

def getShares():
    return shares

def getGifts():
    return gifts

def getDiamonds():
    return diamonds

def getSubscribers():
    return subscribers