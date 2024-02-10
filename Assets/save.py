import os
import json

save_model = {
    'player': {
        'name':None,
        'inventory':None,
        'money':None,
        'computer':None
    }
}

def load():
    if os.path.exists('save.json'):
        with open('save.json', 'r') as file:
            save = json.load(file)
    else:
        save = save_model
        with open('save.json', 'w') as file:
            json.dump(save, file, indent=4)
    return save

def save(save):
    with open('save.json', 'w') as file:
        json.dump(save, file, indent=4)