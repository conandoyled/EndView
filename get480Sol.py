outfile = open('puzzle480.txt','w')
c = 0
for i in ['A','E']:
    for j in ['A','E']:
        for k in ['A','B','C','E','G']:
            print(str(c)+'\n8\nABCDEFG\nBGFD'+i+j+'FC\nCAEDBCFG\nDFEB'+k+'CAG\nBGAFCEDD')
            c += 1
print("Done")
