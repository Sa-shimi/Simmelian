"""
This is the first python script intended for the PhD course "Mathematical models for..XXX".
The script is intended for teaching purposes and has no peculiar function. Each chunk should be running by itself in the
console.

For this specific script we won't need particular requirements.

The first thing you should do when creating a script is "importing" the modules you will need. It is useful as, in case
you're using someone else's script, you quickly know what are the necessary packages.
"""

import random

# Lines preceded by "#" are not read by the interpreter and can, thus, be used to add comments or guiding people through
# your script.

# TODO: YOU CAN ALSO CREATE NOTES FOR YOURSELF BY ADDING A "TODO" AFTER THE "#"

"You can also use quotes - don't recommend as this is not completely ignored"

"""
Or also triple quotes, which is recommended only for particularly long texts.
"""

# Learning to create variables and to read errors. Some actions or functions are not doable with certain object types.

# Let's create an object, x, and assign a value to it
x = 2
print(x)

# When we "print" a value or variable or object, we ask the interpreter to return the content of the variable or object

# If we put 2 "=" together, we're not adding a value, we're creating a boolean statement.
x == 3
# What is the warning telling us?

# Try this one now!
x == 2

# ok ok, we can make multiple variables and make calculations with them
y = 4
z = x + y

# Let's try even mor complex calculus..
k = x * y ** (1 / 2)

# Mmm.. what if we try this?
x = '3'

l = x + y

# What is the error warning telling us?
# Let's investigate what type of object we're dealing with
type(x)
# Remember that some actions or functions are not doable with certain objects. Do not worry, properly developed packages
# have built-in instructions and clear error warnings.

# Let's try new objects. Lists!

lst = [1, 2, 3, 4, 5, 6]

print(lst[1])
# What number shall we expect?

# Indexes in python language start from 0, for lists, arrays, dicts, everything


# Lists are the most commonly used objects on python as they're the corner stone of most python objects (such as arrays,
# DataFrame etc.. they can be created in different ways. the most common is to "append" an element in a list

lst = []

lst.append(0)
print(lst)

# The append function allows us to add an element (the one in brackets) at the end of the list. There are tools that can
# be used to add data (also un chunks) in different points of an already existing index

lst.append(1)
lst.append(2)
lst.append(3)
lst.append(4)
lst.append(5)

# We can utilize a "for _ in _ :" loop to reiterate a specific action for each element present in a list or array or..

for n in lst:
    print(n)

# can we create a list from 0 to 10 without having to type "lst.append" more than once?

for n in range(0, 10):
    lst.append(n)
print(lst)

# If we want to carry out an action n amount of times, we can use this small trick. Creating an ad hoc "list" between 0
# and n. Please, be careful. range(0, 10) or range(10) is not a list. list(range(10)) is a list

for n in range(10):
    lst.append(n)
print(lst)

# Let us introduce the last python element we need for today: if statements. if statements are useful tools that tell
# out interpreter if a specific condition is met.

lst_of_number = random.sample(range(20), 10)
odd_numbers = []
even_numbers = []
for n in lst_of_number:
    if n % 2 == 1:
        odd_numbers.append(n)
    elif n % 2 == 0:
        even_numbers.append(n)

# Sometimes we can shorten our code by eliminating conditions using else (if, of course, it's the only possible
# remaining condition)

odd_numbers = []
even_numbers = []
for n in lst_of_number:
    if n % 2 == 1:
        odd_numbers.append(n)
    else:
        even_numbers.append(n)

# Let's try a little task:
# let's create 3 lists, the first list wil contain odd numbers from 0 to 10, te second list will contain even numbers
# from 0 to 10 and the third, of the same length of the first one, will be composed by the sum of the elements of the
# previous two lists

even = [2, 4, 6, 8, 10]
odd = [1, 3, 5, 7, 9]
result = []

for n in range(len(even)):
    result.append((even[n] + odd[n]))

print(result)

# let's work on if statements

lst = list(range(10))

for n in lst:
    if n == 7:
        print(n)

lst.append('banana')
for n in lst:
    if type(n) == str:
        print(n)

# task for the first day:
# consider a sorted list containing random numbers from 0 to 1000000. what is the fastest way to find the position of
# a randomly generated number?
# explain reasoning


# here is your randomly generated number
random_number = random.randrange(100000000)

