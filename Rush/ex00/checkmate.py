PIECES = {'P', 'B', 'R', 'Q'}  #สร้างตัวแปรเก็บ Queen, Bishop, Rook, Pawn

def checkmate(board):
    rows = board.strip("\n").splitlines()  #board.splitlines() จะแยกกระดานที่เป็น str ออกมาเป็น list
    n = len(rows)     #หาขนาดของกระดาน

    if not rows or any(len(r) != n for r in rows):   #ตรวจกระดานว่างไหม และตรวจว่าทุก col, row เท่ากันไหม
        print("Error")
        return
    kings = []             #ใช้เก็บตำแหน่งของ king อยู่ row ไหน col ไหน
    for r in range(n):             #row ของ king
        for c in range(n):         #col ของ king
            if rows[r][c] == 'K':  
                kings.append((r, c))    #ใส่ตำแหน่ง row, col ของ king ลงไป

    if len(kings) != 1:     #ตรวจ king มีตัวเดียวไหม
        print("Error")
        return
    kr, kc = kings[0]

    for pr, pc in [(kr + 1, kc - 1), (kr + 1, kc + 1)]:            #ตรวจ pawn ว่าเช็ค king ได้ไหม 
        if 0 <= pr < n and 0 <= pc < n and rows[pr][pc] == 'P':
            print("Success")
            return

    for dr, dc in [(-1,0),(1,0),(0,-1),(0,1),(-1,-1),(-1,1),(1,-1),(1,1)]:         #ตรวจตำแหน่งรอบ king
        r, c = kr + dr, kc + dc
        while 0 <= r < n and 0 <= c < n:          #ตรวจตำแหน่งว่าอยู่ในกระดานไหม
            ch = rows[r][c]

            if ch in PIECES or ch == 'K':         #ตรวจว่ามีหมากไหม
                straight = (dr == 0 or dc == 0)   

                if straight and ch in ('R', 'Q'):       #ตรวจการโจมตีของ Rook และ Queen
                    print("Success")
                    return

                if not straight and ch in ('B', 'Q'):
                    print("Success")
                    return

                break

            r += dr
            c += dc

    print("Fail")