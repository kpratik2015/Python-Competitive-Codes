# Problem: https://leetcode.com/problems/simplify-path/

class Solution:
    def simplifyPath(self, path: str) -> str:
        paths = [s for s in path.split("/") if s != ""]
        len_paths = len(paths)
        f = ""
        valid_dir = [""]
        for i in range(len_paths):
            if paths[i] == ".." and valid_dir[-1] != "":
                valid_dir.pop()
            elif paths[i] != "." and paths[i] != "..":
                valid_dir.append(paths[i])
        f = f + '/'.join(valid_dir)
        f = f if f.startswith("/") else "/"+f
        return f

print(Solution().simplifyPath("/a//b////c/d//././/.."))