from tkinter import *
import numpy
c,d = [],[]
#หน้าต่างกดเข้า
def cilck_on1():
    frm1.pack_forget()
    frm2.pack()
def cilck_on2():
    frm1.pack_forget()
    frm3.pack()
def cilck_on3():
    frm1.pack_forget()
    frm4.pack()
def cilck_on4():
    frm2.pack_forget()
    frm5.pack() 
    value()
    # f = numpy.poly1d(d)
    # i = f.integ()
    # p = numpy.poly1d(c)
    # i = p.integ()
    # print("c: ",c)
    # print("p: ",p)
    # print("i: ",i)
    # print("i(1) - i(0): ",i(1) - i(0))

#หน้าต่างกดกลับ
def cilck_back1():
    root.destroy()
def cilck_back2():
    frm5.pack_forget()
    frm1.pack()
def cilck_back3():
    frm3.pack_forget()
    frm1.pack()
def cilck_back4():
    frm4.pack_forget()
    frm1.pack()
#ฟังก์ชัน
def value():
    global c,d
    a,b = [],[]
    depth = float(inp9.get())
    a.append(float(inp1.get()))
    a.append(float(inp3.get()))
    a.append(float(inp5.get()))
    a.append(float(inp7.get()))
    b.append(float(inp2.get()))
    b.append(float(inp4.get()))
    b.append(float(inp6.get()))
    b.append(float(inp8.get()))
    c.append(    b[0]/((a[0]-a[1])*(a[0]-a[2])*(a[0]-a[3]))\
                +b[1]/((a[1]-a[0])*(a[1]-a[2])*(a[1]-a[3]))\
                +b[2]/((a[2]-a[1])*(a[2]-a[0])*(a[2]-a[3]))\
                +b[3]/((a[3]-a[1])*(a[3]-a[2])*(a[3]-a[0]))
    )
    c.append(    b[0]*(-(a[1]+a[2]+a[3]))/((a[0]-a[1])*(a[0]-a[2])*(a[0]-a[3]))\
                +b[1]*(-(a[0]+a[2]+a[3]))/((a[1]-a[0])*(a[1]-a[2])*(a[1]-a[3]))\
                +b[2]*(-(a[0]+a[1]+a[3]))/((a[2]-a[1])*(a[2]-a[0])*(a[2]-a[3]))\
                +b[3]*(-(a[0]+a[1]+a[2]))/((a[3]-a[1])*(a[3]-a[2])*(a[3]-a[0]))
    )
    c.append(   ((b[0]*(a[1]+a[2]+a[3])/((a[0]-a[1])*(a[0]-a[2])*(a[0]-a[3]))\
                -b[1]*(a[0]+a[2]+a[3])/((a[1]-a[0])*(a[1]-a[2])*(a[1]-a[3]))\
                +b[2]*(a[0]+a[1]+a[3])/((a[2]-a[1])*(a[2]-a[0])*(a[2]-a[3]))\
                -b[3]*(a[0]+a[1]+a[2])/((a[3]-a[1])*(a[3]-a[2])*(a[3]-a[0]))))*-1
    )
    c.append(   (b[0]*(a[1]*a[2]*a[3])/((a[0]-a[1])*(a[0]-a[2])*(a[0]-a[3]))\
                +b[1]*(a[0]*a[2]*a[3])/((a[1]-a[0])*(a[1]-a[2])*(a[1]-a[3]))\
                +b[2]*(a[0]*a[1]*a[3])/((a[2]-a[1])*(a[2]-a[0])*(a[2]-a[3]))\
                +b[3]*(a[0]*a[1]*a[2])/((a[3]-a[1])*(a[3]-a[2])*(a[3]-a[0])))*-1 
    )
    d = c.copy()
    # print("d: ",d)
    d[3] -= depth
    
    result_var1.set(f'ฟังก์ชันกราฟด้านบน: {c[0]:.2f}x^3{"" if c[1]<0 else "+"}{c[1]:.2f}x^2{"" if c[2]<0 else "+"}{c[2]:.2f}x{"" if c[3]<0 else "+"}{c[3]:.2f}')
    result_var2.set(f'ฟังก์ชันกราฟด้านล่าง: {d[0]:.2f}x^3{"" if d[1]<0 else "+"}{d[1]:.2f}x^2{"" if d[2]<0 else "+"}{d[2]:.2f}x{"" if d[3]<0 else "+"}{d[3]:.2f}')

    fuc1 = lambda x: (22 / 7) * ((((c[0] ** 2) * (x ** 7)) / 7) + ((1 / 5) * (x ** 5) * (2 * (c[0] * c[2]) + (c[1] ** 2))) + (
        (1 / 2) * (x ** 4) * ((c[0] * c[3]) + (c[1] * c[2]))) + ((1 / 3) * (x ** 6) * (c[0] * c[1])) + (
                                     (1 / 3) * (x ** 3) * (2 * (c[1] * c[3]) + (c[2] ** 2))) + (c[2] * c[3] * (x ** 2)) + (
                                     (c[3] ** 2) * x))

    fuc2 = lambda x: (22 / 7) * ((((c[0] ** 2) * (x ** 7)) / 7) + ((1 / 5) * (x ** 5) * (2 * (c[0] * c[2]) + (c[1] ** 2))) + (
        (1 / 2) * (x ** 4) * ((c[0] * d[3]) + (c[1] * c[2]))) + ((1 / 3) * (x ** 6) * (c[0] * c[1])) + (
                                     (1 / 3) * (x ** 3) * (2 * (c[1] * d[3]) + (c[2] ** 2))) + (c[2] * d[3] * (x ** 2)) + (
                                     (d[3] ** 2) * x))
    # print("(fuc1(a[3]) - fuc1(a[0])) - (fuc2(a[3]) - fuc2(a[0])) + fuc2(depth): ",(fuc1(a[3]) - fuc1(a[0])) - (fuc2(a[3]) - fuc2(a[0])) + fuc2(depth))
    result= (fuc1(a[3]) - fuc1(a[0])) - (fuc2(a[3]) - fuc2(a[0])) + fuc2(depth)
    result_var3.set(int(result * (10 ** 2)) / (10 ** 2))
    # print("c[0],c[1],c[2],c[3]: ",c[0],c[1],c[2],c[3])

