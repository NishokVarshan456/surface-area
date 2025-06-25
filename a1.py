import math

def find_ab(v_a1,v_a2,v_a3,v_b1,v_b2,v_b3):
    ab=[(v_b1-v_a1),(v_b2-v_a2),(v_b3-v_a3)]
    return ab

def find_ac(v_a1,v_a2,v_a3,v_c1,v_c2,v_c3):
    ac = [(v_c1 - v_a1), (v_c2 - v_a2), (v_c3 - v_a3)]
    return ac

def find_cross(ab,ac):
    ans=[ ((ac[2]*ab[1])-(ac[1]*ab[2])), -((ac[2]*ab[0])-(ac[0]*ab[2])), ((ac[1]*ab[0])-(ac[0]*ab[1]))  ]
    return ans

def cal_area(v_ans):
    sr=math.sqrt(v_ans[0]**2+v_ans[1]**2+v_ans[2]**2)
    sr=sr/2
    return sr

file=open("fan_volume.stl","r")

tot_area=0
count=0
a1 = a2 = a3 = b1 = b2 = b3 = c1 = c2 = c3 = 0.0

line=file.readline()

while line:

    words=line.split()

    if words[0]=="vertex" and count==0 :
        
        a1 = float(words[1])
        a2 = float(words[2])
        a3 = float(words[3])
        count += 1
        line=file.readline()

    elif words[0]=="vertex" and count==1:
        
        b1 = float(words[1])
        b2 = float(words[2])
        b3 = float(words[3])
        count += 1
        line = file.readline()

    elif words[0] == "vertex" and count == 2:
        
        count=0
        c1 = float(words[1])
        c2 = float(words[2])
        c3 = float(words[3])

        ans_ab = find_ab(a1, a2, a3, b1, b2, b3)
        ans_ac=find_ac(a1,a2,a3,c1,c2,c3)

        cross_ans=find_cross(ans_ab,ans_ac)
        tot_area=tot_area+cal_area(cross_ans)

        line = file.readline()
        
    else:
        line=file.readline()

print(f"{tot_area:.4f} sq units")
file.close()