# here is your sorted list
lst = list(random.sample(range(100000000), 30000000))

# do not worry! creating this object will take quite some time :/

if random_number not in lst:
    lst.append(random_number)
lst = sorted(lst)

# solution:


not_yet_found = True
goal_index = 0
lst_copy = lst
while not_yet_found:
    half1 = int(len(lst_copy) / 2)
    half2 = len(lst_copy) - half1
    if lst_copy[half1] > random_number:
        lst_copy = lst_copy[:half1]
    elif lst_copy[half1] < random_number:
        goal_index += half1
        lst_copy = lst_copy[-half2:]
    elif lst_copy[half1] == random_number:
        not_yet_found = False
        print(f'This is the number you were looking for: {goal_index + int(len(lst_copy) / 2)}')

"""

Today we will focus on networks. In particular, the scope is to learn how to create, manage and analyze networks 
characteristics utilizing python. As before, let us now import the necessary packages.

"""

import networkx as nx
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

adj = np.array([[0., 1., 0., 1., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 1., 0., 0., 1.],
                [0., 0., 0., 0., 0., 0., 1., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 1.],
                [1., 1., 0., 0., 0., 0., 1., 0., 1., 1., 1., 0., 0., 1., 0., 0., 0., 1., 0., 0., 1.],
                [1., 1., 0., 0., 0., 0., 0., 1., 0., 0., 0., 0., 0., 0., 0., 0., 0., 1., 0., 0., 1.],
                [1., 1., 0., 0., 0., 0., 1., 0., 0., 0., 1., 0., 0., 1., 0., 0., 0., 1., 1., 1., 1.],
                [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 1.],
                [0., 1., 0., 0., 0., 0., 0., 0., 0., 0., 0., 1., 0., 1., 0., 0., 0., 1., 0., 0., 1.],
                [0., 1., 0., 1., 0., 0., 1., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 1., 0., 0., 1.],
                [1., 1., 0., 0., 0., 0., 1., 0., 0., 1., 1., 1., 0., 1., 0., 0., 0., 1., 0., 0., 1.],
                [0., 0., 1., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 1., 0., 0., 0.],
                [0., 1., 1., 0., 1., 0., 1., 0., 0., 0., 0., 0., 0., 1., 0., 0., 0., 1., 0., 0., 0.],
                [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 1.],
                [1., 1., 0., 0., 1., 0., 0., 0., 1., 0., 0., 0., 0., 1., 0., 0., 0., 1., 0., 0., 0.],
                [0., 1., 0., 0., 0., 0., 1., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 1., 0., 0., 1.],
                [0., 1., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 1., 0., 0., 0., 1., 1., 1., 0.],
                [1., 1., 0., 0., 0., 0., 0., 0., 0., 1., 0., 0., 0., 0., 0., 0., 0., 1., 0., 0., 0.],
                [1., 1., 0., 1., 0., 0., 1., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 1.],
                [1., 1., 1., 1., 0., 0., 1., 0., 1., 0., 1., 0., 0., 1., 1., 0., 0., 0., 0., 1., 1.],
                [1., 1., 0., 0., 1., 0., 1., 0., 0., 0., 1., 0., 0., 1., 0., 0., 0., 1., 0., 1., 0.],
                [1., 1., 0., 0., 0., 0., 0., 0., 0., 0., 1., 0., 0., 1., 1., 0., 0., 1., 0., 0., 1.],
                [0., 1., 1., 1., 0., 0., 1., 0., 0., 0., 0., 1., 0., 1., 0., 0., 0., 1., 0., 1., 0.]])

G = nx.from_numpy_array(adj)

# Let us look at a couple of features of the network we just created

list(G.nodes)
list(G.edges)

# Let us now have a look at its appearance:

nx.draw(G, with_labels=True)

# What are the characteristics of the subjects in the network? Features can we discern?

# Let us try out some centrality measurements
print(nx.betweenness_centrality(G))
print(nx.closeness_centrality(G))
print(nx.eigenvector_centrality(G))

# Ok, cool. But now let's say we want to quickly know who's more central than others...

betCent_sorted = dict(sorted(nx.betweenness_centrality(G).items(), key=lambda item: item[1], reverse=True))
betClos_sorted = dict(sorted(nx.closeness_centrality(G).items(), key=lambda item: item[1], reverse=True))
betEige_sorted = dict(sorted(nx.eigenvector_centrality(G).items(), key=lambda item: item[1], reverse=True))
print(betCent_sorted)
print(betClos_sorted)
print(betEige_sorted)


