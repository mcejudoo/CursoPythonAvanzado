import requests

def testHello():
    url = "http://localhost:5000/"
    r = requests.get(url)
    print(r.url)
    print(r.text)

    d = r.json()
    print(d, type(d))

if __name__ == '__main__':
    testHello()

