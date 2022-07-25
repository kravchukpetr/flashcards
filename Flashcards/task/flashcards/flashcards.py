# Write your code here
print("Input the number of cards:")
number_of_cards = int(input())
term_list = []
for i in range(0, number_of_cards):
    print("The term for card #{0}:".format(i+1))
    while True:
        term = input()
        if term in [list(x.keys())[0] for x in term_list]:
            print('The term "{0}" already exists. Try again:'.format(term))
        else:
            break
    print("The definition for card #{0}:".format(i+1))
    while True:
        defin = input()
        if defin in [list(x.values())[0] for x in term_list]:
            print('The definition "{0}" already exists. Try again:'.format(defin))
        else:
            break
    term_list.append({term: defin})
for term in term_list:
    print('Print the definition of "{0}":'.format(list(term.keys())[0]))
    user_answer = input()
    if list(term.values())[0] == user_answer:
        print('Correct!')
    elif user_answer in [list(x.values())[0] for x in term_list]:
        print('Wrong. The right answer is "{0}", but your definition is correct for "{1}"'.format(list(term.values())[0], [list(x.keys())[0] for x in term_list if list(x.values())[0] == user_answer][0]))
    else:
        print('Wrong. The right answer is "{0}".'.format(list(term.values())[0]))
