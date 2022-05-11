import argparse
import os
import shutil
from tqdm import tqdm
import logging
from src.utils.common import read_yaml, create_directories
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
    print(data_file)
    #once the local directory created and file created then we create final path where we store the data
    data_file_path = os.path.join(local_dir,data_file)
    print(data_file_path)

    #req.urlretrieve() function helps to download the data from the online source and store into the destination path and 
    #return filename and headers
    if not os.path.isfile(data_file_path):
        logging.info("downloading started............")
        filename ,headers = req.urlretrieve(URL, data_file_path)
        logging.info(f"filename: {filename} created with info {headers}")
    else:
        print(f"{data_file_path} is already present")
    #params = read_yaml(params_path)
    #pass


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