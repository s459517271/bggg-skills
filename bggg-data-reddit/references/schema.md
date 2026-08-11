# Normalized Reddit JSONL

Each row contains:

- `platform`: always `Reddit`
- `lang`: declared corpus language
- `source_id`: 24-character SHA-256 prefix over native ID and exact text
- `native_id`: Reddit fullname such as `t3_…` or `t1_…`
- `date`: UTC ISO-8601 timestamp when available
- `text_raw`: exact title/body or comment body
- `engagement`: post score, comment count, upvote ratio, or comment score
- `context`: content type, subreddit, parent post, URL, query, source file, source URL
- `keyword_hit`: literal query/keyword matches
- `round`: discovery round

Raw collection must also preserve:

- every source JSON response;
- a manifest with request URL, query, round, language, HTTP status, collection time, and saved path;
- failures and stop reasons;
- parent-thread row counts for cluster-aware analysis.
