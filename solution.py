from ast import If
from decimal import DivisionUndefined
import time
import pprint
import random
import math
import numpy
test_dataset = [[1,4] ,[1,14,-23,15] ,[-3,14,22,44,-14,32,-1,-98] 
,[12,41,-32,11,31,23,-22,-14,44,14,53,-31,15,-80,-14,100],[12,41,-32,11,31,23,-22,-14,44,14,53,-31,15,-80,-14,100,12,41,-32,11,31,23,-22,-14,44,14,53,-31,15,-80,-14,100] 
,[12,41,-32,11,31,23,-22,-14,44,14,53,-31,15,-80,-14,100,12,41,-32,11,31,23,-22,-14,44,14,53,-31,15,-80,-14,100,12,41,-32,11,31,23,-22,-14,44,14,53,-31,15,-80,-14,100,12,41,-32,11,31,23,-22,-14,44,14,53,-31,15,-80,-14,100]
,[random.randint(-100,100) for x in range(64)], [random.randint(-100,100) for x in range(128)]
,[random.randint(-100,100) for x in range(256)],[random.randint(-100,100) for x in range(512)]
,[random.randint(-100,100) for x in range(1024)]
]
brute_test = [[random.randint(-100,100) for x in range(2**i)] for i in range(10,13) ]
kadane_test= [[random.randint(-100,100) for x in range(((40157040)//2)*i)]for i in range(1,3)]
divideandconquer_test = [[random.randint(-100,100) for x in range(((1607437)//2)*i)]for i in range(1,3)]

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
    return Maxsum,indexlow,indexhigh
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
    with open('output.txt', 'wt') as out:
        pprint.pprint(result, stream=out)
    return result
#counter can find the increase of
#Finding max array length that can be clalculated by kadane algo
#Through observation we find that for n = 1000000 t = 0.0746sec
#So having shown O(n) complexity then we find nmax = x t = 3
#Where x = 40214477 elements for about 3 sec time
#randint function would take too much time for these many elements so i didnt show it directly
def maxkadane(n):
    kadanetest=[random.randint(-100,100) for x in range(n)]
    t1_start = time.perf_counter() 
    Kadane_algo(kadanetest,n)
    t1_stop = time.perf_counter()
    tpartial_kadane = t1_stop -t1_start 
    n_max_kadane = 3*n/(tpartial_kadane)

    with open('output.txt', "a") as out:
        pprint.pprint("\nKadane  time for %i : %f "%(n,tpartial_kadane), stream=out)
        pprint.pprint("\nKadane  est. max number elements for 3sec runtime : :%i "%n_max_kadane, stream=out)
#Finding max array length that can be calculated by divide and conquer algo
#Max num of elements 
def maxdivide(n):
    dividetest=[random.randint(-100,100) for x in range(n)]
    t1_start = time.perf_counter() 
    max_sum_divide_and_conquer(dividetest,n)
    t1_stop = time.perf_counter()
    tmax_divide = t1_stop -t1_start 
    n_max_divide = 3*(n)/(tmax_divide)
    with open('output.txt', "a") as out:
        pprint.pprint("\nDivide and conquer time for %i elements :%f "%(n,tmax_divide), stream=out)
        pprint.pprint("\nDivide and conquer est. max number elements for 3sec runtime :%i "%n_max_divide, stream=out)
#Finding max array length that can be calculated by Brute algo
def maxBrute(n):
    dividetest=[random.randint(-100,100) for x in range(n)]
    t1_start = time.perf_counter() 
    bruteforce(dividetest,n)
    t1_stop = time.perf_counter()
    tmax_brute = t1_stop -t1_start 
    const = tmax_brute/(n**2)
    n_max_brute = math.sqrt(3/const)
    with open('output.txt', "a") as out:
        pprint.pprint("\nBrute force time for %i elements :  %f"%(n,tmax_brute), stream=out)
        pprint.pprint("\nBrute force  est. max number elements for 3sec runtime : %i" %n_max_brute, stream=out)
#Finding max array length that can be calculated by Nested Brute algo
def maxBad_Brute_Force(n):
    dividetest=[random.randint(-100,100) for x in range(n)]
    t1_start = time.perf_counter() 
    Bad_Brute_Force(dividetest,n)
    t1_stop = time.perf_counter()
    tmax_Badbrute = t1_stop -t1_start 
    const = tmax_Badbrute/(n**3)
    n_max_Badbrute = (3/const)**(1/3)
    with open('output.txt', "a") as out:
        pprint.pprint("\nBad_Brute_Force time for %i elements : %f"% (n, tmax_Badbrute), stream=out)
        pprint.pprint("\nBad_Brute_Force  est. max number elements for 3sec runtime :  %i" %n_max_Badbrute, stream=out)

def calculatemaxes():
    maxBad_Brute_Force(730)
    maxBrute(6000)
    maxdivide(1600000)
    maxkadane(1000000)
def calc__for_each_set(test_dataset,brute_test,kadane_test,divideandconquer_test):    
    with open('output.txt', "a") as out:
        for i in test_dataset:
            length = len(i)
            t1_start = time.perf_counter() 
            Bad_Brute_Force(i,length)
            t1_stop = time.perf_counter()
            t1 = t1_stop -t1_start 
            pprint.pprint("test_dataset time for %i elements : %f"% (length, t1), stream=out)
        for i in brute_test:
            length = len(i)
            t1_start = time.perf_counter() 
            bruteforce(i,length)
            t1_stop = time.perf_counter()
            t1 = t1_stop -t1_start 
            pprint.pprint("brute_test time for %i elements : %f"% (length, t1), stream=out)
        for i in kadane_test:
            length = len(i)
            t1_start = time.perf_counter() 
            Kadane_algo(i,length)
            t1_stop = time.perf_counter()
            t1 = t1_stop -t1_start 
            pprint.pprint("kadane_test time for %i elements : %f"% (length, t1), stream=out)
        for i in divideandconquer_test:
            length = len(i)
            t1_start = time.perf_counter() 
            max_sum_divide_and_conquer(i,length)
            t1_stop = time.perf_counter()
            t1 = t1_stop -t1_start 
            pprint.pprint("divideandconquer_test time for %i elements : %f"% (length, t1), stream=out)
calc__for_each_set(test_dataset,brute_test,kadane_test,divideandconquer_test)