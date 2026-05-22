import socket


def scan_port(host: str, port: int) -> bool:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Reducimos el tiempo de espera
    sock.settimeout(0.1)

    result = sock.connect_ex((host, port))
    sock.close()

    return result == 0


def puertosAbiertos(host):
    contador = 0

    for puerto in range(1, 1025):
        if scan_port(host, puerto):
            print(f"[+] Puerto {puerto} abierto")
            contador += 1

    print(f"\nPuertos abiertos encontrados: {contador}")


def main():
    host = "127.0.0.1"

    puertosAbiertos(host)


if __name__ == "__main__":
    main()