def hash(boxes, key):
  boxes = 10
  hashed = 0
  for letter in key:
    hashed = hashed + ord(letter)
    print(ord(letter))
  return hashed % boxes 


print(f' dog {hash(10, "dog")}')
print(f' python {hash(10, "python")}')
print(f' python is better than javascript {hash(10, "python is better than javascript")}')
print(f' hope this works {hash(10, "hope this works")}')
print(f' 1205 {hash(10, "1205")}')


hashtableclass(key,value)