# Ok, now let's try to visualize the differences between centralities in terms of


colors = []
for n in G.nodes:
    colors.append(float(nx.betweenness_centrality(G)[n]))
nx.spring_layout(G)
nx.draw(G, with_labels=True, node_color=colors, cmap=plt.colormaps['Blues'])
plt.show()

# If we want to check a new network or new centralities, remember to recreate an empty list of "colors"
colors = []
for n in G.nodes:
    colors.append(float(nx.closeness_centrality(G)[n]))
nx.spring_layout(G)
nx.draw(G, with_labels=True, node_color=colors, cmap=plt.colormaps['Blues'])
plt.show()

colors = []
for n in G.nodes:
    colors.append(float(nx.eigenvector_centrality(G)[n]))
nx.spring_layout(G)
nx.draw(G, with_labels=True, node_color=colors, cmap=plt.colormaps['Blues'])
plt.show()


# Wow! 20 appears to be always the most central person. But is it always the case?
# Let's create an ad-hoc network, called kite network.

# Let us first create an empty network.
G1 = nx.Graph()

# We don't need to add nodes and edges. We can, in fact, simply add edges. The networkx package knows that we're
# implicitly adding nodes

G1.add_edge(1, 2)
G1.add_edge(1, 3)
G1.add_edge(1, 6)
G1.add_edge(1, 4)
G1.add_edge(2, 4)
G1.add_edge(2, 5)
G1.add_edge(2, 7)
G1.add_edge(3, 4)
G1.add_edge(3, 6)
G1.add_edge(4, 6)
G1.add_edge(4, 7)
G1.add_edge(4, 5)
G1.add_edge(5, 7)
G1.add_edge(6, 7)
G1.add_edge(6, 8)
G1.add_edge(7, 8)
G1.add_edge(8, 9)
G1.add_edge(9, 10)
nx.spring_layout(G1)
nx.draw(G1, with_labels=True)
plt.show()

# Let's see who's more central

degCent_sorted = dict(sorted(nx.degree_centrality(G1).items(), key=lambda item: item[1], reverse=True))
print('Most Central node:', list(degCent_sorted)[0])
print('Least Central node:', list(degCent_sorted)[-1])

colors = []
pos = nx.spring_layout(G1)
for n in G1.nodes:
    colors.append(float(nx.closeness_centrality(G1)[n]))
nx.spring_layout(G1)
nx.draw(G1, with_labels=True, node_color=colors, cmap=plt.colormaps['Blues'], pos=pos)
plt.show()

colors = []
for n in G1.nodes:
    colors.append(float(nx.closeness_centrality(G1)[n]))
nx.spring_layout(G1)
nx.draw(G1, with_labels=True, node_color=colors, cmap=plt.colormaps['Blues'], pos=pos)
plt.show()

colors = []
for n in G1.nodes:
    colors.append(float(nx.eigenvector_centrality(G1)[n]))
nx.spring_layout(G1)
nx.draw(G1, with_labels=True, node_color=colors, cmap=plt.colormaps['Blues'], pos=pos)
plt.show()


"""
Task


Let's now try what we learnt using a brand new dataset.

Pick and download a dataset at the site https://networkrepository.com/network-data.php 

You can pick whatever network you want but consider that networks with more than 500 nodes start to be heavy for your 
machine. Something with 30/200 nodes should be good!

The type of files you will meet are matrix files (.mtx).

I'm leaving you the script to open a mtx file and to convert it into a numpy array. Is there a function in networkx to 
convert a matrix or numpy array into a networkx Graph? (yes, try to find it)





from scipy.io import mmread
datamatrix=mmread('\\this\\is\\the\\path\\to\\your\\file.mtx')

npmatrix=datamatrix.A






Try to represent graphically the network and describe what you see.
 
Try some measurement we tested together and, if you want, you can also try something more (check the site regarding 
networkx). Write a quick report with possible explanation regarding what are the possible reasons for discrepancies in 
terms of centrality in your specific network (consider the subject and the type of network you're observing). 

Include everything in a .py file and send it to sasha.piccione@unive.it

Remember that the .py script must be executable without mistakes or interruption.













Here is the third part
"""
