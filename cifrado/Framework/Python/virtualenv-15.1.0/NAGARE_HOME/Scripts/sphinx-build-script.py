#!c:\users\charl\desktop\fpy\virtualenv-15.1.0\nagare_home\scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'Sphinx==1.8.2','console_scripts','sphinx-build'
__requires__ = 'Sphinx==1.8.2'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('Sphinx==1.8.2', 'console_scripts', 'sphinx-build')()
    )
