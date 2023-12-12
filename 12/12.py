with open("input.txt") as file:
    data = file.readlines()
data = [x.strip() for x in data]
data = [x.split() for x in data]
data = [(a,list(map(int, b.split(",")))) for a,b in data]

def is_valid(s:str, l:tuple[int]):
    if sum(l) != s.count("#"):
        return False
    
    count = 0
    broken = []
    for c in s:
        if c=="#":
            count +=1
        elif count>0:
            broken.append(count)
            count = 0
    
    if count> 0:
        broken.append(count)
    
    return broken == l

def can_be_valid(s:str, l:tuple[int]):
    n_springs = sum(l)
    n_planned = s.count("#")
    n_left = s.count("?")
    if n_planned + n_left < n_springs:
        return False
    
    i = 0
    count = 0
    broken = []
    while  i < len(s) and s[i]!= "?":
        if s[i]=="#":
            count +=1
        elif count>0:
            broken.append(count)
            count = 0
        i+=1

    sub:str = "".join(map(str,broken))
    if sub in "".join(map(str,l)):
        return True
    
    return False



def fill(s:str,l:tuple[int],i:int):
    if i == len(s):
        return 1 if is_valid(s,l) else 0
    if not can_be_valid(s,l):
        return 0    

    if s[i] == "?":
        return fill(s[:i]+"#"+s[i+1:], l, i+1) + fill(s[:i]+"."+s[i+1:], l, i+1)
    else:
        return fill(s, l, i+1)

        
res = 0
for line in data:
    s, l = line
    res += fill(s,l,0)
print(res)

cache = {}
# i: index in s
# li: index in l
# current: length of current "#" block
def fill2(dots,blocks,i,bi,current):
    key = (i, bi, current)
    if key in cache:
        return cache[key]
    
    if i == len(dots):
        if bi==len(blocks) and current == 0:
            return 1
        elif bi==len(blocks)-1 and blocks[bi]==current:
            return 1
        else:
            return 0

    ans = 0
    for c in [".","#"]:
        if dots[i] == c or dots[i] == "?":
            if c=="." and current==0:
                ans+=fill2(dots,blocks,i+1,bi,0)
            elif c=="." and current > 0 and bi < len(blocks) and blocks[bi]== current:
                ans+=fill2(dots,blocks,i+1, bi+1, 0)
            elif c=="#":
                ans+=fill2(dots,blocks,i+1,bi,current+1)

    cache[key] = ans
    return ans

res = 0
data2 = [(((a+"?")*5)[:-1],b*5) for a,b in data]
for idx, line in enumerate(data2):
    print(f"current res {res}")
    print(f"{idx}/{len(data)}")
    s, l = line
    cache.clear()
    score = fill2(s,l,0,0,0)
    res += score
print(res)
