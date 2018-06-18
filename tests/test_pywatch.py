import os
import queue
import time

from .utils import DummyLogger


def test_dummy_log():
    _queue = queue.Queue()
    dummy_log = DummyLogger(_queue)
    dummy_log.log_lines(10)

    time.sleep(3)

    assert os.path.exists(dummy_log.tmp_file.name), "File does not exist"
    assert os.path.getsize(dummy_log.tmp_file.name) > 0, "File is empty"

    _queue.empty()
    _queue.put("quit")
