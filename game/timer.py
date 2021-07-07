



class Timer:

    def __init__(self):
        self._ticks = 0

    def tick(self):
        self._ticks += 1

    def get_time(self):
        return self._ticks / 60