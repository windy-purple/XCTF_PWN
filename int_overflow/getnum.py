for i in range(1,0x199):
	if (i & 0xf == 4) or (i & 0xf == 5) or (i & 0xf == 6) or (i & 0xf == 7) or (i & 0xf == 8):
		if i > 0xff:
			print("{}    ".format(i),end="")