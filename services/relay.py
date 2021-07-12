from util import read_file, write_file, get_str

class RelayService():
  def __init__(self, relay_file: str):
    self._relay_file = relay_file

  def all(self):
    return read_file(self._relay_file)

  def get(self, id):
    return self._get(self.all(), id)

  def edit(self, id, payload):
    relays = self.all()
    relay = self._get(relays, id)
    if not relay:
      return False

    name = get_str(payload, 'name')
    relay['name'] = name

    timer = payload['timer']
    relay['timer'] = timer

    write_file(self._relay_file, relays)
    return True

  def _get(self, file_data: list, id):
    for d in file_data:
      if d["id"] == id: return d

    return None