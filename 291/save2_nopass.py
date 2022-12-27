from datetime import timedelta, datetime
from typing import List


def get_srt_section_ids(text: str) -> List[int]:
    """Parse a caption (srt) text passed in and return a
       list of section numbers ordered descending by
       highest speech speed
       (= ratio of "time past:characters spoken")

       e.g. this section:

       1
       00:00:00,000 --> 00:00:01,000
       let's code

       (10 chars in 1 second)

       has a higher ratio then:

       2
       00:00:00,000 --> 00:00:03,000
       code

       (4 chars in 3 seconds)

       You can ignore milliseconds for this exercise.
    """
    lines=iter(text.lstrip().splitlines())
    for line in lines:
        section=int(line)
        timing=next(lines)
        start,stop=timing.split(' --> ')
        start=datetime.strptime(start.split(',')[0], '%H:%M:%S')
        stop=datetime.strptime(stop.split(',')[0], '%H:%M:%S')
        speech_lines=[]
        speech_line=next(lines)
        while speech_line:
            speech_lines.append(speech_line)
            try:
                speech_line=next(lines)
            except StopIteration:
                speech_line =''
        
        speech='\n'.join(speech_lines)
        print('##'.join([str(section),str(start),str(stop),speech]))
    
    
    
    
text = """
1
00:00:00,498 --> 00:00:02,827
Beautiful is better than ugly.

2
00:00:02,827 --> 00:00:06,383
Explicit is better than implicit.
Second line for the laughs.

3
00:00:06,383 --> 00:00:09,427
Simple is better than complex.
"""

print(get_srt_section_ids(text))