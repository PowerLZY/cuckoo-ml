# Copyright (C) 2010-2015 Cuckoo Foundation.
# This file is part of Cuckoo Sandbox - http://www.cuckoosandbox.org
# This signature was contributed by RedSocks - http://redsocks.nl
# See the file 'docs/LICENSE' for copying permission.

from lib.cuckoo.common.abstracts import Signature

class DarkddosMutexes(Signature):
    name = "ddos_darkddos_mutexes"
    description = "Creates known Dark-DDoS Bot files, registry keys and/or mutexes"
    severity = 3
    categories = ["ddos"]
    families = ["darkddos"]
    authors = ["RedSocks"]
    minimum = "2.0"

    mutexes_re = [
        "DARKDDOSER",
        u"\xc3\x81G\xc3\x9bP\xc3\xb2y\xc3\xbdF\xc3\x80N\xc3\x96S",
    ]

    def on_complete(self):
        for indicator in self.mutexes_re:
            if self.check_mutex(pattern=indicator, regex=True):
                return True
