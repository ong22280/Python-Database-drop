from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox
import _sqlite3
con = _sqlite3.connect('SQL_Drop.db')
cur = con.cursor()

window = Tk()
window.title("ลงทะเบียนเพิกถอนรายวิชา")
window.geometry("650x450")
window.option_add('*font', 'tahoma 10')
window.resizable(0, 0)
window.config(bg='#15F043')
frame = Frame(window)
frame.config(bg='#9BFEB0')
frame.pack()

idlable = Label(frame, text="บัญชีนนทรี", width=12, anchor=W)
idlable.grid(column=0, row=0, padx=5, pady=10)
pwlable = Label(frame, text="รหัสผ่าน", width=12, anchor=W)
pwlable.grid(column=0, row=1, padx=5, pady=5)
cpwlabel = Label(frame, text="ยืนยันรหัสผ่าน", width=12, anchor=W)
cpwlabel.grid(column=0, row=2, padx=5, pady=5)
adlable = Label(frame, text="อาจารย์ที่ปรึกษา", width=12, anchor=W)
adlable.grid(column=0, row=6, padx=20, pady=20)

envar1 = StringVar()
entry1 = Entry(frame, textvariable=envar1, width=20)
entry1.grid(column=1, row=0, padx=5, pady=5,)
envar2 = StringVar()
entry2 = Entry(frame, textvariable=envar2, show="*", width=20)
entry2.grid(column=1, row=1, padx=5, pady=5)
envar3 = StringVar()
entry3 = Entry(frame, textvariable=envar3, show="*", width=20)
entry3.grid(column=1, row=2, padx=5, pady=5)
envar4 = StringVar()
entry4 = Entry(frame, textvariable=envar4, width=20)
entry4.grid(column=1, row=6, padx=5, pady=5, columnspan=2)       

def getvalue():
    global rtype
    varlist = {1: "ชาย", 2: "หญิง"} 
    rtype = varlist[var.get()]

var = IntVar()
r1 = Radiobutton(frame, text="ชาย", width=10, variable=var, value=1, anchor=W, command=getvalue)
r1.grid(column=0, row=3, padx=5, pady=5)
r1 = Radiobutton(frame, text="หญิง", width=10, variable=var, value=2, anchor=W, command=getvalue)
r1.grid(column=1, row=3, padx=5, pady=5)

lable4 = Label(frame, text="===== เลือกวิชาที่ดรอป =====", width=39)
lable4.grid(column=0, row=4, columnspan=2, padx=5)
lable4.config(font="tahoma 10 bold")
listbox1 = Listbox(frame, height=10, width=45)
listbox1.grid(column=0, row=5, columnspan=2)
scrolly1 = Scrollbar(frame, orient=VERTICAL, command=listbox1.yview)
scrolly1.grid(column=2, row=5, sticky=NW+SW)
listbox1.config(yscrollcommand=scrolly1.set)

def listbox1_select(event):
    w = event.widget
    data = int(w.curselection()[0])     #กำหนดค่า w และ data เพื่อเข้าถึงข้อมูลที่ผู้อ่านคลิกเลือกใน listbox1
    global freeitem
    freeitem = w.get(data)

listbox1.bind('<<ListboxSelect>>', listbox1_select) #เมื่อมีการคลิกเลือก โปรแกรมจะเรียกใช้ฟังก์ชัน listbox1_select

courselist = ["Engineering Mathematics I", "General Physics I", "Laboratory in Physics I", "Knowledge of the Land",
              "Green Technology", "Programming Fundamentals I", "Engineering Drawing"]

for item in courselist:             #วนลูปข้อมูลใน courselist เพื่อแสดงใน listbox1
    listbox1.insert(END, item)

typelable = Label(frame, text="ชั้นปีการศึกษา", width=15, anchor=W)
typelable.grid(column=3, row=0, padx=5, pady=5)
ycombo = Combobox(frame, width=10)         #สร้าง ycombo จากคลาส Combobox
ycombo.grid(column=4, row=0, padx=5)
yearlist = ["1", "2", "3", "4", "5", "6", "7", "8"]
ycombo['values'] = yearlist       #นำข้อมูลใน yearlist มาแสดงใน mcombo
ycombo.current(0)               #กำหนดค่าเริ่มต้นให้ ycombo ให้เริ่มต้นที่ลำดับที่ 0

