PIECES = {'P', 'B', 'R', 'Q'}

def checkmate(board):
    rows = [r.strip() for r in board.splitlines()]
    n = len(rows)

    if not rows or any(len(r) != n for r in rows):
        print("Error")
        return
    kings = []
    for r in range(n): 
        for c in range(n):
            if rows[r][c] == 'K':
                kings.append((r, c))
    if len(kings) != 1:
        print("Error")
        return
    kr, kc = kings[0]

    for pr, pc in [(kr + 1, kc - 1), (kr + 1, kc + 1)]:
        if 0 <= pr < n and 0 <= pc < n and rows[pr][pc] == 'P':
            print("Success")
            return

    for dr, dc in [(-1,0),(1,0),(0,-1),(0,1),(-1,-1),(-1,1),(1,-1),(1,1)]:
        r, c = kr + dr, kc + dc
        while 0 <= r < n and 0 <= c < n:
            ch = rows[r][c]

            if ch in PIECES or ch == 'K':
                straight = (dr == 0 or dc == 0)

                if straight and ch in ('R', 'Q'):
                    print("Success")
                    return

                if not straight and ch in ('B', 'Q'):
                    print("Success")
                    return

                break

            r += dr
            c += dc

    print("Fail")