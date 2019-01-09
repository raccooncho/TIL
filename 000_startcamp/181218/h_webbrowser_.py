import webbrowser

keywords = [
    'cat',
    'raccoon',
    'whale',
    'squirrel'
]

for keyword in keywords:
    url = 'https://www.google.com/search?q=' + keyword
    webbrowser.open_new(url)


