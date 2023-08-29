import math
import tkinter as tk
from tkinter import Canvas, Text, ttk

def time_add(beat1,tick1,beat2,tick2):
    beat=beat1+beat2
    tick=tick1+tick2
    while tick<0 or tick>=1920:
        if tick<0:
            tick=tick+1920
            beat-=1
        elif tick>=1920:
            tick=tick-1920
            beat+=1
    return beat,tick

class App(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self)
        #状态
        self.state="Hold Divider"        #Hold Divider Mirror Offset
        #Hold Divider 参数
        self.hold_type=["s","没做","没做","没做","没做"]
        #Mirror 参数
        self.slidechange={5:7,6:8,7:5,8:6,23:24,24:23}
        self.middle=89
        self.middle_var=tk.DoubleVar(value=44.5)
        self.img=tk.PhotoImage(file="resource/track.png")

        self.bind_all('<KeyPress>',self.listen_keyboard)
        self.setup_widgets()
        
    #部署物件
    def setup_widgets(self):
        #选择栏
        self.choice_bar = ttk.Notebook(self)
        self.choice_bar.pack(fill="both", expand=True)
        self.choice_bar.bind_all('<Button-1>',self.update_state)
        #Hold Divider
        self.hold_divider = ttk.Frame(self.choice_bar)
        self.setup_hold_divider(self.hold_divider)
        self.choice_bar.add(self.hold_divider, text="Hold Divider")
        #Mirror
        self.mirror = ttk.Frame(self.choice_bar)
        self.setup_mirror(self.mirror)
        self.choice_bar.add(self.mirror,text="Mirror")
        #Offset
        self.offset = ttk.Frame(self.choice_bar)
        self.setup_offset(self.offset)
        self.choice_bar.add(self.offset,text="Offset")

    #窗口状态更新
    def update_state(self,event):
        self.state=self.choice_bar.tab(self.choice_bar.select())['text']
    
    #键盘监听
    def listen_keyboard(self,event):
        if event.char == '\r':
            if self.state == "Hold Divider":
                self.HOLD_DIVIDER()
            elif self.state == "Mirror":
                self.MIRROR()
            elif self.state == "Offset":
                self.OFFSET()

