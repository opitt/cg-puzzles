def alphabet_war(fight):
    fight=list(fight)
    left="wpbst"
    right="mqdzj"
    priest="tj"
    power={"w":4,"p":3,"b":2,"s":1,"t":0,"m":4,"q":3,"d":2,"z":1,"j":0}
    revert={"wj":"m","pj":"q","bj":"d","sj":"z","mt":"w","qt":"p","dt":"b","zt":"s"}
    for i,c in enumerate(fight):
        if c in priest:
            if i-1>=0 and not any(p in fight[i-2:i] for p in priest):
                fight[i-1]=revert.get(fight[i-1]+c,fight[i-1])
            if i+1<len(fight) and not any(p in fight[i+1:i+3] for p in priest):
                fight[i+1]=revert.get(fight[i+1]+c,fight[i+1])
            
    leftpower=sum([power.get(c,0) for i,c in enumerate(fight) if c in left])
    rightpower=sum([power.get(c,0) for i,c in enumerate(fight) if c in right])

    return  "Right side wins!" if leftpower<rightpower else "Left side wins!" if leftpower>rightpower else "Let's fight again!"

alphabet_war("z")# , "Right side wins!" );
alphabet_war("tz")# , "Left side wins!" );
alphabet_war("jbdt")# , "Let's fight again!" );
print(alphabet_war("tbwjttqttjwtzbjsb")) # , "Left side wins!"

"""test.assert_equals( alphabet_war("jz") , "Right side wins!" );
test.assert_equals( alphabet_war("zt") , "Left side wins!" );
test.assert_equals( alphabet_war("sj") , "Right side wins!" );      
test.assert_equals( alphabet_war("azt") , "Left side wins!" );
test.assert_equals( alphabet_war("tzj") , "Right side wins!" );
test.assert_equals( alphabet_war("wololooooo") , "Left side wins!" );      
test.assert_equals( alphabet_war("zdqmwpbs") , "Let's fight again!" );
test.assert_equals( alphabet_war("ztztztzs") , "Left side wins!" );
"""
