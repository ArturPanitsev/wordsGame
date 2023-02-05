import wordsList as wl
import random as rn

def game():
    try:
        WORD = wl.WORDS[rn.randrange(len(wl.WORDS))].lower();
    except:
        return print("Ошибка подгрузки данных. Возможно у вас проблемы с интернет соединением");
    secret = '_'*len(WORD);
    tries = int(len(WORD)*1.5);
    
    print( '\nВы начали новую игру в висилицу слово: ' + secret, '(состоит из букв русского языка)', f'\nУ вас {tries} попыток, чтобы отгадать слово (верная буква на отнимает попытку)\n');
    while tries > 0:
        
        answ = input('Введите букву или целое слово: ').lower();
        p = False;
        
        if(WORD.find(answ) != -1):
            
            if(len(answ) == 1):
                if(secret.find(answ) != -1):
                    print('Эта буква уже была отгадана');
                else:
                    for k in range(len(WORD)):
                        if(WORD[k] == answ):
                            secret = secret[:k] + answ + secret[k+1:];
                    print('Вы угадали букву. Слово: ' + secret);
                p = True
                
            if(WORD == answ or WORD == secret):
                return print(f'Вы победили!. Cлово: {WORD}. Начинаю новую игру...\n'), game();
            
        if(p == False):
            tries -= 1;
            print(f'Попыток осталось: {tries}');
            print(f'Слово: {secret}');
            
    print(f'Вы не угадали слово. Загаданное слово: {WORD}');
    
    game();
    
    
game();