######################################################################################################################
    #Hold Divider 部分
    def setup_hold_divider(self,frame):
        #时间部分:
        #区域
        frame.time_part=ttk.LabelFrame(frame,text="time")
        frame.time_part.grid(row=0,column=0,sticky="wn",padx=2,pady=2)
        #起始时间
        frame.start_time_label=ttk.Label(frame.time_part,text="start time:")
        frame.start_time_label.grid(row=0,column=0,sticky="w",pady=2)
        frame.start_time_entry=ttk.Entry(frame.time_part,state="normal",width=10)
        frame.start_time_entry.insert(0,"like 1 8/16")
        frame.start_time_entry.grid(row=0,column=1,sticky="w",pady=2)
        #结束时间
        frame.end_time_label=ttk.Label(frame.time_part,text="end time:")
        frame.end_time_label.grid(row=1,column=0,sticky="w",pady=2)
        frame.end_time_entry=ttk.Entry(frame.time_part,state="normal",width=10)
        frame.end_time_entry.insert(0,"like 2 0/16")
        frame.end_time_entry.grid(row=1,column=1,sticky="w",pady=2)
        #开始编号
        frame.number_label=ttk.Label(frame.time_part,text="start number:")
        frame.number_label.grid(row=2,column=0,sticky="w",pady=2)
        frame.number_entry=ttk.Entry(frame.time_part,state="normal",width=10)
        frame.number_entry.insert(0,"int≥0")
        frame.number_entry.grid(row=2,column=1,sticky="w",pady=2)

        #hold部分
        #区域
        frame.hold_part=ttk.LabelFrame(frame,text="hold information")
        frame.hold_part.grid(row=1,column=0,sticky="wn",padx=2,pady=2)
        #起始位置
        frame.start_hold_loc_label=ttk.Label(frame.hold_part,text="start location:")
        frame.start_hold_loc_label.grid(row=0,column=0,sticky="w",pady=2)
        frame.start_hold_loc_entry=ttk.Entry(frame.hold_part,state="normal",width=10)
        frame.start_hold_loc_entry.insert(0,"int∈R")
        frame.start_hold_loc_entry.grid(row=0,column=1,sticky="w",pady=2)
        #结束位置
        frame.end_hold_loc_label=ttk.Label(frame.hold_part,text="end location:")
        frame.end_hold_loc_label.grid(row=1,column=0,sticky="w",pady=2)
        frame.end_hold_loc_entry=ttk.Entry(frame.hold_part,state="normal",width=10)
        frame.end_hold_loc_entry.insert(0,"int∈R")
        frame.end_hold_loc_entry.grid(row=1,column=1,sticky="w",pady=2)
        #起始宽度
        frame.start_hold_width_label=ttk.Label(frame.hold_part,text="start width:")
        frame.start_hold_width_label.grid(row=2,column=0,sticky="w",pady=2)
        frame.start_hold_width_entry=ttk.Entry(frame.hold_part,state="normal",width=10)
        frame.start_hold_width_entry.insert(0,"int≥2")
        frame.start_hold_width_entry.grid(row=2,column=1,sticky="w",pady=2)        
        #结束宽度
        frame.end_hold_width_label=ttk.Label(frame.hold_part,text="end width:")
        frame.end_hold_width_label.grid(row=3,column=0,sticky="w",pady=2)
        frame.end_hold_width_entry=ttk.Entry(frame.hold_part,state="normal",width=10)
        frame.end_hold_width_entry.insert(0,"int≥1")
        frame.end_hold_width_entry.grid(row=3,column=1,sticky="w",pady=2)
        #hold类型
        frame.hold_type_label=ttk.Label(frame.hold_part,text="hold type:")
        frame.hold_type_label.grid(row=4,column=0,sticky="w",pady=2)
        frame.hold_type_box=ttk.Combobox(frame.hold_part,values=self.hold_type,width=10,state="readonly")
        frame.hold_type_box.current(0)
        frame.hold_type_box.grid(row=4,column=1,sticky="w",pady=2)

        #确认
        frame.commit_button=ttk.Button(frame,text="run",width=21,command=self.HOLD_DIVIDER)
        frame.commit_button.grid(row=2,column=0,sticky="wn",padx=2,pady=2)

        #信息栏
        frame.info_text=Text(frame,state="normal",width=60)
        frame.info_text.insert('0.0',chars="hello,i'm emu otori.")
        frame.info_text.configure(state='disabled')
        frame.info_text.grid(row=0,column=1,sticky="wnes",padx=5,pady=2,rowspan=3)
    
    def HOLD_DIVIDER(self):
        error_log=[]
        output=[]
        try:
            start_time=self.hold_divider.start_time_entry.get().strip()
            start_beat,start_tick=start_time.split(" ")
            start_beat=int(start_beat)
            a,b=start_tick.split("/")
            a,b=int(a),int(b)
            start_tick=int(1920*a/b)
        except ValueError:
            error_log.append("Error:invalid start time!")

        try:
            end_time=self.hold_divider.end_time_entry.get().strip()
            end_beat,end_tick=end_time.split(" ")
            end_beat=int(end_beat)
            a,b=end_tick.split("/")
            a,b=int(a),int(b)
            end_tick=int(1920*a/b)
        except ValueError:
            error_log.append("Error:invalid end time!")
        
        try:
            number=self.hold_divider.number_entry.get().strip()
            number=int(number)
            if number<0:
                raise ValueError
        except ValueError:
            error_log.append("Error:invalid number!")
        
        try:
            start_hold_loc=self.hold_divider.start_hold_loc_entry.get().strip()
            start_hold_loc=int(start_hold_loc)
        except ValueError:
            error_log.append("Error:invalid start location!")

        try:
            end_hold_loc=self.hold_divider.end_hold_loc_entry.get().strip()
            end_hold_loc=int(end_hold_loc)
        except ValueError:
            error_log.append("Error:invalid end location!")

        try:
            start_hold_width=self.hold_divider.start_hold_width_entry.get().strip()
            start_hold_width=int(start_hold_width)
            if start_hold_width<2:
                raise ValueError
        except ValueError:
            error_log.append("Error:invalid start width!")

        try:
            end_hold_width=self.hold_divider.end_hold_width_entry.get().strip()
            end_hold_width=int(end_hold_width)
            if end_hold_width<1:
                raise ValueError
        except ValueError:
            error_log.append("Error:invalid end width!")
            
        hold_type=self.hold_divider.hold_type_box.get().strip()
        if hold_type == "没做":
            error_log.append("Error:这个hold type以后再来探索吧!")

        if len(error_log) != 0:
            self.hold_divider.info_text.configure(state='normal')
            self.hold_divider.info_text.delete('0.0','end')
            for i in error_log: self.hold_divider.info_text.insert('end',chars=(i+'\n'))
            self.hold_divider.info_text.configure(state='disabled')
            error_log.clear()
            return
        
        d_loc=end_hold_loc-start_hold_loc        
        d_width=end_hold_width-start_hold_width
        #gcd=int(math.gcd(abs(d_loc),abs(d_width)))
        if d_width==0: d_width=1
        if d_loc==0: d_loc=1
        #pace=int((abs(d_loc)*abs(d_width))/gcd)
        #pace=math.gcd(abs(d_loc),abs(d_width))
        pace=max(abs(d_loc),abs(d_width))
        length=1920*(end_beat-start_beat)+end_tick-start_tick
        num=number
        event=1
        for i in range(pace+1):

            d_tick=int(i*length/pace)
            beat,tick=time_add(start_beat,start_tick,0,d_tick)
            n0n_ame=0
            
            if i == 0 :
                type=9
            elif i == pace :
                type=11
            else :
                type=10

            loc=start_hold_loc+int((end_hold_loc-start_hold_loc)*i/pace)
            loc=loc%60
            if loc%15==0 or i==0 or i==pace: n0n_ame=1
            width=start_hold_width+int((end_hold_width-start_hold_width)*i/pace)

            if i != pace:
                text="{:>4s} {:>4s} {:>4s} {:>4s} {:>4s} {:>4s} {:>4s} {:>4s} {:>4s}".format(str(beat),str(tick),str(event),str(type),str(num),str(loc),str(width),str(n0n_ame),str(num+1))
            else:
                text="{:>4s} {:>4s} {:>4s} {:>4s} {:>4s} {:>4s} {:>4s} {:>4s}".format(str(beat),str(tick),str(event),str(type),str(num),str(loc),str(width),str(n0n_ame))
            output.append(text)
            num+=1
            n0n_ame=0
        
        self.hold_divider.info_text.configure(state='normal')
        self.hold_divider.info_text.delete('0.0','end')
        for i in output: self.hold_divider.info_text.insert('end',chars=(i+'\n'))
        self.hold_divider.info_text.configure(state='disabled')
