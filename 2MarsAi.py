import os
import tqdm.auto

PROJECT_ROOT = "E:/Study/CodeProj/transfer2MarsAi"
IMAGE_PATH = PROJECT_ROOT + "/dataset/coco_oil_dataset/images"
OUTPUT_PATH = PROJECT_ROOT + "/dataset/MarsAl_oil_dataset/obj_train_data"

if __name__ == "__main__":
    # 读取IMAGE_PATH下的所有图像文件
    image_files = os.listdir(IMAGE_PATH)
    for image_file in tqdm.auto.tqdm(image_files):
        # 分离文件名和后缀
        image_name, image_extension = os.path.splitext(image_file)
        # 文件路径
        image_path = IMAGE_PATH + "/" + image_file
        # 将文件以新的名字复制到OUTPUT_PATH文件夹下
        os.replace(image_path, OUTPUT_PATH + "/frame" + image_name.zfill(6) + ".jpg")
        print(f"new name: {OUTPUT_PATH}/frame{image_name.zfill(6)}.jpg")
