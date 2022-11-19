import random
import numpy

# spell trace costs

hundred_stat = 510
seventy_stat = 670
thirty_stat = 630
innocence = 1337
clean_slate = 200

total_enhancements = 8
scroll_chance = 30

successfuls = []
buttons_clicked =[]

for aa in range(0, 5000):
    trace_cost = 0
    button_clicked = 0
    for bb in range(0, total_enhancements):
        stat_success = False
        while not stat_success:
            trace_cost += thirty_stat
            button_clicked += 1
            if random.randint(1, 100) <= scroll_chance:
                stat_success = True
            else:
                clean_state_success = False
                while not clean_state_success:
                    trace_cost += clean_slate
                    button_clicked += 1
                    if random.randint(1, 100) <= 15:
                        clean_state_success = True
    successfuls.append(trace_cost)
    buttons_clicked.append(button_clicked)

twentyfifth = numpy.percentile(successfuls, 25)
fiftieth = numpy.percentile(successfuls, 50)
seventyfifth = numpy.percentile(successfuls, 75)

print(f"Spell Trace Percentiles:\n"
      f"{twentyfifth} | {fiftieth} | {seventyfifth}")

print(f"Button Percentiles:\n"
      f"{numpy.percentile(buttons_clicked, 25)} | {numpy.percentile(buttons_clicked, 50)} | {numpy.percentile(buttons_clicked, 75)}")
