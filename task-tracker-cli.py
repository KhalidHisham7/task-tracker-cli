#!/usr/bin/env python3
import os, json, sys
from datetime import datetime

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
                    'id': tasks_json['tasks'][-1]['id'] + 1,
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
                update_field(tasks_json['tasks'], 'description', sys.argv[3], id_to_be_updated)
            else:
                print("Some arguments are missing, please provide id of the task and new description\n")
        case 'delete':
            if len(sys.argv) > 2:
                id_to_be_deleted = int(sys.argv[2])
                index_to_be_deleted = contains(tasks_json['tasks'], lambda task: task['id'] == id_to_be_deleted)
                if index_to_be_deleted >= 0 and index_to_be_deleted < len(tasks_json['tasks']):
                    tasks_json['tasks'].pop(index_to_be_deleted)
                else:
                    print(f"Task with id {id_to_be_deleted} not found\n")
            else:
                print("Some arguments are missing, please provide id of the task\n")
        case 'mark-in-progress':
            if len(sys.argv) > 2:
                id_to_be_updated = int(sys.argv[2])
                update_field(tasks_json['tasks'], 'status', 'in-progress', id_to_be_updated)
            else:
                print("Some arguments are missing, please provide id of the task\n")
        case 'mark-done':
            if len(sys.argv) > 2:
                id_to_be_updated = int(sys.argv[2])
                update_field(tasks_json['tasks'], 'status', 'done', id_to_be_updated)
            else:
                print("Some arguments are missing, please provide id of the task\n")
        case 'list':
            if len(sys.argv) == 2:
                print(json.dumps(tasks_json['tasks'], indent=4))
            elif len(sys.argv) > 2:
                status = sys.argv[2]
                print(json.dumps(field_filter(tasks_json['tasks'], lambda task: task['status'] == status), indent=4))

    write_file = open(file_name, 'w')
    json.dump(tasks_json, write_file, sort_keys=True, indent=4)

def contains(list, filter):
    for x in list:
        if filter(x):
            return list.index(x)
    return -1

def field_filter(list, filter):
    return_list = []
    for x in list:
        if filter(x):
            return_list.append(x)
    return return_list

def update_field(list, field, value, id_to_be_updated):
    index_to_be_updated = contains(list, lambda task: task['id'] == id_to_be_updated)
    if index_to_be_updated >= 0 and index_to_be_updated < len(list):
        list[index_to_be_updated][field] = value
        list[index_to_be_updated]['updated_at'] = str(datetime.now())
    else:
        print(f"Task with id {id_to_be_updated} not found\n")

if __name__ == "__main__":
    main()
