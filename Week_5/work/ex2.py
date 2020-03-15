# -*- coding: cp1251 -*-
# �������� �������� �� Python

import time
import os
import multiprocessing as osw

pid = osw.set_start_method('spawn')
if pid == 0:
    # �������� �������
    while True:
        print("child:", os.getpid())
        time.sleep(5)
else:
    # ������������ �������
    print("parent:", os.getpid())
#    os.wait()
