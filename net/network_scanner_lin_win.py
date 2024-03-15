import platform
import socket
import subprocess

import scapy.all as sc

# https://codeby.net/threads/skaner-lokalnoj-seti-dlja-poluchenija-spiska-ip-i-mac-adresov-na-python.79876/

# получаем локальный IP-адрес
def local_ipv4():
    st = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        st.connect(('10.255.255.255', 1))
        ip_l = st.getsockname()[0]
    except Exception:
        ip_l = '127.0.0.1'
    finally:
        st.close()
    return ip_l


def get_gateway_win():
    # получаем адрес шлюза по умолчанию для текущего сетевого интерфейса
    com = f'route PRINT 0* | findstr {local_ipv4()}'.split()
    return subprocess.check_output(com, shell=True).decode('cp866').split()[2]


# получение ip адреса шлюза используемого по умолчанию
def get_gateway_linx():
    com = 'route -n'.split()
    return str(subprocess.check_output(com, shell=True)).split("\\n")[2].split()[1].strip()


# сканируем сеть, получаем ip и mac сетевых машин
def get_ip_mac_nework(ip):
    answered_list = sc.srp(sc.Ether(dst='ff:ff:ff:ff:ff:ff') / sc.ARP(pdst=ip), timeout=1, verbose=False)[0]
    clients_list = []
    for element in answered_list:
        clients_list.append({'ip': element[1].psrc, 'mac': element[1].hwsrc})
    return clients_list


# функция печати сканированных ip и mac
def print_ip_mac(mac_ip_list):
    print(f"\nMachine in Network:\n\nIP\t\t\t\t\tMAC-address\n{'-' * 41}")
    for client in mac_ip_list:
        print(f'{client["ip"]}\t\t{client["mac"]}')


def main():
    local_ip = local_ipv4()
    if platform.system() == "Windows":
        gateway = get_gateway_win()
    elif platform.system() == 'Linux':
        gateway = get_gateway_linx()
    ip_mac_network = get_ip_mac_nework(f'{local_ip.split(".")[0]}.{local_ip.split(".")[1]}.{local_ip.split(".")[2]}.1/24')
    print(f'\n[+] Local IP: {local_ip}\n[+] Local Gateway: {gateway}')
    print_ip_mac(ip_mac_network)


if __name__ == "__main__":
    main()
