print('Please provide AI some data to learn...')
print('The current data length is 0, 100 symbols left')
training_list = []
count_symbols = 100

while len(training_list) < count_symbols:
    training_input = input('Print a random string containing 0 or 1:')
    for symbol in training_input:
        if symbol == '1' or symbol == '0':
            training_list.append(symbol)
    remainder_symbol = count_symbols - len(training_list)
    print(f'Current data length is {len(training_list)}, {remainder_symbol} symbols left')


ready_string = ''.join(training_list)
print('Final data string:', ready_string, sep="\n")

triad_dict = {'000': [0, 0],
              '001': [0, 0],
              '010': [0, 0],
              '011': [0, 0],
              '100': [0, 0],
              '101': [0, 0],
              '110': [0, 0],
              '111': [0, 0]}

for i, j in zip(range(0, len(ready_string) - 3), range(3, len(ready_string))):
    small_string = ready_string[i:j + 1]
    key = small_string[0:3]
    value = triad_dict[key]
    if small_string[3] == '1':
        value[1] += 1
    else:
        value[0] += 1

print('You have $1000. Every time the system successfully predicts your next press, you lose $1.\n'
      'Otherwise, you earn $1. Print "enough" to leave the game. Let\'s go!')

balance = 1000

def game(input_string):
    result = ''
    global balance
    for sym in input_string:
        if sym != '1' and sym != '0':
            return result
        elif len(input_string) < 4:
            return result
        else:
            index = 0
            count = 0
            prediction = ''
            for i, j in zip(range(0, len(input_string) - 3), range(3, len(input_string))):
                test = input_string[i:j + 1]
                user_number = triad_dict.get(test[0:3])
                if user_number[0] > user_number[1]:
                    prediction = prediction + '0'
                else:
                    prediction = prediction + '1'
            for _ in prediction:
                if prediction[index] != input_string[index + 3]:
                    count += 1
                    balance += 1
                else:
                    balance -= 1
                index += 1
            result = 'predictions:\n' + prediction + '\n' + '\n' + \
                     'Computer guessed ' + str(len(prediction) - count) + ' out of ' + str(len(prediction)) + \
                     ' symbols right (' + str(((len(prediction) - count) / len(prediction)) * 100) + ' %)\n' + \
                'Your balance is now $' + str(balance)
            return result
input_string = ''
while input_string != 'enough':
    input_string = input('Print a random string containing 0 or 1:')
    print(game(input_string))
else:
    print('Game over!')