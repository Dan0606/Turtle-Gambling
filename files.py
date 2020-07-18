from time import strftime
import datetime
from os.path import exists

def write_winner(filename, winner):
    hour = strftime("%H")
    minute = strftime("%M")
    second = strftime("%S")
    datetime_object = str(datetime.datetime.now()).split(" ")[0]
    datetime_object = datetime_object.split('-')
    year, month, day = datetime_object[0], datetime_object[1], datetime_object[2]
    todayDate = f"{year}/{month}/{day} {hour}:{minute}:{second} {winner}"
    with open(filename, 'a') as f:
        f.write(f"{todayDate}\n")

def get_lines(filename):
    with open(filename, 'r+') as f:
            lines = []
            for line in f.readlines():
                lines.append(line.split("\n")[0])
            return lines

def reset_winners(filename):
    with open(filename, "w") as f:
        f.truncate(0)

def can_write(filename, winner):
    file = open(filename, 'r+')
    lines = get_lines(filename)
    data = file.readlines()
    counter = 0
    for line in lines:
        counter += 1
        if winner in line:
            winnerLine = line.split(' ')[2]
            winnerLine = int(winnerLine)
            winnerLine += 1
            data[counter-1] = str(f"{winner}: {winnerLine}\n")
            with open(filename, 'w') as file:
                file.writelines(data)
def write_counter(filename, winner):
    try:
        if exists(filename):
            pass
        else:
            raise FileNotFoundError
    except FileNotFoundError:
        with open(filename, 'w') as f:
            f.write("Player One: 0 \n")
            f.write("Player Two: 0 \n")
            # f.write("Green: 0 \n")
            # f.write("Red: 0")
    finally:
        can_write(filename, winner)
            







