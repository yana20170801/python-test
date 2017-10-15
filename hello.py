import sys

args = sys.argv

print args
dec = args[1]
if dec == "aaa":
    print ("yes")
else:
    print ("no")

f = open("test_account.txt", "w")
f.writelines(dec)
f.writelines("end")
f.close

for line in open("test_account.txt", "r"):
    print line
f.close()
