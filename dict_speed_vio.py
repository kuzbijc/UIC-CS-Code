
import datetime
import calendar

def wday(y, m, d):
    date = datetime.date(y, m, d)
    return calendar.day_name[date.weekday()]

def mname(mnumber):
    return calendar.month_name[mnumber]

def data(s):

    days = {}
    month = {}

    with open(s, 'r') as f:
        for line in f:
            if not line.startswith("ADDRESS"):
                l = line.split(",")
                date = l[2].split("/")
                
                m = int(date[0])
                d  = int(date[1])
                y = int(date[2])
                viol = int(l[3])
                wdayname = wday(y, m, d) 
                monthname = mname(m)

                if wdayname not in days:
                    days.update({wdayname: viol}) # or days[wdayname] = viol
                    #adds viol count to the dictionary for each day
                else:
                    days[wdayname] += viol # adds viol count to existent day in dictionary

                if monthname not in month:
                    month.update({monthname: viol})
                else:
                    month[monthname] += viol # adds viol count to existent day in dictionary

        #DAYS
        print("---DAYS---")
        d = sorted(days.items(), key = lambda x: x[1], reverse = True)
        for e in d:
            print("%s,%i" %(e[0], e[1])) # Friday most speeding tickets

        #MONTHS
        print("---MONTH---")    
        m = sorted(month.items(), key = lambda x: x[1], reverse = True)
        for e in m:
            print("%s,%i" %(e[0], e[1])) # Friday most speeding tickets

def main():
    
    data("speed_camera_violations.csv")
    #print(wday(2018, 10, 15))
    #print(mname(7)) # prints July

main()
