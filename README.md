# :Tiktok-Goal-Widget

[![Latest Version on Packagist][ico-version]][link-packagist]
[![Software License][ico-license]](LICENSE.md)
[![Build Status][ico-travis]][link-travis]
[![Coverage Status][ico-scrutinizer]][link-scrutinizer]
[![Quality Score][ico-code-quality]][link-code-quality]
[![Total Downloads][ico-downloads]][link-downloads]

This is a widget for followers and Sub goals for Tiktok on OBS. Currently in active development. Please report any issues you find with the software.


## Install
NOTE: ONLY FUNCTIONS WHEN LIVE. GO LIVE AND THEN START THIS APPLICATION.
1. Download a code editor like [VSCode](https://code.visualstudio.com/Download)
2. Install [python](https://www.python.org/downloads/) onto your machine
3. Clone this repository or download and extract [this ZIP file](https://github.com/Ice-Coffey/Tiktok-Goal-Widget/archive/refs/heads/main.zip)
4. Open a console/terminal in the root directory of the project. There should be a terminal tab in vs code if you can't find it.
5. Enter `pip install -r requirements.txt` to install all dependencies. If that doesn't work, you may need to install pip. [Follow these steps](https://www.geeksforgeeks.org/download-and-install-pip-latest-version/#windows).
6. Enter `python main.py` to start the application

## FOR DEVELOPERS
NOTE: ONLY FUNCTIONS WHEN LIVE. SO YOU MIGHT HAVE TO CONFIGURE THIS USING SOMEONE ELSE'S USERNAME FIRST.
1. Config.py has all of the configurables. This includes username, text, etc. If the API portion of the code is non functioning, it is most likely because the user selected in the config file is not online. Please change it to a user currently online, and it should work.
2. package/app.py contains the gui. It is able to be updated through updateUI(num), incrementing the number of followers by num amount.
3. package/window/notifications.py contains the api. This takes in live information froma single user's Live and tells you how many followers have followed that stream, as well as who followed individually. Also handles disconnects, etc.

## Usage

1. Change what you need in the Config.py file
2. run this line in a terminal in the directory of the file.
``` python
python main.py
```
3. Select Window Source on OBS
4. Chroma Key out the black and crop out the top of the window
5. Add it to your stream!


![Screenshot (190)](https://user-images.githubusercontent.com/38543752/184234605-9d1f7fa1-1587-49a9-b099-a03166eba961.png)

## Important Config Usage
In Config.py you will find this
```configuration = {
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
    "action": "Followed",
    "show_last": True,
    "intervals_last": 3,
    "sound_on": True,
    "sound_path": "test.mp3"
}
```
1. Username will be your username WITH an @ at the beginning
2. Colors are all in Hex code and start with #
3. Starting amount must be lower than goal amount and both must be integers
4. event_tracked must be one of these values: "on_follow", "on_like", "on_share", "on_gift", "on_subscribe", or "on_diamonds".
      "on_follow" - tracks # of new followers
      "on_like" - tracks # of likes
      "on_share" - tracks when a unique person shares
      "on_gift" - tracks # of gifts
      "on_subscribe" - tracks when a new person subs
      "on_diamonds" -  tracks value of gifts in diamonds
5. show_last is if you show a user after doing the event of your choosing. it will show their profile picture and username.
6. intervals_last is how long the pfp and user is shown after liking, following, etc. If update_interval is 1, and interval_last is 3, then it will be shown for 1*3 = 3 seconds. show_last must be true
7. sound_on is whether a sound plays when someone likes, follows, etc. show_last must be true
8. sound_path is the file name of the sound that plays when someone likes, follows, etc. sound_on must be true
## Change log

Please see [CHANGELOG](CHANGELOG.md) for more information on what has changed recently.

## Contributing

Please see [CONTRIBUTING](CONTRIBUTING.md) and [CODE_OF_CONDUCT](CODE_OF_CONDUCT.md) for details.

## Security

If you discover any security related issues, please use the issue tracker.

## Credits

- [IceCoffey][link-author]
- [All Contributors][link-contributors]

## License

Please see [License File](LICENSE.md) for more information.

[ico-version]: https://img.shields.io/packagist/v/:vendor/:package_name.svg?style=flat-square
[ico-license]: https://img.shields.io/badge/license-MIT-brightgreen.svg?style=flat-square
[ico-travis]: https://img.shields.io/travis/:vendor/:package_name/master.svg?style=flat-square
[ico-scrutinizer]: https://img.shields.io/scrutinizer/coverage/g/:vendor/:package_name.svg?style=flat-square
[ico-code-quality]: https://img.shields.io/scrutinizer/g/:vendor/:package_name.svg?style=flat-square
[ico-downloads]: https://img.shields.io/packagist/dt/:vendor/:package_name.svg?style=flat-square

[link-packagist]: https://packagist.org/packages/:vendor/:package_name
[link-travis]: https://travis-ci.org/:vendor/:package_name
[link-scrutinizer]: https://scrutinizer-ci.com/g/:vendor/:package_name/code-structure
[link-code-quality]: https://scrutinizer-ci.com/g/:vendor/:package_name
[link-downloads]: https://packagist.org/packages/:vendor/:package_name
[link-author]: https://github.com/Ice-Coffey
[link-contributors]: ../../contributors
