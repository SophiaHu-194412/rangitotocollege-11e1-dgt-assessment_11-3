from pydoc import text
from tkinter import * 
import random
root = Tk()
menu = Menu(root)
root.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label='New')
filemenu.add_command(label='Open')
filemenu.add_command(label='Save')
filemenu.add_separator()
filemenu.add_command(label='Exit', command=root.quit)
helpmenu = Menu(menu)
menu.add_cascade(label='Help', menu=helpmenu)
helpmenu.add_command(label='About') 
w = Label(root, text="Hello, World!")
w.pack()
var1 = IntVar()
Checkbutton(root, text='male', variable=var1).pack()
var2 = IntVar()
Checkbutton(root, text='female', variable=var2).pack()
v = IntVar()
Radiobutton(root, text='one', variable=v, value=1).pack(anchor=W)
Radiobutton(root, text='two', variable=v, value=2).pack(anchor=W)
Radiobutton(root, text='three', variable=v, value=3).pack(anchor=W)

numbers_list = [1234, 2345, 3456, 4567, 5678, 6789, 7890, 8901, 9012, 0123, 1357, 2468, 3690, 1470, 2580, 3691, 4701, 5812, 6923, 7034, 8145, 9256,
                1023, 2134, 3245, 4356, 5467, 6578, 7689, 8790, 9801, 0912, 1593, 2684, 3775, 4866, 5957, 6048, 7139, 8220, 9311, 1402, 2513, 3624,
                4735, 5846, 6957, 7068, 8179, 9280, 0391, 1204, 2315, 3426, 4537, 5648, 6759, 7860, 8971, 9082, 0193, 1304, 2415, 3526, 4637, 5748,
                6859, 7960, 8071, 9182, 0293, 1405, 2516, 3627, 4738, 5849, 6950, 7061, 8172, 9283, 0394, 1205, 2316, 3427, 4538, 5649, 6750, 7861, 
                8972, 9083, 0194, 1305, 2416, 3527, 4638, 5749, 6850, 7961, 8072, 9183, 0294, 1406, 2517, 3628, 4739, 5840, 6951, 7062, 8173, 9284, 
                0395, 1206, 2317, 3428, 4539, 5640, 6751, 7862, 8973, 9084, 0195, 1306, 2417, 3528, 4639, 5740, 6851, 7962, 8073, 9184, 0295, 1407,
                2518, 3629, 4730, 5841, 6952, 7063, 8174, 9285, 0396, 1207, 2318, 3429, 4530, 5641, 6752, 7863, 8974, 9085, 0196, 1307, 2418, 3529,
                4630, 5741, 6852, 7963, 8074, 9185, 0296, 1408, 2519, 3620, 4731, 5842, 6953, 7064, 8175, 9286, 0397, 1208, 2319, 3420, 4531, 5642,
                6753, 7864, 8975, 9086, 0197, 1308, 2419, 3520, 4631, 5742, 6853, 7964, 8075, 9186, 0297, 1409, 2510, 3621, 4732, 5843, 6954, 7065, 8176, 9287, 0398,]
randnum = random.choice(numbers_list)
pork = Label(root, text=randnum)
pork.pack()

root.mainloop()
