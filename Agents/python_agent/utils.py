import json
import time

def load_config(config_path):
    # Load configuration from file
    with open(config_path) as f:
        return json.load(f)

def sleep(interval):
    # Sleep for the specified interval
    time.sleep(interval)
