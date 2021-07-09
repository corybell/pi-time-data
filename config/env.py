from os import getenv

class EnvConfig():
  def __init__(self):
    self._api_host = getenv('API_HOST')
    self._api_port = getenv('API_PORT')

  @property
  def api_host(self):
    return self._api_host

  @property
  def api_port(self):
    return self._api_port
