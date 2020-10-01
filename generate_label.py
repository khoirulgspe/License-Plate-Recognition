from os.path import join
from glob import glob

files = []
#extensions = ['*.jpg', '*.png', '*.jpeg', '*.tiff', '*.bmp', '*gif']
extensions = ['*.txt']
for ext in extensions:
   files.extend(glob(join("/home/gspe/CompletedProject/train_yolo/dataset_nopol/images/", ext)))
   #print(files)

with open('nopol3.txt', 'w') as f:
    for item in files:
        f.write("%s\n" % item)

#print(files)