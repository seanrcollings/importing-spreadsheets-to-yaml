import yaml
import pdb

input_file = open("armor_spreadsheets(DS2).csv", "r")
output_file = open("Armor(DS2).yaml", "w")

lines = input_file.readlines()
keys = lines[0].rstrip().split("|")
equipment = []


for line in lines[1:]:
	line = line.rstrip().split("|")
	line_dict = {}
	print(line)
	for index, val in enumerate(line):
		line_dict[keys[index]] = val
	equipment.append(line_dict)


output_file.write(yaml.dump(equipment, default_flow_style = False))

input_file.close()
output_file.close()