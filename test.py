import yaml

my_dictionary = [{"Name": "Nathaniel", "Age": 27}, {"Name": "Seanybob", "Age": 15}]

file_dump = open("test.yaml", "w")
file_dump.write(yaml.dump(my_dictionary, default_flow_style = False))
file_dump.close()