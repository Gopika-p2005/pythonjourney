magazine="panamacanal"

note="man"

#this method not 100% in true

mg_set=set(magazine)

nt_set=set(note)

sub_set=nt_set.issubset(mg_set)

if sub_set==True:

    print("rasome note")

else:

    print("not rasome note")


#another method
#for ch in note:
#   if ch not in magazine:
#       print("not a rasome note")
#       break
#   else:
#       print("rasome note")
