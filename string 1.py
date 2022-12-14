'''
DATE:03TH NOV 2022
DAY: SATURDAY
TOPIC: STRINGS
AUTHOR: RAMA BHARGAVI
'''
b="suresh"
print(b.find('s'))
print(b.find('u'))
print(len(b))
print(b.rfind('h'))
v="rama bhargavi"
print(v.count('a'))
print(v.count('h'))
h="raghu ramlu"
print(h.replace('ramlu','raghu'))
g="core python programing core"
print(g.replace('core',str(2)))
print(g.replace('core','2'))
print(g.replace('o','k',1))
d="         rajani  .        "
print(d.strip())
print(d.lstrip())
print(d.rsplit())
a="hello","world","baru"
print(a  ,type(a))
b ='  rammohan ' .join(a)
print(b)
c="pooja akka"
print(c.removeprefix('p'))
print(c.removeprefix('a'))
print(c.removeprefix('po'))
d="hello python"
print(d.isalnum())
d="hellopython"
print(d.isalnum())
d="hellopython39"
print(d.isalnum())
e="m hajarath"
print(e.isascii())
f="corepython"
print(f.isalpha())
g="python"
print(g.ljust(8),"programming basic")
h="python"
print(h.ljust(10,'r'))