message = "ron jhon 123456789123"
message = message.split(' ')
for inf, elem in enumerate(message, 1):
    print(inf, ')', elem[:10])
