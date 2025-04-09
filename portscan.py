import socket
import threading
from queue import Queue
from tqdm import tqdm
from colorama import init, Fore

# Инициализация цветов
init()
GREEN = Fore.GREEN
RESET = Fore.RESET

# Настройки
target = input("Введите адрес: ")
port_range = "1-1024"
thread_count = 200

# Глобальные переменные
open_ports = []
start_port, end_port = map(int, port_range.split("-"))
total_ports = end_port - start_port + 1
queue = Queue()
progress_lock = threading.Lock()
progress = 0

# Словарь сервисов
common_ports = {
    7: "Echo Protocol",
    20: "FTP Data Transfer",
    21: "FTP Control",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    67: "DHCP Server",
    68: "DHCP Client",
    69: "TFTP",
    80: "HTTP",
    110: "POP3",
    123: "NTP",
    143: "IMAP",
    161: "SNMP",
    194: "IRC",
    389: "LDAP",
    443: "HTTPS",
    465: "SMTPS",
    514: "Syslog",
    587: "SMTP Submission",
    631: "IPP Printing",
    636: "LDAPS",
    873: "rsync",
    990: "FTPS",
    993: "IMAPS",
    995: "POP3S",

    # Базы данных
    1433: "MS SQL Server",
    1521: "Oracle DB",
    2433: "MS SQL Monitor",
    3306: "MySQL",
    3389: "MS RDP",
    5432: "PostgreSQL",
    6379: "Redis",
    27017: "MongoDB",

    # Игровые сервисы
    25565: "Minecraft",
    27015: "Steam/HLDS",
    27960: "Quake Live",
    28960: "Call of Duty",

    # Мультимедиа
    554: "RTSP",
    1935: "RTMP",
    8000: "Streaming",
    8080: "HTTP Alt",
    32400: "Plex Media Server",

    # Безопасность
    500: "IPSec",
    989: "FTPS Data",
    992: "Telnet over SSL",
    1194: "OpenVPN",
    1723: "PPTP",
    1812: "RADIUS",
    3389: "RDP",

    # P2P и распределенные системы
    6881: "BitTorrent",
    9091: "Transmission",

    # Системные сервисы
    4505: "SaltStack Pub",
    4506: "SaltStack Ret",
    5985: "WinRM HTTP",
    5986: "WinRM HTTPS",

    # VoIP и видеоконференции
    5060: "SIP",
    5061: "SIP-TLS",
    5222: "XMPP/Jabber",
    5269: "XMPP Server",
    5349: "STUN/TURN",
    6000: "X11",

    # IoT и умные устройства
    1883: "MQTT",
    5683: "CoAP",
    8883: "MQTT over SSL",

    # Дополнительные сервисы
    2082: "cPanel",
    2083: "cPanel SSL",
    2222: "DirectAdmin",
    2375: "Docker",
    2483: "Oracle DB SSL",
    3128: "Squid Proxy",
    4440: "Phusion Passenger",
    4848: "GlassFish",
    5000: "UPnP",
    5433: "PgBouncer",
    5900: "VNC",
    5938: "TeamViewer",
    6667: "IRC",
    8008: "IBM HTTP",
    8443: "HTTPS Alt",
    9000: "PHP-FPM",
    9042: "Cassandra",
    9200: "Elasticsearch",
    11211: "Memcached",
    27015: "Source Engine",
    47808: "BACnet",

    # Дополнения
    521: "RIPng",
    1080: "SOCKS Proxy",
    1194: "OpenVPN",
    1337: "Hacker Culture",
    2049: "NFS",
    2086: "WHM",
    2087: "WHM SSL",
    3000: "Node.js",
    3260: "iSCSI",
    4040: "Yarn",
    4500: "IPSec NAT",
    4662: "eMule",
    4711: "OpenTTD",
    5050: "YARN",
    5060: "SIP",
    5431: "Postgres SSL",
    5601: "Kibana",
    5672: "AMQP",
    6379: "Redis",
    6881: "BitTorrent",
    6969: "BitTorrent Tracker",
    8086: "InfluxDB",
    8096: "Jellyfin",
    8125: "StatsD",
    8200: "Portainer",
    8333: "Bitcoin",
    8444: "Vivaldi",
    8888: "Jupyter",
    9001: "Tor",
    9090: "Prometheus",
    9092: "Apache Kafka",
    9100: "Printer",
    9200: "Elasticsearch",
    9300: "Elasticsearch",
    9418: "Git",
    9999: "JDebug",
    10000: "Webmin",
    11214: "Memcached SSL",
    15672: "RabbitMQ",
    25575: "Minecraft RCON",
    27018: "MongoDB Shard",
    28015: "Rust",
    32469: "Plex DLNA",
    47808: "BACnet",
    49152: "Windows RPC"
}

def get_service_name(port):
    try:
        return socket.getservbyport(port, 'tcp')
    except:
        return common_ports.get(port, "Unknown")

def update_progress():
    global progress
    with progress_lock:
        progress += 1
        pbar.update(1)

def port_scan(port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)
            if s.connect_ex((target, port)) == 0:
                service = get_service_name(port)
                open_ports.append((port, service))
    finally:
        update_progress()

def worker():
    while not queue.empty():
        port = queue.get()
        port_scan(port)
        queue.task_done()

if __name__ == "__main__":
    # Заполнение очереди
    for port in range(start_port, end_port + 1):
        queue.put(port)

    # Прогресс-бар
    with tqdm(total=total_ports, desc="Scanning ports", unit="port") as pbar:
        # Запуск потоков
        threads = []
        for _ in range(thread_count):
            thread = threading.Thread(target=worker)
            thread.start()
            threads.append(thread)

        # Ожидание завершения
        queue.join()
        for thread in threads:
            thread.join()

    # Вывод результатов
    print(f"\n{GREEN}Scan results for {target}:{RESET}")
    if open_ports:
        print(f"\n{'Port':<8} {'Service':<25}")
        print("-" * 25)
        for port, service in sorted(open_ports):
            print(f"{port:<8} {service:<25}")
    else:
        print("\nNo open ports found.")
