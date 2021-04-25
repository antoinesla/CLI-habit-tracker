# TODO
# store list of days in json file
# create function to accept user input and that passes arguments to other 
#   functions
# create function to display list of days along with intervals between days
# create function to add occurence
# create function to remove occurence

import json

def display_help():
    '''prints available commands'''
    print('available commands:\n'
          'help: prints availalable commands\n'
          'quit: quits the program')

def create_record(filepath):
    '''creates blank record file'''
    record = []
    with open(filepath, 'w') as f:
        json.dump(record, record)

def load_record(filepath):
    '''loads record from json file if it exists, creates one if it doesn't'''
    try:
        with open(filepath) as f:
            record = json.load(f)
    except FileNotFoundError:
        print('record not found, creating one')
        create_record(filepath)
        # record has been created, can now be returned (will be a blank list)
        with open(filepath) as f:
            record = json.load(f)

    return record

def main():
    '''main function that loops while asking for user input'''
    input_message = ("enter command ('help' to see list of "
                     "commands/'quit' to quit): ")
    
    record_filepath = 'record.json'
    record = load_record(record_filepath)
    
    while True:
        user_input = input(input_message)
        if user_input == 'help':
            display_help()
        elif user_input == 'quit':
            break
        else:
            print('input not recognized, type help to see list of commands')


main()
