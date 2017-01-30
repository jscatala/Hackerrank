# Remove does not rise KeyError, returns None
# discard does not rise KeyError if e not in, returns None
# pop does raises KeyError, and returns e
class SetHandler():
    def __init__(self, numbers):
        self.s = set(map(int, numbers))
        self.functions = {
                          'pop': self.pop,
                          'remove': self.remove,
                          'discard': self.discard
                          }
 
    def pop(self, args=None):
        if args:
            self.s.pop(args)
        else:
            self.s.pop()  

    def remove(self, args=None):
        self.s.remove(args) 
    
    def discard(self, args=None):
        self.s.discard(args)    

    def sum(self):
        return sum(self.s) 

    def digest_line(self, line):
        line = line.strip().split()
        if len(line)>1:
            self.functions[line[0]](int(line[1]))
        else:
            self.functions[line[0]]()

if __name__ == '__main__':
    len_s = int(input())
    s = input().split()
    ops = int(input())
    set_obj = SetHandler(s)
    for i in range(0, ops):
        set_obj.digest_line(input())
    print(set_obj.sum())