def getcvalue():
    global facultytype
    facultylist = {1: "วิศวกรรมศาสตร์", 2: "วิทยาการจัดการ", 3: "วิทยาศาสตร์", 4: "เศรษศาสตร์"}
    facultytype = facultylist[var1.get()]       #กำหนดให้กับตัวแปร  โดยอ้างอิงจาก var1 และ facultylist

lable2 = Label(frame, text="======== คณะ ========", width=30)
lable2.grid(column=3, row=1, columnspan=2, padx=5)
lable2.config(font="tahoma 10 bold")
var1 = IntVar()     #สร้างตัวแปร var1 เป็นชนิด Int
c1 = Radiobutton(frame, text="วิศวกรรมศาสตร์", width=12, variable=var1, value=1, anchor=W, command=getcvalue)
c1.grid(column=3, row=2, padx=5, pady=5)
var2 = IntVar()
c2 = Radiobutton(frame, text="วิทยาการจัดการ", width=12, variable=var1, value=2, anchor=W, command=getcvalue)
c2.grid(column=4, row=2, padx=5, pady=5)
var3 = IntVar()
c3 = Radiobutton(frame, text="วิทยาศาสตร์", width=12, variable=var1, value=3, anchor=W, command=getcvalue)
c3.grid(column=3, row=3, padx=5, pady=5)
var4 = IntVar()
c4 = Radiobutton(frame, text="เศรษศาสตร์", width=12, variable=var1, value=4, anchor=W, command=getcvalue)
c4.grid(column=4, row=3, padx=5, pady=5)

lable3 = Label(frame, text="===== ตรวจสอบข้อมูล =====", width=30)
lable3.grid(column=3, row=4, columnspan=2, padx=5)
lable3.config(font="tahoma 10 bold")
displaymsg = Text(frame, bg="white", height=10, width=35)
displaymsg.grid(column=3, row=5, columnspan=2, padx=5, sticky=E)
scrolly2 = Scrollbar(frame, orient=VERTICAL, command=displaymsg.yview)
scrolly2.grid(column=5, row=5, sticky=NW+SW)
displaymsg.config(yscrollcommand=scrolly2.set)

def get_data():
    global entries
    data2 = []
    for w in entries:
        data2.append(w)
    return data2

def add_data():
    sql = 'INSERT INTO รายชื่อนิสิตทะเบียนเพิกถอนรายวิชา VALUES (?, ?, ?, ?, ?, ?, ?)'
    data = get_data()
    r = cur.execute(sql, data)
    if r.rowcount == 1:
        con.commit()
        messagebox.showinfo('Success', 'ข้อมูลบันทึกแล้ว')
        clear_data()
    else:
        messagebox.showerror('Error', 'เกิดข้อผิดพลาด')

def checkdata():
    global entries
    displaymsg.delete("1.0", END)
    msg = "1. ชื่อบัญชีนนทรี: " + entry1.get() + "\n"
    msg += "2. รหัสผ่าน: " + entry2.get() + "\n"
    msg += "3. เพศ: " + rtype + "\n"
    msg += "4. ชั้นปีการศึกษา: " + ycombo.get() + "\n"
    msg += "3. คณะ: " + facultytype + "\n"
    msg += "4. วิชาที่เพิกถอน:\n    - " + freeitem + "\n"
    msg += "5. อาจารย์ที่ปรึกษา: " + entry4.get() + "\n"
    displaymsg.insert(INSERT, msg)
    entries = [str(entry1.get()), str(entry2.get()), str(rtype),
               str(ycombo.get()), str(facultytype), str(freeitem),
               str(entry4.get())]
    add_data()

def clear_data():
    entry1.delete(0, END)
    entry2.delete(0, END)
    entry3.delete(0, END)
    entry4.delete(0, END)
    ycombo.delete(0, END)

def save_data():
    if envar2.get() != envar3.get():
        messagebox.showerror("Error", "รหัสผ่านกับยืนยันรหัสผ่านไม่ตรงกัน")
    elif envar2.get() == envar3.get():
        checkdata()
        button1.focus_set()

button1 = Button(frame, text="บันทึก", width=10, height=3,
                 compound="left", command=save_data)
button1.grid(column=3, row=6, padx=20, pady=20)

window.mainloop()
