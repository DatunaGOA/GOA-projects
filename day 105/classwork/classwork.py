def count_first_char(s):  # vigebt definitons
    if len(s) == 0:   #tu s sigrdze == 0
        return 0   #mash gamovitanot nuli
    return s.count(s[0])   #s.count datvla da s[0] ari sityvis pirveli aso


rogorxar = "kargad"
rogorxar2 = "dzalian kargad"
print (count_first_char(rogorxar)) #gamoitans 1 radgan marto k aris pirveli aso
print (count_first_char(rogorxar2))


