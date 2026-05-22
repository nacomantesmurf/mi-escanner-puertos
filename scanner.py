import socket


def scan_port(host: str, port: int) -> bool:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1.0)
    result = sock.connect_ex((host, port))
    sock.close()
    return result == 0


def main():
    host = "127.0.0.1"
    port = 80
    if scan_port(host, port):
        print(f"[+] Puerto {port} abierto en {host}")
    else:
        print(f"[-] Puerto {port} cerrado en {host}")


if __name__ == "__main__":
    main()
