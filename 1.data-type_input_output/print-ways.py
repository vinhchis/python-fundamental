# 0.
score = 100
name = 'Alice'

# 1. Tuple
print("Total score for %s is %s" % (name, score))

# 2. Dictionary
print("Total score for %(n)s is %(s)s" %{'n': name, 's': score})

# 3. new-style ()
print("Total score for {} is {}".format(name, score))

# 4. new-style (order)
print("Total score for {0} is {1}".format(name, score))

# 5. new-style (explicit names)
print("Total score for {n} is {s}".format(n=name, s=score))

# 6. Concatenate strings
print("Total score for " + str(name) + " is " + str(score))

# 7. Pass as Parameters
print("Total score for", name, "is", score) # auto add a space

print("total score for ", name, " is ", score, sep='') 

# 8. use 'f' in python 3.6
print(f"Total score for {name} is {score}")