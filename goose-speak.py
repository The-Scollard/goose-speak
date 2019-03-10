import random
import sys

i_ch = u"\u200C"
n_ch = u"\u0000"
s_ch = u"\u2063"
d_ch = u"\u200B"

def geesify(str_to_geese):
  wordlist = str_to_geese.split(" ")
  gl = []
  first_word = True
  for word in wordlist:
    gw = ""
    sw = ""
    if (len(word) == 0):
      continue
    true_size = len(word)
    true_start = 0

    for i in range(len(word)):
      if (word[i].isalpha() or word[i].isnumeric()):
        true_start = i;
        break
    for i in range(len(word)):
      if (word[i].isalpha() or word[i].isnumeric()):
        true_size = i;
    if (true_size < len(word)):
        true_size += 1

        
    for i in range(true_size):
      sw += s_ch
      l = word[i]
      if (l == '\''):
        sw += i_ch
      elif (l == '-'):
        sw += i_ch + i_ch;
      elif (l.isnumeric()):
        sw += d_ch
        ci = int(l)
        sw += ci * n_ch
      else:
        if (l.islower()):
          sw += s_ch
          l = l.upper()
        lt = (ord(l) - (ord('A') - 1))
        sw += lt * n_ch
    if (true_size < 4):
      lta = 5 - true_size
      word = word[:true_size] + lta * "F" + word[true_size:]
      true_size = 5
    if (true_size == 4):
      gw = "HONK"
    else:
      if (random.randint(1, 2) == 1):
        for i in range(true_size):
          if (i == 0):
            ch = "Q"
          elif (i == true_size - 1):
            ch = "K"
          elif (i == true_size - 2):
            ch = "C"
          elif (i == true_size - 3):
            ch = "A"
          else:
            ch = "U"
          gw = gw + ch
      else:
        split_letter = true_size / 2
        if (random.randint(1, 2) == 1):
          split_letter -= 1
        for i in range(true_size):
          if (i == 0):
            ch = "H"
          elif (i == true_size - 1):
            ch = "K"
          else:
            if (i < split_letter):
              ch = "O"
            else:
              ch = "N"
          gw = gw + ch
    for i in range(true_size, len(word)):
      gw = gw + word[i]
    if (first_word):
      sw += "\r"
      first_word = False
    gw = word[:true_start] + sw + gw
    gl.append(gw)
  geese_talk = " ".join(gl)
  return geese_talk

def degeesify(str_to_degeese):
  cs = ""
  word = str_to_degeese
  letter = False
  l_case = False
  number = False
  l_count = 0
  for i in range(len(word)):
    if (word[i] == s_ch and letter and (l_count > 0 or number)):
      if (number):
        l = str(l_count)
      elif (l_case):
        l = chr(ord('a') + l_count - 1)
      else:
        l = chr(ord('A') + l_count - 1)
      cs += l
      l_count = 0
      l_case = False
      number = False
    elif(word[i] == s_ch and letter):
      l_case = True
    elif(word[i] == s_ch):
      letter = True
    elif(letter and word[i] == i_ch):
      if (word[i + 1] == i_ch):
        cs += "-"
        i += 1
      else:
        cs += "'"
      letter = False
    elif(letter and word[i] == d_ch):
      number = True
    elif(letter and word[i] == n_ch):
      l_count += 1
    elif(letter):
      if (number):
        l = str(l_count)
      elif (l_case):
        l = chr(ord('a') + l_count - 1)
      else:
        l = chr(ord('A') + l_count - 1)
      cs += l
      if (not(word[i].isalpha()) and word[i] != '\r'):
        cs += word[i]
      letter = False
      l_case = False
      number = False
      l_count = 0
    else:
      if (not(word[i].isalpha()) and word[i] != '\r'):
        cs += word[i]
  return cs

data = sys.stdin
to_geese = True

try:
  for arg in range(0, len(sys.argv)):
    if (sys.argv[arg] == "-d"):
      to_geese = False
    elif(sys.argv[arg] == "-f"):
      try:
        fname = sys.argv[arg + 1]
        data = open(fname, "r")
      except:
        pass
except:
  print("Invalid Parameters")
  exit(1)

contents = data.read().replace("\n", " ")

if (len(sys.argv) > 1):
  if (sys.argv[1] == "-d"):
    to_geese = False

if (to_geese):
  output = geesify(contents)
else:
  output = degeesify(contents)
 
of = open("output.txt", "w+")
of.write(output)

print(output)
