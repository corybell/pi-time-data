from util import write_file
from sys import argv

def get_input():
  if (len(argv) != 2):
    print('Usage: ./scripts/seed.sh <NUM_RELAYS>')
    return 0
  return int(argv[1])
  
num_relays = get_input()

relay_data = []
for r in range(0, num_relays):
  relay_data.append({
  'id': str(r + 1),
  'name': '',
  'timer': None
})

if len(relay_data):
  write_file('data/relay.json', relay_data)
