from sys import argv
import json

if len(argv) > 1:
    date_filter = argv[1]
else:
    date_filter = None

with open("watch-history.json", encoding="utf-8") as history_file:
    history = json.loads(history_file.read())

count = {}
views = 0

for video in history:
    title = video["title"]
    time = video["time"]

    if date_filter and not time.startswith(date_filter):
        continue

    if title not in count:
        count[title] = 1
    else:
        count[title] += 1
    views += 1

sorted_history = sorted(count.items(), key=lambda v: v[1], reverse=True)

for i in range(0, 100):
    print(f"Song {i + 1} ({sorted_history[i][1]} views): {sorted_history[i][0]}")

print(f"{views} views in total across {len(count)} videos")
