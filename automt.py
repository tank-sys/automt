import os,sys,socket
import paramiko
import subprocess
from datetime import datetime

#perintah mikrotiknya
perintah = """
/ system identity pr
/ ip addr pr
/ ip route pr
/ ip firewall nat pr

"""
uport = "22"
uname = "admin"
upass = ""
fld = "semuaip"

isilog = ""
os.system("color")
def helppage():
    print(color.BOLD+"Penggunaan :")
    print(" "+color.BOLD+"python automt.py")
    print(" Default. Alamat ip akan membaca seluruh alamat yang ada di file semuaip.")
    print(" "+color.BOLD+"python automt.py withlog")
    print(" Membuat file log : python automt.py ")
    print(" "+color.BOLD+"python automt.py ip {ipaddress}")
    print(" Menjalankan perintah pada satu host (ipaddress)")

def main():
    print("-----------------TuNK-----------------")
    print("---------Internal Usage Only----------")

    checkdir()
    Y = str(datetime.now().strftime("%Y"))
    M = str(datetime.now().strftime("%b"))
    D = str(datetime.now().strftime("%d"))
    h = str(datetime.now().strftime("%H"))
    s = str(datetime.now().strftime("%S"))
    m = str(datetime.now().strftime("%M"))
    filename =  Y + "-" + M + "-" +D +"-" + h + ":"+ m + ":" + s +".log"
    if len(sys.argv)==2:
        if sys.argv[1] == ("withlog"):
            os.system("python "+sys.argv[0]+ " > log/"+filename )
            print("Saved Log log/"+filename)
        elif sys.argv[1] == ("-h"):
            helppage()
        else:
            print(color.RED+"error : withlog atau ip {ipaddress}")
    elif len(sys.argv)==3:
        if sys.argv[1] == ("ip"):
            verifdevice(sys.argv[2])
        else:
            print(color.RED+"cara : python automt.py ip {ipaddress}")
    elif len(sys.argv)==1:
        md()
    else:
        print(color.RED+"error gak jelas : coba dibaca hasilnya python automt.py -h ")

def md():
    if os.path.exists(fld):
#        print("Checking file "+fld)
        od = open(fld, "r")
        ad = od.readlines()
        td = len(ad)
        i = 0
#        print("Checking list IP ... ")
        for device in ad:
            i = i+1
            dd = device.split("|")
            ldc = len(dd)
            print("+----------------------------------+")
            print("+ "+color.BOLD+str(i)+". IP Device : "+color.CYAN+dd[0])
            if ldc != 1:
                print("## Coba dibaca lagi formatnya dari semuaip!")
            else:
                verifdevice(dd[0].strip())

def checkdir():
    if not os.path.exists("log"):
        os.makedirs("log")

def verifdevice(ipaddr):
    try:
#        print("## Ping device....")
#        subprocess.check_output(['ping', '-c', '2', '-W', '1', ipaddr],stderr=subprocess.STDOUT,universal_newlines=True)
#        print(color.BLUE+"## Device UP. Njajal connect ke device.....")
        eksekusi(ipaddr, uport, uname, upass)
    except:
        print(color.RED+"## Device Down. Lewatin aja.....")

def eksekusi(ipaddr, uport, uname, upass):
    cssh = paramiko.SSHClient()
    cssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        cssh.connect(ipaddr, uport, uname, upass)
        print(color.GREEN+"Success connect ke device.")
        print(color.RED+"Hasilnya :" + color.END)
        stdin, stdout, stderr = cssh.exec_command(format(perintah))
        hsl = (stdout.read())
        print(hsl.decode('utf8'))
    except:
        print(color.RED+"Gagal connect ke device. Lewatin.....")
        pass

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

main()