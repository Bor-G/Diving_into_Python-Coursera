# -*- coding: cp1251 -*-
# Создание процесса на Python

import time
import os
import multiprocessing as osw

pid = osw.set_start_method('spawn')
if pid == 0:
    # дочерний процесс
    while True:
        print("child:", os.getpid())
        time.sleep(5)
else:
    # родительский процесс
    print("parent:", os.getpid())
#    os.wait()
