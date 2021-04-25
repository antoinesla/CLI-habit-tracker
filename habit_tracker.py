# TODO
# store list of days in json file
# create function to accept user input and that passes arguments to other 
#   functions
# create function to display list of days along with intervals between days
# create function to add occurence
# create function to remove occurence
# ideally parameters would be passed directly, i.e. in terminal: 'add [date]'
#   or 'add today [time]' or add now'
# once this all works well, add a way to have different categories (e.g.
#   different lists that keep track of different activities)

import json

def display_help():
    '''prints available commands'''
    print('available commands:\n'
          'help: prints availalable commands\n'
          'add: add occurence to record\n'
          'wipe: wipe all values from the record'
          'quit: quits the program')

def create_record():
    '''creates blank record file'''
    record = []
    with open(filepath, 'w') as f:
        json.dump(record, f)

def load_record():
    '''
    loads record from json file and returns
    calls function to create json file if there is none
    '''
    try:
        with open(record_filepath) as f:
            record = json.load(f)
    except FileNotFoundError:
        print('record not found, creating one')
        create_record(record_filepath)
        # record has been created, can now be returned (will be a blank list)
        with open(record_filepath) as f:
            record = json.load(f)
        
    return record

def save_record(record):
    '''saves record to json file'''
    with open(record_filepath, 'w') as f:
        json.dump(record, f)

def reset_record(record):
    user_input = input("are you sure you want to wipe the record?")
    record.clear()
    save_record(record)

def add_to_record(record):
    '''adds value to record'''
    user_input = input('what do you want to add? ')
    record.append(user_input)
    save_record(record)

def display_record(record):
    '''displays each occurence in record'''
    if record:
        for i in record:
            print(i)
    else:
        print('record is empty')


def main():
    '''main function that loops while asking for user input'''
    input_message = ("enter command ('help' to see list of "
                     "commands/'quit' to quit): ")
    
    record = load_record()
    
    while True:
        user_input = input(input_message)
        # split user input string in list to get command (first word) and
        #   parameters (following words)
        if user_input == 'help':
            display_help()
        elif user_input == 'add':
            add_to_record(record)
        elif user_input == 'display':
            display_record(record)
        elif user_input == 'wipe':
            wipe_record(record)
        elif user_input == 'quit':
            break
        else:
            print('input not recognized, type help to see list of commands')


record_filepath = 'record.json'

main()