root=Tk()
root.geometry("800x600")
root.option_add("*Font","impact 18")
root.title("Vase volume")
#frame1
frm1=Frame(root,width=800,height=600,background="#CC99FF")
Label(frm1, text="โปรเเกรมหาปริมาตรของเเจกัน",font=("Times New",25),bg="#CC99FF").place(x=200,y=10)
Button(frm1, text="Start",font=("Times New",20), command=cilck_on1, bg="#990066",width="12").place(x=290,y=100)
Button(frm1, text="วิธีใช้",font=("Times New",20), command=cilck_on2, bg="#990066",width="12").place(x=290,y=200)
Button(frm1, text="ผู้จัดทำ",font=("Times New",20), command=cilck_on3, bg="#990066",width="12").place(x=290,y=300)
Button(frm1, text="Exit",font=("Times New",20), command=cilck_back1, bg="#990066",width="12").place(x=290,y=400)

#frame2
frm2=Frame(root,width=800,height=600,background="#336600")
Label(frm2, text="ป้อนจุดตำเเหน่งที่กำหนด",font=("Times New",25),bg="#336600").place(x=250,y=10)
Label(frm2, text="x1:",font=("Times New",21),bg="#00CC33").place(x=400,y=100)
inp1=Entry(frm2,width=5)
inp1.config(font=("Times New",16),bg="#FFFFFF")
inp1.place(x=450,y=105)
Label(frm2, text="y1:",font=("Times New",21),bg="#00CC33").place(x=600,y=100)
inp2=Entry(frm2, width=5)
inp2.config(font=("Times New",16),bg="#FFFFFF")
inp2.place(x=650,y=105)
Label(frm2, text="x2:",font=("Times New",21),bg="#00CC33").place(x=400,y=200)
inp3=Entry(frm2, width=5)
inp3.config(font=("Times New",16),bg="#FFFFFF")
inp3.place(x=450,y=205)
Label(frm2, text="y2:",font=("Times New",21),bg="#00CC33").place(x=600,y=200)
inp4=Entry(frm2, width=5)
inp4.config(font=("Times New",16),bg="#FFFFFF")
inp4.place(x=650,y=205)
Label(frm2, text="x3:",font=("Times New",21),bg="#00CC33").place(x=400,y=300)
inp5=Entry(frm2, width=5)
inp5.config(font=("Times New",16),bg="#FFFFFF")
inp5.place(x=450,y=305)
Label(frm2, text="y3:",font=("Times New",21),bg="#00CC33").place(x=600,y=300)
inp6=Entry(frm2, width=5)
inp6.config(font=("Times New",16),bg="#FFFFFF")
inp6.place(x=650,y=305)
Label(frm2, text="x4:",font=("Times New",21),bg="#00CC33").place(x=400,y=400)
inp7=Entry(frm2, width=5)
inp7.config(font=("Times New",16),bg="#FFFFFF")
inp7.place(x=450,y=405)
Label(frm2, text="y4:",font=("Times New",21),bg="#00CC33").place(x=600,y=400)
inp8=Entry(frm2, width=5)
inp8.config(font=("Times New",16),bg="#FFFFFF")
inp8.place(x=650,y=405)
Label(frm2, text="ความหนาของเเจกัน:",font=("Times New",21),bg="#00CC33").place(x=410,y=500)
inp9=Entry(frm2, width=5)
inp9.config(font=("Times New",16),bg="#FFFFFF")
inp9.place(x=640,y=505)
Button(frm2, text="ต่อไป",font=("Times New",19), command=cilck_on4, bg="#BEBEBE",width="12").place(x=460,y=550)

