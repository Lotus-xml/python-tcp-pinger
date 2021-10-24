import os
import time
import sys
import argparse
from sys import argv
import socket

###########################
#                         #
#  Made By: @N3m3s1s.ngo  #
#                         #
###########################

if sys.platform == "linux":
    os.system("clear")
elif sys.platform == "win32":
    os.system("cls")

parser = argparse.ArgumentParser()
parser.add_argument("host", nargs="?", help="Host to perform TCP ping on")
parser.add_argument("-p", "--port", default=80, type=int, help="Port of host to perforn TCP ping on")
parser.add_argument("-t", "--timeout", default=5, type=int, help="TCP connection timeout value")

args = parser.parse_args()

print("""\033[0;31m\033[1m\033[5m
 
 ▄▀▀▄ █  ▄▀▀█▄   ▄▀▀▄▀▀▀▄  ▄▀▀▄ ▄▀▄  ▄▀▀█▄  
█  █ ▄▀ ▐ ▄▀ ▀▄ █   █   █ █  █ ▀  █ ▐ ▄▀ ▀▄ 
▐  █▀▄    █▄▄▄█ ▐  █▀▀█▀  ▐  █    █   █▄▄▄█ 
  █   █  ▄▀   █  ▄▀    █    █    █   ▄▀   █ 
▄▀   █  █   ▄▀  █     █   ▄▀   ▄▀   █   ▄▀  


╔══════════════════════════════════════════════════════════════════╗
║                                                                  ║
║    TCP Pinger Made By: https://www.instagram.com/n3m3s1s.ngo/    ║
║    Karma IG: https://www.instagram.com/karma.ngo_/               ║
║                                                                  ║
╚══════════════════════════════════════════════════════════════════╝
""")

if not args.host:
    parser.print_help()
    print("\033[0;35mDomain/IP is required!")
    sys.exit()

host = args.host

port = args.port

timeout = args.timeout

socket.setdefaulttimeout(timeout)

sequence = 1

try:
    ip = socket.gethostbyname(host)
except Exception as e:
    print(f"\033[0;35mFailed to resolve host name: {e}")
    sys.exit()

print(f"\033[1;31mStarting TCP ping to: \033[4m{host}\u001b[0;0m:\033[1m\033[1;31m{port}\u001b[0;0m...")
print(f"")
while True:
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        time1 = time.time()
        sock.connect((ip, port))
        time2 = time.time()
        ping = (time2 - time1) * 1000
        print(f"""
\033[1mHost: \033[0;31m\033[1m\033[5m{ip}
\u001b[0;0m\033[1mPort: \033[0;31m\033[1m\033[5m{port}
\u001b[0;0m\033[1mTime: \033[0;31m\033[1m\033[5m{ping:.2f}ms
\u001b[0;0m\033[1mSequence: \033[0;31m\033[1m\033[5m{sequence}\u001b[0;0m
""")
        sock.close()
        time.sleep(2.5)
    except Exception as e:
        print(f"""
\033[0;31m\033[1m\033[5mError\u001b[0;0m:\033[1m 
Message: \033[0;31m\033[1m\033[5m{e}
\u001b[0;0m\033[1m Sequence: \033[0;31m\033[1m\033[5m{sequence}\u001b[0;0m
""")
        pass
    except KeyboardInterrupt:
        print("""\033[0;34m\033[1m
Stopping Karma TCP Pinger""")
        sys.exit()
    finally:
        sequence += 1
