#!/bin/sh
wget https://raw.githubusercontent.com/fergusch/weemote/master/weemote/weemote.py -O $HOME/.weechat/python/autoload/weemote.py
mkdir $HOME/.weechat/python/weemote
wget https://raw.githubusercontent.com/fergusch/weemote/master/weemote/emotes.cfg -O $HOME/.weechat/python/weemote/emotes.cfg
