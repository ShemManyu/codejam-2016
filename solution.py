fh = open('A-small-practice.in', 'r')
target = open('soultion.txt', 'w')
n = 0
next(fh)
for line in fh.readlines():
    combinations = []
    if len(line.strip()) == 1:
        combinations.append(line)
        n += 1
        #print('Case #{}: {}'.format(n, combinations[0]), end='')
        target.write('Case #{}: {}'.format(n, combinations[0]))
    else:
        frontier = [line[1] + line[0], line[0] + line[1]]
        while len(combinations) < (2 ** len(line.strip())):
            if len(frontier) > 0 : node = frontier.pop()
            if len(node) == len(line.strip()):
                combinations.append(node)
            else:
                frontier.append(line[len(node)] + node)
                frontier.append(node + line[len(node)])
        combinations.sort()
        n += 1
        #print('Case #{}: {}'.format(n, combinations[2 ** len(line.strip()) - 1]))
        target.write('Case #{}: {}\n'.format(n, combinations[2 ** len(line.strip()) - 1]))