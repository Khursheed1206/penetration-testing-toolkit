# penetration-testing-toolkit

*Objective*

The primary objective of this project is to develop a lightweight Python-based penetration testing toolkit capable of performing various security assessments such as port scanning, SSH brute force attacks, directory brute-forcing, banner grabbing, and WHOIS lookups. This tool is designed for educational and research purposes to simulate real-world ethical hacking techniques.

# Modules Overview

*1. Port Scanner*

Description: Scans a target host for open ports (e.g., 20–1024).

Use: Identifies exposed services on a system.

Libraries: socket, threading

*2. SSH Brute Forcer*

Description: Tries multiple passwords for an SSH login using a wordlist.

Use: Demonstrates brute-force password attacks.

Libraries: paramiko, file reading

Input: Host, Port, Username, Password list

*3. HTTP Directory Bruteforcer*

Description: Attempts to find hidden directories on a web server.

Use: Reveals potential admin panels or entry points.

Libraries: requests

Input: Base URL, Wordlist of common paths

*4. Banner Grabber*

Description: Retrieves and displays server banners.

Use: Gathers information about the server and services.

Libraries: socket, requests

Input: Host and port

*5. WHOIS Lookup*

Description: Fetches domain registration information using WHOIS.

Use: Provides details about the domain owner and expiry.

Libraries: whois

# Process Workflow

-> Start main.py

-> Menu displayed with 5 options.

-> User selects a module (1-5).

-> Each module prompts the user for relevant input.

-> Output is displayed in the terminal.

-> After completion, the menu reappears, allowing repeated use.

-> User can terminate manually.

# Use Cases:

1.Educational Use: Helps students understand core principles of ethical hacking.

2.Network Security Practice: Assists in learning how to detect and mitigate vulnerabilities.

3.Internal Penetration Testing (Lab Use): Can be used in a safe, isolated lab setup.

4.Demonstrations/Projects: Ideal for college projects, presentations, or technical interviews.

# OUTPUT:

![Image](https://github.com/user-attachments/assets/8c76276d-4923-4d70-8933-ebdade3dc684)

# Port Scanner

Host: 127.0.0.1

Open Ports Detected: 80, 135, 443, 445

![Image](https://github.com/user-attachments/assets/f18c52fe-7678-4d28-90a2-21f60c5fd22b)

# SSH Brute Forcer 

Host: 192.168.0.101

Port: 22

Username Prompted: user

![Image](https://github.com/user-attachments/assets/abfaba19-7e61-47ad-ae47-c1161001974b)

# HTTP Directory Bruteforcer

Base URL: http://localhost/dvwa/

Found Path: /setup.php

![Image](https://github.com/user-attachments/assets/98865e7c-67a8-4cb4-b043-9f6b1aa34790)

# Banner Grabber

Host: 127.0.0.1

Port: 80

Banner: HTTP/1.1 302 Found

![Image](https://github.com/user-attachments/assets/dc6a95bb-b88d-4efd-a644-c20f38dc58a2)

![Image](https://github.com/user-attachments/assets/b9cb52d5-2cfa-4cc9-ae07-fe28cde2f90c)

# WHOIS Lookup

Domain: google.com

Output: Full WHOIS information including:

Registrar

Domain creation and expiry dates

Name servers

Status links











