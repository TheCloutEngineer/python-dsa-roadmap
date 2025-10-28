# Week 01 — Baseline & Big-O Fluency

**Goal:** Speak Big-O out loud, measure cost, feel iteration vs. recursion.

## Day 1

- [ ] Skim `notes/big-o.md` (5 min), say definitions out loud.
- [ ] Implement `scripts/timer.py` (perf_counter helper).
- [ ] Write a loop that sums 1...n and estimate ops; verify with timer.
- [ ] Reflection (2–3 lines): Why did measured time deviate from expectation?

## Day 2

- [ ] Implement `src/week01/baseline_loops.py` with: linear scan, nested loops.
- [ ] Annotate expected complexity in comments (`O(n)`, `O(n^2)`).
- [ ] Add three inputs: small/medium/large; record timings in `notes/big-o.md`.
- [ ] Reflection: Where’s the tight loop? Any hidden constant costs?

## Day 3

- [ ] Write `src/week01/recursion_iter.py`: factorial (rec & iter), fibonacci (iter).
- [ ] Explain stack growth in comments; add a `sys.setrecursionlimit` note.
- [ ] Tests in `tests/test_week01.py` (edge cases).
- [ ] Reflection: When would recursion be clearer but dangerous?

## Day 4

- [ ] Micro-drill: describe algorithm → estimate Big-O → confirm with timing.
- [ ] Implement mini benchmark table (n vs. time) in `scripts/timer.py`.
- [ ] Reflection: One production story where Big-O mattered.

## Day 5 (Review)

- [ ] Make five flashcards (index cards or `notes/flashcards-week01.md`).
- [ ] Summarize: five bullets on Big-O pitfalls.
- [ ] Queue three problems for Week 2 (arrays and hashing).
