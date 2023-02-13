import socket
import requests
import pandas as pd
import os
import hashlib

def subdomain_enum(domain):
    """
    Enumerate subdomains of a given domain
    """
    try:
        subdomains = [subdomain.decode("utf-8").split(",")[0] for subdomain in 
                      socket.getaddrinfo(domain, None, socket.AF_INET)[0][4]]
        return subdomains
    except:
        return []

def subdomain_check(subdomain):
    """
    Check if a subdomain is takeoverable and if bypass is possible via HTTP verb tampering or custom header
    """
    takeover = False
    bypass = False
    try:
        response = requests.get("http://" + subdomain)
        status_code = response.status_code
        if status_code == 404 or status_code == 451:
            takeover = True
        response = requests.post("http://" + subdomain)
        if response.status_code != status_code:
            bypass = True
        response = requests.put("http://" + subdomain)
        if response.status_code != status_code:
            bypass = True
    except:
        pass
    return takeover, bypass

def port_scan(subdomain):
    """
    Scan for open ports on a given subdomain
    """
    open_ports = []
    for port in [80, 443, 22, 21, 20, 23, 25, 53, 69, 123, 161, 162, 389, 443, 636, 993, 995]:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(2)
        result = sock.connect_ex((subdomain, port))
        if result == 0:
            open_ports.append(port)
        sock.close()
    return open_ports

def hash_results(results):
    """
    Hash the results of a scan to easily detect changes between scans
    """
    result_hash = hashlib.sha256()
    for result in results:
        result_hash.update(str(result).encode("utf-8"))
    return result_hash.hexdigest()

def save_results(results, domain):
    """
    Save the results of a scan to a file
    """
    if not os.path.exists(domain):
        os.makedirs(domain)
    df = pd.DataFrame(results, columns=["Subdomain", "Takeover", "Bypass", "Open Ports"])
    df.to_csv(os.path.join(domain, "results.csv"))

def load_results(domain):
    """
    Load the results of a previous scan from a file
    """
    try:
        df = pd.read_csv(os.path.join(domain, "results.csv"))
        results = df.to_dict("records")
        return results
    except FileNotFoundError:
        return None

def run_tool(domain):
    subdomains = subdomain_enum(domain)
    results = []
    for subdomain in subdomains:
        takeover,
bypass = subdomain_check(subdomain)
open_ports = port_scan(subdomain)
results.append([subdomain, takeover, bypass, open_ports])
current_hash = hash_results(results)
previous_results = load_results(domain)
if previous_results is not None:
previous_hash = hash_results(previous_results)
if current_hash != previous_hash:
print("Changes detected between scans.")
save_results(results, domain)

if name == "main":
domain = input("Enter the domain name: ")
run_tool(domain)
