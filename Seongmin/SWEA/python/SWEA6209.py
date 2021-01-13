a = float(input())

print("%(fc).2f ℉ =>  %(dc).2f ℃" % {"fc": a, "dc": (a-32)*100/180})
