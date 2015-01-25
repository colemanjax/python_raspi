##var = raw_input("ANOTHER VIDEO (y/n)?: ")

while True:
    var = raw_input("ANOTHER VIDEO (y/n)?: ")
    if (str(var) == 'y'):
    ##if (int(var) == '1'):
        var_fileheader = raw_input("Enter animal ID and day (e.g.: mouseB_day1): ")
        print("New filename = "+var_fileheader+"_picam001.h264")

##        print "you entered ", var
##    else:
##        break;
##        print "exiting..."
    if (str(var) == 'n'):
        print "exiting..."
        break;

##x = 1
##
##i_cmd = 1
##while True:
##  s = raw_input('Input [{0:d}] '.format(i_cmd))
##  i_cmd += 1
##  n = len(s)
##  if n > 0 and s.lower() == 'break'[0:n]:
##    break
##  exec(s)
##
##print 'x = ', x
##print 'I am out of the loop.'
