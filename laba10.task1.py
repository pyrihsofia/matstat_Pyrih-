B = [1, -3, 0, 4, -2, 6, -5]

last_pos_index=-1
for i in range(len(B)):
  if B[i]>0:
      last_pos_index=i
  if last_pos_index==-1:
      s=0
  else:
      s = sum(B[:last_pos_index + 1])
print("Сума елементів:", s)
