import socket
import requests
import netifaces

def get_private_ip():
    try:
        host_name = socket.gethostname()
        private_ip = socket.gethostbyname(host_name)
        return private_ip
    except Exception as e:
        return f"Gagal mendapatkan IP privat: {e}"

def get_public_ip():
    try:
        response = requests.get('https://api.ipify.org?format=json', timeout=5)
        return response.json()['ip']
    except Exception as e:
        return f"Gagal mendapatkan IP publik: {e}"

def resolve_hostname(hostname):
    try:
        # Mendapatkan IP dari hostname target
        ip_address = socket.gethostbyname(hostname)
        return ip_address
    except socket.gaierror:
        return "Hostname tidak dapat diresolusi"
    except Exception as e:
        return f"Error: {str(e)}"

def get_network_interfaces():
    try:
        interfaces = netifaces.interfaces()
        interface_details = {}
        
        for interface in interfaces:
            addrs = netifaces.ifaddresses(interface)
            if netifaces.AF_INET in addrs:
                interface_details[interface] = [
                    addr['addr'] for addr in addrs[netifaces.AF_INET]
                ]
        
        return interface_details
    except Exception as e:
        return f"Gagal mendapatkan detail antarmuka jaringan: {e}"

def show_menu():
    print("\n=== IP Checker Menu ===")
    print("1. Cek IP Privat dan Antarmuka Jaringan")
    print("2. Cek IP Publik")
    print("3. Resolve Hostname ke IP")
    print("4. Keluar")
    return input("Pilih menu (1-4): ")

def main():
    while True:
        choice = show_menu()
        
        if choice == '1':
            print("\n=== IP Privat ===")
            print(f"Hostname: {socket.gethostname()}")
            print(f"IP Privat: {get_private_ip()}")
            
            print("\n=== Antarmuka Jaringan ===")
            interfaces = get_network_interfaces()
            if isinstance(interfaces, dict):
                for interface, ips in interfaces.items():
                    print(f"{interface}: {', '.join(ips)}")
            else:
                print(interfaces)
                
        elif choice == '2':
            print("\n=== IP Publik ===")
            print(f"IP Publik: {get_public_ip()}")
            
        elif choice == '3':
            hostname = input("\nMasukkan hostname/domain target (contoh: google.com): ")
            result = resolve_hostname(hostname)
            print(f"Hasil resolusi untuk {hostname}: {result}")
            
        elif choice == '4':
            print("Keluar dari program...")
            break
            
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()
