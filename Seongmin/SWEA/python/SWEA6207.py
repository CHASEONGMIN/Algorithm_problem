a = float(input())

print("%(dc).2f ℃ =>  %(fc).2f ℉" % {"dc": a, "fc": a/100*180+32})
