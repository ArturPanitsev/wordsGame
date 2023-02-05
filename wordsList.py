import requests

r = requests.get('https://raw.githubusercontent.com/Harrix/Russian-Nouns/main/dist/russian_nouns.txt');

WORDS = r.text.split('\n')