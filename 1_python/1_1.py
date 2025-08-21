print("*** Rabbit & Turtle ***")

d, vr, vt, vf = input("Enter Input : ").split(" ")
d = int(d)
vr = int(vr)
vt = int(vt)
vf = int(vf)
if d <= 5000 and vr <= 5000 and vt <= 5000 and vf <= 5000 and vt > vr:
    vd = vt - vr
    td = d/vd
    print("%.2f"%(vf*td))
