# from os import getenv
from injector import Module, singleton
from config import EnvConfig

class AppContainer(Module):
  def __init__(self, app):
    self.app = app

  def configure(self, binder):
    env_config = EnvConfig()
    binder.bind(EnvConfig, to=env_config, scope=singleton)
