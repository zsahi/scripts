import iptools

heystack = input ("Enter IPs/subnets/ranges (HeyStack):")

heystack = heystack.strip()

parts = heystack.split(",")

heystack = []

for part in parts:
    if '-' in part:
        r = part.split('-')
        heystack.append((r[0],r[1]))
    else:
        heystack.append(part)

#keys = input ("Enter IPs/subnets/ranges (Key(s)):")

heystack = iptools.IpRangeList(*[line for line in heystack])




keys = input ("Enter IPs/subnets/ranges (Keys):")

keys = keys.strip()

parts = keys.split(",")

keys = []

for part in parts:
    if '-' in part:
        r = part.split('-')
        keys.append((r[0],r[1]))
       
    else:
        keys.append(part)
        
keys = iptools.IpRangeList(*[line for line in keys])

for key in keys:
    if key not in heystack:
        print(key)


