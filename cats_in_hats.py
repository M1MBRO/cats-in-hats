def do_my_homework(cats_count, rounds_count):

  def round(cats, increment):
    i = increment-1
    while i < len(cats):
      cats[i] = not cats[i]
      i += increment

  cats = []
  for i in range(cats_count):
    cats.append(False)

  for i in range(rounds_count):
    round(cats, i+1)

  print(cats)
