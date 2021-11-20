

class CharNode:
	def __init__(self):
		self.key ='\0'
		self.colour = False

NIL = CharNode()

class CharTree:
	def __init__(self):
		self.root = NIL

def CharNode_init(parent, c):
	node = CharNode()
	node.parent = parent
	node.key = c
	node.count = 1
	node.child = [None, None]
	node.child[0] = NIL
	node.child[1] = NIL
	node.colour = True
	return node


def CharNode_destroy(node):
	print(f'Eliminando {node.key}')
	del node


# OPERACIONES AUXILIARES.
def nodecmp(M, N):
	return M.key == N.key

def rotateDirRoot(T, N, dir):
	G = N.parent 
	S = N.child[1-dir]
	C = S.child[dir]
	N.child[1-dir] = C

	if not nodecmp(C, NIL):
		C.parent = N

	S.child[dir] = N
	N.parent = S
	S.parent = G

	if not nodecmp(G, NIL):
		if nodecmp(N, G.child[1]):
			G.child[1] = S
		else:
			G.child[0] = S
	else:
		T.root = S

	return S

def rotateLeft(T, N):
	return rotateDirRoot(T, N, 0)

def rotateRight(T, N):
	return rotateDirRoot(T, N, 1)

def minimum(N):
	if nodecmp(N.child[0], NIL):
		return N
	return minimum(N.child[0])

def removeMin(N):
	if nodecmp(N.child[0], NIL): 
		n = N.child[1]
		N.child[1] = NIL
		return n

	N.child[0] = removeMin(N.child[0])
	return N

def treeInsert(T, c):
	if nodecmp(T.root, NIL):
		T.root = CharNode_init(NIL, c)
		return T.root

	N = T.root
	find = True

	while N.key != c: 
		if N.key < c and not nodecmp(N.child[1], NIL): 
			N = N.child[1]
		elif N.key < c:
			find = False
			break
		elif not nodecmp(N.child[0], NIL):
			N = N.child[0]
		else:
			find = False
			break

	if find:
		N.count = N.count + 1; 
		return N
	elif N.key < c:
		N.child[1] = CharNode_init(N, c)
		return N.child[1]
	else:
		N.child[0] = CharNode_init(N, c)
		return N.child[0]

def treeRemove(N, c):
	if nodecmp(N, NIL): return NIL 

	if c < N.key: 
		N.child[0] = treeRemove(N.child[0], c)
		return N
	elif c > N.key:
		N.child[1] = treeRemove(N.child[1], c)
		return N
	else:
		if nodecmp(N.child[0], NIL):
			n = N.child[1]
			N.child[1] = NIL
			CharNode_destroy(N)
			return n

		if nodecmp(N.child[1], NIL):
			n = N.child[0]
			N.child[0] = NIL
			CharNode_destroy(N)
			return n

		n = minimum(N.child[1])
		n.child[1] = removeMin(N.child[1])
		n.child[0] = N.child[0]
		CharNode_destroy(N)
		return n


# OPERACIONES PRINCIPALES
def CharTree_search(T, c):
	if nodecmp(T.root, NIL):
		return NIL

	N = T.root

	while N.key != c and not nodecmp(N, NIL):
		if N.key < c:
			N = N.child[1]
		else:
			N = N.child[0]

	return N

def CharTree_insert(T, c):
	x = treeInsert(T, c)

	if x.count == 1: return

	while not nodecmp(x, T.root) and x.parent.colour:
		if nodecmp(x.parent, x.parent.parent.child[0]): 
			y = x.parent.parent.child[1]
			if y.colour:
				x.parent.colour = False
				y.colour = False
				x.parent.parent.colour = True
				x = x.parent.parent
			else:
				if nodecmp(x, x.parent.child[1]):
					x = x.parent
					rotateLeft(T, x)

				x.parent.colour = False
				x.parent.parent.colour = True
				rotateRight(T, x.parent.parent)
		else:
			y = x.parent.parent.child[0]
			if y.colour:
				x.parent.colour = False
				y.colour = False
				x.parent.parent.colour = True
				x = x.parent.parent
			else :
				if nodecmp(x, x.parent.child[0]):
					x = x.parent
					rotateRight(T, x)

				x.parent.colour = False
				x.parent.parent.colour = True
				rotateLeft(T, x.parent.parent)

	T.root.colour = False

def CharTree_erase(T, c):
	x = CharTree_search(T, c)

	if nodecmp(x, NIL):
		return False
	if x.count > 1:
		x.count = x.count - 1
		return True

	T.root = treeRemove(T.root, c)

def CharNode_print(N, level):
	if nodecmp(N, NIL): 
		print("    " * level + "--")
	else:
		print(f'{"    " * level}({N.key}, {N.count})')
		CharNode_print(N.child[0], level+1)
		CharNode_print(N.child[1], level+1)

def CharTree_print(T):
	CharNode_print(T.root, 0)

tree = CharTree()

for c in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
	CharTree_insert(tree, c)
	CharTree_insert(tree, c)
	CharTree_insert(tree, c)

for c in "abcdefghijklOPQRSTUVWXYZ":
	CharTree_erase(tree, c)
	CharTree_erase(tree, c)
	CharTree_erase(tree, c)



CharTree_print(tree)