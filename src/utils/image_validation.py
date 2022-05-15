import logging
import shutil
import imghdr
from PIL import Image
import os
from src.utils.common import create_directories

def validating_img(config:dict) -> None :
    FINAL_PARENT_DIR = os.path.join(config["data"]["unzip_data_dir"],config["data"]["parent_data_dir"])
    BAD_DATA_DIR = os.path.join(config["data"]["unzip_data_dir"],config["data"]["bad_data_dir"])
    create_directories([BAD_DATA_DIR])

    for dirs in os.listdir(FINAL_PARENT_DIR):
            full_path_data_dir = os.path.join(FINAL_PARENT_DIR, dirs)
            for imgs in os.listdir(full_path_data_dir):
                path_to_img = os.path.join(full_path_data_dir, imgs)
                try:
                    img = Image.open(path_to_img)#the images which are not open that will go the Exception block
                    img.verify()  
                        
                    if len(img.getbands()) !=3 or imghdr.what(path_to_img) not in ['jpeg','png']:
                        bad_data_path = os.path.join(BAD_DATA_DIR, imgs)
                        shutil.move(path_to_img, bad_data_path)
                        logging.info(f"{path_to_img} is verified with unexpected format")
                        continue
                        
                    
                except Exception as e:
                    logging.info(f"{path_to_img} not an expected format")
                    bad_data_path = os.path.join(BAD_DATA_DIR, imgs)
                    shutil.move(path_to_img, bad_data_path)
                    logging.info(f"moved bad data file  from {path_to_img} to {bad_data_path}")
                    logging.exception(e)