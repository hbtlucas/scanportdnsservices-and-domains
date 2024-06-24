import requests
def system_http():
    with open('dados.txt', 'r') as system:
        for line in system:
            sub = line.split()[0]
            try:
                res = requests.get('http://' +sub+ '')
                if res.status_code == 200:
                    print('http://'+sub+'')
                    with open('urls.txt', 'a') as file:
                        file.write('http://'+sub+'\n')
            except:
                pass
def system_https():
    with open('dados.txt', 'r') as system:
        for line in system:
            sub = line.split()[0]
            try:
                res = requests.get('https://' +sub+ '')
                if res.status_code == 200:
                    print('https://'+sub+'')
                    with open('urls.txt', 'w') as file:
                        file.write('https://'+sub+'\n')
            except:
                pass

def main():
    system_http()
    system_https()

if __name__ == '__main__':
    main()