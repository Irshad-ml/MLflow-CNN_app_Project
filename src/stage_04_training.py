import argparse
import os
import shutil
from tqdm import tqdm
import logging
from src.utils.common import read_yaml, create_directories
import tensorflow as tf
import mlflow


STAGE = "TRAINING" ## <<< change stage name 

logging.basicConfig(
    filename=os.path.join("logs", 'running_logs.log'), 
    level=logging.INFO, 
    format="[%(asctime)s: %(levelname)s: %(module)s]: %(message)s",
    filemode="a"
    )


def main(config_path):
    ## read config files
    config = read_yaml(config_path)
    
    #get ready the data
    FINAL_PARENT_DIR = os.path.join(config["data"]["unzip_data_dir"],config["data"]["parent_data_dir"])
    
    train_ds = tf.keras.preprocessing.image_dataset_from_directory(
                FINAL_PARENT_DIR,
                validation_split=config["params"]["validation_split"],
                subset="training",
                seed=config["params"]["seed"],
                image_size=tuple(config["params"]["img_shape"][:-1]),
                batch_size=config["params"]["batch_size"])

    val_ds = tf.keras.preprocessing.image_dataset_from_directory(
                FINAL_PARENT_DIR,
                validation_split=config["params"]["validation_split"],
                subset="validation",
                seed=config["params"]["seed"],
                image_size=tuple(config["params"]["img_shape"][:-1]),
                batch_size=config["params"]["batch_size"])
    
    
    #Data Augmentation
    
    
    #load the data
    path_to_model =os.path.join(config["data"]["local_dir"],
                                config["data"]["model_dir"],
                                config["data"]["init_model_file"])
    print(path_to_model)
    logging.info(f"load the base model from {path_to_model}")
    classifier = tf.keras.models.load_model(path_to_model)
    
    #train the model
    logging.info("training started............")
    classifier.fit(train_ds, epochs=config["params"]["epochs"], validation_data = val_ds) 

    trained_model_file = os.path.join(config["data"]["local_dir"],
                                      config["data"]["model_dir"], 
                                      config["data"]["trained_model_file"])

    classifier.save(trained_model_file)
    logging.info(f"trained model is saved at : {trained_model_file}")
    
    #Till now we did mlflow project pipeline .Now below is the code for Mlflow ui part
    with mlflow.start_run() as runs:
        mlflow.log_params(config["params"])
        mlflow.keras.log_model(classifier,"model")


if __name__ == '__main__':
    # argparse.ArgumentParser() is used to take  user input value from command line
    args = argparse.ArgumentParser()
    args.add_argument("--config", "-c", default="configs/config.yaml")
    parsed_args = args.parse_args()

    try:
        logging.info("\n********************")
        logging.info(f">>>>> stage {STAGE} started <<<<<")
        main(config_path=parsed_args.config)
        logging.info(f">>>>> stage {STAGE} completed!<<<<<\n")
    except Exception as e:
        logging.exception(e)
        raise e