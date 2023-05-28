from requests import get
import time


infohash = input("Enter infohash or magnet link: ").upper()

if infohash.startswith("MAGNET:?XT=URN:BTIH:"):
    infohash = infohash[20:60]


def itorrent():
    response = get(f"https://itorrents.org/torrent/{infohash}.torrent", allow_redirects=False, headers={"User-Agent": "Mozilla/5.0"})
    if response.status_code == 200:
        return f"https://itorrents.org/torrent/{infohash}.torrent"
    else:
        print(f"iTorrent: Error {response.status_code}")
        return False


def btcache():
    response = get(f"https://btcache.me/torrent/{infohash}", allow_redirects=False, headers={"User-Agent": "Mozilla/5.0"}).text
    if 'Error!' in response:
        print("Btcache: Error")
        return False
    else:
        return f"https://btcache.me/torrent/{infohash}"


def torrage():
    def caesar_shift(text, shift):
        if shift < 0:
            return caesar_shift(text, shift + 26)
        result = ''
        for char in text:
            if char.isalpha():
                if 'A' <= char <= 'Z':
                    char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
                elif 'a' <= char <= 'z':
                    char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            result += char
        return result

    def get_ttl(input_string):
        return caesar_shift(input_string, -12)[::-1]
    encrypted_key = get(f'https://torrage.info/torrent.php?h={infohash}&ttl=' + str(round(time.time())), headers={"User-Agent":"Mozilla/5.0"}).text.replace('getTTL("', '').replace('"\n);', '')
    ttl = get_ttl(encrypted_key)
    response = get(f"https://torrage.info/download.php?h={infohash}&ttl={ttl}", headers={"User-Agent":"Mozilla/5.0"}, allow_redirects=True).text
    if '<' in response:
        print("Torrage: Error")
        return False
    else:
        return f"https://torrage.info/torrent.php?h={infohash}"


modules = ['btcache', 'torrage', 'itorrent']
for module in modules:
    response = eval(module + "()")
    if response:
        print(f"{module}: {response}")
