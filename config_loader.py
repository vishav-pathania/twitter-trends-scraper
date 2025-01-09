import json
import os
import requests

def load_config(config_file="config.json"):
    if not os.path.exists(config_file):
        raise FileNotFoundError(f"Configuration file '{config_file}' not found.")
    try:
        with open(config_file, "r") as file:
            return json.load(file)
    except json.JSONDecodeError as e:
        raise ValueError(f"Error parsing JSON in '{config_file}': {e}")

def fetch_proxy_list(proxymesh_url):
    try:
        # a GET request to ProxyMesh to fetch the list of proxies
        response = requests.get(proxymesh_url)
        response.raise_for_status()  # Raise error for bad status codes

        # Parse JSON response
        data = response.json().get("data", [])

        # Extract IP addresses and ports of available proxies
        proxy_list = [
            {"ip": proxy["ip"], "port": proxy["port"]}
            for proxy in data if "ip" in proxy and "port" in proxy
        ]

        if not proxy_list:
            print("No valid proxies found.")
        return proxy_list

    except Exception as e:
        print(f"Failed to fetch proxy list: {e}")
        return []