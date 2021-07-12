from util import read_file

class TimerService():
  def __init__(self, option_file: str):
    self._option_file = option_file

  def all(self):
    return read_file(self._option_file)
