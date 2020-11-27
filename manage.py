import os
import sys
from zowe.zos_console_for_zowe_sdk import Console
print('Hello World!')
host = sys.argv[1]
port = sys.argv[2]
user = sys.argv[3]
pwd = sys.argv[4]
command = "zowe --version"
os.system(command)
