# Make a list of your own. And remove all the duplicates element from that list.
a = [1, 2, 3, 4, 5, 6, 7, 7, 8, 9, 7]
ans = []
for i in a:
    if i not in ans:
        ans.append(i)
print(ans)
