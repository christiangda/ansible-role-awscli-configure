import yaml
from jinja2 import Environment, FileSystemLoader, Template

ENV = Environment(loader=FileSystemLoader('../templates/aws/'))

with open('credentials.yaml') as file:
    print(file.read())

with open("credentials.yaml") as credentials:
    credentials = yaml.safe_load(credentials)

type(credentials)

print("Content:")
print(credentials)


template = ENV.get_template("credentials.j2")
print("Rendered:")
print(template.render(credentials=credentials))
