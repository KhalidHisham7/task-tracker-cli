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
            if len(sys.argv) > 3:
                id_to_be_updated = int(sys.argv[2])
                index_to_be_updated = contains(tasks_json['tasks'], lambda task: task['id'] == id_to_be_updated)
                if index_to_be_updated >= 0:
                    tasks_json['tasks'][index_to_be_updated]['description'] = sys.argv[3]
                    tasks_json['tasks'][index_to_be_updated]['updated_at'] = str(datetime.now())
                else:
                    print(f"Task with id {id_to_be_updated} not found\n")
            else:
                print("Some arguments are missing, please provide id of the task and new description\n")
        case 'delete':
            if len(sys.argv) > 2:
                id_to_be_deleted = int(sys.argv[2])
                index_to_be_deleted = contains(tasks_json['tasks'], lambda task: task['id'] == id_to_be_deleted)
                if index_to_be_deleted >= 0:
                    tasks_json['tasks'][index_to_be_deleted]['updated_at'] = str(datetime.now())
                    tasks_json['tasks'][index_to_be_deleted]['deleted_at'] = str(datetime.now())
                else:
                    print(f"Task with id {id_to_be_deleted} not found\n")
            else:
                print("Some arguments are missing, please provide id of the task\n")
        case 'mark-in-progress':
            print("mark-in-progress")
        case 'mark-done':
            print("mark-done")
        case 'list':
            print("list")


    write_file = open(file_name, 'w')
    json.dump(tasks_json, write_file, sort_keys=True, indent=4)

def contains(list, filter):
    for x in list:
        if filter(x):
            return list.index(x)
    return False

if __name__ == "__main__":
    main()
