import os
lines = open("antimalware.txt").read().split("\n")
alt = open("Alternative list formats/antimalware_domains.txt","w")
donedomains = []
for line in lines:
  if line.startswith("||") and "^" in line:
    domain = line.split("$")[0][2:-1]
    if domain not in donedomains:
       alt.write("{}\n".format(domain))
       donedomains.append(domain)
    continue
  if line == '' or line.startswith("!") or line.startswith("||"):
    continue
  if line.split("$")[0] not in donedomains:
    alt.write("{}\n".format(line.split("$")[0]))
    donedomains.append(line.split("$")[0])