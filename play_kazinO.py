from decouple import config
from hw5_kazino import check_win_loss

def play():
    slots = list(range(1, 31))
    money = float(config("MY_MONEY"))
    playing = True
    
    while playing: 
        print(f"Ваш счет: {money}$") 
        bet = float(input("Сколько денег хотите поставить: "))

        user = int(input("На какой слот: ")) 
        chosen = user if user in slots else print('Выберите от 1 до 30') 
        win = check_win_loss(chosen)


        print(float(f"Хотите ли вы дальше играть?"))
        if win: 
            money += 2 * bet 
            print("Вы выиграли")          
        else:
            money -= bet
            print("Вы проиграли")
            
        choice= input("Хотите еще сыграть? (Yes/No)")
        if choice.lower() != "no" or money == 0:
            playing = False
        else:
          choice.lower() != "yes"
          return
        
        if money > float(config("MY_MONEY")): 
            print("вы выиграли!") 
        elif money == float(config("MY_MONEY")): 
            print("ничья") 
        else: 
            print("вы проиграли")

