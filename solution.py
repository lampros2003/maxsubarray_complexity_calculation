from ast import If
import time
import pprint
import random
test_dataset = [[1,4] ,[1,14,-23,15] ,[-3,14,22,44,-14,32,-1,-98] 
,[12,41,-32,11,31,23,-22,-14,44,14,53,-31,15,-80,-14,100],[12,41,-32,11,31,23,-22,-14,44,14,53,-31,15,-80,-14,100,12,41,-32,11,31,23,-22,-14,44,14,53,-31,15,-80,-14,100] 
,[12,41,-32,11,31,23,-22,-14,44,14,53,-31,15,-80,-14,100,12,41,-32,11,31,23,-22,-14,44,14,53,-31,15,-80,-14,100,12,41,-32,11,31,23,-22,-14,44,14,53,-31,15,-80,-14,100,12,41,-32,11,31,23,-22,-14,44,14,53,-31,15,-80,-14,100]
,[random.randint(-100,100) for x in range(64)], [random.randint(-100,100) for x in range(128)]
,[random.randint(-100,100) for x in range(256)],[random.randint(-100,100) for x in range(512)]
,[random.randint(-100,100) for x in range(1024)]
]


def max_sum_divide_and_conquer(arr,length):
    indexlow =-199
    indexhigh = 100000
    def maxCrossingSum(arr, left, middle, right): 
        sm = 0
        left_sum = -10000
        
        for i in range(middle, left-1, -1): 
            sm = sm + arr[i] 
            if (sm > left_sum): 
                left_sum = sm 
        sm = 0
        right_sum = -1000
        for i in arr[middle:right + 1] :
            sm = sm + i
            if (sm > right_sum): 
                right_sum = sm 
        return max(left_sum + right_sum - arr[middle], left_sum, right_sum) 
    def maxSubArraySum(arr, left, right): 
        nonlocal indexlow
        nonlocal indexhigh
        indexlow = left
        indexhigh = right
        if (left > right): 
            return -10000
        if (left == right): 

            return arr[left]  
        middle = (left + right) // 2
        a = maxSubArraySum(arr, left, middle-1)
        b= maxSubArraySum(arr, middle+1, right)
        c =  maxCrossingSum(arr, left, middle, right)
        maxim = max(a,b,c)
        if maxim ==a:
            indexlow = left
            indexhigh = middle-1
        if maxim ==b:
            indexlow =  middle+1
            indexhigh =right
        if maxim ==c:
            indexlow = left
            indexhigh =right
        return maxim
    
    return maxSubArraySum(arr, 0, length-1), indexlow,indexhigh
max_sum_divide_and_conquer(test_dataset[1],len(test_dataset[1])) 


def Bad_Brute_Force(arr,length):
    Maxsum = -1000
    indexlow =-199
    indexhigh = 100000
    for start in range(length):
        for end in range(start,length):
            sum = 0
            for middle in range(start,end+1):
                sum = sum +arr[middle]            
            if  sum>Maxsum:
                Maxsum = sum
                indexlow = start
                indexhigh = end
                    
    return Maxsum , indexlow , indexhigh

def Kadane_algo(arr,length):
    maxsum = -1000000
    max_at_index = 0
    indexlow =-199
    indexhigh = 100000
    temp = 0 
    for i in range(length):
        max_at_index = max_at_index + arr[i]
        if (maxsum < max_at_index):
            maxsum = max_at_index
            indexlow = temp
            indexhigh = i
 
        if max_at_index < 0:
            max_at_index = 0
            temp = i+1
    return maxsum, indexlow , indexhigh

def bruteforce(arr,length):
    Maxsum = -1000
    indexlow =0
    indexhigh = 0
    for start in range(length):
        sum = arr[start]
        Maxsum = max(sum,Maxsum)
        if Maxsum == sum:
            indexlow = start
        for end in range(start+1,length):
            sum = sum + arr[end]
            Maxsum = max(sum,Maxsum)
            if Maxsum == sum:
                indexhigh = end
    return Maxsum,indexlow,indexhighS

def counter(dataset):
    result = []
    for i in dataset:
        length = len(i)
        t1_start = time.perf_counter() 
        Bad_Brute_Force(i,length)
        t1_stop = time.perf_counter()
        t1 = t1_stop -t1_start 
        t1_start = time.perf_counter() 
        bruteforce(i,length)
        t1_stop = time.perf_counter()
        t2 = t1_stop -t1_start 
        t1_start = time.perf_counter() 
        max_sum_divide_and_conquer(i,length)
        t1_stop = time.perf_counter()
        t3 = t1_stop -t1_start 
        t1_start = time.perf_counter() 
        Kadane_algo(i,length)
        t1_stop = time.perf_counter()
        t4 = t1_stop -t1_start 
        result.append({"Badbrute":t1,"Brute":t2,"Divide and Conquer":t3,"Kadane":t4})
    return result

pprint.pprint(counter(test_dataset))