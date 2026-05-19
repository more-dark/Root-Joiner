_S='desktop'
_R='Discord'
_Q='windows'
_P=''
_O=''
_N='properties'
_M='heartbeat_interval'
_L='Channel ID: '
_K='Server ID: '
_J='tokens.txt'
_I="Don't forget to put your tokens in Tokens.txt"
_H='self_deaf'
_G='self_mute'
_F='channel_id'
_E='guild_id'
_D=False
_C=True
_B='op'
_A='d'

from pystyle import *
import os
from colorama import *
import time, asyncio, json, websockets
import random

os.system('clear' if os.name == 'posix' else 'cls')

intro = r'''

                                           ╔═════════════════════════════════════════════════════════════════════╗ 
                                           ║                                                                     ║ 
                                           ║                   ██████╗  ██████╗  ██████╗ ████████╗               ║
                                           ║                   ██╔══██╗██╔═══██╗██╔═══██╗╚══██╔══╝               ║
                                           ║                   ██████╔╝██║   ██║██║   ██║   ██║                  ║
                                           ║                   ██╔══██╗██║   ██║██║   ██║   ██║                  ║
                                           ║                   ██║  ██║╚██████╔╝╚██████╔╝   ██║                  ║
                                           ║                   ╚═╝  ╚═╝ ╚═════╝  ╚═════╝    ╚═╝                  ║
                                           ║                                                                     ║      
                                           ║            ████████╗ ██████╗ ██╗  ██╗ ███████╗███╗   ██╗            ║      
                                           ║            ╚══██╔══╝██╔═══██╗██║██║   ██╔════╝████╗  ██║            ║      
                                           ║               ██║   ██║   ██║███║     █████╗  ██╔██╗ ██║            ║
                                           ║               ██║   ██║   ██║██║██║   ██╔══╝  ██║╚██╗██║            ║       
                                           ║               ██║   ╚██████╔╝██║  ██║ ███████╗██║ ╚████║            ║ 
                                           ║               ╚═╝    ╚═════╝ ╚═╝  ╚═╝ ╚══════╝╚═╝  ╚═══╝            ║      
                                           ║                                                                     ║
                                           ╚═════════════════════════════════════════════════════════════════════╝ 
                                           ╔═════════════════════════════════════════════════════════════════════╗                                                                                                               
                                           ║                      --Made BY ROOT & BLADE--                       ║                                                       
                                           ╚═════════════════════════════════════════════════════════════════════╝                                                                    
                                                                    
                                                              ╔═════════════════════════════════╗
                                                              ║         > Press Enter           ║                                
                                                              ╚═════════════════════════════════╝
''' 

Anime.Fade(Center.Center(intro), Colors.red_to_purple, Colorate.Vertical, interval=.035, enter=_C)

print(fr"""{Fore.LIGHTRED_EX}
                                           ╔═════════════════════════════════════════════════════════════════════╗ 
                                           ║                                                                     ║ 
                                           ║                   ██████╗  ██████╗  ██████╗ ████████╗               ║
                                           ║                   ██╔══██╗██╔═══██╗██╔═══██╗╚══██╔══╝               ║
                                           ║                   ██████╔╝██║   ██║██║   ██║   ██║                  ║
                                           ║                   ██╔══██╗██║   ██║██║   ██║   ██║                  ║
                                           ║                   ██║  ██║╚██████╔╝╚██████╔╝   ██║                  ║
                                           ║                   ╚═╝  ╚═╝ ╚═════╝  ╚═════╝    ╚═╝                  ║
                                           ║                                                                     ║      
                                           ║            ████████╗ ██████╗ ██╗  ██╗ ███████╗███╗   ██╗            ║      
                                           ║            ╚══██╔══╝██╔═══██╗██║██║   ██╔════╝████╗  ██║            ║      
                                           ║               ██║   ██║   ██║███║     █████╗  ██╔██╗ ██║            ║
                                           ║               ██║   ██║   ██║██║██║   ██╔══╝  ██║╚██╗██║            ║       
                                           ║               ██║   ╚██████╔╝██║  ██║ ███████╗██║ ╚████║            ║ 
                                           ║               ╚═╝    ╚═════╝ ╚═╝  ╚═╝ ╚══════╝╚═╝  ╚═══╝            ║      
                                           ║                                                                     ║
                                           ╚═════════════════════════════════════════════════════════════════════╝ 
                 
                                           ╔═════════════════════════════════════════════════════════════════════╗                                                  
                                           ║                                                                     ║
                                           ║                        --Made BY ROOT & BLADE--                     ║
                                           ║                                                                     ║
                                           ║                                                                     ║
                                           ╚═════════════════════════════════════════════════════════════════════╝                                                              
""")
time.sleep(1)

