import yaml
from jinja2 import Environment, FileSystemLoader, Template

ENV = Environment(loader=FileSystemLoader('../templates/aws/'))

with open('config.yaml') as file:
    print(file.read())

with open("config.yaml") as config:
    config = yaml.safe_load(config)

type(config)

print("Content:")
print(config)

template = ENV.get_template("config.j2")
print("Rendered:")
print(template.render(config=config))
