# -*- coding: utf-8 -*-
"""Main module."""
import subprocess
import select


class PyWatch(object):
    # TODO: asynch ssh
    def watch(self, filename):
        f = subprocess.Popen(
            ['tail', '-F', filename],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        p = select.poll()
        p.register(f.stdout)

        while True:
            if p.poll(1):
                yield f.stdout.readline()
