import random
import tempfile
import time

from loremipsum import generate_sentence
from threading import Thread


class DummyLogger(Thread):

    def __init__(self, _queue):
        Thread.__init__(self)

        self._queue = _queue
        self.tmp_file = tempfile.NamedTemporaryFile(delete=False)
        self.suffix = "EOF"
        self.daemon = True
        self.start()

    def run(self):
        while True:
            msg = self._queue.get()

            if isinstance(msg, str) and msg == "quit":
                with open(self.tmp_file.name, "a") as fd:
                    fd.write("\n{}".format(self.suffix))
                break
            else:
                with open(self.tmp_file.name, "a") as fd:
                    _, _, sentence = generate_sentence()
                    fd.write("\n{}".format(sentence.encode("ascii")))
                pause = random.randint(1, 3)
                time.sleep(pause)

    def log_lines(self, lines):
        for i in range(lines):
            self._queue.put("")
