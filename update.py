"""Auto-create the domains versions of porn.txt and antimalware.txt"""
alldomains = {}
allips = {}

def mkalt(file,alt):
  lines = open(file).read().split("\n")
  alt = open("Alternative list formats/{}".format(alt),"w")
  iponly = open("Alternative list formats/{}_ips.txt".format(file.split(".")[0]),"w")
  donedomains = []
  def isipdomain(domain):
    try:
      import socket
      if socket.gethostbyname(domain) == domain:
        return True
    except:
      pass
    return False
  alldomains[file] = []
  allips[file] = []
  for line in lines:
    if len(line.split("$")[0].split(".")) > 2:
      if isipdomain(line.split("$")[0]) == True:
        iponly.write(line.split("$")[0] + "\n")
        try:
          allips[file].append(line.split("$")[0])
        except Exception as err:
          print("Error:{}".format(err))
        continue
    if line == '' or line.startswith("!") or line.startswith("||") or line == '[Adblock Plus 2.0]':
      continue
    if line.split("$")[0] not in donedomains:
      alt.write("{}\n".format(line.split("$")[0].lower()))
      donedomains.append(line.split("$")[0].lower())
      alldomains[file].append(line.split("$")[0].lower())
mkalt("antimalware.txt","antimalware_domains.txt")
mkalt("porn.txt","porn_domains.txt")
mkalt("antitypo.txt","antitypo_domains.txt")

print(allips)
print(alldomains)

def mkhosts(file,altname):
  donedomains = []
  List = open(file).read().split("\n")
  altfile = open(altname,"w")
  def isipdomain(domain):
    try:
      return domain in allips[file]
    except:
      pass
    return False
  for line in List:
    if line.startswith("! Format notes: "):
      altfile.write('# Format notes: This format is designed for a system wide HOSTS file, and can also be used with tools that support this format. Not recommended for uBlock Origin or AdGuard\n')
      continue
    if line.startswith("!"):
      altfile.write(line.replace("!","#"))
    elif line == "" or line.startswith("||") or line.startswith("[Adblock Plus 2.0]"):
      continue
    elif "$" in line:
      domain = line.split("$")[0].lower()
      isip = isipdomain(domain)
      if isip == True:
        altfile.write("#IP address: {}".format(domain))
      if isip == False and domain != "" and domain not in donedomains:
        altfile.write("127.0.0.1 {}".format(domain))
        donedomains.append(domain)
    altfile.write("\n")

mkhosts("antimalware.txt","Alternative list formats/antimalware_hosts.txt")


def mkagh(file,altname):
  donedomains = []
  List = open(file).read().split("\n")
  altfile = open(altname,"w")
  def isipdomain(domain):
    try:
      return domain in allips[file]
    except:
      pass
    return False
  for line in List:
    if line.startswith("! Format notes: "):
      altfile.write('! Format notes: This format is designed for AdGuard Home, and should not be used in AdGuard\n')
      continue
    if line.startswith("!"):
      altfile.write(line)
    elif line == "" or line.startswith("||") or line.startswith("[Adblock Plus 2.0]"):
      continue
    elif "$" in line:
      domain = line.split("$")[0].lower()
      if domain != "" and domain not in donedomains:
        if isipdomain(domain):
          altfile.write("{}".format(domain))
        else:
          altfile.write("||{}^".format(domain))
        donedomains.append(domain)
    altfile.write("\n")

try:
  mkagh("antimalware.txt","Alternative list formats/antimalware_adguard_home.txt")
except:
  print("Error")
def mkabp(file,altname):
  donedomains = []
  List = open(file).read().split("\n")
  altfile = open(altname,"w")
  def isipdomain(domain):
    try:
      return domain in allips[file]
    except:
      pass
    return False
  for line in List:
    if line.startswith("! Format notes: "):
      altfile.write("! Format notes: This format is designed for use in AdBlock Plus. However, I recommend you do not use AdBlock Plus with this list, due to lack of support for full website blocking and some other more advanced features\n")
    if line.startswith("!"):
      altfile.write(line)
      altfile.write("\n")
      continue
    if line.startswith("||"):
      altfile.write(line.split("$")[0])
      altfile.write("\n")
      continue
    if "[Adblock Plus 2.0]" in line:
      altfile.write(line)
      
    if "$" in line:
      domain = line.split("$")[0].lower()
      isip = isipdomain(domain)
      if isip == True:
        altfile.write("||{}^".format(domain))
      if isip == False and domain != "" and domain not in donedomains:
        altfile.write("||{}^".format(domain))
        donedomains.append(domain)
    altfile.write("\n")
                    
                    
try:
                    mkabp("antimalware.txt","Alternative list formats/antimalware_abp.txt")
                    mkabp("porn.txt","Alternative list formats/porn_abp.txt")
except:
                    print("ABP error")
def mkpurehosts(file,altname):
  altfile = open(altname,"w")
  for domain in alldomains[file]:
      altfile.write("127.0.0.1 {}\n".format(domain))

try:
  mkpurehosts("porn.txt","Alternative list formats/porn_pure_hosts.txt")
  mkpurehosts("antimalware.txt","Alternative list formats/antimalware_pure_hosts.txt")
except:
  print("Pure hosts error")

def mkadguard(file,altname):
  donedomains = []
  List = open(file).read().split("\n")
  altfile = open(altname,"w")
  def isipdomain(domain):
    try:
      return domain in allips[file]
    except:
      pass
    return False
  for line in List:
    if line.startswith("! Format notes: "):
      altfile.write("! Format notes: This format is designed for use in AdGuard's desktop app")
    if line.startswith("!"):
      altfile.write(line)
      altfile.write("\n")
      continue
    if line.startswith("||"):
      altfile.write(line.split("$")[0])
      altfile.write("\n")
      continue
    if "[Adblock Plus 2.0]" in line:
      altfile.write(line)
      
    if "$" in line:
      domain = line.split("$")[0].lower()
      isip = isipdomain(domain)
      if isip == True:
        altfile.write("{}$network".format(domain))
      if isip == False and domain != "" and domain not in donedomains:
        altfile.write("||{}^".format(domain))
        donedomains.append(domain)
    altfile.write("\n")

  
try:
  mkadguard("antimalware.txt","Alternative list formats/antimalware_adguard_app.txt")
except:
  print("AdGuard error")
