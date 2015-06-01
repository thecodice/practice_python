#a markov chain is a way to prdict what to do next based on what you did recently.it maintains a fixed series of states,and based on those states determines what to do next.it is something like walking a path.

#the direction you take on your next step is determind by a fixed number of previous steps.The number of previous steps that are remembered is fixed at the beginning of the process.

#lets construct a markov chain using dictionary.the key being two previous words and the value as the next word.

#random.sample() and random.randint()
import sys
import random

the_filename = sys.argv[1]
 
def process_file():
    f = open(str(the_filename),"r+")
    file_content = f.readlines()
    return file_content
    
def make_markov_relationship():
    content = process_file()
    all_in_one = "".join(content)
    splitted = all_in_one.split(" ")
    markov = {}
    how_far_key = 2
    for i in range(len(splitted)):
        if i == 0 or i == 1:
            pass
        else:
            if str(splitted[i-2])+" " + str(splitted[i-1]) not in markov:
                markov[str(splitted[i-2])+" " + str(splitted[i-1])] = [splitted[i]]
            else:
                markov[str(splitted[i-2])+" " + str(splitted[i-1])].append(splitted[i])        
                print "easdgsd"
    return markov
def party():
    s = make_markov_relationship()
    with open("output.txt","a") as f:
        for i in range(80):
            parents =  random.sample(s,10)
            for item in range(len(parents)):
                f.write(str(parents[item]) + " " + " ".join(random.sample(s[parents[item]],1)))
         
                    
            f.write(".")
            f.write("\n")        
    return "am done"

party()
