# Python Competitive Codes

## Backtracking

```
boolean findSolutions(n, other params) :
  if (found a solution) :
    displaySolution();
    return true;

  for (val = first to last) :
    if (isValid(val, n)) :
      applyValue(val, n);
      if (findSolutions(n+1, other params))
        return true;
      removeValue(val, n);
  return false;

findSolutions(n)
```

Backtracking way used in sudoku.

```
def dfs():
  if done_condition:
    return True
  to_visit = visit[0] # pick one from visit
  for dig in {"1", "2", "3", "4", "5", "6", "7", "8", "9"}:
    if is_valid(dig):
      add_dig(dig)
      remove_from_visit(to_visit, visit)
      if dfs():
        return True
      else:
        remove_dig(dig)
        add_to_visit(to_visit, visit)
  return False
```

Instead of passing any parameters to function, we keep a separate list of posibilities to try (visit)

Backtracking way used in combination_sum (General purpose for many)

```
results = []
target = 7
candidates = [2,3,6,7]
def backtrack(remain, path, start):
  if done_condition:
    results.append(list(path))
    return
  elif fail_path_condition:
    return
  for i in range(start, len(candidates)):
    path.append(candidates[i])
    backtrack(remain - candidates[i], path, i)
    path.pop() # backtrack
backtrack(target, [], 0)
```

## Pointers

For trapping rain water

```
total = 0
l, r = 0, n-1
l_max, r_max = bars[l], bars[r]
while l < r:
  l_max = max(l_max, bars[l])
  r_max = max(r_max, bars[r])
  if l_max <= r_max:
    l += 1
    total += l_max - bars[l]
  else:
    r -= 1
    total += r_max - bars[r]
```
