# Overview
This project is a lightweight network scanning tool built using Python. It takes a CIDR subnet as input, scans for live hosts, and checks for commonly open ports on each reachable device.

The tool produces clean and structured results in JSON format, along with a clear Markdown report that is easy to read and interpret. This makes it useful for basic security assessments, learning network scanning concepts, and showcasing automation skills.
# Features
Subnet scanning using CIDR notation

Detection of live hosts using ICMP (ping)

Scanning of commonly used ports

Output generation in JSON format

Well-structured Markdown security report
# Technologies Used
Python 3

Standard Python libraries:

ipaddress

subprocess

socket

json
# How It Works
The user provides a CIDR subnet as input.

The tool scans the subnet to find reachable (live) hosts.

Common ports are scanned on each detected host.

The final results are saved in:

scan_results.json – for structured data processing

scan_report.md – for easy review and documentation
# Installation
Make sure Python 3 is installed on your system