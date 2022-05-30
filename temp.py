# use python3 ya bro
# Liat apa anjing >:(
try:
	import requests as r, random, json, os
	from time import sleep
except ModuleNotFoundError:
	exit("[!] Module not installed")

list_mail = ["vintomaper.com","tovinit.com","mentonit.net"]
url = "https://cryptogmail.com/"
num = 0

def get_teks(accept, key):
	cek = r.get(url+"api/emails/"+key, headers={"accept": accept}).text
	if "error" in cek:
		return "-"
	else:
		return cek.strip()

def get_random(digit):
	lis = list("abcdefghijklmnopqrstuvwxyz0123456789")
	dig = [random.choice(lis) for _ in range(digit)]
	return "".join(dig), random.choice(list_mail)

def animate(teks):
	lis = list("\|/-")
	for cy in lis:
		print("\r["+cy+"] "+str(teks)+".. ", end="")
		sleep(0.5)

def run(email):
	while True:
		try:
			animate("Waiting for incoming message")
			raun = r.get(url+"api/emails?inbox="+email).text
			if "404" in raun:
				continue
			elif "data" in raun:
				z = json.loads(raun)
				for data in z["data"]:
					print("\r[•] ID: "+data["id"], end="\n")
					got = json.loads(r.get(url+"api/emails/"+data["id"]).text)
					pengirim = got["data"]["sender"]["display_name"]
					email_pe = got["data"]["sender"]["email"]
					subject  = got["data"]["subject"]
					print("\r[•] Sender Name: "+pengirim, end="\n")
					print("\r[•] Sender mail: "+email_pe, end="\n")
					print("\r[•] Subject    : "+subject, end="\n")
					print("\r[•] Message    : "+get_teks("text/html,text/plain",data["id"]), end="\n")
					atc = got["data"]["attachments"]
					if atc == []:
						print("\r[•] attachments: -", end="\n")
					else:
						print("[•] attachments: ")
						for atch in atc:
							id = atch["id"]
							name = atch["file_name"]
							name = name.split(".")[-1]
							svee = r.get("https://cryptogmail.com/api/emails/"+data["id"]+"/attachments/"+id)
							open(id+"."+name, "wb").write(svee.content)
							print("      ~ "+id+"."+name)
					print("-"*45)
					r.delete(url+"api/emails/"+data["id"])
				continue
			else:
				continue
		except (KeyboardInterrupt,EOFError):
				exit("\n[✓] Program finished, exiting...\n")

def cek_update(version):
	check = r.get("https://raw.githubusercontent.com/hekelpro/temp-mail/main/__version__").text.strip()
	if float(version) < float(check):
		print("[✓] Update found ..\n")
		os.system("git pull")
		main()
	else:
		print("[×] Update not found, back menu")
		sleep(2)
		main()

def main():
	os.system('clear')
	global num
	print("""
                                                                                                  
.-----.                          .-..-.        _ .-.    
`-. .-'                          : `' :       :_;: :    
  : : .--. ,-.,-.,-..---.  _____ : .. : .--.  .-.: :    
  : :' '_.': ,. ,. :: .; `:_____:: :; :' .; ; : :: :_   
  :_;`.__.':_;:_;:_;: ._.'       :_;:_;`.__,_;:_;`.__;  
                    : :                                 
                    :_;                                 
                    
    * Author: Zihad Vau 
    * Github: https://github.com/ZihadVau99
    * Team  : 🥀it’s Mafia boy🥀

[01] SET EMAIL RANDOM
[02] SET EMAIL CUSTOM
[03] CEK UPDATE
[00] EXIT
""")

	pil = input("[?] Choose: ")
	while pil == "" or not pil.isdigit():
		pil = input("[?] Choose: ")
	if pil in ["01","1"]:
		set_name, set_email = get_random(10)
		print("\n[*] Your email: "+set_name+"@"+set_email)
		print("[*] CTRL+ C to stopped..")
		print("-"*45)
		run(set_name+"@"+set_email)
	elif pil in ["02","2"]:
		set_name = input("[•] Set mail name: ")
		print()
		for cy in list_mail:
			num += 1
			print(" "*5,"["+str(num)+"] @"+cy)
		print()
		set_email = input("[?] Select: ")
		while set_email == "" or not set_email.isdigit() or int(set_email) > len(list_mail):
			set_email = input("[?] Select: ")
		mail = list_mail[int(set_email)-1]
		print("\n[*] Your email: "+set_name+"@"+mail)
		print("[*] CTRL+ C to stopped..")
		print("-"*45)
		run(set_name+"@"+mail)
	elif pil in ["03","3"]:
		try:
			versi = open("__version__","r").read().strip()
		except:
			print("[!] No further updates..")
			sleep(2)
			main()
		print("[!] Please wait, check update")
		cek_update(versi)
	elif pil in ["00","0"]:
		exit("[=] Exit program, enjoyy\n")
	else:
		exit("[-] Menu not found, exit..\n")


if __name__ == "__main__":
	main()
