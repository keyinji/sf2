'''
Input specificatrion:
first line is N number of vilalgerts
second line E number of eveniong 
next e lines contain lst lof villagers present each line beins with [ositive integer k
the number of villagers present this evening followed by K posiytib itegers separated by
spaces representing the villagers 
note that the bard is villager 1

ypu must ue set, if bard (1) is evening teaches villagers 1 new songif not there villagers exchange songs they know. must return all the villagers that know the song

sample input 
4
3
2 1 2
3 2 3 4
3 4 2 1

Output
1
2
4
input 2

8
5
4 1 3 5 4
2 5 6
3 6 7 8
2 6 2
5 2 6 8 1
output
1
2
6
8

'''

villagers = int(input())
evenings = int(input())

evn_attendees = []
for _ in range(evenings):
    line = input().split() 
    k = int(line[0])  
    attendees = set(int(x) for x in line[1:k+1])
    evn_attendees.append(attendees)

villagers_with_song = set()

for attendees in evn_attendees:
    if 1 in attendees: 
        villagers_with_song = attendees  
    else:  
        if villagers_with_song: 
            villagers_with_song.update(attendees)  

for villager in villagers_with_song:
    print(villager)