import socket
from xml.etree.ElementTree import Element, SubElement, ElementTree
from datetime import datetime
import threading
import time

# Our super fancy spinner!
def spinner():
    spinner_chars = "|/-\\"
    while True:
        for char in spinner_chars:
            print(f"\rScanning... {char}", end="")
            time.sleep(0.1)

# Function to scan a given range of ports on a host
def scan_ports(host, port_range):
    open_ports = []
    for port in port_range:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((host, port))
        if result == 0:
            open_ports.append(port)
        sock.close()
    return open_ports

# Function to identify service on an open port
def identify_service(port):
    try:
        service = socket.getservbyport(port, 'tcp')
    except:
        service = None
    return service

# Function to save the scan results to an XML file
def save_to_xml(host, port_data):
    date_str = datetime.now().strftime("%m_%d_%Y")  # Getting the current date
    root = Element("host")
    SubElement(root, "hostname").text = host

    for port, service in port_data.items():
        port_element = SubElement(root, "port")
        SubElement(port_element, "port_number").text = str(port)
        SubElement(port_element, "service").text = service if service else "unknown"

    tree = ElementTree(root)
    tree.write(f"scan_results_{date_str}.xml")  # Filename includes the date

# Main function to kick off the scanning
def main():
    host = input("Enter the host to scan (default: 127.0.0.1): ")
    host = host if host else '127.0.0.1'

    start_port = input("Enter the start port for scanning (default: 20): ")
    start_port = int(start_port) if start_port else 20

    end_port = input("Enter the end port for scanning (default: 1024): ")
    end_port = int(end_port) if end_port else 1024

    port_range = range(start_port, end_port + 1)

    # Start the spinner in a separate thread
    spinner_thread = threading.Thread(target=spinner)
    spinner_thread.daemon = True  # This ensures the spinner thread exits when the main program exits
    spinner_thread.start()

    open_ports = scan_ports(host, port_range)

    # Stop the spinner thread by killing the entire program (bit of a hack, but it works for this example)
    print("\rScanning... done!\n")

    port_data = {}
    for port in open_ports:
        service = identify_service(port)
        port_data[port] = service
        print(f"Port {port} is open! Service: {service if service else 'unknown'}")

    save_to_xml(host, port_data)
    date_str = datetime.now().strftime("%m_%d_%Y")
    print(f"Scan results saved to scan_results_{date_str}.xml.")

# Standard Python script entry point
if __name__ == "__main__":
    main()
