# Solar aur Electric status (True ya False)
solar = True   # Solar available hai
electric = True  # Electric available hai

# Agar dono available hain, toh electric ko on karo aur solar ko off karo
status = (electric == solar)
print(status)
status =(electric>solar)
print(status)
solar = not status
electric = status
print (solar)
print (electric)
