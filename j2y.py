import json
import yaml

json_path1 = "/Users/robert/Desktop/DataProjects/PyJsonYaml/donuts.json"
json_path2 = "/Users/robert/Desktop/DataProjects/PyJsonYaml/emojis.json"

# def read_json(file_path):
#     with open(file_path) as file:
#         new_data = json.load(file)
#         return new_data

def yaml_converter(filepath):
    with open(filepath) as file:
        with open ("output.yaml", 'w') as new_file:
            json_data = json.loads(file.read())
            converted_jason = json.dumps(json_data)

            yaml_data = yaml.safe_load(converted_jason)
            convert_yaml = yaml.dump(yaml_data)

            new_file.write((convert_yaml))


yaml_converter(json_path1)
# yaml_converter(json_path2)

