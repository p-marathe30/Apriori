# Apriori

## This is an implementation of the apriori algorithm to mine frequent pattern sets.

## Use: 
  
from algorithm import apriori

obj=apriori(matrix)    #the matrix should be vector matrix with assignments 1 or 0 to the indices with the item present.

obj.apalgo(min_supp)   #min_support shall be given as >1 for support count and >0 and < 1 for support percentage

obj.item_list()        #converts sparse vectors of item sets to item vectors

obj.res_items          #frequent item list

obj.res                #frequent item sparse list
  
