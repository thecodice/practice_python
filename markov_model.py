#a markov chain is a way to prdict what to do next based on what you did recently.it maintains a fixed series of states,and based on those states determines what to do next.it is something like walking a path.

#the direction you take on your next step is determind by a fixed number of previous steps.The number of previous steps that are remembered is fixed at the beginning of the process.

#lets construct a markov chain using dictionary.the key being two previous words and the value as the next word.

#random.sample() and random.randint()
import sys
the_file = sys.argv[1]
class Markovchain:

    def __init__(self):
        self.filename = the_file

    def process_file(self):
        f = open(str(self.filename,"r+"))
        file_content = f.readlines()
        return file_content
        #:def make_markov_relationship(self):

    def party(self):
        content = self.process_file()
        print content

markov_1 = Markovchain()
markov_1.party()
