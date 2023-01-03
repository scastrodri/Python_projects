# Exploring Common Words and SETI

# We are gping to use a list of the 5000 most common words. This particular list list of words is based
# on analyzing over 450 million words from magazines, newspapers, works of fiction and academic writing.
# The list we will be using is kindly made available from the Word Frequency data project.

# What do common words and the search for extra terrestrial intelligence have to do with one another? A 
# linguistic relationship called Zipf’s Law appears to be one of the conditions for complex 
# communications. A simple way to describe Zipf’s law is to say that words are not evenly distributed 
# across texts; but rather a few words are very common and a lot of words are very rare. There is a nice 
# straight line plotted on a log-log scale that links the common and the rare words. The slope of this 
# line is approximately -1.

# READING DATA

# The words from our list are in order from most frequently used to least where the rank order is a 
# function of both frequency and “dispersion”, which measures how evenly the word is spread across the 
# corpus (1 = most evenly distributed; 0 = appears irregularly in few texts). This means that its not 
# the frequency column does not go perfectly from highest to lowest, there may be some cases where the 
# frequency is high but the dispersion is low. For example the word ‘re’ has a frequency of 15,773 but a 
# dispersion of only .47 its primarily used in legal writing not in writing for the general public.

# Each word also has a part of speech which will be one of
# ‘a’ - article
# ‘v’ - verb
# ‘c’ - conjunction
# ‘i’ - preposition
# ‘t’ - infinitive (to)
# ‘p’ - pronoun
# ‘d’ - pronoun
# ‘x’ - not or n’t
# ‘r’ - adverb
# ‘m’ - number
# ‘n’ - noun
# ‘e’ - there
# ‘j’ - adjective
# ‘u’ - interjection

# The data is a CSV file (Comma Separated Values). Could be handle with pandas library, but just for
# fun, let's not use that ;)


# The first task is to read this file and store the contents into five lists. 
# The goal is to split the line into five parts and put each of those parts onto the appropriate list.
import math
import matplotlib.pyplot as plt

Rank = []
Words = []
Part_speech = []
Frequency = []
Dispersion = []
with open('words5000.csv') as wf:
    for line in wf.readlines():
        Rank.append(line.split(',')[0])
        Words.append(line.split(',')[1])
        Part_speech.append(line.split(',')[2])
        Frequency.append(line.split(',')[3])
        Dispersion.append(line.split(',')[4])
        
Rank = Rank[1:]
Words = Words[1:]
Part_speech = Part_speech[1:]
Frequency = Frequency[1:]
Dispersion = Dispersion[1:]
# Let's convert in numbers those "columns" that requery it
Rank = [int(number) for number in Rank]
Frequency = [int(number) for number in Frequency]
Dispersion = [float(number) for number in Dispersion]

# Now lets explore Zipf’s Law.
# First lets look at what fraction of overall usage the top 10 most common words represent. The first 
# thing we will need to do to accomplish this is turn the frequency count for each word into a percentage.
# Once we have a new “column” for our table, then we can sum up the percentages for the first 10.
total = sum([value for value in Frequency]) 
percentage = [(value / total) for value in Frequency] # The new 'column'


# Calculate the total usage percentage for the top 10 words in the list. Store this result in a variable
# called top_10 At the same time calculate the percentage for teh bottom 10 words in the list and store 
# that result in bottom_10
top_10 = sum(percentage[:10])
bottom_10 = sum(percentage[-10:])


# Just to get a sense for the distribution of the words lets graph the frequency of the words on the Y 
# axis against the rank of the words on the X axis. We should see a pretty dramatic (exponential) curve. 
# Its also not very useful because a few very large values dwarf all of the small # values. 
fig, ax = plt.subplots()
ax.plot(Rank, Frequency)
ax.set(xlabel='Rank', ylabel='Frequency', title='Distribution of the words')


# So The next step in our quest is to add two more columns of data to our table. The log of the 
# frequency and the log [Logarithm] of the rank. Once we have added these two 'columns' use Altair to 
# graph the new # quantities and be amazed!
log_Freq = [math.log10(value) for value in Frequency]
log_Rank = [math.log10(value) for value in Rank]

fig, ax = plt.subplots()
ax.plot(log_Rank, log_Freq, color='r')
ax.set(xlabel='Rank in log(10)', ylabel='Frequency in log(10)', title='Distribution of the words')


# More Fun with words
# Which of the words when spelled forward are also on the list when spelled backward? For example ‘pot’ 
# is one of the most common words and when you spell pot backwards you get ‘top’ which is also on the 
# list.
def backw_str(a_str:str)->str:
    '''Returns a string spelled backward'''
    return a_str[::-1]

forw_backw = []
for word in Words:
    if backw_str(word) in Words:
        forw_backw.append(word)
forw_backw = list(set(forw_backw))


# How many new words can be reversed if you you add an ‘s’ on the end? For example adding an ‘s’ to the 
# end of ‘pot’ gives you ‘stop’ when reversed which is definitely on the list.
def plus_s(a_str:str)->str:
    '''Returns a string adding an 's' on the end'''
    return a_str + 's'

new_words = []
for word in Words:
    if backw_str(plus_s(word)) in Words:
        new_words.append(word)
new_words = list(set(new_words))


# Finally lets look at the distribution of the different parts of speech in this 5000 word dataset. 
# Create a bar chart where the part of speech is on the x-axis and the number of words on the list that 
# fall into that category is the y axis.
a_dict = {} # A dictionary to save every part of the speech and the number of words
for a_tup in zip(Part_speech,Frequency):
    a_dict[a_tup[0]] = a_dict.get(a_tup[0], 0) + a_tup[1]

fig, ax = plt.subplots()
bar_labels = ['a - article', 'v - verb', 'c - conjunction', 'i - preposition', 't - infinitive (to)',
                'p - pronoun', 'd - pronoun', "x - not or n't", 'r - adverb', 'm - number', 'n - noun',
                'e - there', 'j - adjective', 'u - interjection']
bar_color = ['blue', 'orange', 'green', 'red', 'purple', 'brown', 'pink', 'gray', 'olive', 'cyan', 
                'coral', 'gold', 'lime', 'teal']

bar1 = ax.bar(a_dict.keys(), a_dict.values(), color=bar_color)
ax.legend(bar1, bar_labels)
ax.set(xlabel='Part of speech', ylabel='Number of words on the list',
        title='Distribution of the different parts of speech')
plt.show()