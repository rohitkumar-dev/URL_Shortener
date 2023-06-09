import pyshorteners

def shorten_url(long_url):
    shortener = pyshorteners.Shortener()
    short_url = shortener.tinyurl.short(long_url)
    return short_url

if __name__ == '__main__':
    long_url = input('Enter the URL you want to shorten: ')
    short_url = shorten_url(long_url)
    print(f'Shortened URL: {short_url}')