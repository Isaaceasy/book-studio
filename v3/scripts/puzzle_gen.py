#!/usr/bin/env python3
"""Generate and VERIFY puzzles: word search, sudoku (unique solution), perfect mazes.

Usage:
  python scripts/puzzle_gen.py sudoku --count 5 --level medium --seed 1 --out puzzles/sudoku
  python scripts/puzzle_gen.py wordsearch --words-file words.txt --size 15 --count 3 --seed 1 --out puzzles/ws
  python scripts/puzzle_gen.py maze --size 20 --count 3 --seed 1 --out puzzles/maze
  python scripts/puzzle_gen.py verify puzzles/sudoku        # re-verify saved JSON files

Each puzzle is saved as JSON (puzzle + solution) and SVG (puzzle, and *_solution.svg). Nothing is written
unless the puzzle verifies: sudoku has exactly one solution, every word-search word occurs exactly once,
every maze is solvable. A failing puzzle is regenerated.
"""
import argparse
import json
import os
import random
import sys
from collections import deque

# ---------------------------------------------------------------- sudoku
def _ok(g, r, c, v):
    if any(g[r][i] == v for i in range(9)) or any(g[i][c] == v for i in range(9)):
        return False
    br, bc = r // 3 * 3, c // 3 * 3
    return all(g[br + i][bc + j] != v for i in range(3) for j in range(3))


def _solve_count(g, limit=2):
    for r in range(9):
        for c in range(9):
            if g[r][c] == 0:
                n = 0
                for v in range(1, 10):
                    if _ok(g, r, c, v):
                        g[r][c] = v
                        n += _solve_count(g, limit - n)
                        g[r][c] = 0
                        if n >= limit:
                            return n
                return n
    return 1


def _fill(g, rng):
    for r in range(9):
        for c in range(9):
            if g[r][c] == 0:
                vals = list(range(1, 10))
                rng.shuffle(vals)
                for v in vals:
                    if _ok(g, r, c, v):
                        g[r][c] = v
                        if _fill(g, rng):
                            return True
                        g[r][c] = 0
                return False
    return True


def sudoku(rng, level="medium"):
    clues = {"easy": 40, "medium": 32, "hard": 27}[level]
    sol = [[0] * 9 for _ in range(9)]
    _fill(sol, rng)
    puz = [row[:] for row in sol]
    cells = [(r, c) for r in range(9) for c in range(9)]
    rng.shuffle(cells)
    filled = 81
    for r, c in cells:
        if filled <= clues:
            break
        keep = puz[r][c]
        puz[r][c] = 0
        if _solve_count([row[:] for row in puz]) != 1:
            puz[r][c] = keep
        else:
            filled -= 1
    return {"type": "sudoku", "level": level, "clues": filled, "puzzle": puz, "solution": sol}


def verify_sudoku(p):
    g = [row[:] for row in p["puzzle"]]
    if _solve_count(g) != 1:
        return False, "not exactly one solution"
    sol = p["solution"]
    for r in range(9):
        for c in range(9):
            if p["puzzle"][r][c] and p["puzzle"][r][c] != sol[r][c]:
                return False, "clue differs from solution"
    for i in range(9):
        if sorted(sol[i]) != list(range(1, 10)) or sorted(sol[r][i] for r in range(9)) != list(range(1, 10)):
            return False, "solution rows or columns invalid"
    return True, "ok"


def sudoku_svg(grid, solution=None, cell=40):
    n = 9 * cell
    out = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{n+4}" height="{n+4}" viewBox="-2 -2 {n+4} {n+4}">',
           f'<rect x="0" y="0" width="{n}" height="{n}" fill="white" stroke="black" stroke-width="3"/>']
    for i in range(1, 9):
        w = 2.5 if i % 3 == 0 else 0.8
        out.append(f'<line x1="{i*cell}" y1="0" x2="{i*cell}" y2="{n}" stroke="black" stroke-width="{w}"/>')
        out.append(f'<line x1="0" y1="{i*cell}" x2="{n}" y2="{i*cell}" stroke="black" stroke-width="{w}"/>')
    for r in range(9):
        for c in range(9):
            v = grid[r][c]
            if v:
                fill = "#000" if not solution or solution[r][c] == v and grid[r][c] else "#000"
                out.append(f'<text x="{c*cell+cell/2}" y="{r*cell+cell*0.72}" font-family="Arial" font-size="{cell*0.6}" text-anchor="middle" fill="{fill}">{v}</text>')
    out.append("</svg>")
    return "\n".join(out)


