import yaml
from collections import OrderedDict

my_dictionary = OrderedDict([{"Name": "Nathaniel", "Age": 27}, {"Name": "Seanybob", "Age": 15}])
print(my_dictionary)

file_dump = open("test.yaml", "w")
file_dump.write(yaml.dump(my_dictionary, default_flow_style = False))
file_dump.close()