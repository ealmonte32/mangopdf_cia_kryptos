coded = "pbatenghyngvbaf, lbh fbyirq zl yhvtv chmmyr. @ zr ba gjvggre jvgu lbhe snibhevgr qrffreg gb trg lbhe erjneq. Vg'f yvxr, abg n irel tbbq erjneq fb hu"

#coded = "EMUFPHZLRFAXYUSDJKZLDKRNSHGNFIVJ YQTQUXQBQVYUVLLTREVJYQTMKYRDMFD VFPJUDEEHZWETZYVGWHKKQETGFQJNCE GGWHKK?DQMCPFQZDQMMIAGPFXHQRLG TIMVMZJANQLVKQEDAGDVFRPJUNGEUNA QZGZLECGYUXUEENJTBJLBQCRTBJDFHRR YIZETKZEMVDUFKSJHKFWHKUWQLSZFTI HHDDDUVH?DWKBFUFPWNTDFIYCUQZERE EVLDKFEZMOQQJLTTUGSYQPFEUNLAVIDX FLGGTEZ?FKZBSFDQVGOGIPUFXHHDRKF FHQNTGPUAECNUVPDJMQCLQUMUNEDFQ ELZZVRRGKFFVOEEXBDMVPNFQXEZLGRE DNQFMPNZGLFLPMRJQYALMGNUVPDXVKP DQUMEBEDMHDAFMJGZNUPLGEWJLLAETG"

base = ord("a")
upper = ord("A")
for i in range(1, 26):
    out = ""
    for char in coded:
        # only transpose alphanumeric characters
        # ascii lower case is 97 to 122
	# ascii upper case is 65 to 90
	if 97 <= ord(char) <= 122: #if lower case
            out += chr(base + (ord(char) + i - base) % 26)
	elif 65 <= ord(char) <=  90: #if upper case
	    out += chr(upper + (ord(char) + i - upper) % 26)
        else: #if there is a space then just print it
            out += char
    print(i, out)
