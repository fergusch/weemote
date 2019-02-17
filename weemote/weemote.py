import configparser
import os
import_ok = True
try:
	import weechat as w
except ImportError:
	print("This script is to be used in WeeChat only.")
	import_ok = False
import re

SCRIPT_NAME    = "weemote"
SCRIPT_AUTHOR  = "fergusch"
SCRIPT_VERSION = "0.1"
SCRIPT_LICENSE = "GPL3"
SCRIPT_DESC    = "Allows defining of custom emote commands"
HOME_DIR = os.environ['HOME']

# check if config file exists, create it if not
if not os.path.isfile(HOME_DIR + "/.weechat/python/weemote/emotes.cfg"):
	f = open(HOME_DIR + "/.weechat/python/weemote/emotes.cfg", "w+")
	f.write("[EMOTES]")
	f.close()

# load config file
config = configparser.ConfigParser()
config.read(HOME_DIR + "/.weechat/python/weemote/emotes.cfg", encoding="utf-8")
emotes = config['EMOTES']

# replace the given command name with the emote in input box
def put_emote(name, data, buffer, args):
	face = emotes[name].encode("utf-8")
	w.buffer_set(buffer, 'input', face)
	w.buffer_set(buffer, 'input_pos', '%d' % len(face))
	return w.WEECHAT_RC_OK

if __name__ == '__main__' and import_ok and w.register(SCRIPT_NAME, SCRIPT_AUTHOR, SCRIPT_VERSION, SCRIPT_LICENSE, SCRIPT_DESC, "", ""):
	for key in emotes.keys():
		# make sure command name is valid before hooking, otherwise raise ImportError
		if bool(re.match(r"^[a-zA-Z0-9]*$", key)):
			exec("""def """ + key + """(data, buffer, args):
					return put_emote(\"""" + key + """\", data, buffer, args)""")
			w.hook_command(key, "", "", "", "", key, "")
		else:
			raise ImportError('Invalid emote name given: must be alphanumeric')
