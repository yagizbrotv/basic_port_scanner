import socket
import sys

def get_service_name(port):
    try:
        service_name = socket.getservbyport(port)
        return service_name
    except (socket.error, OSError):
        return "Unknown Service"

def scan_ports(target, start_port, end_port):
    print(f"Scanning target {target} for open ports...\n")
    count = 0
    try:
        for port in range(start_port, end_port + 1):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((target, port))
            if result == 0:
                count += 1
                service_name = get_service_name(port)
                print(f"Port {port} is open. Service: {service_name}")
            sock.close()
    except KeyboardInterrupt:
        print("\nScan interrupted by user. Exiting...")
        sys.exit(1)
    print(f"There are {count} ports open out of {end_port - start_port + 1} ports")

if __name__ == "__main__":
    # Check if the correct number of command-line arguments is provided
    if len(sys.argv) != 4:
        print("Usage: python script.py <target_ip> <start_port> <end_port>")
        sys.exit(1)

    target_host = sys.argv[1]
    start_port = int(sys.argv[2])
    end_port = int(sys.argv[3])
    
    scan_ports(target_host, start_port, end_port)

