from collections import defaultdict

word_counts = defaultdict(int)

for w in open('Tweet_input.txt').read().split():
    word_counts[w.lower()] += 1

for w, c in word_counts.iteritems():
    print w, "occurs", word_counts[w], "times"