######################################################################################################################
    #Mirror 部分
    def setup_mirror(self,frame):
        #选择区域
        frame.select_part=ttk.Frame(frame,padding=(0, 10, 0, 0))

        frame.select_part.grid(row=0, column=0, padx=2, pady=5, sticky="nw")
        #滑动条
        frame.select_scale=ttk.Scale(
            frame.select_part,
            from_=0,
            to=119,
            length=270,
            variable=tk.DoubleVar(value=self.middle),
            command=self.offset_update_middle,
        )
        frame.select_scale.grid(row=0, column=0, padx=2, pady=5, sticky="nw")
        #位置信息
        frame.select_label=ttk.Label(frame.select_part,textvariable=self.middle_var)
        frame.select_label.grid(row=0, column=1, padx=2, pady=5, sticky="nw")

        #显示
        frame.pic_label=Canvas(frame.select_part,width=self.img.width(),height=self.img.height())
        frame.pic_label.create_image(self.img.width()/2,self.img.height()/2,image=self.img)
        frame.pic_label.grid(row=1,column=0,padx=2, pady=5, sticky="nw",columnspan=2)
        COLOR={0:'cyan',45:'#FF00FF',90:'cyan',135:'#FF00FF',180:'cyan',225:'#FF00FF',315:'#FF00FF',270:'cyan'}
        for key,value in COLOR.items():
            frame.pic_label.create_line(
            self.img.width()/2+125*math.cos(key*math.pi/180),
            self.img.height()/2-125*math.sin(key*math.pi/180),
            self.img.width()/2+150*math.cos(key*math.pi/180),
            self.img.height()/2-150*math.sin(key*math.pi/180),
            width=2,
            fill=value
        )
        frame.midline=frame.pic_label.create_line(
            self.img.width()/2-200*math.cos((3*self.middle+3)*math.pi/180),
            self.img.height()/2+200*math.sin((3*self.middle+3)*math.pi/180),
            self.img.width()/2+200*math.cos((3*self.middle+3)*math.pi/180),
            self.img.height()/2-200*math.sin((3*self.middle+3)*math.pi/180),
            width=2,
            fill='#FFFF00'
        )

        #确认
        frame.submit_button=ttk.Button(frame.select_part,text="run",command=self.MIRROR)
        frame.submit_button.grid(row=2,column=0,padx=2,pady=5,sticky="nwes",columnspan=2)

        #文本部分
        frame.text_part=ttk.Frame(frame,padding=(0, 10, 0, 0))
        frame.text_part.grid(row=0, column=2, padx=2, pady=5,sticky="nw")
        
        #序号
        frame.number_label=ttk.Label(frame.text_part,text="开始序号:",width=8)
        frame.number_label.grid(row=0,column=0,padx=0,pady=5,sticky="nw")
        frame.number_text=Text(frame.text_part,state="normal",height=1,width=10)
        frame.number_text.insert("0.0","0")
        frame.number_text.place(x=60,y=6)

        #输入
        frame.input_text=Text(frame.text_part,state='normal',width=40,height=8)
        frame.input_text.insert('0.0',"Input.")
        frame.input_text.grid(row=1,column=0, padx=2, pady=5,sticky="nw",columnspan=2)

        #输出
        frame.output_text=Text(frame.text_part,state='normal',width=40,height=8)
        frame.output_text.insert('0.0',"Output.")
        frame.output_text.grid(row=2,column=0, padx=2, pady=5,sticky="nw",columnspan=2)
        
    def offset_update_middle(self,event):
        self.middle=int(self.mirror.select_scale.get())
        self.middle_var.set(self.middle/2)
        self.mirror.pic_label.delete(self.mirror.midline)
        self.mirror.midline=self.mirror.pic_label.create_line(
            self.img.width()/2-200*math.cos((3*self.middle+3)*2*math.pi/360),
            self.img.height()/2+200*math.sin((3*self.middle+3)*2*math.pi/360),
            self.img.width()/2+200*math.cos((3*self.middle+3)*2*math.pi/360),
            self.img.height()/2-200*math.sin((3*self.middle+3)*2*math.pi/360),
            width=2,
            fill='#FFFF00'
        )

    def MIRROR(self):
        output=[]
        try:
            d_number=-1
            number=int(self.mirror.number_text.get('0.0','end'))
            INPUT=self.mirror.input_text.get('0.0','end')
            INPUT=INPUT.split("\n")
            for line in INPUT:
                #文件头
                if "#" in line:
                    output.append(line)
                    continue

                elements=line.split(" ")
                elements=[eval(e) for e in elements if e!=""]

                if 0<len(elements)<3: raise
                elif len(elements)==0: continue
                if elements[2]==1:#物件
                    if d_number == -1:
                        d_number=number-elements[4]
                    if elements[3] in [9,10,25]:#hold头,中继点,R类型hold头
                        elements[4]=elements[4]+d_number
                        elements[5]=(self.middle-elements[6]-elements[5]+1)%60
                        elements[8]=elements[8]+d_number
                    elif elements[3] in [5,6,7,8,23,24]:#slide
                        elements[3] = self.slidechange[elements[3]]
                        elements[4]=elements[4]+d_number
                        elements[5]=(self.middle-elements[6]-elements[5]+1)%60
                    elif elements[3] == 14:#mask
                        elements[4]=elements[4]+d_number
                    else:
                        elements[4]=elements[4]+d_number
                        elements[5]=(self.middle-elements[6]-elements[5]+1)%60

                s=[]
                for e in elements:
                    s.append("{:>4}".format(e))
                if len(s)==0 : continue
                output.append(" ".join(s))
        except:
            output.clear()
            output.append("Error!")
        
        self.mirror.output_text.delete('0.0','end')
        self.mirror.output_text.insert('0.0',"\n".join(output))
