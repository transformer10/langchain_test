import os
import util.config

print(dict(util.config.get_ini_config().items('mysql')).get('username'))
