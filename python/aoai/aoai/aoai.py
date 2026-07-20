import os

import pandas as pd
from sklearn import neural_network as nn
from sklearn.model_selection import train_test_split

from aolog import AoLog
import aoutil

config = {
    "data": {
        "columns": {
            "column_1": {
                "data_type": "numeric",
                "has_header": True,
                "null_value": 0,
                "null_value_replacement": "avg",
                "outlier_thresholds": [0, 1000],
            },
            "column_2": {},
        },
        "rows": {
            "drop_threshold": 0.3,
            "incompatable_value_groups": [
                {
                    "column_2": "this",
                    "column_5": "that"
                },
                {
                    "column_3": .5,
                    "column_4": 0,
                    "column_6": -1
                }            
            ],
        }
    },
    "model": {
        "train_test_split": .8,
        "shuffle": True,
        
    }
}

def _handle_csv(data_file_path, csv_config, logger: AoLog):
    logger.reset_errors()
    data = pd.DataFrame()
    config = {

    }

    return data, logger
    
def _handle_excel(data_file_path, excel_config, logger: AoLog):
    logger.reset_errors()
    data = pd.DataFrame()
    config = {

    }

    return data, logger

def _handle_json(data_file_path, json_config, logger: AoLog):
    logger.reset_errors()
    data = pd.DataFrame()
    config = {

    }

    return data, logger

def _handle_xml(data_file_path, xml_config, logger: AoLog):
    logger.reset_errors()
    data = pd.DataFrame()
    config = {

    }

    return data, logger

def _handle_html(data_file_path, htmlConfig, logger: AoLog):
    logger.reset_errors()
    data = pd.DataFrame()
    config = {

    }

    return data, logger

def ai_data_prep(data_set, logger: AoLog, config: dict):
    logger.reset_errors()
    data = pd.DataFrame()

    if isinstance(data_set, str):
        data_file_path = data_set
        logger.log_info(f"Detected string input for 'data_set' treating as a file path.")
        allowedExtensions = ["csv", "xlsx", "json", "xml", "html"]            
        logger.log_debug(f"Allowed list of file extensions: {allowedExtensions}")
        fileExtension = data_set.split(".")[-1]
        logger.log_debug(f"Detected file extension is {fileExtension}")

        df = pd.DataFrame()

        if os.path.exists(data_set) and os.path.isfile(data_set):
            pass

        else:
            logger.log_error(f"Invalid path", f"parameter 'data_set' must be a valid file path, cannot be dir, symlink, or other file system object.")
            return data

        if fileExtension in allowedExtensions:
            logger.log_debug(f"Allowed extension detected")

        else:
            logger.log_error(f"Invalid file extension detected: {fileExtension}", f"The only allowed file extensions are {allowedExtensions}")
            return data, logger
        
        if fileExtension == "csv":
            csvConfig = config["csv"]
            df, logger = _handle_csv(data_file_path, csvConfig, logger)
        
        elif fileExtension == "xlsx":
            excelConfig = config["excel"]
            df, logger = _handle_csv(data_file_path, excelConfig, logger)
        
        elif fileExtension == "json":
            jsonConfig = config["json"]
            df, logger = _handle_json(data_file_path, jsonConfig, logger)

        elif fileExtension == "xml":
            xmlConfig = config["xml"]
            df, logger = _handle_xml(data_file_path, xmlConfig, logger)
        
        elif fileExtension == "html":
            htmlConfig = config["html"]
            df, logger = _handle_html(data_file_path, htmlConfig, logger)
            
        else:
            logger.log_error(f"Unknown file extension. Please make sure the file is properly named with '.FILE_EXTENSION'", f"file name: {data_set}")
            return data, logger
        

    elif isinstance(data_set, list):
        pass

    elif isinstance(data_set, dict):
        pass

    elif isinstance(data_set, pd.DataFrame):
        pass

    else:
        pass
    
    return data, logger

def create_predictive_neural_network(X_train, Y_train, logger: AoLog, config):
    logger.reset_errors()
    model = None
    modelConfig = config["model"]
    logger.log_debug(f"Creating predictive model with the following configuration: {config}")
    config = {
        "model_type": ["regressor", "classifier", "generative"],
        "model": {
            "learning_rate_init": .01,
            "learning_rate": "constant",
            "momentum": 0.9,
            "hidden_layer_sizes": (100, 30),
            "solver": "sgd",
            "activation_function": "tanh",
            "random_seed": 42
        }
    }

    if config["model_type"] == "regressor":
        model = nn.MLPRegressor(**modelConfig)

    elif config["model_type"] == "classifier":
        model = nn.MLPClassifier(**modelConfig)

    elif config["model_type"] == "generative":
        model = nn.BernoulliRBM(**modelConfig)

    else:
        logger.log_error(f"Invalid model type supplied. Must be one of ['regressor', 'classifier', 'generative'].", config["model_type"])
        return logger, model

    try:
        logger.log_info("Begin training...")
        model.fit(X_train, Y_train)
        logger.log_info("Training complete.")

    except Exception as e:
        logger.log_error(f"Failed to train the {config["model_type"]} model.", str(e))
        model = None
        return logger, model
        
    return model
    
def create_feature_extraction_neural_network(X_train, Y_train, logger: AoLog, config):
    logger.reset_errors()
    model = None
    modelConfig = config["model"]
    logger.log_debug(f"Creating predictive model with the following configuration: {config}")
    
    model = nn.BernoulliRBM(**modelConfig)
    try:
        logger.log_info("Begin training...")
        model.fit(X_train, Y_train)
        logger.log_info("Training complete.")

    except Exception as e:
        logger.log_error(f"Failed to train the {config["model_type"]} model.", str(e))
        model = None
        return logger, model

    return logger, model
    

def ai_engine():
    pass

if __name__ == "__main__":
    pass