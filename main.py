def check_for_overlap():
    rectangle_a  = {"x1":12, "y1":12, "x2":5,"y2":8}
    rectangle_b  = {"x1": 18, "y1":15, "x2":5,"y2":8}
    
    if(rectangle_a["y1"]<rectangle_b["y2"] or rectangle_a["x1"]<rectangle_b["x2"]):
        print("no overlap ")
    
    elif(rectangle_a["x2"]>rectangle_b["x1"] or rectangle_a["y2"]>rectangle_b["y1"]):
        print("no overlap ")
    else:
        print("YES ! there is a overlap")

check_for_overlap()