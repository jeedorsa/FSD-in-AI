import csv
import shutil 
src = "C:\\Users\\jesus\\Desktop\\PROYECTO\\results\\PRINGLESQUESO\\render1\\" 
dst= "C:\\Users\\jesus\\Desktop\\BEANCHMARKING\\train1\\"
i=0
with open('train_labels.csv', newline='') as File:  
    reader = csv.reader(File)
    for row in reader:
        if(i>1600):
            origen = src + row[0]
            destino= dst + row[0]
            shutil.copyfile(origen, destino)
        i=i+1
            
