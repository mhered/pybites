INDENTS = 4
rosetti_unformatted = """
                      Remember me when I am gone away,
                      Gone far away into the silent land;
                      When you can no more hold me by the hand,

                      Nor I half turn to go yet turning stay.

                      Remember me when no more day by day
                      You tell me of our future that you planned:
                      Only remember me; you understand
"""

shakespeare_unformatted = """
                          To be, or not to be, that is the question:
                          Whether 'tis nobler in the mind to suffer

                          The slings and arrows of outrageous fortune,
                          Or to take Arms against a Sea of troubles,
                          """


def print_hanging_indents(poem):

    indent =""
    for line in poem.splitlines():
        if len(line.lstrip())==0:
            indent = ""
        else:
            print(indent+line.lstrip())
            indent=INDENTS*" "
            
print_hanging_indents(shakespeare_unformatted)