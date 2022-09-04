# Enter your code here. Read input from STDIN. Print output to STDOUT

import re

class Main():
    def __init__(self):
        self.n = int(input())
        
        for i in range(self.n):
            self.a = input()
            print(bool(re.match(r'^[-+]?[0-9]*\.[0-9]+$', self.a)))
                    
if __name__ == '__main__':
    obj = Main()
    
    