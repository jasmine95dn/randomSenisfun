import re
import random
from sys import stdout, stdin

def create_vocab(filename):
    stdout.write('load %s\n'%(filename))
    with open(filename, 'r') as rawtext:
        lines = ''.join(rawtext)

    words = ['']+[word for word in re.split(r'(\n| )+', lines) if word not in [' ', '', '\n']]
    new_words =[]
    bow = {}
    
    for word in words:
        if re.search('[\.\?\!]$', word):
            new_words += [re.search('[\.\?\!]$', word).group(), '']
        else:
            new_words.append(word)

    bow = {}
    
    for i,word in enumerate(new_words[:-1]):
        if not re.search('[\.\?\!]$', word):
            if word not in bow.keys(): bow[word] = set()
            bow[word].add(new_words[i+1])

    return bow

def create_bow(word, bow):
    return bow[word]

def random_follower(words):
    return random.choice(tuple(words))

def create_random_sent(bow):
    start,sent='',[]
    sent.append(random_follower(bow[start]))

    # don't stop creating the sentence until mark of ending found
    while not re.search('[\.\?\!]$', sent[-1]):
        sent.append(random_follower(bow[sent[-1]]))

    return ' '.join(sent)+'\n'

def main():
    stdout.write('file to create vocab\n:')
    s=input()
    
    vocab = create_vocab(s)

    stdout.write('What to do next? Only break when command is \'break\', else process\n')
    command = input()
    while command.lower() != 'break':
        if not re.search('say(.)*something',command.lower()):
            stdout.write('word\n:')
            word = input()
            while word not in vocab:
                stdout.write('word not found, new word please!\n')
                word = input()
            followers = create_bow(word, vocab)
            
            stdout.write('%s\n'%followers)
            stdout.write('pick a random member: %s\n'%random_follower(followers))

            stdout.write('What to do next? Want to see a sentence? Then say something\n')
            command= input()
            
        else:
            stdout.write(create_random_sent(vocab))
            stdout.write('What to do next?\n')
            command= input()
if __name__ == '__main__':
    main()

    
                
        

    
        
    