Write.Print('\n╔════════════════════════════════════════╗', Colors.red_to_purple)
Write.Print('\n║     ROOT TOKEN JOINER v1.0             ║', Colors.red_to_purple)
Write.Print('\n╚════════════════════════════════════════╝', Colors.red_to_purple)

Write.Print('\n\n┌────────────────────────────────────────┐', Colors.blue_to_green)
Write.Print('\n│         SELECT AN OPTION               │', Colors.blue_to_green)
Write.Print('\n├────────────────────────────────────────┤', Colors.blue_to_green)
Write.Print('\n│  [1] - Join Voice Channel              │', Colors.green_to_blue)
Write.Print('\n│  [2] - Exit Program                    │', Colors.red_to_purple)
Write.Print('\n└────────────────────────────────────────┘', Colors.blue_to_green)

askim = int(input('\n➜ Choice: '))

# Tokenları toplu işlemek için max bağlantı sayısını sınırla
MAX_WORKERS = 20  # İnterneti korumak için eşzamanlı bağlantı sınırı
RECONNECT_DELAY = 10  # Hata sonrası yeniden bağlanma gecikmesi (saniye)
HEARTBEAT_MULTIPLIER = 1.5  # Heartbeat aralığını artırarak yükü azalt

if askim == 1:
    print(f"\n{Fore.YELLOW}[!] {_I}{Fore.RESET}")
    
    # Tokenları oku
    with open(_J, 'r') as token_file:
        tokens = []
        for t in token_file.readlines():
            token = t.strip()
            if token:
                # Tırnakları temizle (hem tek hem çift tırnak)
                token = token.strip('"').strip("'").strip()
                if token:
                    tokens.append(token)
    
    print(f"{Fore.GREEN}[✓] Loaded {len(tokens)} tokens{Fore.RESET}")
    
    server_id = input(f"{Fore.CYAN}{_K}{Fore.RESET}")
    channel_id = input(f"{Fore.CYAN}{_L}{Fore.RESET}")
    
    print(f"{Fore.YELLOW}[!] Starting token joiners...{Fore.RESET}")

    async def connect(token):
        while _C:
            try:
                async with websockets.connect(
                    'wss://gateway.discord.gg/?v=9&encoding=json',
                    ping_interval=30,
                    ping_timeout=60,
                    max_size=2**20,  # Daha düşük veri boyutu
                    max_queue=16  # Kuyruk boyutunu sınırla
                ) as websocket:
                    hello = await websocket.recv()
                    hello_json = json.loads(hello)
                    heartbeat_interval = hello_json[_A][_M] * HEARTBEAT_MULTIPLIER
                    await websocket.send(json.dumps({
                        _B: 2,
                        _A: {'token': token, _N: {'': _Q, _O: _R, _P: _S}}
                    }))
                    await websocket.send(json.dumps({
                        _B: 4,
                        _A: {_E: server_id, _F: channel_id, _G: _D, _H: _D}  # self_mute ve self_deaf False - açık kalacak
                    }))
                    
                    print(f"{Fore.GREEN}[✓] Token {token[:15]}... connected successfully{Fore.RESET}")

                    while _C:
                        await asyncio.sleep(heartbeat_interval / 1000)
                        try:
                            await websocket.send(json.dumps({
                                _B: 1,
                                _A: random.randint(1, 1000000)
                            }))
                        except Exception:
                            print(f"{Fore.RED}[!] Token {token[:10]}... heartbeat failed, reconnecting.{Fore.RESET}")
                            break
            except Exception as e:
                print(f"{Fore.RED}[!] Token {token[:10]}... connection error: {e}, retrying in {RECONNECT_DELAY}s{Fore.RESET}")
                await asyncio.sleep(RECONNECT_DELAY)

    async def main():
        tasks = []
        for i, token in enumerate(tokens[:MAX_WORKERS]):  # Token sayısını sınırla
            task = asyncio.create_task(connect(token))
            tasks.append(task)
            print(f"{Fore.CYAN}[+] Starting token {i+1}/{min(len(tokens), MAX_WORKERS)}{Fore.RESET}")
            await asyncio.sleep(0.5)  # Rate limit için gecikme
        await asyncio.gather(*tasks, return_exceptions=True)

    asyncio.run(main())

elif askim == 2:
    print(f"\n{Fore.RED}[!] Exiting ROOT TOKEN JOINER...{Fore.RESET}")
    time.sleep(1)
    os.system('clear' if os.name == 'posix' else 'cls')
    print(f"{Fore.GREEN}[✓] Program terminated successfully{Fore.RESET}")
else:
    print(f"\n{Fore.RED}[✗] Invalid option selected. Please run the program again.{Fore.RESET}")
    time.sleep(2)
