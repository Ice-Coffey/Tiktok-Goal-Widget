from argparse import Action

#configurables
configuration = {
    "username": "@romileon_6",
    "starting_amount": 500,
    "goal_amount": 1000,
    "goal_name": "Follower Goal",
    "background_color": "#000000",
    "bar_color": "#EE1D52",
    "goal_text_color": "#69C9D0",
    "goal_unit": "Followers",
    "font": "Arial",
    "action": "followed"
}

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