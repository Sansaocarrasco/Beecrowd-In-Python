while True:
  try:
    N = int(input())
    if (not N):
        print ("vai ter copa!")
    else :
        print ("vai ter duas!")
  except EOFError:
    break
