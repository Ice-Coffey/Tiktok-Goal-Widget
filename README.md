# :Tiktok-Goal-Widget

[![Latest Version on Packagist][ico-version]][link-packagist]
[![Software License][ico-license]](LICENSE.md)
[![Build Status][ico-travis]][link-travis]
[![Coverage Status][ico-scrutinizer]][link-scrutinizer]
[![Quality Score][ico-code-quality]][link-code-quality]
[![Total Downloads][ico-downloads]][link-downloads]

This is a widget for followers and Sub goals for Tiktok on OBS. Currently in production and may not function properly.


## Install
1. Download a code editor like [VSCode](https://code.visualstudio.com/Download)
2. Install [python](https://www.python.org/downloads/) onto your machine
3. Clone this repository or download and extract [this ZIP file](https://github.com/Ice-Coffey/Tiktok-Goal-Widget/archive/refs/heads/main.zip)
4. Open a console/terminal in the root directory of the project. There should be a terminal tab in vs code if you can't find it.
5. Enter `pip install requirements.txt -r` to install all dependencies
6. Enter `python main.py` to start the application

## FOR DEVELOPERS
1. main.py currently is commented out. The top comments control the main GUI. The bottom comments control the API.
2. Config.py has all of the configurables. This includes username, text, etc. If the API portion of the code is non functioning, it is most likely because the user selected in the config file is not online. Please change it to a user currently online, and it should work.
3. package/app.py contains the gui. It is able to be updated through updateUI(num), incrementing the number of followers by num amount.
4. package\window\notifications.py contains the api. This takes in live information froma single user's Live and tells you how many followers have followed that stream, as well as who followed individually. Also handles disconnects, etc.

## Usage

1. Change what you need in the Config.py file
2. run this line in a terminal in the directory of the file.
``` python
python main.py
```
3. Select Window Source on OBS
4. Chroma Key out the black and crop out the top of the window
5. Add it to your stream!

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
