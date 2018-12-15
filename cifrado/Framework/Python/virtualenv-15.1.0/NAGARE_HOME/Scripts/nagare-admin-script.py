#!c:\users\charl\desktop\fpy\virtualenv-15.1.0\nagare_home\scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'nagare==0.5.1','console_scripts','nagare-admin'
__requires__ = 'nagare==0.5.1'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('nagare==0.5.1', 'console_scripts', 'nagare-admin')()
    )
