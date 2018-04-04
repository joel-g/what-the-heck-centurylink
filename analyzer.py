from decimal import Decimal

dec = Decimal

f = open("logs.txt")

logs = f.readlines()

def convert_speeds_to_floats(logs):
  speeds = []
  for line in logs:
    line = line.split(", ")
    print(line)
    line[1] = float(line[1])
    line[2] = float(line[2].rstrip())
    print(line)
    speeds.append(line)
  return speeds

def get_average_speeds(data):
  down_total = 0.0
  up_total = 0.0
  for line in data:
    down_total += line[1]
    up_total +=  line[2]
  averages = {'down': down_total / len(data), 'up': up_total / len(data)}
  return averages

speeds = convert_speeds_to_floats(logs)
print(speeds)
# averages = get_average_speeds(speeds)
# print(averages)