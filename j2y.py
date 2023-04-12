import json
import yaml

json_path1 = "/Users/robert/Desktop/DataProjects/PyJsonYaml/donuts.json"
json_path2 = "/Users/robert/Desktop/DataProjects/PyJsonYaml/emojis.json"

def yaml_converter(filepath):
    with open(filepath) as file:
        with open ("output.yaml", 'w') as new_file:
            json_data = json.loads(file.read())
            converted_json = json.dumps(json_data)

            yaml_data = yaml.safe_load(converted_json)
            convert_yaml = yaml.dump(yaml_data)

            new_file.write((convert_yaml))


yaml_converter(json_path1)
# yaml_converter(json_path2)

