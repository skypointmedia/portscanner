## Port Scanner

Are you looking to find out which ports are open on a specific host? Look no further! This is a basic but useful Python port scanner to aid you in your cybersecurity journey. It scans a range of ports for a given IP address and identifies potentially open ports and the services running on them. Plus, it outputs the findings to your terminal and saves them in an XML file for further review. 🚀

## Table of Contents
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Disclaimer](#disclaimer)
- [Learn More](#learn-more)

## Features

- **User-Friendly**: Interactive CLI with smart defaults.
- **XML Output**: Saves scan results in an easily parsable XML file.
- **Terminal Output**: Gives immediate feedback on open ports and their associated services.

```python
# Sample code to scan ports
open_ports = scan_ports(host, port_range)
```

## Requirements

- Python 3.x
- `xmltodict` Python package

## Installation

1. Clone this repository:
    ```bash
    git clone https://github.com/your_username/PortScanner.git
    ```
2. Navigate to the directory:
    ```bash
    cd PortScanner
    ```
3. Install the required Python packages:
    ```bash
    pip install -r requirements.txt
    ```
## Usage

1. Run the script:
    ```bash
    python port_scanner.py
    ```
2. Follow the on-screen instructions. If you're unsure, just press enter to use the defaults.

```python
# Main function showcasing user input and scan initiation
def main():
    host = input("Enter the host to scan (default: 127.0.0.1): ")
    ...
    open_ports = scan_ports(host, port_range)
    ...
```

## Disclaimer

Port scanning someone else's network without explicit permission is a quick way to end up in a place with really, *really* bad Wi-Fi (also known as prison). So make sure you have proper authorization before running this script on any network other than your own.

## Learn More

- [Cybersecurity Basics](https://www.cybrary.it/course/intro-cyber-security/)
- [Introduction to Ethical Hacking](https://www.udemy.com/course/learn-ethical-hacking-from-scratch/)
- [Python for Cybersecurity](https://realpython.com/python-cyber-security/)

Feel free to dive deeper into the world of cybersecurity with these resources. Your quest for knowledge is only a click away! 📘
