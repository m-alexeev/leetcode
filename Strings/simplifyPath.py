def simplifyPath(path: str) -> str:
    arr = []
    split_path = path.split("/")
    for s in split_path:
        if s == ".." and arr:
            arr.pop()
        elif s not in ["..", "", "."]:
            arr.append(s)
    return "/" + "/".join(arr)


print(simplifyPath("/../"))
print(simplifyPath("/"))
print(simplifyPath("/home/"))
print(simplifyPath("/home//foo/"))
print(simplifyPath("/home/user/Documents/../Pictures"))
print(simplifyPath("/.../a/../b/c/../d/./"))