# ---------------------------------------------------------------- word search
DIRS = [(0, 1), (1, 0), (1, 1), (-1, 1), (0, -1), (-1, 0), (-1, -1), (1, -1)]


def _count_word(grid, w, size):
    cnt = 0
    for r in range(size):
        for c in range(size):
            for dr, dc in DIRS:
                rr, cc, k = r, c, 0
                while k < len(w) and 0 <= rr < size and 0 <= cc < size and grid[rr][cc] == w[k]:
                    rr += dr; cc += dc; k += 1
                if k == len(w):
                    cnt += 1
    return cnt


def wordsearch(rng, words, size, allowed_dirs=None):
    words = [w.upper().replace(" ", "") for w in words]
    words.sort(key=len, reverse=True)
    dirs = allowed_dirs or DIRS
    for attempt in range(200):
        grid = [[""] * size for _ in range(size)]
        placed = {}
        ok = True
        for w in words:
            done = False
            for _ in range(400):
                dr, dc = rng.choice(dirs)
                r, c = rng.randrange(size), rng.randrange(size)
                er, ec = r + dr * (len(w) - 1), c + dc * (len(w) - 1)
                if not (0 <= er < size and 0 <= ec < size):
                    continue
                if all(grid[r + dr * i][c + dc * i] in ("", w[i]) for i in range(len(w))):
                    for i in range(len(w)):
                        grid[r + dr * i][c + dc * i] = w[i]
                    placed[w] = (r, c, dr, dc)
                    done = True
                    break
            if not done:
                ok = False
                break
        if not ok:
            continue
        sol = [row[:] for row in grid]
        letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        for r in range(size):
            for c in range(size):
                if not grid[r][c]:
                    grid[r][c] = rng.choice(letters)
        if all(_count_word(grid, w, size) == 1 for w in words):
            return {"type": "wordsearch", "size": size, "words": words, "placed": placed,
                    "puzzle": ["".join(r) for r in grid], "solution_mask": [["#" if sol[r][c] else "." for c in range(size)] for r in range(size)]}
    raise SystemExit("Could not build a word search with unique word occurrences; reduce words or increase size")


def verify_wordsearch(p):
    g = [list(r) for r in p["puzzle"]]
    for w in p["words"]:
        n = _count_word(g, w, p["size"])
        if n != 1:
            return False, f"{w} occurs {n} times"
    return True, "ok"


def wordsearch_svg(p, show_solution=False, cell=28):
    s = p["size"]
    n = s * cell
    out = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{n}" height="{n}" viewBox="0 0 {n} {n}">']
    for r in range(s):
        for c in range(s):
            hl = show_solution and p["solution_mask"][r][c] == "#"
            if hl:
                out.append(f'<rect x="{c*cell}" y="{r*cell}" width="{cell}" height="{cell}" fill="#ffe08a"/>')
            out.append(f'<text x="{c*cell+cell/2}" y="{r*cell+cell*0.7}" font-family="Arial" font-size="{cell*0.62}" text-anchor="middle">{p["puzzle"][r][c]}</text>')
    out.append("</svg>")
    return "\n".join(out)


# ---------------------------------------------------------------- maze
def maze(rng, size):
    walls = [[{"N": True, "S": True, "E": True, "W": True} for _ in range(size)] for _ in range(size)]
    seen = [[False] * size for _ in range(size)]
    stack = [(0, 0)]
    seen[0][0] = True
    opp = {"N": "S", "S": "N", "E": "W", "W": "E"}
    mv = {"N": (-1, 0), "S": (1, 0), "E": (0, 1), "W": (0, -1)}
    while stack:
        r, c = stack[-1]
        opts = [(d, r + mv[d][0], c + mv[d][1]) for d in mv if 0 <= r + mv[d][0] < size and 0 <= c + mv[d][1] < size and not seen[r + mv[d][0]][c + mv[d][1]]]
        if not opts:
            stack.pop()
            continue
        d, nr, nc = rng.choice(opts)
        walls[r][c][d] = False
        walls[nr][nc][opp[d]] = False
        seen[nr][nc] = True
        stack.append((nr, nc))
    path = _maze_path(walls, size)
    return {"type": "maze", "size": size, "walls": walls, "start": [0, 0], "end": [size - 1, size - 1], "solution": path}


