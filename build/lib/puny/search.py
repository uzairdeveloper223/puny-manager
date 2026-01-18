import shutil
import subprocess

def entry_text(entry: dict) -> str:
    return f"{entry['name']} {entry.get('notes','')}".lower()

def exact_match(entries, query):
    for e in entries:
        if e["name"] == query:
            return e
    return None

def python_fuzzy_all(entries, query):
    q = query.lower()
    scored = []

    for e in entries:
        text = f"{e['name']} {e.get('notes','')}".lower()
        score = text.count(q)
        if score:
            scored.append((score, e))

    scored.sort(key=lambda x: x[0], reverse=True)
    return [e for _, e in scored]

def fzf_pick(entries):
    names = [e["name"] for e in entries]

    p = subprocess.run(
        ["fzf"],
        input="\n".join(names),
        text=True,
        capture_output=True,
    )

    if p.returncode != 0:
        return None

    chosen = p.stdout.strip()
    for e in entries:
        if e["name"] == chosen:
            return e

    return None

def smart_find(entries, query):
    for e in entries:
        if e["name"] == query:
            return e

    matches = python_fuzzy_all(entries, query)

    if not matches:
        return None
        
    if len(matches) == 1:
        return matches[0]

    if shutil.which("fzf"):
        return fzf_pick(matches)

    return matches[0]
