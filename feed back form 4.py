import tkinter as tk
root=tk.Tk()

root.title("form inputs")

root.geometry("400x400")

heading=tk.Label(root,text="feed back form")

heading.grid(row=0,column=1,pady=15)


field1=tk.Label(root,text="name")
field1.grid(row=1,column=0,pady=10)
input1=tk.Entry(root)
input1.grid(row=1,column=1,pady=10)


field2=tk.Label(root,text="Roll number")
field2.grid(row=1,column=0,pady=10)
input2=tk.Entry(root)
input2.grid(row=1,column=1,pady=10)

field2=tk.Label(root,text="college")
field2.grid(row=1,column=0,pady=10)
input2=tk.Entry(root)
input2.grid(row=1,column=1,pady=10)


field2=tk.Label(root,text="phone number")
field2.grid(row=1,column=0,pady=10)
input2=tk.Entry(root)
input2.grid(row=1,column=1,pady=10)

field2=tk.Label(root,text="address")
field2.grid(row=1,column=0,pady=10)
input2=tk.Entry(root)
input2.grid(row=1,column=1,pady=10)

field2=tk.Label(root,text="Remarks")
field2.grid(row=1,column=0,pady=10)
input2=tk.Entry(root)
input2.grid(row=1,column=1,pady=10)




submit_btn=tk.Button(root,text="submit",bg="blue",fg="red")
submit_btn.grid(row=8, column=0, columnspan=3, pady=25)

tk.mainloop()