class node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def pathToNode(root, path, k):
    if root is None:
        return False
    path.append(root.data)
    if root.data == k:
        return True
    if ((root.left != None and pathToNode(root.left, path, k)) or
            (root.right != None and pathToNode(root.right, path, k))):
        return True
    path.pop()
    return False


def distance(root, data1, data2):
    if root:
        path1 = []
        pathToNode(root, path1, data1)
        path2 = []
        pathToNode(root, path2, data2)
        i = 0
        while i < len(path1) and i < len(path2):
            if path1[i] != path2[i]:
                break
            i = i+1
        return (len(path1)+len(path2)-2*i)
    else:
        return 0


def generatePairs(root, pairs, k):
    count = 0
    for i in range(len(pairs)):
        for j in range(i+1, len(pairs)):
            if distance(root, pairs[i], pairs[j]) <= k:
                count += 1
    return count


def findLeafNodes(root):
    if root is None:
        return

    if root.left is None and root.right is None:
        pairs.append(root.data)
        return

    if root.left:
        findLeafNodes(root.left)

    if root.right:
        findLeafNodes(root.right)


def insertLevelOrder(arr, root, i, n):
    if i < n and arr[i] != -1:
        temp = node(arr[i])
        root = temp
        root.left = insertLevelOrder(arr, root.left, 2 * i + 1, n)
        root.right = insertLevelOrder(arr, root.right, 2 * i + 2, n)
    return root


arr = []
k = int(input())
n = int(input())
if n != -1:
    for i in range(n+1):
        line = list(map(int, input().split(' ')))
        if len([True for i in line if i == -1]) == len(line):
            continue
        arr = arr+line
n = len(arr)
root = None
root = insertLevelOrder(arr, root, 0, n)
pairs = []
findLeafNodes(root)
print(generatePairs(root, pairs, k))
