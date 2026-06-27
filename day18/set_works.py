
#st={1,2,3,1,101,10,4,1,5}

#for num in st:

#    print(num)

set_a={10,20,30,40}


set_b={30,40,100,200}

print(set_a.issuperset(set_b))

print(set_b.issubset(set_a))

union_set=set_a.union(set_b)

print("union",union_set)

intersection_set=set_a.intersection(set_b)

print("intersection",intersection_set)

difference_set=set_a.difference(set_b)

print("difference",difference_set)