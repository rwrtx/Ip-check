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
        public_ip = response.json()['ip']
        return public_ip
    except Exception as e:
        return f"Gagal mendapatkan IP publik: {e}"

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

def main():
    print("=== IP Checker ===")
  
    private_ip = get_private_ip()
    print(f"\nIP Privat (Host): {private_ip}")
    
    interfaces = get_network_interfaces()
    if isinstance(interfaces, dict):
        print("\nDetail Antarmuka Jaringan:")
        for interface, ips in interfaces.items():
            print(f"{interface}: {', '.join(ips)}")
    else:
        print(interfaces)
    
    
    public_ip = get_public_ip()
    print(f"\nIP Publik: {public_ip}")

if __name__ == "__main__":
    main()
