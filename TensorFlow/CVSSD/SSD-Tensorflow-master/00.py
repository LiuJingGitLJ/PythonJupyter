import os
import random

xmlfilepath=r'./VOC2018/test/Annotations'
saveBasePath=r"./"

trainval_percent=0.98
train_percent=0.98
total_xml = os.listdir(xmlfilepath)
num=len(total_xml)
list=range(num)
tv=int(num*trainval_percent)
tr=int(tv*train_percent)
trainval= random.sample(list,tv)
train=random.sample(trainval,tr)

print("train and val size",tv)
print("traub suze",tr)
ftrainval = open(os.path.join(saveBasePath,'VOC2018/test/ImageSets/Main/trainval.txt'), 'w')
ftest = open(os.path.join(saveBasePath,'VOC2018/test/ImageSets/Main/test.txt'), 'w')
ftrain = open(os.path.join(saveBasePath,'VOC2018/test/ImageSets/Main/train.txt'), 'w')
fval = open(os.path.join(saveBasePath,'VOC2018/test/ImageSets/Main/val.txt'), 'w')

for i  in list:
    name=total_xml[i][:-4]+'\n'
    if i in trainval:
        ftrainval.write(name)
        if i in train:
            ftrain.write(name)
        else:
            fval.write(name)
else:
    ftest.write(name)

ftrainval.close()
ftrain.close()
fval.close()
ftest .close()
