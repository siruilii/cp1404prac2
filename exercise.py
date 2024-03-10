
query_string = "?name=Bob&age=99&day=Wed"
pairs = query_string[1:].split('&')

value = []
for pair in pairs:
    txt1, txt2 = pair.split('=')
    value.append((txt1,txt2))

print(value)