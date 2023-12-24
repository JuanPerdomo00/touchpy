# Touchpy
tuchpy came about after the need and constant repetition of adding headers in Python code such as binary path and encoding, sometimes even license to use the code. 
That's why touchpy was born, it is expected to add support for other files, for now it only works with files with a .py extension


## Usage

### Getting Started

1. Clone the repository.
2. Navigate to the directory containing the script.

## Install

```bash
sudo install
```

### Command-Line Arguments

The script accepts the following command-line arguments:

- `-f`, `--file`: Specifies the name of the Python file to create.
- `-a`, `--author`: Specifies the author of the Python file (default is 'Anonymous').
- `-l`, `--license`: Specifies the license type for the Python file (e.g., 'gplv3', 'mit', 'apache2').
- `-v`, `--version`: Displays version information.
- `-pl`, `--printlicenses`: Displays a list of available licenses.

### Examples

- Create a Python file named `example.py` with the MIT license and author "John Doe":
```bash
python touchpy.py -f example.py -a "jakepy" -l gplv3

# Display the available licenses:

python touchpy.py -pl

# Display version information:

python touchpy.py -v
```                

### Video Example 
[![asciicast](https://asciinema.org/a/628537.svg)](https://asciinema.org/a/628537)

### License Information

The script supports multiple licenses, including:

- GNU General Public License v3
- MIT License
- Apache License 2.0
- BSD License
- Mozilla Public License 2.0
- ISC License


### Contributing

Contributions are welcome! To contribute to the project, please follow these steps:

- Fork the repository.
- Create a new branch (git checkout -b feature-branch).
- Make your changes.
- Commit your changes (git commit -am 'Add new feature').
- Push to the branch (git push origin feature-branch).
- Create a new Pull Request.


### License
This project is licensed under the GPLv3  - see the LICENSE file for details.
