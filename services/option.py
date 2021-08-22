from util import read_file, collection_to_dict

class OptionService():
  def __init__(self, option_file: str):
    self._option_file = option_file

  def all(self):
    all_options = read_file(self._option_file)

    hr_list = all_options['hour']
    min_list = all_options['minute']

    hr_dict = collection_to_dict(hr_list)
    min_dict = collection_to_dict(min_list)

    hours = { 'list': hr_list, 'dict': hr_dict }
    minutes = { 'list': min_list, 'dict': min_dict }

    return { 'hours': hours, 'minutes': minutes }
