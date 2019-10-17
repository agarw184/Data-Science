import re

#Match phone numbers. Return True or False. See README for details.
def problem1(searchstring):
    #fill in
    p1 = re.compile(r'\(\d{3}\)\s\d{3}[-]\d{4}')
    p2 = re.compile(r'\d{3}[-]\d{3}[-]\d{4}')
    p3 = re.compile(r'\d{3}[-]\d{4}')
    if p1.fullmatch(searchstring) or p2.fullmatch(searchstring) or p3.fullmatch(searchstring):
        return True
    else:
        return False

#Extract street name from address. See README for details.
def problem2(searchstring):
    #fill in
    p = re.compile(r'(\d+)\s(.+)\s(Rd\.|Ave\.|Dr\.|St\.)')
    m = p.search(searchstring)
    if m :
        return m.group(2)
    else:
        return False

#Garble street name. See README for details
def problem3(searchstring):
    #fill in

    p = re.compile(r'(\d+\s)(.+)(\s(Rd\.|Ave\.|Dr\.|St\.))')
    m = p.search(searchstring)
    if m :
        oldstring = m.group(1) + m.group(2) + m.group(3)
        reversestring = m.group(2)[::-1]
        newstring = m.group(1) + reversestring + m.group(3)
        return re.sub(oldstring,newstring,searchstring)
    else:
        return False

if __name__ == '__main__' :

    print(problem1('765-494-4600')) #True
    print(problem1(' 765-494-4600 ')) #False
    print(problem1('(765) 494 4600')) #False
    print(problem1('(765) 494-4600')) #True
    print(problem1('494-4600')) #True

    print(problem2('The EE building is at 465 Northwestern Ave.')) #Northwestern
    print(problem2('Meet me at 201 South First St. at noon')) #South First

    print(problem3('The EE building is at 465 Northwestern Ave.'))
    print(problem3('Meet me at 201 South First St. at noon'))
