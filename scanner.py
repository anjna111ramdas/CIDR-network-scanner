import ipaddress
import subprocess
import socket
import json


# Check if a device is reachable (ping)
def is_host_alive(ip):
    try:
        result = subprocess.run(
            ["ping", "-c", "1", ip],
            stdout=subprocess.DEVNULL
        )
        return result.returncode == 0
    except Exception:
        return False


# Scan common ports on a live host
def scan_open_ports(ip):
    open_ports = []
    common_ports = [22, 80, 443, 21, 25, 3306, 8080]

    for port in common_ports:
        try:
            sock = socket.socket()
            sock.settimeout(1)
            sock.connect((ip, port))
            open_ports.append(port)
            sock.close()
        except:
            continue

    return open_ports


# ---------------- MAIN PROGRAM ---------------- #

print("\nSimple Network Scanner - Security Assessment Tool\n")

subnet = input("Enter CIDR subnet ").strip()

network = ipaddress.ip_network(subnet, strict=False)
scan_results = {}

print("\nScanning subnet... Please wait.\n")

for ip in network.hosts():
    ip = str(ip)

    if is_host_alive(ip):
        print(f"[+] {ip} is reachable")
        ports = scan_open_ports(ip)
        scan_results[ip] = ports
    else:
        print(f"[-] {ip} is not reachable")


# Save results in JSON format
with open("scan_results.json", "w") as json_file:
    json.dump(scan_results, json_file, indent=4)


# Generate Markdown report
with open("scan_report.md", "w") as report:
    report.write("# Network Security Scan Report\n\n")
    report.write(f"**Scanned Subnet:** `{subnet}`\n\n")

    if scan_results:
        report.write("## Live Hosts & Open Ports\n\n")
        for ip, ports in scan_results.items():
            if ports:
                report.write(f"- **{ip}** → Open Ports: {ports}\n")
            else:
                report.write(f"- **{ip}** → No common ports open\n")
    else:
        report.write("No live hosts detected.\n")


print("\nScan completed successfully.")
print("Results saved as: scan_results.json and scan_report.md\n")
