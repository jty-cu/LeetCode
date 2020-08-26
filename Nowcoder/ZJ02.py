# Consider
# 1.d1,d2的符号，分4种情况
# 2.已经完成的比赛场数和 k 的关系
# 3.打平所需的最少数量和 n-k 的关系

N = int(input())
for _ in range(N):
    n,k,d1,d2 = map(int,input().split())
    
    # 1>2,2>3
    minnow = d1+d2+d2
    if minnow<=k and (k-minnow)%3==0:
        left = n-k-(d1+d1+d2)
        if left>=0 and left%3==0:
            print('yes')
            continue
    # 1<2,2>3
    minnow = 2*max(d1,d2)-min(d1,d2)
    if minnow<=k and (k-minnow)%3==0:
        left = n-k-(d1+d2)
        if left>=0 and left%3==0:
            print('yes')
            continue
    # 1>2,2<3
    minnow = d1+d2
    if minnow<=k and (k-minnow)%3==0:
        left = n-k-(2*max(d1,d2)-min(d1,d2))
        if left>=0 and left%3==0:
            print('yes')
            continue
    # 1<2,2<3
    minnow = d1+d1+d2
    if minnow<=k and (k-minnow)%3==0:
        left = n-k-(d2+d1+d2)
        if left>=0 and left%3==0:
            print('yes')
            continue
    print('no')
        
