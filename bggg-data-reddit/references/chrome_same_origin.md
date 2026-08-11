# Chrome same-origin collection

Use this route when shell requests to Reddit return TLS failures, `403`, or network status `000`, but Reddit loads in the user's Chrome session.

1. Open `https://www.reddit.com/` in a Chrome tab with the Chrome-control skill.
2. Read `request_plan.json`.
3. For each request, evaluate `fetch(url, {credentials: "include"})` inside that Reddit tab. Capture the HTTP status and parse JSON only for a successful JSON response.
4. Continue a search listing by copying `data.after` into the next request's `after` parameter. Stop on null, a repeated cursor, no new post IDs, or the declared cap.
5. Save the exact parsed response as JSON. Do not modify the payload or store browser cookies.
6. Append a JSONL manifest row:

```json
{"kind":"search","file":"../../../data/raw/source_json/reddit_search_round1_sample-ingredient_001_page001.json","url":"https://www.reddit.com/search.json?...","query":"sample-ingredient","lang":"EN","round":1,"http_status":200,"collected_at":"2026-07-25T12:00:00+08:00"}
```

For a comment tree:

```json
{"kind":"comments","file":"../../../data/raw/source_json/reddit_comments_1fukkvr.json","url":"https://www.reddit.com/comments/1fukkvr.json?limit=500&depth=10&sort=top&raw_json=1","query":"sample-ingredient","lang":"EN","round":1,"post_id":"1fukkvr","http_status":200,"collected_at":"2026-07-25T12:10:00+08:00"}
```

Keep paths relative to the manifest file where practical. If Reddit shows a login wall, unusual-activity warning, challenge, or rate limit, stop that route and record the visible state. Do not submit account recovery forms or export session data.
