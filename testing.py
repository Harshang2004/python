import os
if os.path.exists("E:\dell.txt"):
  os.remove("E:\dell.txt")
else:
  print("The file does not exist")