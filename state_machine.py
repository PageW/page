import matplotlib.pyplot as plt
nums = [11,8,9,5,8,7,6,7,7,4,8,12,13,9,12,11,10,11,11,8,20]
dic = dict()
i = 0
for num in set(nums):
    dic[num] = i
    i += 1

def preProcess(nums,dic):
    new_nums = []
    for num in nums:
        new_nums.append(dic[num])
    return new_nums
#计算马尔科夫链
def caculateMarkovChain(nums,dic):
    numOfStates = len(dic)
    #一阶markov chain
    #pxy计算每一个从nums[i]到nums[i+1]的次数
    pxy = [[0.05]*numOfStates for _ in range(numOfStates)]
    for i in range(len(nums)-1):
        pxy[nums[i]][nums[i+1]] += 1
    #利用计算转移概率
    px = [0] * numOfStates
    for x in range(numOfStates):
        for y in range(numOfStates):
            px[x] += pxy[x][y]
    for x in range(numOfStates):
        for y in range(numOfStates):
            pxy[x][y] /= px[x]
    print('pxy=',pxy)
    return pxy
p1=caculateMarkovChain(preProcess(nums,dic),dic)
p2=caculateMarkovChain(preProcess(nums[5:],dic),dic)
#plt.figure()
#ax1=plt.subplot(121)
#plt.sca(ax1)
plt.matshow(p1)
#ax2=plt.subplot(122)
#plt.sca(ax2)
plt.matshow(p2)
plt.show()

