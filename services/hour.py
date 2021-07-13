from util import read_file

class HourService():
  def __init__(self, hour_file: str):
    self._hour_file = hour_file

  def get(self, id: str):
    file_data = read_file(self._hour_file)
    return file_data.get(id)
