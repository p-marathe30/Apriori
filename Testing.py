from algorithm import apriori


mat=[]
"""
test_file=open("75000-out2.csv","r")
arrays=(test_file.read()).split("\n")
for i in arrays[:3000]:
	arr=i.split(',')
	x=[int(j) for j in arr[1:]]
	mat=mat+[x]
"""

mat=[[1,1,1,1],[1,1,0,1],[1,1,0,0],[0,1,1,1],[0,1,1,0],[0,0,1,1],[0,1,0,1]]

ap=apriori(mat)

while True:
	min_supp=float(raw_input("Enter the minimum support count:"))
	ap.apalgo(min_supp)
	ap.item_list()
	print ap.res_items