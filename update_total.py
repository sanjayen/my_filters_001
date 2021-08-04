num = 0
lists = ["porn.txt","antimalware.txt","antitypo.txt","anti-redirectors.txt","anti-cookie+sign up.txt","anti-rickroll-list.txt","annoyances.txt","duckduckgo-clean-up.template","enhanced_protection.txt"]
reviewedlines = {}
for list in lists:
  reviewedlines[list] = []
  lines = open(list).read().split('\n')
  for line in lines:
    if line.startswith("!") != True and line != "" and line != "[Adblock Plus 2.0]" and line not in reviewedlines[list]:
      num += 1
      reviewedlines[list].append(line)
      
allentries = """<svg height="20" width="130" xmlns="http://www.w3.org/2000/svg" version="1.1">
  <text x="0" y="15" fill="red">{} total entries</text>
</svg>"""
totalentries = open("totalentries.svg","w")
totalentries.write(allentries.format(num))
totalentries.close()
