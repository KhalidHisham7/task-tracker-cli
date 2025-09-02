#!/usr/bin/env python3
import argparse
import os
import json
from datetime import datetime

id_incremental = 0

def main():
    # Setup main runtime and get operation argument
    parser = argparse.ArgumentParser(description="Hello, this is a task tracker CLI.")
    parser.add_argument("operation")
    args = parser.parse_args()
    operation = args.operation

    # open file if it exists, otherwise create
    file_name = 'tasks.json'
    tasks_json = {}
    if not os.path.exists(file_name) or os.path.getsize(file_name) == 0:
        with open(file_name, 'w') as f:
            json.dump({"tasks": []}, f, sort_keys=True, indent=4)

    read_file = open(file_name, 'r+')
    tasks_json = json.loads(read_file.read())

    write_file = open(file_name, 'w')
    json.dump(tasks_json, write_file, sort_keys=True, indent=4)
    

def incrementing_id():
    global id_incremental
    id_incremental += 1
    

if __name__ == "__main__":
    main()
