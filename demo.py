from housing.pipeline.pipeline import Pipeline
from housing.exception import HousingException
from housing.config.configuration import Configuration
from housing.logger import logging
import os, sys

def main():
    try:
        config_path = os.path.join("config", "config.yaml")
        pipeline = Pipeline(Configuration(config_file_path=config_path))
        pipeline.run_pipeline()
        # pipeline.start()
        logging.info(f"Main Function Execution COmpleted...")
    except Exception as e:
        logging.error(f"{e}")
        print(e)


if __name__ == "__main__":
    main()