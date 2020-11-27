import os
import sys
from git import Repo
repo = Repo.clone_from('https://github.com/raghug-source/sampleapp.git',branch='new-branch')
# command = "zowe zos-jobs submit data-set 'RGOPALK.JCL.CNTL(HELLO)' --view-all-spool-content"
# #command = "zowe --version"
# os.system(command)
