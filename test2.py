import sys
if len(sys.argv)>1 :
    print ('Per Hour: ' + str(float(sys.argv[1])/12/30/8)) 
    print ('Per Day: ' + str(float(sys.argv[1])/12/30))
    print ('Per Month: ' + str(float(sys.argv[1])/12)) 
else:
    print('please provide an annual income income')