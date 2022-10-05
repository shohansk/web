import webbrowser
# webbrowser.open('mapit 870 Valencia St, San Francisco, CA 94110')


import webbrowser, sys, pyperclip
if len(sys.argv) > 1:
    # Get address from command line.
    address = ' '.join(sys.argv[1:])
else:
    # Get address from clipboard.
    address = pyperclip.paste()

# webbrowser.open('https://www.google.com/maps/place/' + 'address')
import webbrowser, sys
if len(sys.argv) > 1:
    # Get address from command line.
    address = ' '.join(sys.argv[1:])

import requests
res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
res.raise_for_status()
playFile = open('RomeoAndJuliet.txt', 'wb')
for chunk in res.iter_content(100000):
        playFile.write(chunk)

playFile.close()

# res.status_code == requests.codes.ok
# len(res.text)
# print(res.text[:250])


# import requests
# res = requests.get('https://inventwithpython.com/page_that_does_not_exist')
# try:
#     res.raise_for_status()
# except Exception as exc:
#     print('There was a problem: %s' % (exc))