from random import choice #импорт библиотеки

print('Привет Игрок')
print('Выбери уровень сложности и количество раундов.')
difficulty_select = input('Выберите сложность: ')
round = 1
CARD_TOP = '┌──┐'
CARD_MID = '│' 
CARD_BOT = '└──┘'
HEARTS   = chr(9829)
SPADES   = chr(9824)
DIAMONDS = chr(9830)
CLUBS    = chr(9827)
CARD_NUMBER = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
CARD_SUIT = [DIAMONDS, HEARTS, SPADES, CLUBS]
score = 0

#def print_card(num, suit):
#    print(CARD_TOP)
#    print(CARD_MID, num, suit, CARD_MID, sep = '')
#    print(CARD_BOT)

if difficulty_select == '1':  # первый уровень сложности
  print('Вы выбрали', difficulty_select, 'уровень сложности.')
  print('Я загадываю карту. Тебе нужно угадать цвет масти карты: "Черная" или "Красная"')
  print('Для выхода введите "q"')
  round_select = int(input('Выберите количество раундов: '))
  while round <= round_select:
    print('Раунд:', round, 'из', round_select)
    random_card_number = choice(CARD_NUMBER)
    random_card_suit = choice(CARD_SUIT)
    player_answer = input('Введите цвет масти карты красная или черная?: ')
    if player_answer in ['красная', 'черная']:
      if player_answer == 'красная' and random_card_suit in [CARD_SUIT[0], CARD_SUIT[1]]:
        score += 1
#        print_card(random_card_number, random_card_suit)
        print('Поздравляем! Вы угадали цвет масти карты: ' + random_card_number + random_card_suit)
        print('Ваш счёт:', score)
      elif player_answer == 'черная' and random_card_suit in [CARD_SUIT[2], CARD_SUIT[3]]:
        score += 1
        print('Поздравляем! Вы угадали цвет масти карты: ' + random_card_number + random_card_suit)
        print('Ваш счёт:', score)
      else:
        print('К сожалению вы не угадали цвет масти карты: ' + random_card_number + random_card_suit)
      round += 1
    elif player_answer == 'q':
      break
    else:
      print('Нет такого цвета! Пробуем еще раз!')
elif difficulty_select == '2':  #Второй уровень сложности
  print('Вы выбрали', difficulty_select, 'уровень сложности.')
  print('Я загадываю карту. Тебе нужно угадать карту 2, 3, J и т.д.')
  print('Для выхода введите "q"')
  round_select = int(input('Выберите количество раундов: '))
  while round <= round_select:
    print('Раунд:', round, 'из', round_select)
    random_card_number = choice(CARD_NUMBER)
    random_card_suit = choice(CARD_SUIT)
    player_answer = input('Введите карту: ')
    if player_answer in CARD_NUMBER:
      if random_card_number == player_answer:
        score += 1
        print('Поздравляем! Вы угадали карту:' + random_card_number + random_card_suit)
        print('Ваш счёт:', score)
      else:
        print('К сожалению вы не угадали карту:' + random_card_number + random_card_suit)
      round += 1
    elif player_answer == 'q':
      break
    else:
      print('Нет такой карты в калоде!')
elif difficulty_select == '3':  #Третий уровень сложности
  print('Вы выбрали', difficulty_select, 'уровень сложности.')
  print('Я загадываю карту. Тебе нужно угадать карту 2, 3, J и т.д., а так же цвет масти карты.')
  round_select = int(input('Выберите количество раундов: '))
  score = 0
  while round <= round_select:
    print('Раунд:', round, 'из', round_select)
    random_card_number = choice(CARD_NUMBER)
    random_card_suit = choice(CARD_SUIT)
    # player_answer_card = input('Введите карту: ')
    # player_answer_color = input('Введите цвет масти карты красная или черная?: ')
    player_answer_color = input('Введите цвет масти карты красная или черная?: ')
    if player_answer_color in ['красная', 'черная']:
      if player_answer_color == 'красная' and random_card_suit in [CARD_SUIT[0], CARD_SUIT[1]]:
        print('Вы угадали цвет!', random_card_suit)
        print('Теперь угадайте саму карту!')
        player_answer_card = input('Введите карту: ')
        if random_card_number == player_answer_card:
          score += 1
          print('Поздравляем! Вы угадали карту и цвет:' + random_card_number + random_card_suit)
          print('Ваш счёт:', score)
        else:
          print('Вы угадали цвет, но карту нет:' + random_card_number + random_card_suit)
      elif player_answer_color in ['красная', 'черная']:
        if player_answer_color == 'черная' and random_card_suit in [CARD_SUIT[2], CARD_SUIT[3]]:
          print('Вы угадали цвет!', random_card_suit)
          print('Теперь угадайте саму карту!')
          player_answer_card = input('Введите карту: ')
          if random_card_number == player_answer_card:
            score += 1
            print('Поздравляем! Вы угадали карту и цвет:' + random_card_number + random_card_suit)
            print('Ваш счёт:', score)
          else:
            print('Вы угадали цвет, но карту нет:' + random_card_number + random_card_suit)
      else:
        print('К сожалению вы не угадали карту и цвет: ' + random_card_number + random_card_suit)
      round += 1
    elif player_answer_color == 'q':
      break  
    else:
      print('Нет такого цвета!')  
else:
  print('Некоректный уровень сложности!')

print('Конец игры!')
print('Ваш итоговый счёт:', score)
