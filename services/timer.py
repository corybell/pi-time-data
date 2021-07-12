from util import read_file
import logging

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)

OPTIONS_DATA_FILE = 'data/timer-options.json'

class TimerService():
  def __init__(self):
    pass

  def all(self):
    return read_file(OPTIONS_DATA_FILE)
  

