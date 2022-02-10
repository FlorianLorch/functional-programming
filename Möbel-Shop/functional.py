"""
function Cook( i1, i2, f ) 
{ 
   alert("get the " + i1); 
   f(i1); 
   f(i2); 
} 

Cook( "lobster", "water", PutInPot ); 
Cook( "chicken", "coconut", BoomBoom );
"""


def Cook(i1, i2, f):
    print("get the" + i1)
    f(i1)
    f(i2)

Cook("Lobster", "Water", lambda x: print("in Pot: " + x))

mylist = [1,2,3]



def test(x):
    print(x)
    return lambda x : x*2

func = test(5)
print(func(2))

print(list(map(lambda x : x + 1, mylist)))



