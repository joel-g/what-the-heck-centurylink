f = open("logs.txt")

logs = f.readlines()

def convert_speeds_to_floats(logs):
  for line in logs:
    line = line.split(", ")
    line[2] = float(line[2].rstrip())
    line[1] = float(line[1])
  return logs

def get_average_speeds(data):
  down_total = 0.0
  up_total = 0.0
  for line in data:
    down_total += line[1]
    up_total +=  line[2]
  averages = {'down': down_total / data.length, 'up': up_total / data.length }
  return averages

speeds = convert_speeds_to_floats(logs)
averages = get_average_speeds(speeds)
print(averages)