######################################################################################################################
    #Offset 部分
    def setup_offset(self,frame):
        #时间区域
        frame.time_part=ttk.Frame(frame)
        frame.time_part.grid(row=0,column=0,sticky="wn",padx=2,pady=2)
        #时间偏移
        frame.offset_time_label=ttk.Label(frame.time_part,text="时间偏移:")
        frame.offset_time_label.grid(row=0,column=0,sticky="w",pady=2)
        frame.offset_time_entry=ttk.Entry(frame.time_part,state="normal",width=10)
        frame.offset_time_entry.insert(0,"0 0/0")
        frame.offset_time_entry.grid(row=0,column=1,sticky="w",pady=2)
        #序号偏移
        frame.offset_num_label=ttk.Label(frame.time_part,text="序号偏移:")
        frame.offset_num_label.grid(row=1,column=0,sticky="w",pady=2)
        frame.offset_num_entry=ttk.Entry(frame.time_part,state="normal",width=10)
        frame.offset_num_entry.insert(0,"0")
        frame.offset_num_entry.grid(row=1,column=1,sticky="w",pady=2)
        #提交
        frame.commit_button=ttk.Button(frame.time_part,text="Run",command=self.OFFSET)
        frame.commit_button.grid(row=2,column=0,sticky="we",pady=2,columnspan=2)
        #tips
        frame.tips_label=ttk.Label(frame.time_part,text="时间偏移:1 12/16\n谱面时间加上1 12/16拍\n时间偏移:-1 12/16\n谱面时间减去1 12/16拍\n时间偏移0 0/0\n谱面时间不变\n")
        frame.tips_label.grid(row=3,column=0,sticky="we",pady=2,columnspan=2)

        #文本部分
        frame.text_part=ttk.Frame(frame)
        frame.text_part.grid(row=0, column=2, padx=2, pady=5,sticky="nw")
        #输入
        frame.input_text=Text(frame.text_part,state='normal',width=65,height=12)
        frame.input_text.insert('0.0',"Input.")
        frame.input_text.grid(row=1,column=0, padx=2, pady=5,sticky="nw",columnspan=2)
        #输出
        frame.output_text=Text(frame.text_part,state='normal',width=65,height=12)
        frame.output_text.insert('0.0',"Output.")
        frame.output_text.grid(row=2,column=0, padx=2, pady=5,sticky="nw",columnspan=2)    

    def OFFSET(self):
        output=[]
        try:
        #if True:
            flag=1
            offset_time=self.offset.offset_time_entry.get()
            offset_beat,offset_tick=offset_time.split(" ")
            if "-" in offset_time: flag=-1
            offset_beat=int(offset_beat)
            a,b=offset_tick.split("/")
            a,b=int(a),int(b)
            if b != 0:  offset_tick=int(1920*a/b)*flag
            if a==0 and b==0: offset_tick=0

            offset_num=int(self.offset.offset_num_entry.get())

            INPUT=self.offset.input_text.get('0.0','end')
            INPUT=INPUT.split("\n")
            for line in INPUT:
                #文件头
                if "#" in line:
                    output.append(line)
                    continue

                elements=line.split(" ")
                elements=[eval(e) for e in elements if e!=""]

                if 0<len(elements)<3: raise
                elif len(elements)==0: continue
                if elements[2]==1:#物件
                    elements[4]=elements[4]+offset_num
                    #mask end
                    if elements[3] in [12,13,14]: 
                        if elements[0] != 0 or elements[1] != 0:
                            elements[0],elements[1]=time_add(elements[0],elements[1],offset_beat,offset_tick)
                    #hold头,中继点,R类型hold头
                    elif elements[3] in [9,10,25]: 
                        elements[8]=elements[8]+offset_num
                        elements[0],elements[1]=time_add(elements[0],elements[1],offset_beat,offset_tick)
                    else:
                        elements[0],elements[1]=time_add(elements[0],elements[1],offset_beat,offset_tick)

                elif elements[2] in [2,3,5,6,7,8,9,10]:#BPM 拍号 hi-speed reverse reverse_end1/2 stop continue
                    if elements[0] != 0 or elements[1] != 0:
                        elements[0],elements[1]=time_add(elements[0],elements[1],offset_beat,offset_tick)     
                s=[]
                for e in elements:
                    s.append("{:>4}".format(e))
                if len(s)==0 : continue
                output.append(" ".join(s))
        except:
            output.clear()
            output.append("Error!")
        
        self.offset.output_text.delete('0.0','end')
        self.offset.output_text.insert('0.0',"\n".join(output))
################################################################################################
if __name__ == "__main__":
    mainframe = tk.Tk()
    mainframe.title("WACCA Tools")
    mainframe.iconbitmap("resource/wacca reverse.ico")
    mainframe.geometry('625x475')
    mainframe.maxsize(625,475)
    mainframe.minsize(625,475)

    # Simply set the theme
    mainframe.tk.call("source", "azure.tcl")
    mainframe.tk.call("set_theme", "light")

    app = App(mainframe)
    app.pack(fill="both", expand=True)

    mainframe.update()
    mainframe.minsize(mainframe.winfo_width(), mainframe.winfo_height())
    x_cordinate = int((mainframe.winfo_screenwidth() / 2) - (mainframe.winfo_width() / 2))
    y_cordinate = int((mainframe.winfo_screenheight() / 2) - (mainframe.winfo_height() / 2))
    mainframe.geometry("+{}+{}".format(x_cordinate, y_cordinate-20))

    mainframe.mainloop()