#frame3
frm3=Frame(root,width=800,height=600,background="#FF3333")
Label(frm3, text="วิธีใช้",font=("Times New",21),bg="#FF3333").place(x=380,y=50)
Label(frm3, text="1.ป้อนค่า(x,y)ตามภาพที่เเสดง",font=("Times New",21),bg="#FF3333").place(x=200,y=150)
Label(frm3, text="2.ป้อนความหนาของเเจกันที่ต้องการ",font=("Times New",21),bg="#FF3333").place(x=200,y=250)
Label(frm3, text="3.กดต่อไปเพื่อเเสดงฟังก์ชันเเละปริมาณดิน",font=("Times New",21),bg="#FF3333").place(x=200,y=350)
Button(frm3, text="ย้อนกลับ",font=("Times New",19), command=cilck_back3, bg="#B5B5B5",width="12").place(x=600,y=540)

#frame4
frm4=Frame(root,width=800,height=600,background="#3366CC")
Label(frm4, text="สมาชิก",font=("Times New",21),bg="#3366CC").place(x=360,y=50)
Label(frm4, text="นางสาวกัญญาณัฐ จันทร์คง เลขที่ 17",font=("Times New",21),bg="#3366CC").place(x=200,y=150)
Label(frm4, text="นางสาวกันติชา เเก้วทอง เลขที่ 18",font=("Times New",21),bg="#3366CC").place(x=210,y=250)
Label(frm4, text="ชั้นมัธยมศึกษาปีที่ 5 ห้องโอเมก้า",font=("Times New",21),bg="#3366CC").place(x=220,y=350)
Button(frm4, text="ย้อนกลับ",font=("Times New",19), command=cilck_back4, bg="#B5B5B5",width="12").place(x=600,y=540)

#frame5
frm5=Frame(root,width=800,height=600,background="#9FB6CD")
result_var1=StringVar()
result_var1.set("ฟังก์ชันกราฟด้านบน:")
Label(frm5, textvariable=result_var1,font=("Times New",21),bg="#9FB6CD").place(x=100,y=100)
result_var2=StringVar()
result_var2.set("ฟังก์ชันกราฟด้านล่าง:")
Label(frm5, textvariable=result_var2,font=("Times New",21),bg="#9FB6CD").place(x=100,y=200)
Label(frm5, text="ปริมาตรดินที่ใช้ทำเเจกัน:",font=("Times New",21),bg="#9FB6CD").place(x=150,y=300)
result_var3=StringVar()
result_var3.set("ปริมาตรดินที่ใช้ทำเเจกัน:")
Label(frm5, textvariable=result_var3,font=("Times New",21),bg="#9FB6CD").place(x=420,y=300)
Button(frm5, text="ย้อนกลับ",font=("Times New",19), command=cilck_back2, bg="#B5B5B5",width="12").place(x=600,y=550)

frm1.pack()
root.mainloop()