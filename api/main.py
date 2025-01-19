import socket
import sys

# SOCK_STREAM = TCP
# SOCK_DGRAM = UDP

def port_scan_tcp(host, ports):
    try:
        host = socket.gethostbyname(host)
        for port in ports:
            # Scan de todas as portas
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((host, port))
            print(f"Resultado da conexão com o {host}: {result}")

            if result == 0:
                print(f"Porta {port} está liberada")
            else:
                print(f"Porta {port} está bloqueada")
            sock.close()
    except InterruptedError:
        print("Interrupted")
        sys.exit()
    except TimeoutError:
        print("Timeout")
        sys.exit()
    except socket.error:
        print("Server not responding!")
        sys.exit()


