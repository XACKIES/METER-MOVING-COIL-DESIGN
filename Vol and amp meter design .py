def num():#ฟังก์ชั่นตรวจค่าจำนวนเต็มสำหรับจำนวนย่านวัด
    print('-'*62)
    while True:
        sys_num = input('ใส่จำนวนย่านวัดที่ต้องการขยาย:')
        if sys_num.isdigit():
           sys_num = int(sys_num)
           return sys_num
           break
    print('-'*80)
    
def c_num(max_num):#ฟังก์ชั่นตรวจค่าจำนวนเต็มสำหรับตัวเลื่อก
    while True:
        sys_num = input('กรุณาเลือก:')
        if sys_num.isdigit():
           sys_num = int(sys_num)
           if sys_num > 0 and sys_num <= max_num :
               return sys_num
               break
            
def float_in(text):#ฟังก์ชันรับ และ ตรวจสอบเลขที่เป็นทศนิยม
    while True:
        user_in = input(text)
        try:
            out = float(user_in)
            if out >= 0:
                return out
                break
            print('**ไม่สามรถใช้ค่านี้ได้ กรุณาป้อนค่าใหม่อีกครั้ง**')
        except:
            print('**ไม่สามรถใช้ค่านี้ได้ กรุณาป้อนค่าใหม่อีกครั้ง**')

########################################################

def ind(vrange_num): #Induvidual Voltmeter
    print('-'*62)
    print('***กรุณาใส่ย่านวัดโดยเรียงจากน้อยไปหามาก โดยหากใส่สลับกัน')
    print('โปรแกรมจะทำกาารเรียงให้ย่านวัดที่น้อยที่สุดเป็นย่านที่ 1***')
    print('-'*62)
    for v in range(0,vrange_num):
        volt.append(float_in('ย่านวัดที่'+str(v+1)+' (V):')) 
    volt.sort()
    for r in range(0,vrange_num):
        resis.append(float((volt[r+1]-volt[0])/If))
    print('-'*62)

##########################################################

def vuni(vrange_num): #Universal Voltmeter
    print('-'*62)
    print('***กรุณาใส่ย่านวัดโดยเรียงจากน้อยไปหามาก โดยหากใส่สลับกัน')
    print('โปรแกรมจะทำกาารเรียงให้ย่านวัดที่น้อยที่สุดเป็นย่านที่ 1***')
    print('-'*62)
    for n in range (0,vrange_num):
        volt.append(float_in('ย่านวัดที่'+str(n +1)+' (V):'))
    volt.sort()
    for k in range (0,vrange_num):
        rs = float((volt[k+1]/If)-(volt[k]/If))
        resis.append(rs)
    print('-'*62)

############################################################

def auni(irange_num): # Ayrton shunt Ammter
    for v in range(0,irange_num):
        in_am = float_in('ย่านวัดที่'+str(v+1)+' (mA):')*(10**(-3))   
        amp.append(in_am)
    amp.sort()
    rt=(c_resis*If )/(amp[0]-If)
    for r in range(1,irange_num):
        resis.append(float((((amp[r]-If)*(rt-sum(resis)))-(If*(c_resis+sum(resis))))/amp[r]))
    resis.append(rt-sum(resis))
    print('-'*62)
    
##################################################################

def single(irange_num): #Single shunt  Ammeter and Multi range Ammter
    V_amp=   If*c_resis
    for v in range(0,irange_num):
        in_am = float_in('ย่านวัดที่'+str(v+1)+' (mA):')*(10**(-3))
        amp.append(in_am)
    amp.sort()
    for r in range(0,irange_num):
        resis.append(float((V_amp)/(amp[r]-If)))
    print('-'*62)
    
mchoice = 2
while True:
    if mchoice == 2:
        If = float_in('ระบุค่ากระแสเต็มสเกล(µA):') *(10**(-6))
        c_resis = float_in('ระบุค่าความต้านทานขดลวดเคลื่่อนที่(Ω):')
    volt = [If*c_resis]
    resis = []
    amp = []
    ampm = []
    print('-'*62)
    print('คุณต้องการใช้งานขดลวดเคลื่่อนที่นี้แบบไหน')
    print('-'*62)
    print('1.ทำเป็นโวลต์มิเตอร์และขยายย่านวัดแบบอินดิวิดวล')
    print('2.ทำเป็นโวลต์มิเตอร์และขยายย่านวัดแบบยูนิเวอร์แซล')
    print('3.ทำเป็นแอมมิเตอร์และขยายย่านวัดแบบซิงเกิลชันต์')
    print('4.ทำเป็นแอมมิเตอร์และขยายย่านวัดแบบยูนิเวอร์แซล')
    print('-'*62)
    choice = c_num(4)
    if choice == 1:
        r_num = num()
        ind(r_num)
    elif choice == 2:
        r_num = num()
        vuni(r_num)
    elif choice == 3:
        r_num = num()
        single(r_num)
    elif choice == 4:
        r_num = num()
        auni(r_num)

    if choice == 1 or choice == 2:    
        for m in range(0,r_num):
                if resis[m] < 0 or resis[m] < c_resis:
                    print('ย่านวัด',volt[m+1],'V |','Resistor',m+1,': ไม่จำเป็นต้องขยายย่านวัด')
                else:
                    if resis[m] > 1000:
                        d_in = str(resis[m]/1000).find('.')
                        out = str(resis[m]/1000)[0:d_in+4]
                        print('ย่านวัด',format(volt[m+1],'.1f'),'V |',' Resistor',m+1,':',out,' kΩ')
                    else:
                            print('ย่านวัด',volt[m+1],'V |','Resistor',m+1,':',resis[m],' Ω')
    elif choice == 3 or choice == 4:    
            for m in range(0,r_num):
                        d_in = str(resis[m]).find('.')
                        out = str(resis[m])[0:d_in+8]######################################
                        print('ย่านวัด',format(amp[m] * 1000,'.1f'),'mA |','Resistor',m+1,':',out,' Ω')
    resis = []
    print('-'*62)
    print('คุณต้องการจะทำอะไรต่อ')
    print('-'*62)
    print('1.ทำการคำนวณใหม่โดยใช้ค่าความต้านทานลวดและกระแสเต็มสเกลเดิม')
    print('2.ทำการคำนวณใหม่โดยแก้ไขค่าความต้านทานลวดและกระแสเต็มสเกล')
    print('3.ออกจากโปรแกรม')
    print('-'*62)
    mchoice = c_num(3)
    if mchoice == 3:
        break
    
exit()
