"""Fetch every server (latest version) from the official MCP Registry and keep those with a remote URL.
Output: research/mcpscan/registry_remotes.json  [{name, title, description, version, url, type, website, repo}]"""
import json, time, urllib.parse, urllib.request
from pathlib import Path
OUT = Path(__file__).resolve().parents[1] / "build"; OUT.mkdir(parents=True, exist_ok=True)
base = "https://registry.modelcontextprotocol.io/v0/servers"
rows, cursor, pages = [], None, 0
while True:
    q = {"limit": "100", "version": "latest"}
    if cursor: q["cursor"] = cursor
    for attempt in range(4):
        try:
            d = json.loads(urllib.request.urlopen(urllib.request.Request(base + "?" + urllib.parse.urlencode(q), headers={"User-Agent": "free-remote-mcp-servers/1.0 (+https://github.com/diegobruegger-prog/free-remote-mcp-servers)"}), timeout=30).read())
            break
        except Exception as e:
            time.sleep(3 * (attempt + 1))
    else:
        print("giving up at page", pages); break
    for s in d.get("servers", []):
        x = s.get("server", s)
        for r in x.get("remotes") or []:
            u = r.get("url", "")
            if u.startswith("https://") and "{" not in u:
                rows.append({"name": x.get("name"), "title": x.get("title") or "", "description": x.get("description") or "", "version": x.get("version"),
                             "url": u, "type": r.get("type"), "website": x.get("websiteUrl") or "", "repo": (x.get("repository") or {}).get("url", ""),
                             "headers": bool(r.get("headers"))})
    pages += 1
    cursor = (d.get("metadata") or {}).get("nextCursor")
    if not cursor: break
    time.sleep(0.3)
(OUT / "registry_remotes.json").write_text(json.dumps(rows, ensure_ascii=False))
print(pages, "pages,", len(rows), "remotes,", len({r["url"] for r in rows}), "unique urls")
