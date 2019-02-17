# weemote

Plugin for [WeeChat](https://weechat.org) that allows the user to define custom emote commands. Now you can flip tables in WeeChat with ease. (╯°□°）╯︵ ┻━┻

## Installation
```
wget https://raw.githubusercontent.com/fergusch/weemote/master/install.sh | sh
```
This script will automatically download and place the needed files where they need to go. Specifically, `weemote.py` will be downloaded to 
`~/.weechat/python/autoload/` and `emotes.cfg` will be downloaded to `~/.weechat/python/weemote/`.

## Defining emotes
The install script will download the config file from this repo, which includes a couple of example emotes. To define your own, edit the `emotes.cfg` 
file in your favorite editor: `~/.weechat/python/weemote/emotes.cfg`.

Place emotes in the config file under the `[EMOTES]` section in the format `<name> = <emote>`. Names must be alphanumeric characters only.

## Using emotes in WeeChat
In WeeChat, your emotes will be registered as commands based on the names you gave, for example, `/tableflip`, `/shrug`, etc. 

## License
This plugin is licensed under the GNU GPL v3 license. See the LICENSE file for more information.

## Note
This plugin is experimental. Use at your own risk.
