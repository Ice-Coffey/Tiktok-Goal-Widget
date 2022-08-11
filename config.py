from argparse import Action

#configurables - NOTE: EDIT LINES 19 to 30 to configure it for your stream

#username: the @username you want to track
#starting_amount: you can start at 0 for a new stream, or input any other starting value for where you want your bar to start
#goal_amount: number of events you want to achieve this stream. ie, 1000 new followers by the end of stream
#background_color: the color of the window. Set to black for tiktok color scheme and easy chroma key removal
#bar_color: the color of the goal bar. Set to tiktok red for tiktok color scheme
#goal_text_color: the color of the text underneath and above the bar. Set to turqoise for tiktok color scheme
#font: font of text
#update_interval: integer in seconds for how often the bar should update
#event_tracked: requires values of either "on_follow", "on_like", "on_share", "on_gift", "on_subscribe", or "on_diamonds" depending on what you're tracking
#goal_unit: what you're trying to get (likes, followers, etc), but can be set to something like "degenerates" to be funny
#goal_name: The name of what you want to achieve, ie. "Like Goal", "Follower Goal", "Degenerate Accumulations"
#action: what people did. "liked", "followed", etc. Only used in logs, not important for UI. Can ignore.

configuration = {
    "username": "@DummyUser",
    "starting_amount": 0,
    "goal_amount": 1000,
    "background_color": "#000000",
    "bar_color": "#EE1D52",
    "goal_text_color": "#69C9D0",
    "font": "Arial",
    "update_interval": 1,
    "event_tracked": "on_follow",
    "goal_unit": "Followers",
    "goal_name": "Follower Goal",
    "action": "Followed"
}


#DON'T MODIFY CODE BELOW THIS LINE UNLESS YOU KNOW WHAT YOU'RE DOING

class Config():
    def __init__(self):
        self.username = configuration["username"]
        self.starting_amount=configuration["starting_amount"]
        self.goal_amount= configuration["goal_amount"]
        self.goal_name=configuration["goal_name"]
        self.background_color=configuration["background_color"]
        self.bar_color=configuration["bar_color"]
        self.goal_text_color=configuration["goal_text_color"]
        self.goal_unit=configuration["goal_unit"]
        self.Font=configuration["font"]
        self.action = configuration["action"]
        self.update_interval = configuration["update_interval"]
        self.event_tracked = self.eventToAction(configuration["event_tracked"])
    
    def eventToAction(self, event):
        d = {
            "on_follow":('follow', 'getFollowers()'),
            "on_like":('like', 'getLikes()'),
            "on_share":('share', 'getShares()'),
            "on_gift":('gift', 'getGifts()'),
            "on_subscribe":('subscribe', 'getSubscribers()'),
            "on_diamonds":('gift', 'getDiamonds()')
        }
        if(event == "on_diamonds"):
             return ("on_gift", d[event][0], d[event][1])

        return (event, d[event][0], d[event][1])