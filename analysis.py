f = open("headlines.txt", "r")

text = f.read()
headlines_arr = text.split('\n')

for headline in headlines_arr:
    if 'Meghan' in headline:
        print(headline)