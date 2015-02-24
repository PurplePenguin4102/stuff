

###################################################################
#
#   CSSE1001/7030 - Assignment 1
#
#   Student Number: s4081775
#
#   Student Name: Joseph Ray
#
###################################################################

#####################################
# Support given below - DO NOT CHANGE
#####################################

from assignment_support import *

#####################################
# End of support 
#####################################

def load_data(dateStr):
    """takes a string representing a date in the correct format and returns a
    list of data for each minute of the day in time order

    load_data(str) = list
    """

    
    text = get_data_for_date(dateStr) 
    blocks = text.splitlines() 
    data = []

    for rawdata in blocks:
        rawdata = rawdata.split(',') #we create the raw data from the string. rawdata = ["time","temp","sunlight","power1",...,"power9"]
        time, rawdata = rawdata[0], map(float,rawdata[1:])  #We create a new raw data that doesn't include time (because we've already stored it separately) and maps all numbers to floats

        event = (time,rawdata[0],rawdata[1],tuple(rawdata[2:])) #From this point forward, event will be used to refer to an "event" object, event = ("time", temp, sunlight, (powers))
        data.append(event) #our answer is a list of events, which will be referred to as "data" in future
    
    return data
    

def max_temperature(data):
    """takes data produced by load_data and returns
    a pair consisting of the maximum temperature
    and the list of all the times at which the temperature
    was maximum

    """

    templist = []
    
    for event in data:
        templist.append(event[1]) #event is an "event" object, so the second element (event[1]) will be the temperature for that minute
    maxtemp = sorted(templist)[-1] #We create a list of temperatures and order them, the maximum will be the final element, this is less memory efficient, but I believe list processing is faster

    timelist = []
    for event in data:
        if maxtemp == event[1]:
            timelist.append(event[0]) #if our maxtemp is the same temperature as the temperature in that minute, store the time in timelist. "else: pass" is implied

    ans = (maxtemp, timelist) 
    return ans

def total_energy(data):
    """ takes data as produced by load_data and returns the
    total power produced in kWh of all the arrays over the entire day."""
    #The way we do this question, is to first sum the tuple stored in event[3], then store that. That value represents the power output over all the grids for 1 minute
    #Because we want the power output for all minutes, we then sum over the minutes to get the total energy for the entire day
    minute_total = []
    
    for event in data:
        powerkWh = [] #We do a conversion to kWh and store the powers as a list to allow sums
        
        for i in event[3]:
            powerkWh.append(i*(float(1)/float(60000))) #0.00001666 is the conversion rate

        minute_total.append(sum(powerkWh)) #contains the total output for that minute

    return sum(minute_total) 
        
def maximum_output(data):

    outputs = []
    for event in data:
        outputs.append(event[3])  #We extract the event[3] tuples for easier access and call it outputs.

    maximums = []
    for i in range(0,len(outputs[0])):        
        dummy = [] #we create a dummy list, this list will contain all the outputs for array 1, then all the outputs for array 2 etc. until i == len(outputs)
        for row in outputs: #the outputs list can be thought of as a matrix, with the rows being minutes and the columns being arrays. for each minute we want to store information for a single array in dummy
            dummy.append(row[i])         
        maximums.append(sorted(dummy)[-1]/1000.0) #we sort dummy and then take the largest value, this is why dummy is a list so we can run sorted, there's also a conversion to kW

    return zip(ARRAYS,maximums)
    
def display_stats(date):

    data = load_data(date)

    temp = max_temperature(data)
    energy = total_energy(data)
    outputs = maximum_output(data)
    
    print "\nStatistics for {0} \n".format(date)
    print "Maximum Temperature: {0}C at times".format(temp[0]), ", ".join(temp[1])
    print "\nTotal Energy Production: {0:.1f}kWh \n".format(energy)
    print "Maximum Power Outputs: \n"

    for t in outputs:
        print "{0:<25}{1:>15}kW".format(t[0],t[1])

    print " "
    return

def display_weekly_data(dateStr):

    (day,month,year) = dateStr.split('-') 

    start = datetime.date(int(year),int(month),int(day))
    
    dates = []
    for i in range(7):
        dates.append(str(start))
        start += datetime.timedelta(days=1) 

    data = []
    for c in dates:
        (year,month,day) = c.split('-')    
        data.append(get_max_data(day+'-'+month+'-'+year)[:-2]) 
    
    print WEEKLY_HEADER

    for d in data:
        event = d.split(',')
        s = sum(map(float, event[3:]))
        print WEEKLY_ROW.format(event[0],float(event[1]),float(event[2]),float(s)/1000.0)

    return


commands = {'date ': 'display_stats',
            "week ": 'display_weekly_data'}


def interact():
    print "Welcome to PV Calculator!\n"

    while True:
        c = raw_input("Command:" )
       
        if c[:5] in commands:
            try:
                eval(commands[c[:5]])(c[5:])
            except Exception:
                print "unknown command: {0}\n".format(c)
        elif c == 'q':
            break
        else:
            print "unknown command: {0}\n".format(c)
    return

##################################################
# !!!!!! Do not change (or add to) the code below !!!!!
# 
# This code will run the interact function if
# you use Run -> Run Module  (F5)
# Because of this we have supplied a "stub" definition
# for interact above so that you won't get an undefined
# error when you are writing and testing your other functions.
# When you are ready please change the definition of interact above.
###################################################

#if __name__ == '__main__':
#    interact()
#
