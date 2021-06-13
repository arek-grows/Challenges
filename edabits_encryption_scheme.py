import math


def encryption(txt):
    txt = txt.replace(' ', '')
    max_l = math.ceil(math.sqrt(len(txt)))
    end_string = ''
    for x in range(max_l):
        i = 0
        try:
            while True:
                end_string += txt[x+i]
                i += max_l
        except IndexError:
            end_string += ' '
    return end_string.rstrip()


print(encryption("if man was meant to stay on the ground god would have given us roots"))
print(encryption("Back to Square One is a popular saying that means a person has to start over, similar to: back to the drawing board."))
# "Brpgatroea aeutpo,:dr cOlhessbrd knaartiaa. tertsamcw oismoriki Ssaentltn qayahoaog upinavrtb aonssetho"