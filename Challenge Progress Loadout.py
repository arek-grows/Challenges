from Challenge_Completion_Checklist import challenge_checklist
from Challenge_Links_Dictionry import challenge_links
import webbrowser


def create_and_print_list(checklist):
    completed = []
    uncompleted = []
    not_started = []
    for ch_number in checklist:
        if checklist[ch_number] == True or type(checklist[ch_number]) is int:
            completed.append(ch_number)
        elif checklist[ch_number] == 'not_started':
            not_started.append(ch_number)
        else:
            uncompleted.append(ch_number)
    # print
    print("Completed Challenges:", len(completed), '-', len(completed) / len(checklist) * 100, '%', completed)
    print("Uncompleted Challenges:", len(uncompleted), '-', len(uncompleted) / len(checklist) * 100, '%', uncompleted)
    print("Challenges Not Started:", len(not_started), '-', len(not_started) / len(checklist) * 100, '%', not_started)
    return


create_and_print_list(challenge_checklist)
opened = True
while opened:
    link = input("which challenge would you like to read about? 176+ only")
    if link.isdigit() is False:  # or int(link) not in challenge_links.keys():
        opened = False
        print('exiting')
        break
    webbrowser.open('https://github.com/beginnerpy-com/challenges/blob/main/weekday/challenge_' + str(link) + '.md')
