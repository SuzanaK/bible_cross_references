#!/usr/bin/env python 
# -*- coding: utf-8 -*-

from __future__ import division
from collections import defaultdict
import codecs

import numpy as np
import matplotlib.pyplot as plt

# bible book names in german - replace if necessary 
books = ['1. Mose',
 '2. Mose',
 '3. Mose',
 '4. Mose',
 '5. Mose',
 'Josua',
 'Richter',
 'Ruth',
 '1. Samuel',
 '2. Samuel',
 '1. Könige',
 '2. Könige',
 '1. Chronika',
 '2. Chronika',
 'Esra',
 'Nehemia',
 'Esther',
 'Hiob',
 'Psalm',
 'Sprüche',
 'Prediger',
 'Hohes Lied',
 'Jesaja',
 'Jeremia',
 'Klagelieder',
 'Hesekiel',
 'Daniel',
 'Hosea',
 'Joel',
 'Amos',
 'Obadja',
 'Jona',
 'Micha',
 'Nahum',
 'Habakuk',
 'Zephanja',
 'Haggai',
 'Sacharja',
 'Maleachi',
 'Matthäus',
 'Markus',
 'Lukas',
 'Johannes',
 'Apostelgeschichte',
 'Römer',
 '1. Korinther',
 '2. Korinther',
 'Galater',
 'Epheser',
 'Philipper',
 'Kolosser',
 '1. Thessalonicher',
 '2. Thessalonicher',
 '1. Timotheus',
 '2. Timotheus',
 'Titus',
 'Philemon',
 'Hebräer',
 'Jakobus',
 '1. Petrus',
 '2. Petrus',
 '1. Johannes',
 '2. Johannes',
 '3. Johannes',
 'Judas',
 'Offenbarung']


# convert to unicode 
books = [b.decode('utf-8') for b in books]

data = np.genfromtxt('../data/all_cross_refs_abs.csv', delimiter=';')
data = np.log(data) #natural log 


plt.figure(figsize=(4, 4), dpi=300)

plt.imshow(data, interpolation='nearest', cmap=plt.cm.jet)

plt.xticks(range(66))
plt.yticks(range(66))
plt.axes().set_xticklabels(books, rotation=40, ha='right')
plt.axes().set_yticklabels(books)
plt.tick_params(axis='both', which='both', bottom='off', top='off', left='off', right='off', labelsize=3)
plt.tick_params(axis='x', which='both', direction=70, labelsize=2.5)

plt.savefig(('../plots/heatmap_bible_references.png'), dpi=600)
#plt.show()
