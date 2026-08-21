# Lab Report — Chapter 5: Hash Tables

*Complete both sections and commit this file with your code.*

## Test Results

*Paste your cache hit/miss output and your collision comparison.*

```text

```

## Reflection Questions

1. **Explain a hash table to someone who has never programmed.**
   - *A hash table is like a row of mailboxes in an apartment lobby. Each mailbox has a number, and instead of searching every mailbox one by one, a rule tells you exactly which mailbox to check. That rule is the "hash function". It takes a piece of information, such as a person's name, and converts it into a mailbox number where the information is stored. This makes finding information very fast because you usually only need to look in one place.*

2. **Chapter 5 says lookups are fast "on average." When is that not true, and what makes it go wrong?**
   - *Lookups are not fast when "many keys are assigned to the same location", creating "collisions". If a poor hash function doesn't spread data evenly, or if the hash table becomes too full, multiple items end up in the same bucket. Instead of finding the item immediately, the program has to search through several items, making lookups slower. In the worst case, a lookup can become as slow as searching through a regular list.*
3. **Your page cache avoided repeating expensive work. Where have you seen caching in software you use?**
   - *One common example is a web browser. When you revisit a website, the browser stores images, styles, and other files in a cache. Instead of downloading them again, it loads them from the cache, making the website open much faster. Another example is streaming services like Netflix or YouTube, which temporarily store video data so playback is smoother and doesn't constantly re-download the same content.*
