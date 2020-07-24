# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
def pt():
    try:
        n = int(input('enter number of electrons:'))
    except ValueError:
        print('number of elections should be an integer')
    
    print('you entered '+str(n)+' electrons')
    
    numok = 1
    if n < 1:
        print('n must be > 0')
        numok = 0
    if n > 54:
        print('n must be < 55 because this program only works for 5 rows')
        numok = 0
        """ determine row"""
    
    if numok == 1:
        
        r=0
        ''' row 5 has between 36 and 55 electrons '''
        if n < 55: 
            r=5 
        ''' row 4 has between 18 and 37 electrons '''
        if n < 37:
            r=4
        ''' row 3 has between 10 and 19 electrons '''
        if n < 19: 
            r=3 
        ''' row 2 has between 2 and 11 electrons '''
        if n < 11:
            r=2
        ''' row 1 has between 0 and 3 electrons '''
        if n < 3: 
            r=1 

        blurb = 'Row = ' + str(r)     
        print(blurb)
    

        c='TBD'
        '''
        These equations are based on the number of
        electrons in a given row
        '''
        
        ''' c = str((n-1)*7 + 1) + 'A' '''
        if r == 1:
            c= str((n-1)*7 + 1) + 'A'       

        ''' c = n - 2 + 'A' '''
        if r == 2:
            m=n-2
            c= str(m) + 'A'
            
        ''' c = n - 10 + 'A' '''
        if r == 3:
            m=n-10
            c= str(m) + 'A'
         
        ''' c = n - 18 + 'A' '''
        if r == 4:
            m=n-18
            ''' These are the A columns '''
            if m < 3:
                c= str(m) + 'A'
            if m > 12:
                c= str(m-10) + 'A'
            ''' These are the B columns '''
            if m > 2 and m < 8: 
                c= str(m) + 'B'
            if m >10 and m < 13:
                c= str(m-10) + 'B'
            if m > 7 and m < 11:
                c= str(8) + 'B'                

        ''' c = n - 18 + 'A' '''
        if r == 5:
            m=n-36
            ''' These are the A columns '''
            if m < 3:
                c= str(m) + 'A'
            if m > 12:
                c= str(m-10) + 'A'
            ''' These are the B columns '''
            if m > 2 and m < 8: 
                c= str(m) + 'B'
            if m >10 and m < 13:
                c= str(m-10) + 'B'
            if m > 7 and m < 11:
                c= str(8) + 'B'       

        print('Col = ' + c)

        g = 'Transition Metal'               
        if c=='1A':
            g = 'Alkaline Metal'
        if c=='2A':
            g = 'Alkaline Earth Metal'
        
        '''
        if c=='3A':
            g = 'Transitional Metal'
        '''
           
        if c=='4A':
            g = 'Carbon Family'
        if c=='5A':
            g = 'Nitrogen Family'
        if c=='6A':
            g = 'Oxygen Family'
        if c=='7A':
            g = 'Halogen'
        if c=='8A':
            g = 'Noble Gas'
            
            
        print('Group=' + g)
            
    else:
        print('ERROR! !!!!!!!!!!!!!!!!!!')
        print('ERROR! !!!!!!!!!!!!!!!!!!')
        print('Try again with 0 < n < 55')
        print('ERROR! !!!!!!!!!!!!!!!!!!')
        print('ERROR! !!!!!!!!!!!!!!!!!!')
        
pt()
