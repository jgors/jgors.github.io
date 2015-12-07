#!/usr/bin/python

"""
#----------------------------------------------------------------
Author: Jason Gors <jasonDOTgorsATgmail>
Creation Date: 04-13-2015
Purpose:
#----------------------------------------------------------------
"""


TITLE = 'Jason Gors'

H1 = '''Data Scientist, <br/>
Software Engineer, <br/> 
adorable things enthusiast.
''' 

RESUME = 'pdfs/Jason_Gors_Resume.pdf'

H2 = '''A bit about me'''

P1a = '''I have done graduate work in statistics (frequentist & bayesian) and 
statistical methods, and as a data scientist I routinely use statistical & machine 
learning analysis tools & techniques.  I also wear many hats as a generalist 
software engineer. In these roles, I enjoy using 
<a href="http://www.vim.org">Vim</a>, 
within 
<a href="http://tmux.sourceforge.net">Tmux</a>, 
from a 
<a href="http://www.zsh.org">Z-shell</a> 
environment, whilst inside Linux.'''

P1b = '''Moreover, I have several years of experience in programming with 
<a href="http://www.python.org">Python</a> 
and 
<a href="http://www.r-project.org">R</a>
(among other languages),
where I enjoy using many different data analysis libraries, including 
<a href="http://www.numpy.org">NumPy</a>, 
<a href="http://www.scipy.org">SciPy</a>, 
<a href="http://scikit-learn.org">Scikit-Learn</a>, 
<a href="http://pandas.pydata.org">Pandas</a>,
<a href="http://ipython.org">IPython</a>,
as well as many data visualization libraries.'''

P3 = '''Drop me a line if you'd like to say hi.''' 

ADDRESS = '''Hanover, NH 03755<br/>
United States'''

#PHONE = '402.606.1081'
MAILTO = 'mailto:jason.gors@gmail.com'
EMAIL = 'jasonDOTgorsATgmail'
GITHUB = 'https://github.com/jgors'
GOOGLE_PLUS = 'https://plus.google.com/114658657385978136683'
TWITTER = 'https://twitter.com/jasongors'
AUTHOR = TITLE


if __name__ == '__main__':
    index_edited = open('index_edited.html', 'r').read().format(**locals())
    with open('index.html', 'w') as index:
        index.writelines(index_edited)
