from util import read_file, write_file, get_str

class RelayService():
  def __init__(self, relay_file: str):
    self._relay_file = relay_file

  def all(self):
    return read_file(self._relay_file)

  def all_active(self):
    relays = self.all()
    filtered = []
    for relay in relays:
      if relay['active']:
        filtered.append(relay)

    return filtered

  def get(self, id: str):
    return self._get(self.all(), id)

  def edit(self, id: str, payload: dict):
    relays = self.all()
    relay = self._get(relays, id)
    if not relay:
      return None

    name = get_str(payload, 'name')
    relay['name'] = name

    timer = payload['timer']
    relay['timer'] = timer

    active_value = payload.get('active')
    if active_value is not None:
      relay['active'] = active_value

    write_file(self._relay_file, relays)
    return relay

  def _get(self, file_data: list, id: str):
    for d in file_data:
      if d['id'] == id: return d
    return None