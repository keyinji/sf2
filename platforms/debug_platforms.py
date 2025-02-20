def pillar_from(platforms, height, platform_y1, platform_y2):
    '''
    :param platforms: a list of platforms (as lists)
    :param height: vertical position
    :param horizontal_pos: horizontal position
    :return : minimum length of pillar from height and horizontal_pos to the platform/ground below
    '''
    for platform in platforms:
        bottom = 0
        if platform[0] > height and (platform[1] in range(platform_y1, platform_y2) or platform[2] in range(platform_y1, platform_y2)):
            
    return height - bottom

n = int(input("No of platforms: "))

platforms = []

# read input from user as lists of integers
for i in range(n):
    platform = input().split()
    platforms.append(platform)

for i in range(len(platforms)):
    for j in range(len(platforms[i])):
        platforms[i][j] = int(platforms[i][j])

print(platforms)
total = 0

for platform in platforms:    
    total = total + pillar_from(platforms, platform[0], platform[1], platform[2])

print(total)
