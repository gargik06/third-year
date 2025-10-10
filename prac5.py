from random import randint

if __name__ == '__main__':
    P = 23
    G = 9
    
    print('The value of P is: %d' % (P))
    print('The value of G is: %d' % (G))
    
    a = 4
    print('Secret number for Alice is: %d' % (a))
    x = int(pow(G, a, P))
    
    b = 3
    print('Secret number for Bob: %d' % (b))
    y = int(pow(G, b, P))
    
    ka = int(pow(y, a, P))
    kb = int(pow(x, b, P))
    
    print('Secret key for Alice is: %d' % (ka))
    print('Secret key for Bob is: %d' % (kb))
