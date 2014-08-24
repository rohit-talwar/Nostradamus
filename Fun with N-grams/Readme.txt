                          Fun with N-Grams
=======================================================================

What it is?
-----------
A set of python scripts that play on a given test. To run it just put 
your randomly selected text of about 50000 words into the file 
ngrams-dataset.txt 


What each script does 
---------------------
1.py - Prepare a unigram count table. Compute % of coverage, and
probabilities of each unigram. Find the number of types and tokens.

2.py - Prepare a bigram count table and bigram probability table. 
Compute unigram counts from the bigram count table and verify
that the counts are same as in (a)

Select 5 sentences (of length 6- 10 words) at random from your corpus.
For each of the selected sentence S,

3.py (i) Gets P(S), the probability of sentence S, using
(a) unigram counts,
(b) bigram counts,

4.py (ii) For each sentence S, keep only the first three words, and 
drop the remaining words. If the length of the sentence was length n,
select (n-3) words after the first three, based on the maximum bi-gram 
probability given the earlier words. Construct the new sentence.

5.py (iii) The probabilily of the constructed sentences.

** Alternatively, you could use the corpus in resource section 
(WSJ artciles).

