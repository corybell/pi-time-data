from util import write_file
from sys import argv

def build_relay(r: int):
  if r == 0:
    return {
      'id': '1',
      'name': 'Primary Lights',
      'timer': {
        'hr': '*',
        'min': 'toggleOne'
      }
    }

  return {
    'id': str(r + 1),
    'name': '',
    'timer': None
  }

def get_input():
  if (len(argv) != 2):
    print('Usage: ./scripts/seed.sh <NUM_RELAYS>')
    return 0
  return int(argv[1])
  
num_relays = get_input()

relay_data = []
for r in range(0, num_relays):
  relay_data.append(build_relay(r))

if len(relay_data):
  write_file('data/relay.json', relay_data)
