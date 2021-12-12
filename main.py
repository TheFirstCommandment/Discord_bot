from operator import itemgetter

import json
import random


people = '''
{
    "characters": [
        {
            "name": "Battler",
            "quote": "You need three types"
        },
        {
            "name": "Beatrice",
            "quote": "you will die, battler"
        }
    ]
}
'''

data = json.loads(people)



def get_quote():
    data_in = data['characters']
    for quote in data_in:
        if data_in['name'] == 'Battler':
            quote_1 = quote['quote'][1]
            print(quote_1)

n = get_quote()
