import yaml
import pdb

ask_for_input = input("Input file: ")
ask_for_output = input("Output file: ")

input_file = open("input_files/" + ask_for_input, "r")
output_file = open("output_files/" + ask_for_output, "w")

lines = input_file.readlines()
keys = lines[0].rstrip().split("|")
order = keys
equipment = []


for line in lines[1:]:
	line = line.rstrip().split("|")
	line_dict = {}
	for index, val in enumerate(line):
		line_dict[keys[index]] = val
	equipment.append(line_dict)


output_file.write(yaml.dump(equipment, default_flow_style = False)) 	

input_file.close()
output_file.close()
