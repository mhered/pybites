def get_weekdays(calendar_output):
    """Receives a multiline Unix cal output and returns a mapping (dict) where
       keys are int days and values are the 2 letter weekdays (Su Mo Tu ...)"""
    
    cal_lines= calendar_output.splitlines()
    weekdays=[item.strip() for item in cal_lines[1].split()]
    
    result ={}
    for line in cal_lines[2:]:
        cal_days= [line[i:i+3] for i in range(0, len(line), 3)]
        for i, day in enumerate(cal_days):
            label = day.strip()
            if label:
                result[int(label)]=weekdays[i]
    return result

april_1981 = """     April 1981
Su Mo Tu We Th Fr Sa
          1  2  3  4
 5  6  7  8  9 10 11
12 13 14 15 16 17 18
19 20 21 22 23 24 25
26 27 28 29 30
"""


print(get_weekdays(april_1981))