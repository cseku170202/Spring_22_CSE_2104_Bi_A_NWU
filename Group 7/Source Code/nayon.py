import tkinter as tk
from tkinter import *
from tkinter import messagebox
import time


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add_begin(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def add_node(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            curr_node = self.head
            while curr_node.next is not None:
                curr_node = curr_node.next
            curr_node.next = new_node

    def add_after_x(self, data, x):
        n = self.head
        while n is not None:
            if x == n.data:
                break
            n = n.next

        if n is None:
            print("Node is not found in the linked list....")
        else:
            new_node = Node(data)
            new_node.next = n.next
            n.next = new_node

    def add_before_x(self, data, x):
        if self.head is None:
            print("Linked list is empty...!")
            return
        if self.head.data == x:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
            return

        n = self.head
        while n.next is not None:
            if n.next.data == x:
                break
            n = n.next
        if n.next is None:
            print("Node is not present in the linked list....")
        else:
            new_node = Node(data)
            new_node.next = n.next
            n.next = new_node

    def delete_node(self, data):
        curr_node = self.head
        prev_node = None
        while curr_node != None:
            if curr_node.data == data:
                if prev_node == None:
                    self.head = curr_node.next
                else:
                    prev_node.next = curr_node.next
                return True
            prev_node = curr_node
            curr_node = curr_node.next
        return False

    def display_list(self):
        curr_node = self.head
        while curr_node is not None:
            print(curr_node.data)
            curr_node = curr_node.next


class Ssd(LinkedList):
    def __init__(self, ssd):
        self.updated_value_entry = None
        self.current_value_entry = None
        self.array_update_entry = None
        self.array_delete_entry = None
        self.array_insert_entry = None
        self.array_search_element = None
        self.ssd = ssd
        self.current_interface = 0
        self.array_size = 0
        self.array = []

        self.home_interface()

    def home_interface(self):
        self.current_interface = 0
        self.ssd.title("Basic Data Structures")
        tk.Label(self.ssd, text="Choose one of tham", relief="solid", font="Arial, 40 bold",
                 bg="light salmon3").pack(pady=50)

        tk.Button(self.ssd, text="Array", font="Sans-serif, 20 bold", fg="black", bg="RosyBrown3", relief="raised",
                  bd=5,
                  command=self.array_interface).place(x=300, y=250)

        tk.Button(self.ssd, text="Linked List", font="Sans-serif, 20 bold", fg="black", bg="deep sky blue",
                  relief="raised", bd=5,
                  command=self.linkedlist).place(x=450, y=250)

        tk.Button(self.ssd, text="Quit", font="Sans-serif, 15 bold", fg="red", bg="black", relief="groove", bd=2,
                  command=self.ssd.destroy).place(x=700, y=500)

    def array_interface(self):

        self.ary = tk.Toplevel(bg="rosy brown")
        self.ary.title("Array")
        self.ary.geometry("900x600+300+80")
        tk.Label(self.ary, text="Input the size of array:", font="Sans-serif, 20 bold", bg="rosy brown").pack(pady=10)
        self.array_size_entry = tk.Entry(self.ary, width="3", font="Arial 25")
        self.array_size_entry.pack(pady=5)
        tk.Button(self.ary, text="Next", font="Sans-serif, 15", fg="black", bg="light salmon3",
                  command=self.create_array).place(x=455, y=115)
        tk.Button(self.ary, text="Back", font="Sans-serif, 15", fg="black", bg="chocolate",
                  command=self.ary.destroy).place(x=390, y=115)

    def create_array(self):

        self.array_size = int(self.array_size_entry.get())
        self.array_interface_2()

    def array_interface_2(self):
        # self.arr = tk.Toplevel()
        # self.arr.title("Array")
        self.current_interface = 2
        # self.master.title("Arrays: Input Elements")
        tk.Label(self.ary, text="Input array elements:", font="Sans-serif, 20 bold", bg="rosy brown").place(x=300,
                                                                                                            y=230)
        self.array_entries = []
        for i in range(self.array_size):
            entry = tk.Entry(self.ary, width="3", font="Arial 25")
            entry.place(x=300 + (i * 50), y=280)
            self.array_entries.append(entry)
        tk.Button(self.ary, text="Next", font="Sans-serif, 15", fg="black", bg="light salmon3",
                  command=self.show_array).place(x=455, y=330)
        tk.Button(self.ary, text="Back", font="Sans-serif, 15", fg="black", bg="sandybrown",
                  command=self.ary.destroy).place(x=390, y=330)

    def show_array(self):
        self.out = tk.Toplevel(bg="salmon")
        self.out.title("Arrays: Operations")
        self.out.geometry("900x600+300+80")
        # self.current_interface = 3
        # self.master.title("Arrays: Operations")
        self.array = []
        for entry in self.array_entries:
            self.array.append(int(entry.get()))
        tk.Label(self.out, text="Array: " + str(self.array), font="Sans-serif, 30 bold", bg="salmon").pack(pady=30)

        tk.Button(self.out, text="Insert", font="Sans-serif, 15", bg="sandybrown", fg="blue",
                  activeforeground="white", activebackground="grey", command=self.array_insert).place(x=270, y=250)

        tk.Button(self.out, text="Delete", font="Sans-serif, 15", bg="RosyBrown", fg="blue",
                  activeforeground="white", activebackground="grey", command=self.array_delete).place(x=370, y=250)
        tk.Button(self.out, text="Search", font="Sans-serif, 15", fg="black", bg="chocolate",
                  command=self.array_search).place(x=470, y=250)
        tk.Button(self.out, text="Update", font="Sans-serif, 15", fg="black", bg="light salmon3",
                  command=self.array_update).place(x=570, y=250)

        tk.Button(self.out, text="Back", font="Sans-serif, 15 bold", fg="green", bg="white", relief="groove", bd=1,
                  command=self.out.destroy).place(x=380, y=330)
        tk.Button(self.out, text="Exit", font="Sans-serif, 15 bold", fg="red", bg="black", relief="groove", bd=2,
                  command=self.ssd.destroy).place(x=460, y=330)

    def array_insert(self):
        self.insrt = tk.Toplevel(bg="azure4")
        self.insrt.title("Insert Operation")
        self.insrt.geometry("900x600+300+80")
        tk.Label(self.insrt, text="Input the value: ", font="Sans-serif, 20 bold",
                 bg="azure4").pack(pady=10)
        self.array_insert_entry = tk.Entry(self.insrt, width="3", font="Arial 25")
        self.array_insert_entry.pack(pady=5)
        tk.Label(self.insrt, text="Input the index number: ",
                 font="Sans-serif, 20 bold", bg="azure4").pack(pady=10)
        self.insert_position_entry = tk.Entry(self.insrt, width="3", font="Arial 25")
        self.insert_position_entry.pack(pady=5)
        tk.Button(self.insrt, text="Next", font="Sans-serif, 15", fg="black", bg="sandy brown",
                  command=self.insert_interface).pack(
            pady=5)
        tk.Button(self.insrt, text="Back", font="Sans-serif, 15", fg="black", bg="chocolate",
                  command=self.insrt.destroy).pack()

    def insert_interface(self):
        element = int(self.array_insert_entry.get())
        position = int(self.insert_position_entry.get())
        self.array.insert(position, element)
        tk.Label(self.insrt,
                 text=f"\nAfter inserting {element} at position {position}:\n\nUpdated array: {str(self.array)}",
                 font="Sans-serif, 20 bold", bg="azure4").pack(pady=20)
        tk.Button(self.insrt, text="Go to Array Home", font="Sans-serif, 15", bg="light coral", fg="black",
                  command=self.insrt.destroy).pack()

    def array_delete(self):
        self.dlt = tk.Toplevel(bg="azure4")
        self.dlt.title("Delete Operation")
        self.dlt.geometry("900x600+300+80")
        tk.Label(self.dlt, text="Choose one of tham delete option:", font="Sans-serif, 20 bold", bg="azure4").pack(pady=10)
        tk.Button(self.dlt, text="Delete by Index", font="Sans-serif, 15", bg="Lightsteelblue2", fg="black",
                  activeforeground="white", activebackground="grey", command=self.delete_by_index).pack(pady=5)
        tk.Button(self.dlt, text="Delete by Value", font="Sans-serif, 15", bg="Lightsteelblue2", fg="black",
                  activeforeground="white", activebackground="grey", command=self.delete_by_value).pack()

        tk.Button(self.dlt, text="Back", font="Sans-serif, 15 bold", fg="green", bg="white", relief="groove", bd=1,
                  command=self.dlt.destroy).place(x=380, y=200)
        tk.Button(self.dlt, text="Exit", font="Sans-serif, 15 bold", fg="red", bg="black", relief="groove", bd=1,
                  command=self.ssd.destroy).place(x=460, y=200)

    def delete_by_index(self):
        self.dlt.destroy()
        self.dlt_idx = tk.Toplevel(bg="azure4")
        self.dlt_idx.title("Delete by Index")
        self.dlt_idx.geometry("900x600+300+80")
        tk.Label(self.dlt_idx, text="Input the index number:", font="Sans-serif, 20 bold",
                 bg="azure4").pack(pady=10)
        self.array_delete_entry = tk.Entry(self.dlt_idx, width="3", font="Arial 25")
        self.array_delete_entry.pack(pady=5)
        tk.Button(self.dlt_idx, text="Next", font="Sans-serif, 15", bg="light salmon3", fg="black",
                  activeforeground="white", activebackground="grey", command=self.delete_by_index_interface).pack(
            pady=5)
        tk.Button(self.dlt_idx, text="Back", font="Sans-serif, 15", bg="chocolate", fg="black",
                  activeforeground="white", activebackground="grey", command=self.dlt_idx.destroy).pack()

    def delete_by_index_interface(self):
        index = int(self.array_delete_entry.get())
        if index >= 0 and index < len(self.array):
            self.array.pop(index)
            tk.Label(self.dlt_idx,
                     text="\nAfter deleting index No. " + str(index) + "\n\n Updated array: " + str(self.array),
                     font="Sans-serif, 20 bold", bg="azure4").pack(pady=20)
            tk.Button(self.dlt_idx, text="Go to Array Home", font="Sans-serif, 15", bg="Lightsteelblue2", fg="black",
                      activeforeground="white", activebackground="grey", command=self.dlt_idx.destroy).pack()
        else:
            tk.Label(self.dlt_idx, text="Invalid index. Please! enter a valid index.", font="Sans-serif, 20 bold",
                     bg="azure4").pack()

    def delete_by_value(self):
        self.dlt.destroy()
        self.dlt_val = tk.Toplevel(bg="azure4")
        self.dlt_val.title("Delete by Value")
        self.dlt_val.geometry("900x600+300+80")
        tk.Label(self.dlt_val, text="Input the value: ", font="Sans-serif, 20 bold",
                 bg="azure4").pack(pady=10)
        self.array_delete_entry = tk.Entry(self.dlt_val, width="3", font="Arial 25")
        self.array_delete_entry.pack(pady=5)
        tk.Button(self.dlt_val, text="Next", font="Sans-serif, 15", bg="light salmon3", fg="black",
                  activeforeground="white", activebackground="grey", command=self.delete_by_value_interface).pack(
            pady=5)
        tk.Button(self.dlt_val, text="Back", font="Sans-serif, 15", bg="chocolate", fg="black",
                  activeforeground="white", activebackground="grey", command=self.dlt_val.destroy).pack()

    def delete_by_value_interface(self):
        value = int(self.array_delete_entry.get())
        if value in self.array:
            self.array = [x for x in self.array if x != value]
            tk.Label(self.dlt_val,
                     text="\nAfter deleting value " + str(value) + "\n\n Updated array: " + str(self.array),
                     font="Sans-serif, 20 bold", bg="azure4").pack(pady=20)
            tk.Button(self.dlt_val, text="Go to Array Home", font="Sans-serif, 15", bg="Lightsteelblue2", fg="black",
                      activeforeground="white", activebackground="grey", command=self.dlt_val.destroy).pack()
        else:
            tk.Label(self.dlt_val, text="Value not found in the array",
                     font="Sans-serif, 20 bold",
                     bg="azure4").pack()

    def array_search(self):

        self.src = tk.Toplevel(bg="azure4")
        self.src.title("Search Operation")
        self.src.geometry("900x600+300+80")
        tk.Label(self.src, text="Input the element: " + str(self.array), font="Sans-serif, 20 bold",
                 bg="azure4").pack(pady=10)
        self.array_search_element = tk.Entry(self.src, width="3", font="Arial 25")
        self.array_search_element.pack(pady=5)
        tk.Button(self.src, text="Next", font="Sans-serif, 15", fg="black", bg="sandybrown",
                  command=self.search_interface).pack(pady=5)
        tk.Button(self.src, text="Back", font="Sans-serif, 15", fg="black", bg="light salmon3",
                  command=self.src.destroy).pack()

    def search_interface(self):

        global s_e
        global z
        global pos
        s_e = int(self.array_search_element.get())

        if s_e in self.array:
            pos = self.array.index(s_e)

            tk.Label(self.src, text=self.array_search_element.get() + " found in the Array at position " + str(pos),
                     font="Sans-serif, 20 bold", bg="azure4").pack(pady=5)

        else:
            tk.Label(self.src, text=self.array_search_element.get() + " not found in the Array:" + str(self.array),
                     font="Sans-serif, 20 bold", bg="azure4").pack(pady=5)

    def array_update(self):
        self.updt = tk.Toplevel(bg="azure4")
        self.updt.title("Update Operation")
        self.updt.geometry("900x600+300+80")
        tk.Label(self.updt, text="Input the index no and the value: " + str(self.array),
                 font="Sans-serif, 20 bold", bg="azure4").pack(pady=10)

        self.current_value_index = tk.Entry(self.updt, width="3", font="Arial 25")
        self.current_value_index.pack(pady=2)
        self.updated_value = tk.Entry(self.updt, width="3", font="Arial 25")
        self.updated_value.pack()
        tk.Button(self.updt, text="Next", font="Sans-serif, 15", fg="black", bg="chocolate",
                  command=self.update_interface).pack(pady=5)
        tk.Button(self.updt, text="Back", font="Sans-serif, 15", fg="black", bg="sandy brown",
                  command=self.updt.destroy).pack()

    def update_interface(self):
        index = int(self.current_value_index.get())
        value = int(self.updated_value.get())
        if index >= 0 and index < len(self.array):
            self.array[index] = value
            tk.Label(self.updt, text="After updating the element " + str(self.array),
                     font="Sans-serif, 20 bold", bg="azure4").pack()
        else:
            tk.Label(self.updt, text="Invalid index",
                     font="Sans-serif, 20 bold", bg="azure4").pack()

    def linkedlist(self):

        self.window = Toplevel(bg="sandy brown")
        self.window.title("Singly Linked List Operations")
        self.window.geometry("900x700+300+80")

        def add_begin():
            data = entryBox.get()
            if data.isdigit():
                links.add_begin(int(data))
                resultList.delete(0, END)
                resultList.insert(END, "Node added: " + data)
            else:
                resultList.delete(0, END)
                resultList.insert(END, "Invalid input")

        def add_node():
            data = entryBox.get()
            if data.isdigit():
                links.add_node(int(data))
                resultList.delete(0, END)
                resultList.insert(END, "Node added: " + data)
            else:
                resultList.delete(0, END)
                resultList.insert(END, "Invalid input")

        def add_after_x():
            data = entryBox.get()
            x = entryX.get()
            if data.isdigit() and x.isdigit():
                links.add_after_x(int(data), int(x))
                resultList.delete(0, END)
                resultList.insert(END, "Node added: " + data + " after " + x)
            else:
                resultList.delete(0, END)
                resultList.insert(END, "Invalid input")

        def add_before_x():
            data = entryBox.get()
            x = entryX.get()
            if data.isdigit() and x.isdigit():
                links.add_before_x(int(data), int(x))
                resultList.delete(0, END)
                resultList.insert(END, "Node added: " + data + " before " + x)
            else:
                resultList.delete(0, END)
                resultList.insert(END, "Invalid input")

        def delete_node():
            data = entryBox.get()
            if data.isdigit():
                if links.delete_node(int(data)):
                    resultList.delete(0, END)
                    resultList.insert(END, "Node deleted: " + data)
                else:
                    resultList.delete(0, END)
                    resultList.insert(END, "Node not found")
            else:
                resultList.delete(0, END)
                resultList.insert(END, "Invalid input")

        def display_list():
            resultList.delete(0, END)
            if links.head is None:
                resultList.insert(END, "NULL")
            else:
                resultList.insert(END, "List contents:")
                curr_node = links.head
                while curr_node is not None:
                    resultList.insert(END, curr_node.data)
                    curr_node = curr_node.next
                resultList.insert(END, "NULL")

        links = LinkedList()

        titleLabel = Label(self.window, text="Singly Linked List Operation", relief="solid", font="Arial, 30 bold",
                           bg="sandy brown")
        titleLabel.place(x=180, y=30)

        label = Label(self.window, text="Enter the value: ", bg="sandy brown", font="Arial 16 bold")
        label.place(x=210, y=110)

        entryBox = Entry(self.window, width=20, font="Arial 16")
        entryBox.place(x=420, y=110)

        entryLabelX = Label(self.window, text="Enter the node: ", bg="sandy brown", font="Arial 16 bold")
        entryLabelX.place(x=210, y=145)

        entryX = Entry(self.window, width=20, font="Arial 16")
        entryX.place(x=420, y=145)

        addButton = Button(self.window, text="Add at the beginning", font="Sans-serif, 14", bg="sandy brown", fg="blue",
                           activeforeground="white", activebackground="grey", command=add_begin)
        addButton.place(x=352, y=185)

        addButton = Button(self.window, text="Add at the end", font="Sans-serif, 14", bg="light coral", fg="blue",
                           activeforeground="white", activebackground="grey", command=add_node)
        addButton.place(x=310, y=232)

        addButton = Button(self.window, text="Add after X", font="Sans-serif, 14", bg="RosyBrown", fg="blue",
                           activeforeground="white", activebackground="grey", command=add_after_x)
        addButton.place(x=550, y=185)

        addButton = Button(self.window, text="Add before X", font="Sans-serif, 14", bg="light salmon3", fg="blue",
                           activeforeground="white", activebackground="grey", command=add_before_x)
        addButton.place(x=213, y=185)

        deleteButton = Button(self.window, text="Delete Node", font="Sans-serif, 14", bg="chocolate", fg="blue",
                              activeforeground="white", activebackground="grey", command=delete_node)
        deleteButton.place(x=460, y=232)

        displayButton = Button(self.window, text="Display List", font="Sans-serif, 14", bg="sandy brown", fg="blue",
                               activeforeground="white", activebackground="grey", command=display_list)
        displayButton.place(x=388, y=280)

        scrollbar = Scrollbar(self.window)
        scrollbar.pack(side=RIGHT, fill=Y)

        resultList = Listbox(self.window, width=30, height=15, font="arial 16", yscrollcommand=scrollbar.set)
        resultList.place(x=250, y=340)

        # Configure the scrollbar to work with the Listbox
        scrollbar.config(command=resultList.yview)

        tk.Button(self.window, text="Back", font="Sans-serif, 15 bold", fg="black", bg="light salmon3", relief="groove",
                  bd=1,
                  command=self.window.destroy).place(x=220, y=280)
        tk.Button(self.window, text="Exit", font="Sans-serif, 15 bold", fg="red", bg="RosyBrown", relief="groove", bd=1,
                  command=self.ssd.destroy).place(x=600, y=280)


root = tk.Tk()
root.geometry("900x600+300+80")
root.config(bg="light salmon3")
app = Ssd(root)
root.mainloop()

