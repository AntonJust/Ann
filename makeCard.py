import pandas as pd
import jinja2
import math


data = pd.read_excel('data.xlsx')
print(data.number)


def make_file(pet, template):
    
    if type(pet['name']) != str:
        pet['name'] = "Клички нет"

    filename = f'{pet["name"]}_id_{pet["number"]}.html'
    content = template.render(name=pet['name'],
                                id=pet['number'],
                                cipFem = pet['cipFem'],
                                sign = pet['sign'],
                                character = pet['character']
                                 )

    with open('cards/' + filename, 'w', encoding='utf-8') as f:
        f.write(content)
        print(f'... wrote {filename}')







env = jinja2.Environment(loader=jinja2.FileSystemLoader("templates/"))

template = env.get_template('Templ.html')


for index, pet in data.iterrows():
    print(pet.number)
    petd = {}
    for key in data:

        petd[key] = pet[key]
    print(type(pet['name']) != str)
    print(pet['name'])
    make_file(petd, template)