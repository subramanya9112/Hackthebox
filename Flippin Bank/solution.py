# username: bdmin
# password: g0ld3n_b0y
flag = "99007b9ef78777db419ad2dc83d7fd134b61e3a5472c4b3ecd834a5b8a4e327f3507248924e35394c9a965a76def27e2"
flag = format(ord('a') ^ ord('b') ^ int(flag[:2], 16), 'x') + flag[2:]
print(flag)
