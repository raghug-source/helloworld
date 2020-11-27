import os
import sys
from git import Repo
repo = Repo.clone_from('https://github.com/raghug-source/sampleapp.git','/home/circleci/project/raghu/',branch='new-branch')
#command = "zowe zos-files upload file-to-data-set '/home/circleci/project/raghu/sampleapp/cobol/SAM1.cbl' 'RGOPALK.RAG.COBOL(SAM5)'"
# command = "zowe zos-jobs submit data-set 'RGOPALK.JCL.CNTL(HELLO)' --view-all-spool-content"
# #command = "zowe --version"
#os.system(command)
