
<!-- ABOUT THE PROJECT -->
## About The Project
I just started looking into ideas for personal projects to keep my skills sharpened, and I stumbled upon roadmap.sh projects list for BE engineers, I thought I should start looking into these projects as they cover a majority of really interesting topics.
This particular project is a task tracker CLI that users can use to keep track of the tasks they had, list these tasks, add new ones and update/delete already existing tasks, all through the CLI without much prerequisites.


### Built With

* [![Python][Python.com]][Python-url]


<!-- GETTING STARTED -->
## Getting Started

In the following sections I'll be outlining how to run this script locally.

### Prerequisites

This is an example of how to list things you need to use the software and how to install them.
* python3
  it can be installed through the official website https://www.python.org/downloads/macos/

### Installation

1. Clone the repo
  through ssh
   ```sh
   git clone git@github.com:KhalidHisham7/task-tracker-cli.git
   ```
   or through https
   ```sh
   git clone https://github.com/KhalidHisham7/task-tracker-cli.git
   ```
3. The script then needs to be made as an executable
   ```sh
   chmod +x task-tracker-cli.py
   ```

<!-- USAGE EXAMPLES -->
## Usage
```sh
# Adding a new task
task-cli add "Buy groceries"
# Output: Task added successfully (ID: 1)

# Updating and deleting tasks
task-cli update 1 "Buy groceries and cook dinner"
task-cli delete 1

# Marking a task as in progress or done
task-cli mark-in-progress 1
task-cli mark-done 1

# Listing all tasks
task-cli list

# Listing tasks by status
task-cli list done
task-cli list todo
task-cli list in-progress
```

<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<!-- MARKDOWN LINKS & IMAGES -->
[Python-url]: https://www.python.org/
[Python.com]: https://www.python.org/static/img/python-logo.png
