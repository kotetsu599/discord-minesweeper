import random
import requests
import time
channel_id = input("チャンネルid:")
token = input("トークン:")
#amount_of_bombs = input("爆弾の数:")
while True:
    amount_of_bombs = random.randint(0,20)
    count = int(amount_of_bombs)
    masu = {i:0 for i in range(25)}# 5*5 0~24
    bombs = []
    for _ in range(count):
        pos = random.randint(0,24)
        if pos not in bombs:
            bombs.append(pos)
        else:
            count-=1

    for pos in bombs:
        masu[pos]= "爆"
    for mas in masu:

        if mas not in bombs:
            masu[mas] = 0

            if mas in [0,1,2,3,4,9,14,19,24,23,22,21,20,5,10,15]:
                if mas == 0:
                    for _ in range(3):
                        if _ == 0:
                            check_pos = mas+1
                            if masu[check_pos]=="爆":
                                masu[mas]+=1
                        elif _ == 1:
                            check_pos = mas+6
                            if masu[check_pos]=="爆":
                                masu[mas]+=1

                        elif _ == 2:
                            check_pos = mas+5
                            if masu[check_pos]=="爆":
                                masu[mas]+=1
                
                elif mas == 4:
                    for _ in range(3):
                        if _ == 0:
                            check_pos = mas-1
                            if masu[check_pos]=="爆":
                                masu[mas]+=1
                        elif _ == 1:
                            check_pos = mas+4
                            if masu[check_pos]=="爆":
                                masu[mas]+=1

                        elif _ == 2:
                            check_pos = mas+5
                            if masu[check_pos]=="爆":
                                masu[mas]+=1

                elif mas == 20:
                    for _ in range(3):
                        if _ == 0:
                            check_pos = mas+1
                            if masu[check_pos]=="爆":
                                masu[mas]+=1
                        elif _ == 1:
                            check_pos = mas-4
                            if masu[check_pos]=="爆":
                                masu[mas]+=1

                        elif _ == 2:
                            check_pos = mas-5
                            if masu[check_pos]=="爆":
                                masu[mas]+=1
                
                elif mas == 24:
                    for _ in range(3):
                        if _ == 0:
                            check_pos = mas-1
                            if masu[check_pos]=="爆":
                                masu[mas]+=1
                        elif _ == 1:
                            check_pos = mas-6
                            if masu[check_pos]=="爆":
                                masu[mas]+=1

                        elif _ == 2:
                            check_pos = mas-5
                            if masu[check_pos]=="爆":
                                masu[mas]+=1
                
                #計算で求まる場合...
                elif mas in [1,2,3]: #list1
                    masu[mas]=0
                    for _ in range(5):
                        if _ == 0:
                            check_pos = mas-1
                            if masu[check_pos]=="爆":
                                masu[mas]+=1
                        elif _ == 1:
                            check_pos = mas+1
                            if masu[check_pos]=="爆":
                                masu[mas]+=1
                        elif _ == 2:
                            check_pos = mas+4
                            if masu[check_pos]=="爆":
                                masu[mas]+=1
                        elif _ == 3:
                            check_pos = mas+5
                            if masu[check_pos]=="爆":
                                masu[mas]+=1
                        elif _ == 4:
                            check_pos = mas+6
                            if masu[check_pos]=="爆":
                                masu[mas]+=1

                elif mas in [9,14,19]: #list2
                    for _ in range(5):
                        if _ == 0:
                            check_pos = mas-5
                            if masu[check_pos]=="爆":
                                masu[mas]+=1
                        elif _ == 1:
                            check_pos = mas-6
                            if masu[check_pos]=="爆":
                                masu[mas]+=1
                        elif _ == 2:
                            check_pos = mas-1
                            if masu[check_pos]=="爆":
                                masu[mas]+=1
                        elif _ == 3:
                            check_pos = mas+4
                            if masu[check_pos]=="爆":
                                masu[mas]+=1
                        elif _ == 4:
                            check_pos = mas+5
                            if masu[check_pos]=="爆":
                                masu[mas]+=1

                elif mas in [21,22,23]: #list3
                    for _ in range(5):
                        if _ == 0:
                            check_pos = mas-1
                            if masu[check_pos]=="爆":
                                masu[mas]+=1
                        elif _ == 1:
                            check_pos = mas-6
                            if masu[check_pos]=="爆":
                                masu[mas]+=1
                        elif _ == 2:
                            check_pos = mas-5
                            if masu[check_pos]=="爆":
                                masu[mas]+=1
                        elif _ == 3:
                            check_pos = mas-4
                            if masu[check_pos]=="爆":
                                masu[mas]+=1
                        elif _ == 4:
                            check_pos = mas+1
                            if masu[check_pos]=="爆":
                                masu[mas]+=1

                elif mas in [5,10,15]: #list4
                    for _ in range(5):
                        if _ == 0:
                            check_pos = mas-5
                            if masu[check_pos]=="爆":
                                masu[mas]+=1
                        elif _ == 1:
                            check_pos = mas-4
                            if masu[check_pos]=="爆":
                                masu[mas]+=1
                        elif _ == 2:
                            check_pos = mas+1
                            if masu[check_pos]=="爆":
                                masu[mas]+=1
                        elif _ == 3:
                            check_pos = mas+6
                            if masu[check_pos]=="爆":
                                masu[mas]+=1
                        elif _ == 4:
                            check_pos = mas+5
                            if masu[check_pos]=="爆":
                                masu[mas]+=1
                
            elif mas in [6,7,8,11,12,13,16,17,18]:

                for _ in range(8):
                    if _ == 0:#lists = [mas-1,mas-6,mas-5,mas-4,mas+1,mas+6,mas+5,mas+4]
                        check_pos = mas-1
                        if masu[check_pos]=="爆":
                            masu[mas]+=1

                    elif _ == 1:
                        check_pos = mas-6
                        if masu[check_pos]=="爆":
                            masu[mas]+=1

                    elif _ == 2:
                        check_pos = mas-5
                        if masu[check_pos]=="爆":
                            masu[mas]+=1

                    elif _ == 3:
                        check_pos = mas-4
                        if masu[check_pos]=="爆":
                            masu[mas]+=1

                    elif _ == 4:
                        check_pos = mas+1
                        if masu[check_pos]=="爆":
                            masu[mas]+=1

                    elif _ == 5:
                        check_pos = mas+6
                        if masu[check_pos]=="爆":
                            masu[mas]+=1

                    elif _ == 6:
                        check_pos = mas+5
                        if masu[check_pos]=="爆":
                            masu[mas]+=1

                    elif _ == 7:
                        check_pos = mas+4
                        if masu[check_pos]=="爆":
                            masu[mas]+=1


    def to_fullwidth(num):
        return ''.join(chr(ord('０') + ord(c) - ord('0')) if c.isdigit() else c for c in str(num))


    def send_5x5(masu):
        global channel_id
        global token
        global amount_of_bombs
        content = ""
        for i in range(0, 25, 5):
            row = [f"||{to_fullwidth(str(masu[j]))}||" for j in range(i, i + 5)]
            content += ''.join(row) + '\n'
        r=requests.post(
            f"https://discord.com/api/v9/channels/{channel_id}/messages",
            headers={"authorization":f"{token}"},
            json={"content": content}
        )
        r=requests.post(
            f"https://discord.com/api/v9/channels/{channel_id}/messages",
            headers={"authorization":f"{token}"},
            json={"content": f"爆弾:{amount_of_bombs}個"}
        )

        print(r.status_code)
        time.sleep(5)
    send_5x5(masu)
    #list1 = n-1,n+1,n+4,n+5,n+6
    #list2 = n-5,n-6,n-1,n+4,n+6
    #list3 = n-1,n-6,n-5,n-4,n+1
    #list4 = n-5,n-4,n+1,n+6,n+5
    #lists = [mas-1,mas-6,mas-5,mas-4,mas+1,mas+6,mas+5,mas+4]
