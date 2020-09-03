# hop 2 toan tu (union)

A={1,2,3,4,5}
B={4,5,6,7,8}

print(A|B)

print(A.union(B))
print(B.union(A))

# giao 2 toan tu (intersection)
print(A&B)
print(A.intersection(B))
print(B.intersection(A))


# hieu cua A va B (A-B) la tap hop phan tu chi co trong A, khong co trong B (difference)
print(A-B)
print(A.difference(B))
print(B.difference(A))

# Bu la tap hop nhung phan tu co trong A va B nhung khong phai phan tu chung cua 2 tap hop (symmetric_difference)
print(A^B)
print(A.symmetric_difference(B))

for letter in set("Python"):
	print(letter)
