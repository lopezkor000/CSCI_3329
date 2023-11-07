"""
Couple Class
    * INHERIT FROM ~selection~ *
    
    constructor:
    - # of people = 2
    - call selection super()
"""

from selection import Selection

class Couple(Selection):
    def __init__(self):
        super().__init__(2)