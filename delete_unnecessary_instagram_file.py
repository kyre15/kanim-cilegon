import os

list_of_file = os.listdir(os.getcwd() + "/imigrasi_cilegon/")
for item in list_of_file:
   if item.endswith(".json.xz") or item.endswith(".txt") or item.endswith(".mp4") or item.endswith("2.jpg") \
           or item.endswith("3.jpg") or item.endswith("4.jpg") or item.endswith("5.jpg") \
           or item.endswith("6.jpg") or item.endswith("7.jpg") or item.endswith("8.jpg") \
           or item.endswith("9.jpg") or item.endswith("10.jpg"):
       os.remove(os.path.join(os.getcwd()+"/imigrasi_cilegon/", item))

