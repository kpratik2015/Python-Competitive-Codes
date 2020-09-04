'''
Note: Pass sorted(nums) as arg[0]

Conditions of early termination:
1. Numbers are less than N
2. N < 2
3. target is lower than lowest number times N
4. target is higher than highest number times N

Two routes:
[I] N == 2 i.e. 2-sum problem
[II] N > 2 i.e. reduce to 2-sum problem

Route [II]:
1. For loop as number of different N size permutes e.g. For nums=[1,2,3,4,5,6], N=4 => Loop 3 times.
  1.a. if first iteration or (not first iteration & previous number != current number)
    1.a.i. (Recursion) Keep current number as part of result, target is subtracted by current number, N - 1 and nums is every next number after current number

Route [I]:
1. l (pointer 1) = 0, r (pointer 2) = len(nums) - 1
2. While l does not reach r:
  2.a. sum numbers at l & r (call it, s)
  2.b. Three Routes:
    2.b[i] sum is target -> results array is appended with concat of result and numbers at l & r as a solution set,
                            l is incremented and while l < r and current number at l is same as previous then keep incrementing l
    2.b[ii] sum is less than target -> l is incremented
    2.b[iii] sum is greater than target -> r is decremented (Note: r is only moved in this case)

'''
def findNsum(nums, target, N, result, results):
  if len(nums) < N or N < 2 or target < nums[0]*N or target > nums[-1]*N:  # early termination
      return
  if N == 2: # two pointers solve sorted 2-sum problem
      l,r = 0,len(nums)-1
      while l < r:
          s = nums[l] + nums[r]
          if s == target:
              results.append(result + [nums[l], nums[r]])
              l += 1
              while l < r and nums[l] == nums[l-1]:
                  l += 1
          elif s < target:
              l += 1
          else:
              r -= 1
  else: # recursively reduce N
      for i in range(len(nums)-N+1):
          if i == 0 or (i > 0 and nums[i-1] != nums[i]):
              findNsum(nums[i + 1 :], target - nums[i], N - 1, result + [nums[i]], results)

'''
E.g. 
results = []
findNsum(sorted(nums), target, 4, [], results)
'''