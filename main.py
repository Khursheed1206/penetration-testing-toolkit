from modules import port_scanner, ssh_brute_forcer, http_dir_brute, banner_grabber, whois_lookup

def main():
    print("""
    ================================
       Penetration Testing Toolkit
    ================================
    1. Port Scanner
    2. SSH Brute Forcer
    3. HTTP Directory Bruteforcer
    4. Banner Grabber
    5. WHOIS Lookup
    """)

    choice = input("Select module [1-5]: ")

    if choice == '1':
        host = input("Enter host (e.g., 127.0.0.1): ")
        open_ports = port_scanner.scan_ports(host, range(20, 1025))
        print("Open Ports:", open_ports)

    elif choice == '2':
        host = input("Enter SSH host: ")
        port = int(input("Enter port (e.g., 22): "))
        username = input("Enter username: ")

        try:
            with open("passwords.txt") as f:
                password_list = [line.strip() for line in f.readlines()]
        except FileNotFoundError:
            print("[!] passwords.txt not found.")
            return

        ssh_brute_forcer.brute_force_ssh(host, port, username, password_list)


    elif choice == '3':
        url = input("Enter base URL (e.g., http://example.com): ")
        try:
            with open("common_dirs.txt") as f:
                wordlist = f.readlines()
            http_dir_brute.brute_force_dirs(url, wordlist)
        except FileNotFoundError:
            print("[!] Error: 'common_dirs.txt' file not found.")

    elif choice == '4':
        host = input("Enter host: ")
        port = int(input("Enter port: "))
        banner = banner_grabber.grab_http_banner(host, port)
        print("Banner:", banner)

    elif choice == '5':
        domain = input("Enter domain (e.g., example.com): ")
        info = whois_lookup.lookup(domain)
        print(info)  # <-- Make sure this is included


    else:
        print("Invalid selection.")

if __name__ == "__main__":
    main()
