file_name = 'test_img_ids.json'
with open(file_name, "r") as f:
    lines = []
    for l in f:
        lines.append(l)

with open(file_name, "w") as f:
    f.write('{\n\"images\":\n')
    for line in lines:
        f.write(line)
    f.write(', \n')

    f.write('\"categories\": \n')
    f.write('[\n')
    f.write('{\"id\": 1, \"name\": 1}\n')
    f.write(']\n}')