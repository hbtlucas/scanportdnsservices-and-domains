import socket

portas = [
    21, 22, 23, 25, 53, 80, 110, 111, 135, 139,
    143, 161, 194, 389, 443, 445, 514, 515, 587, 631,
    636,666, 993, 995, 1080, 1433, 1521, 2049, 3306, 3389,
    5432,5900, 6660, 8000, 8080, 8443, 8888, 9100, 9418, 9999,
    10000, 11211, 27017, 28015, 3306, 3389, 5432, 5900, 6660, 8000,
    80808333, 8880, 9000, 9042, 9200, 9300, 9418, 11211, 27017,
    33060, 50070, 54321, 5984, 6379, 6666, 8008, 8081, 8333, 8880,
    9000, 9042, 9160, 10000, 11211, 27017, 28015, 33060, 50070, 54321,
    5601, 6379, 7077, 9042, 9160, 10000, 11211, 27017, 28015, 33060,
    50070, 54321, 5672, 6379, 9042, 9160, 10250,10255, 2375, 3198,
    3306050070, 54321, 5672, 6379, 8080, 8123, 9042, 9160
    ]

def scan_ports(ip):
    for porta in portas:
        try:
            scan = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            scan.settimeout(1)
            resultado = scan.connect_ex((ip,porta))

            if resultado == 0:
                serviço = scan.recv(1024).decode('utf-8')
                print(f"IP: {ip}")
                print(f"Porta: {porta}")
                print(f"Serviço: {serviço}")
                scan.close()

                with open('serviços.txt', 'a') as serviços:
                    serviços.write(f"IP: {ip}\n")
                    serviços.write(f"PORTA: {porta}\n")
                    serviços.write(f"SERVIÇO: {serviços}\n")
                    serviços.write("\n")
                    
        except:
            pass
def parse():
    with open("dados.txt", "r") as dados:
        for linha in dados:
                ip = linha.split()[1]
                scan_ports(ip)
def main():
    parse()

if __name__ == "__main__":
    main()