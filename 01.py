movies = ["The Holy Grail", 1975,"Terry Jones & Terry Gilliam",91, ["Graham Chapman",["Michael Palin","John Cleese","Terry Gilliam","Eric Idle"]]]
'''
for L1 in movies:
    if isinstance(L1,list):
        for L2 in L1:
            if isinstance(L2,list):
                for L3 in L2:
                    print(L3)
            else:
                print(L2)
    else:
        print(L1)
'''

def _Level_(List):
    for L1 in List:
        if isinstance(L1,list):
            _Level_(L1)
        else:
            print(L1)

_Level_(movies)
