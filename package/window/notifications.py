from TikTokLive import TikTokLiveClient
from TikTokLive.types.events import CommentEvent, ConnectEvent, FollowEvent, DisconnectEvent
import asyncio
from config import *

# Instantiate the client with the user's username
config: Config = Config()
client: TikTokLiveClient = TikTokLiveClient(unique_id=config.username)
followers: int = config.starting_amount
retries: int = 0

# Define how you want to handle specific events via decorator
@client.on("connect")
async def on_connect(_: ConnectEvent):
    print("Connected to Room ID:", client.room_id)

# Notice no decorator?
async def on_comment( event: CommentEvent):
    print(f"{event.user.nickname} -> {event.comment}")

#handles when client is diconnected. Simple exponential backoff
async def on_disconnect(event: DisconnectEvent):
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

#add listener for the follow event
def run():
    client.add_listener("follow", on_follow)
    client.run()