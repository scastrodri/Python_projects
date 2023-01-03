# Exploring Common Words and SETI
Using a list of the 5000 most common words. This particular list of words is based on analyzing over 450 million words from magazines, newspapers, works of fiction 
and academic writing. The list we will be using is kindly made available from the [Word Frequency data project.](https://www.wordfrequency.info/intro.asp)
A linguistic relationship called Zipf’s Law appears to be one of the conditions for complex communications. A simple way to describe Zipf’s law is to say that words 
are not evenly distributed across texts; but rather a few words are very common and a lot of words are very rare. There is a nice straight line plotted on a log-log 
scale that links the common and the rare words. The slope of this line is approximately -1.
* Graph the frequency of the words on the Y axis against the rank of the words on the X axis. It would should see a pretty dramatic (exponential) curve. Its also not 
very useful because a few very large values dwarf all of the small # values.
* Graph the frequency of the words on the Y axis against the rank of the words on the X axis. This one will be in a log-log scale.
* Which of the words when spelled forward are also on the list when spelled backward?
* How many new words can be reversed if you you add an ‘s’ on the end?
* Finally lets look at the distribution of the different parts of speech in this 5000 word dataset.

## Resources used:
* **Python version:** 3.11
* **Packages:** math, matplotlib.

## Frequency of the words
![](https://github.com/scastrodri/Python_projects/blob/main/Exploring_Common_Words/Figure_1.png)
## Frequency of the words in a log-log scale
![](https://github.com/scastrodri/Python_projects/blob/main/Exploring_Common_Words/Figure_2.png)
## Distribution of the different parts of speech
![](https://github.com/scastrodri/Python_projects/blob/main/Exploring_Common_Words/Figure_3.png)
