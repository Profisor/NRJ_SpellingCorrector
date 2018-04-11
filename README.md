# NRJ_SpellingCorrector
Spelling Correction for Text Data
Spell Checker:
I have used python to check the spelling.
Algorithm:
I have used Peter Norvig’s approach to build the spell corrector.
This algorithm mainly consists of as follows. They are,
1.	It will find all the possible outputs and it selects the most probable word by choosing the best probability.
2.	The probability of the typed word being correctly typed by the user.
How it Works?
It works on Bayes therom,
P(A/B)= P(B/A).P(A)/P(B)
The call correction(B) tries to choose the most likely spelling correction for w. There is no way to know for sure (for example, should "lates" be corrected to "late" or "latest" or "lattes" or ...?), which suggests we use probabilities. We are trying to find the correction c, out of all possible candidate corrections, that maximizes the probability that c is the intended correction, given the original word B: 
argmaxc ∈ candidates P(A/ B) 

On which it works?
1.	It works on wrongly repeated letters like fooood.
2.	It works on mis-spelt words.

correction('smyle')
smile

correction(‘cykle’)
cycle

correction(‘foood’)
food

correction(‘aplycation’)
application

Accuracy checking:
By using this method I got 0.80 which is quite better. 




