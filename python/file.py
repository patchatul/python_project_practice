# .txt file .read .write .seek .truncate
greekgods = ['Zeus', 'Poseidon', 'Hera', 'Hades', 'Athena', 'Aphrodite', 'Artemis', 'Apollo']

try:
    file = open('greekgodsfile.txt', 'w')
    for god in greekgods:
        file.write(f'{god}\n')
finally:
    file.close()

with open('greekgodsfile.txt', 'r+') as file:
    print(file.read())
    #file.seek(2) move to 2nd byte
    #file.truncate(20) limit file size 20 bytes