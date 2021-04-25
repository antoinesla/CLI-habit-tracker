# TODO
# store list of days in json file
# create function to accept user input and that passes arguments to other 
#   functions
# create function to list list of days along with intervals between days
# ideally parameters would be passed directly, i.e. in terminal: 'add [date]'
#   or 'add today [time]' or add now'
# once this all works well, add a way to have different categories (e.g.
#   different lists that keep track of different activities)

import json

def display_help():
    '''prints available commands'''
    print('-------------------\n'
          'available commands:\n'
          '-------------------\n'
          '  help: lists availalable commands\n'
          '  list: lists entries on the record\n'
          '  add: add entry to record\n'
          '  remove: remove a specific entry from the record\n'
          '  wipe: wipe all entries from the record\n'
          '  quit: quits the program')

def create_record():
    '''creates blank record file'''
    record = []
    with open(record_filepath, 'w') as f:
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
        create_record()
        # record has been created, can now be returned (will be a blank list)
        with open(record_filepath) as f:
            record = json.load(f)
    return record

def save_record(record):
    '''saves record to json file'''
    with open(record_filepath, 'w') as f:
        json.dump(record, f)

def wipe_record(record):
    '''wipes record (replaces it by blank list)'''
    user_input = input(('are you sure you want to wipe the record?\n'
                        "type 'yes' if so: "))
    if user_input == 'yes':
        record.clear()
        save_record(record)
        print('record cleared')
    else:
        print('record not cleared')

def add_to_record(record):
    '''adds value to record'''
    user_input = input('what do you want to add? ')
    record.append(user_input)
    save_record(record)

def remove_from_record(record):
    '''remove a specific from record'''
    print("type 'list' to list entries or 'quit' to go back to main menu")

    done = False

    while not done:
        user_input = input('type entry number to remove it from the record: ')
        if user_input == 'list':
            list_record(record)
        elif user_input == 'quit':
            print('going back to main menu')
            break
        else:
            # check for ValueError or IndexError
            try:
                user_input = int(user_input)
                record.pop(user_input - 1)
                save_record(record)
                print('entry removed, going back to main menu')
                done = True
            except ValueError:
                print("please enter a positive integer, or 'done' to quit")
            except IndexError:
                print('this entry does not exist')

def list_record(record):
    '''lists each entry in record'''
    x = 1
    if record:
        print('entries:')
        for i in record:
            print(f'  {x}. {i}')
            x += 1
    else:
        print('record is empty')


def main():
    '''main function that loops while asking for user input'''    
    record = load_record()
    print(('-----------------\n'
           'CLI Habit Tracker\n'
           '-----------------\n'
           "type 'help' to see list of commands, 'quit' to quit"))
    
    while True:
        user_input = input()
        # split user input string in list to get command (first word) and
        #   parameters (following words)
        if user_input == 'help':
            display_help()
        elif user_input == 'list':
            list_record(record)
        elif user_input == 'add':
            add_to_record(record)
        elif user_input == 'remove':
            remove_from_record(record)
        elif user_input == 'wipe':
            wipe_record(record)
        elif user_input == 'quit':
            break
        else:
            print('input not recognized, type help to see list of commands')


record_filepath = 'record.json'

main()
