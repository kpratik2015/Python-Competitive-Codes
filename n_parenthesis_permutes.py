def generateParenthesis(N):
  ans = []
  def backtrack(S='', left=0, right=0):
      print(f'backtrack("{S}",{left},{right})')
      if len(S) == 2 * N:
          ans.append(S)
          return
      if left < N:
          backtrack(S+'(', left+1, right)
      if right < left:
          backtrack(S+')', left, right+1)
  backtrack()
  return ans

print(generateParenthesis(3))

'''
backtrack("",0,0)
backtrack("(",1,0)
backtrack("((",2,0)
backtrack("(((",3,0)
backtrack("((()",3,1)
backtrack("((())",3,2)
backtrack("((()))",3,3)
backtrack("(()",2,1)
backtrack("(()(",3,1)
backtrack("(()()",3,2)
backtrack("(()())",3,3)
backtrack("(())",2,2)
backtrack("(())(",3,2)
backtrack("(())()",3,3)
backtrack("()",1,1)
backtrack("()(",2,1)
backtrack("()((",3,1)
backtrack("()(()",3,2)
backtrack("()(())",3,3)
backtrack("()()",2,2)
backtrack("()()(",3,2)
backtrack("()()()",3,3)
['((()))', '(()())', '(())()', '()(())', '()()()']
'''