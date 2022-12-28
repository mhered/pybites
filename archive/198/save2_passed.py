from datetime import date, datetime


MAC1 = """
reboot    ~                         Wed Apr 10 22:39
reboot    ~                         Wed Mar 27 16:24
reboot    ~                         Wed Mar 27 15:01
reboot    ~                         Sun Mar  3 14:51
reboot    ~                         Sun Feb 17 11:36
reboot    ~                         Thu Jan 17 21:54
reboot    ~                         Mon Jan 14 09:25
"""

YEAR=date.today().year

def calc_max_uptime(reboots):
    """Parse the passed in reboots output,
       extracting the datetimes.

       Calculate the highest uptime between reboots =
       highest diff between extracted reboot datetimes.

       Return a tuple of this max uptime in days (int) and the
       date (str) this record was hit.

       For the output above it would be (30, '2019-02-17'),
       but we use different outputs in the tests as well ...
    """
    time_objects=[]
    for line in reboots.strip().splitlines():
        _, timestamp_raw =line.split('~')
        timestamp=f'{YEAR} {timestamp_raw.strip()[4:]}'
        time_objects.append(datetime.strptime(timestamp,'%Y %b %d %H:%M'))
        # print(timestamp, str(time_object))
    
    durations = [(
                    (time_objects[i]-time_objects[i+1]).days, 
                    datetime.strftime(time_objects[i],'%Y-%m-%d')
                    ) for i in range(len(time_objects)-1)
                ]
    return max(durations, key=lambda x:x[0])
        
        
print(calc_max_uptime(MAC1))