#!/usr/bin/env python3
import os
import json
from datetime import datetime
import sys

def main():
    # open file if it exists, otherwise create
    file_name = 'tasks.json'
    tasks_json = {}
    if not os.path.exists(file_name) or os.path.getsize(file_name) == 0:
        with open(file_name, 'w') as f:
            json.dump({"tasks": []}, f, sort_keys=True, indent=4)

    read_file = open(file_name, 'r+')
    tasks_json = json.loads(read_file.read())

    operation = sys.argv[1]
    match operation:
        case 'add':
            if len(sys.argv) > 2:
                tasks_json['tasks'].append({
                    'id': len(tasks_json['tasks']) + 1,
                    'description': sys.argv[2],
                    'status': 'todo',
                    'created_at': str(datetime.now()),
                    'updated_at': str(None)
                })
            else:
                print("Description is required!\n")
        case 'update':
            print("update")
        case 'delete':
            print("update")
        case 'mark-in-progress':
            print("mark-in-progress")
        case 'mark-done':
            print("mark-done")
        case 'list':
            print("list")


    write_file = open(file_name, 'w')
    json.dump(tasks_json, write_file, sort_keys=True, indent=4)


if __name__ == "__main__":
    main()
