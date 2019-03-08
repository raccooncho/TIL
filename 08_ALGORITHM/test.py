for t in range(10):
    a = input()
    miro = []
    for i in range(16):
        ass = input()
        row = [x for x in ass]
        miro.append(row)
    former_status = []
    now_status = ['11']
    finds = ['2']
    while '3' not in finds or now_status == []:
        former_status_dum = now_status[:]
        now_status_dum = []
        finds_dum = []
        for pos in range(len(now_status)):
            aa = int(now_status[pos][0])
            b = int(now_status[pos][1])
            check = [str(aa-1)+str(b-2), str(aa-1)+str(b+1), str(a+1)+ str(b-1), str(a+1)+str(b+1)]
            for direc in check:
                aaa = int(direc[0])
                bb = int(direc[1])
                mm = miro[aaa][bb]
                if direc not in former_status and mm != 1:
                    now_status_dum.append(direc)
                    finds_dum.append(mm)
        now_status = now_status.dum
        finds = finds_dum
    if now_status:
        print(f'#{a} 1')
    else:
        print(f'#{a} 0')