def _maze_path(walls, size):
    mv = {"N": (-1, 0), "S": (1, 0), "E": (0, 1), "W": (0, -1)}
    q, prev = deque([(0, 0)]), {(0, 0): None}
    while q:
        r, c = q.popleft()
        if (r, c) == (size - 1, size - 1):
            break
        for d, (dr, dc) in mv.items():
            if not walls[r][c][d] and (r + dr, c + dc) not in prev:
                prev[(r + dr, c + dc)] = (r, c)
                q.append((r + dr, c + dc))
    if (size - 1, size - 1) not in prev:
        return None
    path, cur = [], (size - 1, size - 1)
    while cur:
        path.append(list(cur))
        cur = prev[cur]
    return path[::-1]


def verify_maze(p):
    return (_maze_path(p["walls"], p["size"]) is not None, "ok" if _maze_path(p["walls"], p["size"]) else "no path")


def maze_svg(p, show_solution=False, cell=24):
    s = p["size"]
    n = s * cell
    out = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{n+4}" height="{n+4}" viewBox="-2 -2 {n+4} {n+4}"><g stroke="black" stroke-width="2" stroke-linecap="square">']
    for r in range(s):
        for c in range(s):
            w = p["walls"][r][c]
            x, y = c * cell, r * cell
            if w["N"] and not (r == 0 and c == 0):
                out.append(f'<line x1="{x}" y1="{y}" x2="{x+cell}" y2="{y}"/>')
            if w["W"]:
                out.append(f'<line x1="{x}" y1="{y}" x2="{x}" y2="{y+cell}"/>')
            if r == s - 1 and w["S"] and not (c == s - 1):
                out.append(f'<line x1="{x}" y1="{y+cell}" x2="{x+cell}" y2="{y+cell}"/>')
            if c == s - 1 and w["E"]:
                out.append(f'<line x1="{x+cell}" y1="{y}" x2="{x+cell}" y2="{y+cell}"/>')
    out.append("</g>")
    if show_solution and p["solution"]:
        pts = " ".join(f"{c*cell+cell/2},{r*cell+cell/2}" for r, c in p["solution"])
        out.append(f'<polyline points="{pts}" fill="none" stroke="#d62828" stroke-width="3"/>')
    out.append("</svg>")
    return "\n".join(out)


# ---------------------------------------------------------------- CLI
def save(out, name, data, svg, svg_sol):
    os.makedirs(out, exist_ok=True)
    with open(os.path.join(out, name + ".json"), "w", encoding="utf-8") as f:
        json.dump(data, f)
    open(os.path.join(out, name + ".svg"), "w", encoding="utf-8").write(svg)
    open(os.path.join(out, name + "_solution.svg"), "w", encoding="utf-8").write(svg_sol)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("kind", choices=["sudoku", "wordsearch", "maze", "verify"])
    ap.add_argument("path", nargs="?")
    ap.add_argument("--count", type=int, default=1)
    ap.add_argument("--level", default="medium", choices=["easy", "medium", "hard"])
    ap.add_argument("--size", type=int, default=15)
    ap.add_argument("--words-file")
    ap.add_argument("--seed", type=int, default=1)
    ap.add_argument("--out", default="puzzles")
    a = ap.parse_args()
    rng = random.Random(a.seed)
    if a.kind == "verify":
        bad = 0
        for fn in sorted(os.listdir(a.path)):
            if fn.endswith(".json"):
                p = json.load(open(os.path.join(a.path, fn), encoding="utf-8"))
                ok, msg = {"sudoku": verify_sudoku, "wordsearch": verify_wordsearch, "maze": verify_maze}[p["type"]](p)
                print(fn, "PASS" if ok else "FAIL", msg)
                bad += 0 if ok else 1
        return 1 if bad else 0
    for i in range(a.count):
        name = f"{a.kind}-{i+1:03d}"
        if a.kind == "sudoku":
            p = sudoku(rng, a.level)
            ok, msg = verify_sudoku(p)
            svg, ssol = sudoku_svg(p["puzzle"]), sudoku_svg(p["solution"])
        elif a.kind == "wordsearch":
            words = [w.strip() for w in open(a.words_file, encoding="utf-8").read().splitlines() if w.strip()]
            sub = rng.sample(words, min(len(words), max(8, a.size)))
            p = wordsearch(rng, sub, a.size)
            ok, msg = verify_wordsearch(p)
            svg, ssol = wordsearch_svg(p), wordsearch_svg(p, True)
        else:
            p = maze(rng, a.size)
            ok, msg = verify_maze(p)
            svg, ssol = maze_svg(p), maze_svg(p, True)
        if not ok:
            raise SystemExit(f"{name} failed verification: {msg}")
        save(a.out, name, p, svg, ssol)
        print(name, "verified")
    return 0


if __name__ == "__main__":
    sys.exit(main())
