from util import read_file

class MinuteService():
  def __init__(self, minute_file: str):
    self._minute_file = minute_file

  def get(self, id: str):
    file_data = read_file(self._minute_file)
    return file_data.get(id)
