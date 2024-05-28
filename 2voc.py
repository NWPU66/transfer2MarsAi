import os, random
from tqdm.auto import tqdm

PROJECT_ROOT = "E:/Study/CodeProj/transfer2MarsAi"

# 划分数据集
# 根据挂载的数据集制作制作标签文件，并进行划分
# 生成train.txt和val.txt
random.seed(2020)
xml_dir = PROJECT_ROOT + "/dataset/orignal_oil_dataset/Annotations"  # 标签文件地址
img_dir = PROJECT_ROOT + "/dataset/orignal_oil_dataset/JPEGImages"  # 图像文件地址
path_list = list()
for img in tqdm(os.listdir(img_dir)):
    # img_path = os.path.join(img_dir, img)
    img_path = img_dir + "/" + img
    # xml_path = os.path.join(xml_dir, img.replace("jpg", "xml"))
    xml_path = xml_dir + "/" + img.replace("jpg", "xml")
    path_list.append((img_path, xml_path))
random.shuffle(path_list)
ratio = 1.0  # 测试集和验证集划分比例0.8:0.2
train_f = open(
    PROJECT_ROOT + "/dataset/orignal_oil_dataset/train.txt", "w"
)  # 生成训练文件
val_f = open(PROJECT_ROOT + "/dataset/orignal_oil_dataset/val.txt", "w")  # 生成验证文件

for i, content in tqdm(enumerate(path_list)):
    img, xml = content
    text = img + " " + xml + "\n"
    if i < len(path_list) * ratio:
        train_f.write(text)
    else:
        val_f.write(text)
train_f.close()
val_f.close()

# 生成标签文档
label = ["oil"]  # 设置你想检测的类别
with open(PROJECT_ROOT + "/dataset/orignal_oil_dataset/label_list.txt", "w") as f:
    for text in tqdm(label):
        f.write(text + "\n")

"""
python tools/x2coco.py \
        --dataset_type voc \
        --voc_anno_dir /home/aistudio/data/oil/Annotations \
        --voc_anno_list /home/aistudio/data/oil/train.txt \
        --voc_label_list /home/aistudio/data/oil/label_list.txt \
        --voc_out_name /home/aistudio/data/oil/train.json
python tools/x2coco.py \
        --dataset_type voc \
        --voc_anno_dir /home/aistudio/data/oil/Annotations \
        --voc_anno_list /home/aistudio/data/oil/val.txt \
        --voc_label_list /home/aistudio/data/oil/label_list.txt \
        --voc_out_name /home/aistudio/data/oil/valid.json
"""
