import sys
import os
from ex12 import mytimer


def end_timer(txt= "End time"):
    """
        ```
    """
    global start_time
    if start_time is None:
        raise SystemError("end_timer() called with a strt_timer()")
    end_time = os.times()[:2]
    print("{0:<12}:{1:03.3f} sedonds".format(txt, end_time - start_time))

    start_time = None
    return


try:
    mytimer.end_timer()
except SystemError as err:
    print("end_timer error: ", err, file= sys.stderr)