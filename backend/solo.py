"""
Solo Class
    * INHERIT FROM ~selection~ *

    constructor:
    - # of people = 1
    - call selection super()
"""

from selection import Selection

class Solo(Selection):
    def __init__(self):
        super().__init__(1)