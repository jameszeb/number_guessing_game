import main

name = 'james'
assert name == main.ask_for_name()
print('Ask_for_name passed')


number = main.create_a_number(name)
assert number >= 1 and number <= 100
print('create_a_number passed')

guess = main.guess_the_number(number)
assert guess == number
print('guess_the_number passed')
