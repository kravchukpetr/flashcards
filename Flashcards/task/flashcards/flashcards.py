# Write your code here
import pickle

action_list = ['add', 'remove', 'import', 'export', 'ask', 'exit']
term_list = []


def add_card(card_list):
    print("The card:")
    while True:
        term = input()
        if term in [list(x.keys())[0] for x in card_list]:
            print('The term "{0}" already exists. Try again:'.format(term))
        else:
            break
    print("The definition of the card:")
    while True:
        defin = input()
        if defin in [list(x.values())[0] for x in card_list]:
            print('The definition "{0}" already exists. Try again:'.format(defin))
        else:
            break
    card_list.append({term: defin})
    print('The pair ("{0}":"{1}") has been added'.format(term, defin))
    return card_list


def ask_card(card_list):
    print('How many times to ask?')
    num_ask = int(input())
    i = 1
    # for i, term in enumerate(card_list):
    while i <= num_ask:
        term = card_list[i % len(card_list)]
        print('Print the definition of "{0}":'.format(list(term.keys())[0]))
        user_answer = input()
        if list(term.values())[0] == user_answer:
            print('Correct!')
        elif user_answer in [list(x.values())[0] for x in card_list]:
            print('Wrong. The right answer is "{0}", but your definition is correct for "{1}"'.format(list(term.values())[0], [list(x.keys())[0] for x in card_list if list(x.values())[0] == user_answer][0]))
        else:
            print('Wrong. The right answer is "{0}".'.format(list(term.values())[0]))
        i += 1


def remove_card(card_list):
    print("Which card?")
    card_to_remove = input()
    if card_to_remove in [list(x.keys())[0] for x in card_list]:
        card_list.remove({card_to_remove: [list(x.values())[0] for x in card_list if list(x.keys())[0] == card_to_remove][0]})
        print("The card has been removed.")
    else:
        print("Can't remove", '"{0}": there is no such card.'.format(card_to_remove))
    return card_list


def export_card(card_list):
    print('File name:')
    file_name = input()
    with open(file_name, 'wb') as fp:
        pickle.dump(card_list, fp)
    print("{0} cards have been saved.".format(len(card_list)))


def import_card(card_list):
    print("File name:")
    file_name = input()
    try:
        with open(file_name, 'rb') as fp:
            tmp_list = pickle.load(fp)
        print("{0} cards have been loaded.".format(len(tmp_list)))
        for card in tmp_list:
            if list(card.keys())[0] in [list(x.keys())[0] for x in card_list]:
                card_list.remove({list(card.keys())[0]: [list(x.values())[0] for x in card_list if list(x.keys())[0] == list(card.keys())[0]][0]})
            card_list.append(card)
    except FileNotFoundError:
        print('File not found.')
    return card_list


while True:
    print("Input the action (add, remove, import, export, ask, exit):")
    action = input()
    # if action in action_list:
    if action == 'add':
        term_list = add_card(term_list)
    elif action == 'remove':
        term_list = remove_card(term_list)
    elif action == 'import':
        term_list = import_card(term_list)
    elif action == 'export':
        export_card(term_list)
    elif action == 'ask':
        ask_card(term_list)
    elif action == 'exit':
        print("Bye bye!")
        break
    # else:
    #     print("Incorrect action")
