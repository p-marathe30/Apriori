from pprint import pprint
#look for optimizations
def conv_bin(arr,num_items):
		sum=0L
		for i in range(num_items):
			sum+=(2**i)*arr[i]
		return sum

def merge_vecs(vec1,vec2,num_items):
	res_dict={}
	res_vec=[]
	for i in range(num_items):
		if ((2**i)&vec1)!=0 and ((2**i)&vec2==0):
			res_dict[((2**i)|vec2)]=1
	for i in range(num_items):
		if ((2**i)&vec2)!=0 and ((2**i)&vec1==0):
			res_dict[((2**i)|vec1)]=1
	for i in res_dict.keys():
		res_vec=res_vec+[i]
	return res_vec
			
		
class apriori(object):	
	
	def __init__(self,mat):
		self.mat=mat
		self.num_items=len(mat[0])
		self.num_recpt=len(mat)
		self.vec=[]
		for arr in mat:
			self.vec=self.vec+[conv_bin(arr,self.num_items)]
		self.pre_filt_array=[]
		self.pre_candidate=[]
		self.pre_filtered={}
		self.res=[]
		self.supp_count=0
		self.res_items=[]
	
	def item_list(self):
		self.res_items=[]
		for i in self.res:
			x=[]
			for j in range(self.num_items):
				if i[j]==1:
					x=x+[j]
			self.res_items=self.res_items+[x]
		return self.res_items
	
	def conv_mat(self):
		self.res=[]
		for i in self.pre_filt_array:
			ans=[]
			for j in range(self.num_items):
				if i&(2**j)==0:
					ans=ans+[0]
				else:
					ans=ans+[1]
			self.res=self.res+[ans]
			
	
	def apalgo(self,min_supp):
		if min_supp<1:
			self.supp_count=min_supp*(self.num_recpt)
		else:
			self.supp_count=min_supp
		candidate={}
		filtered={}
		filt_array=[]
		for i in range(self.num_items):
			candidate[(2**i)]=0
		for i in candidate.keys():
			for j in self.vec:
				if (i&j)!=0:
					candidate[i]+=1
		for i in candidate.keys():
			if candidate[i]>=min_supp:
				filtered[i]=candidate[i]
				filt_array=filt_array+[i];
		self.pre_filt_array=filt_array
		self.pre_filtered=filtered
		self.pre_candidate=candidate
		while len(filt_array)!=0:
			self.pre_filt_array=filt_array
			self.pre_filtered=filtered
			self.pre_candidate=candidate
			candidate={}
			for i in range(len(filt_array)-1):
				for j in range(i+1,len(filt_array)):
					res_vec=merge_vecs(filt_array[i],filt_array[j],self.num_items)	
					for k in res_vec:
						include=True
						for l in range(self.num_items):
							if (2**l)&k!=0:
								if (self.pre_filtered.get((2**l)^k),0)==0:
									include=False
							if not include:
								break
						if include:
							candidate[k]=0;
		
		#for j in filt_array:
		#	for i in range(50):
		#		if (2**i)&j!=0:
		#			print str(i)+' ',
		#	print '\n'
			filtered={}
			filt_array=[]
			for i in candidate.keys():
				for j in self.vec:
					if (i|j)==j:
						candidate[i]+=1
		#pprint(candidate)
			for i in candidate.keys():
				if candidate[i]>=self.supp_count:
					filtered[i]=candidate[i]
					filt_array=filt_array+[i];
			#print len(filt_array)
			#raw_input()
		
		#else:
		#	print pre_filt_array
		#return pre_filt_array
		self.conv_mat()