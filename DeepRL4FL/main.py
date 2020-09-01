from __future__ import absolute_import

import os
import sys
import time
os.environ["CUDA_VISIBLE_DEVICES"]="1"
path = os.getcwd()
path = path + "/Fault_localization/"
sys.path.append(path)
import run


start = time.clock()
run.whole_process()
time_length = time.clock() - start
print("Cost " + str(time_length) + " s to finish the model")
