def encode(text):
  word = "";chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890=\ "
  for i in range(len(text)):
    letter = chars.find(text[i])
    if letter == -1:continue
    if letter < 10:
      word += "0"+str(letter)
    else:
      word += str(letter)
  return word

def decode(text):
  word = "";chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890==\ "
  for i in range(0, len(text), 2):
    working = True
    try:
      chars[int(text[i]+text[i+1])]
    except Exception:
      working = False
    if i + 1 < len(text) and working:
      word += chars[int(text[i]+text[i+1])]
    i += 1
  return word

def encode_file(file):
  import base64
  y = open(file, "rb").read()
  x = base64.encodebytes(y).decode()
  #return encode(x)
  return encode(x)

def decode_file_data(text):
  import base64
  x = decode(text)
  return base64.b64decode(x).decode()

#m = encode_file("main.py")
#m2 = decode_file_data(m)
