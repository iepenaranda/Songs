import csv
import matplotlib.pyplot as plt

def read_csv(path):
  with open(path, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=';')
    header = next(reader)
    data = []
    for row in reader:
      iterable = zip(header, row)
      country_dict = {key: value for key, value in iterable}
      data.append(country_dict)
    return data
  
def get_data(data):
  genres = {song['genre'] for song in data}
  info = {}
  for genre in genres:
    genre_data = list(filter(lambda song: song['genre']==genre, data))
    info[genre] = len(genre_data)
  return info

def create_bar_char(data):
  fig, ax = plt.subplots()
  ax.bar(data.keys(), data.values())
  plt.show()