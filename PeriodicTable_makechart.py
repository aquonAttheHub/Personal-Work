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
        
#pt()
def readwrite():
    infile = 'test.data'
    outfile = 'out.data'
    f = open(infile)
    f2 = open(outfile, "w")
    for line in f:
        x = int(line)
        print("read in " + line)
        f2.write(str(x+1) + "\n")
    f.close()
    f2.close()

#    newfile = 'out.data'
    f3 = open('out.data')
    for line in f3:
        print("I read this:" + line)
    f3.close()

#readwrite()

def pt2(n):
    try:
#        n = int(input('enter number of electrons:'))
#        print(n)
        j=n
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
        
#pt(

def testpt2():
#    for i in 5, 10, 15, 23:
#        print(i)
        
    for i in range(5):
        j=i+1
#        print(j)
        pt2(j)
        
#testpt2()


def filept2(n, fname):
    try:
#        n = int(input('enter number of electrons:'))
#        print(n)
        j=n
        print(fname)
        f=open(fname,"a")
    except ValueError:
        print('number of elections should be an integer')
        
    print('you entered '+str(n)+' electrons')
    f.write("\n" + 'you entered '+str(n)+' electrons')
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
        f.write(blurb)

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
        f.write("\n" + 'Col = ' + c)

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
        f.write("\n" + 'Group=' + g)
            
    else:
        print('ERROR! !!!!!!!!!!!!!!!!!!')
        print('ERROR! !!!!!!!!!!!!!!!!!!')
        print('Try again with 0 < n < 55')
        print('ERROR! !!!!!!!!!!!!!!!!!!')
        print('ERROR! !!!!!!!!!!!!!!!!!!')
        
    f.close()
        
def testfilept2():
    f=open("periodicTable.data","w")
    f.close()
    
    for i in range(54):
        j=i+1
        filept2(j, "periodicTable.data")
   
    
#testfilept2()   
def filept3(n, fname):
    try:
#        n = int(input('enter number of electrons:'))
#        print(n)
        j=n
        print(fname)
        f=open(fname,"a")
        cfile = fname + ".corr" 
        f2=open(cfile,"a") 
        
        g_line = ''
        
    except ValueError:
        print('number of elections should be an integer')
        
    print('you entered '+str(n)+' electrons')
    f.write("\n" + 'you entered '+str(n)+' electrons')
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
        f.write(blurb)
        g_line = g_line + str(r)

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
        f.write("\n" + 'Col = ' + c)
 
        c2 = 0
        if c == '1A': 
            c2 = 1
        if c == '2A': 
            c2 = 2
        if c == '3B': 
            c2 = 3
        if c == '4B': 
            c2 = 4
        if c == '5B': 
            c2 = 5
        if c == '6B': 
            c2 = 6
        if c == '7B': 
            c2 = 7
        if c == '8B': 
            c2 = 8
        if c == '1B': 
            c2 = 11
        if c == '2B': 
            c2 = 12
        if c == '3A': 
            c2 = 13
        if c == '4A': 
            c2 = 14
        if c == '5A': 
            c2 = 15
        if c == '6A': 
            c2 = 16
        if c == '7A': 
            c2 = 17
        if c == '8A': 
            c2 = 18

         #this is the actual column in the table
         #works for all columns except 8,9, 10
        g_line = g_line + "," + str(c2)
        
        # this is the column name
        g_line= g_line + "," + str(c)
        
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
        f.write("\n" + 'Group=' + g)
        g_line = g_line + "," + g
        
        
    else:
        print('ERROR! !!!!!!!!!!!!!!!!!!')
        print('ERROR! !!!!!!!!!!!!!!!!!!')
        print('Try again with 0 < n < 55')
        print('ERROR! !!!!!!!!!!!!!!!!!!')
        print('ERROR! !!!!!!!!!!!!!!!!!!')
    
    g_line = g_line + "," + str(n)
    f2.write(g_line + "\n")    
    
    f2.close()
    f.close()
       
def testfilept3():
    
    test = "periodicTable.data"
    f=open(test,"w")
    f.close()
    f2=open(test + ".corr","w")
    f2.close()

    
    for i in range(54):
        j=i+1
        filept3(j, test)
   
testfilept3()