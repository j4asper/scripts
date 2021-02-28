import requests

url = input("Input URL to check: ")
print()
print("URL redirecting to:")
print()

if not url.startswith("https://" or "http://"):
    url = "https://" + url

try:
    r = requests.get(url)
except:
    print("Invalid URL")

for redirect in r.history:
    print(redirect.url)

print()
print("Done.")
