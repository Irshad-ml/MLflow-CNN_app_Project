import argparse
import os
import shutil
from tqdm import tqdm
import logging
#Import the validdating image from src/utils/data_mgmt.py ,here src used as a package
from src.utils.image_validation import validating_img 
from src.utils.common import read_yaml, create_directories,unzip_file
import random
import urllib.request as req


STAGE = "GET_DATA" ## <<< change stage name 

logging.basicConfig(
    filename=os.path.join("logs", 'running_logs.log'), 
    level=logging.INFO, 
    format="[%(asctime)s: %(levelname)s: %(module)s]: %(message)s",
    filemode="a"
    )


def main(config_path, params_path):
    ## read config files
    config = read_yaml(config_path)
    print(config)
    URL = config["data"]["source_url"]
    print(URL)
    local_dir = config["data"]["local_dir"]
    #Whatever the directory we fetched from config.yaml file by using that we create directory
    create_directories([local_dir])

    data_file = config["data"]["data_file"]
    print("data: ",data_file)
    #once the local directory created and file created then we create final path where we store the data
    data_file_path = os.path.join(local_dir,data_file)
    print("path of the file: ",data_file_path)

    #req.urlretrieve() function helps to download the data from the online source and store into the destination path and 
    #return filename and headers
    if not os.path.isfile(data_file_path):
        logging.info("downloading started............")
        filename ,headers = req.urlretrieve(URL, data_file_path)
        logging.info(f"filename: {filename} created with info {headers}")
    else:
        logging.info(f"{data_file_path} is already present")
    #params = read_yaml(params_path)
    #pass

    #Unzipped 
    unzipped_dir = config["data"]["unzip_data_dir"]
    if not os.path.isdir(unzipped_dir):
         create_directories([unzipped_dir]) 
         print("unzipped directory: ",unzipped_dir)    
         unzip_file(source = data_file_path, dest = unzipped_dir)
    else:
        logging.info(f"data is already extrated")
        
        

    #config value == {'data': {'source_url': 'https://download.microsoft.com/download/3/E/1/3E1C3F21-ECDB-4869-8368-6DEBA77B919F/kagglecatsanddogs_5340.zip', 
    # 'local_dir': 'data', 
    # 'data_file': 'data.zip', 
    # 'unzip_data_dir': 'data',
    # 'parent_data_dir :'PetImages',
    # 'bad_data_dir':'bad_data'}}

    #Validation of the data means good images will go the good directory and bad images will go the bad directory
    validating_img(config)
 

if __name__ == '__main__':
    # argparse.ArgumentParser() is used to take  user input value from command line
    args = argparse.ArgumentParser()
    args.add_argument("--config", "-c", default="configs/config.yaml")
    args.add_argument("--params", "-p", default="params.yaml")
    parsed_args = args.parse_args()

    try:
        logging.info("\n********************")
        logging.info(f">>>>> stage {STAGE} started <<<<<")
        main(config_path=parsed_args.config, params_path=parsed_args.params)
        logging.info(f">>>>> stage {STAGE} completed!<<<<<\n")
    except Exception as e:
        logging.exception(e)
        raise e