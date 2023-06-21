# import os
import tkinter as tk
from tkinter import *
# from tkinter import messagebox
import time
from tkinter import colorchooser


class Raj:
    def __init__(self, majhar):
        self.value = None
        self.array_label = None
        self.delete_value_entry = None
        self.updated_value_entry = None
        self.current_value_entry = None
        self.array_update_entry = None
        self.array_delete_entry = None
        self.array_insert_entry = None
        self.array_search_element = None
        self.majhar = majhar
        self.current_interface = 0
        self.array_size = 0
        self.array = []
        self.home_interface()
        self.index_entry = None
        self.index_value = None

    def home_interface(self):
        self.current_interface = 0
        self.majhar.title("Basic Data Structures")
        Label(self.majhar, text="\u2744 Choose a Data Structure \u2744", relief="raised", font=("Times New Roman", 40, "bold"), bg="#8FB9A8").pack(pady=30)
        Button(self.majhar, text="Array", bg="#4D648D", fg="white",
                                     font=("Times New Roman", 15, "bold"), relief=RAISED, bd=10,
                  activeforeground="white", activebackground="grey", command=self.array_interface).pack(pady=5)
        Button(self.majhar, text="Linked List", font=("Times New Roman", 15, "bold"), bg="#4D648D", fg="white", relief="raised", bd=10,
                  activeforeground="white", activebackground="grey", command=self.llnew).pack(pady=5)
        # Button(self.majhar, text="Stack", font=("Times New Roman", 15, "bold"), bg="#ecf0f1", fg="black", relief="raised",
        #           activeforeground="white", activebackground="grey").pack(pady=5)
        # Button(self.majhar, text="Queue", font=("Times New Roman", 15, "bold"), bg="#ecf0f1", fg="black", relief="raised",
        #           activeforeground="white", activebackground="grey").pack(pady=5)
        # Button(self.majhar, text="Graph", font=("Times New Roman", 15, "bold"), bg="#ecf0f1", fg="black", relief="raised",
        #           activeforeground="white", activebackground="grey").pack(pady=5)
        # Button(self.majhar, text="Trees", font=("Times New Roman", 15, "bold"), bg="#ecf0f1", fg="black", relief="raised",
        #           activeforeground="white", activebackground="grey").pack(pady=5)
        Button(self.majhar, text="EXIT", bg="red", fg="black",font=("Times New Roman", 15, "bold"), relief=RAISED,
                           bd=10, state=NORMAL,activeforeground="white", activebackground="grey",
                  command=self.majhar.destroy).pack(pady=200)

    def array_interface(self):
        self.ary = tk.Toplevel(bg="#8FB9A8")
        self.ary.title("Array")
        self.ary.geometry("1520x792+0+0")
        tk.Label(self.ary, text="Enter the size of array:", font="Sans-serif, 20 bold", bg="#8FB9A8").pack(pady=10)
        self.array_size_entry = tk.Entry(self.ary, width="3", font="Arial 25")
        self.array_size_entry.place(x=710, y=62)
        self.array_size_entry.focus()
        Button(self.ary, text="Enter", font="Sans-serif, 15", bg="black", fg="lightsteelblue", bd=5, relief="raised",
                  activeforeground="white", activebackground="grey", command=self.new).place(x=770, y=61)

    # def create_array(self):
    #
    #     self.array_size = int(self.array_size_entry.get())
    #     self.array_interface_2()
    #
    # def array_interface_2(self):
    #     tk.Label(self.ary, text="Enter array elements:", font="Sans-serif, 20 bold", bg="#8FB9A8").pack(pady=5)
    #     self.array_entries = []
    #     for i in range(self.array_size):
    #         entry = tk.Entry(self.ary, width="3", font="Arial 25")
    #         entry.pack(pady=2)
    #         self.array_entries.append(entry)
    #     tk.Button(self.ary, text="Next", font="Sans-serif, 15", bg="black", fg="lightsteelblue", bd=10, relief="raised",
    #               activeforeground="white", activebackground="grey", command=self.show_array).pack(pady=5)
    #     tk.Button(self.ary, text="Back", font="Sans-serif, 15", bg="black", fg="lightsteelblue", bd=10, relief="raised",
    #               activeforeground="white", activebackground="grey", command=self.ary.destroy).pack()


    def new(self):

        tk.Label(self.ary, text="Enter array elements: ", font="Sans-serif, 20 bold", bg="#8FB9A8").place(x=610, y=102)
        self.array_elements = tk.Entry(self.ary, width="15", font="Arial 25")
        self.array_elements.place(x=620, y=142)
        self.array_elements.focus()
        tk.Button(self.ary, text="Create", font="Sans-serif, 15", bg="green", fg="white", bd=10, relief="raised",
                  activeforeground="white", activebackground="grey", command=self.show_array).place(x=715, y=186)

        tk.Button(self.ary, text="Goto Home", font="Sans-serif, 15", bg="purple", fg="white", bd=10,
                  relief="raised",
                  activeforeground="white", activebackground="grey", command=self.ary.destroy).place(x=690, y=400)




    def show_array(self):
        self.out = tk.Toplevel(bg="#8FB9A8")
        self.out.title("Arrays: Operations")
        self.out.geometry("1520x792+0+0")

        global array
        array = Label(self.out, text="", font=("Times New Roman", 40, "bold"), bg="#8FB9A8")
        array.pack()


        self.size = int(self.array_size_entry.get())

        array_str = self.array_elements.get()
        self.array = [int(num) for num in array_str.split()[:self.size]]


        array.config(text="Array: " + str(self.array))

        self.refreshbtn = Button(self.out, text="\u27F3 Refresh", font=("Times New Roman", 12, "bold"), bg="skyblue", fg="black", bd=5, relief="raised",
                  activeforeground="white", activebackground="grey", command=self.refresh).place(x=730, y=80)

        # tk.Button(self.out, text="Sort The Array", bg="black", fg="white", bd=5, relief="raised",
        #           activeforeground="white", activebackground="grey", command=self.sorting).pack(pady=10)

        tk.Button(self.out, text="Search", font="Sans-serif, 15", bg="#4B3832", fg="white", bd=10, relief="raised",
                  activeforeground="white", activebackground="grey", command=self.array_search).place(x=725, y=150)
        tk.Button(self.out, text="Insert", font="Sans-serif, 15", bg="#4B3832", fg="white", bd=10, relief="raised",
                  activeforeground="white", activebackground="grey", command=self.array_insert).place(x=550, y=270)
        tk.Button(self.out, text="Delete", font="Sans-serif, 15", bg="#4B3832", fg="white", bd=10, relief="raised",
                  activeforeground="white", activebackground="grey", command=self.array_delete).place(x=900, y=270)
        tk.Button(self.out, text="Update", font="Sans-serif, 15", bg="#4B3832", fg="white", bd=10, relief="raised",
                  activeforeground="white", activebackground="grey", command=self.update).place(x=725, y=400)
        # tk.Button(self.out, text="Back", font="Sans-serif, 15", bg="black", fg="white", bd=10, relief="raised", activeforeground="white",
        #           activebackground="grey", command=self.out.destroy).pack(pady=50)
        tk.Button(self.out, text="EXIT", bg="red", fg="black",font=("Times New Roman", 15, "bold"), relief=RAISED,
                           bd=10, state=NORMAL, activeforeground="white",
                  activebackground="grey", command=self.majhar.destroy).place(x=730, y=270)

        tk.Button(self.out, text="Next", font="Sans-serif, 15", bg="purple", fg="white", bd=10, relief="raised",
                  activeforeground="white", activebackground="grey", command=self.array_search).place(x=1400, y=600)
        tk.Button(self.out, text="Back", font="Sans-serif, 15", bg="purple", fg="white", bd=10, relief="raised",
                  activeforeground="white", activebackground="grey", command=self.out.destroy).place(x=50, y=600)


    # def sorting(self):
    #     self.array.sort()
    #     self.sorted = tk.Label(self.out, text="Sorted Array: " + str(self.array), font="Sans-serif, 30 bold", bg="#8FB9A8").pack(pady=30)




    def array_search(self):

        self.src = tk.Toplevel(bg="#8FB9A8")
        self.src.title("Search Operation")
        self.src.geometry("1520x792+0+0")

        tk.Label(self.src, text="\u2605 Search Operation \u2605", font=("Times New Roman", 40, "bold"),
                 relief="raised", bg="#8FB9A8").pack(pady=30)

        tk.Label(self.src, text="Enter the element you want to search: " + str(self.array), font="Sans-serif, 20 bold",
                 bg="#8FB9A8").pack(pady=10)
        self.array_search_element = tk.Entry(self.src, width="3", font="Arial 25")
        self.array_search_element.pack(pady=5)
        self.array_search_element.focus()
        tk.Button(self.src, text="Search", font="Sans-serif, 15", bg="green", fg="white", bd=10, relief="raised",
                  activeforeground="white", activebackground="grey", command=self.V_search_result).pack(pady=5)

        tk.Button(self.src, text="Next", font="Sans-serif, 15", bg="purple", fg="white", bd=10, relief="raised",
                  activeforeground="white", activebackground="grey", command=self.array_insert).place(x=1400, y=600)
        tk.Button(self.src, text="Back", font="Sans-serif, 15", bg="purple", fg="white", bd=10, relief="raised",
                  activeforeground="white", activebackground="grey", command=self.src.destroy).place(x=50, y=600)



    def V_search_result(self):

        global lblSearch
        global SearchElement
        global pos
        global ShowPos
        SearchElement = int(self.array_search_element.get())

        if SearchElement in self.array:
            pos = self.array.index(SearchElement)
            ShowPos = pos + 1

            lblSearch = Label(self.src, text=str(SearchElement) + " Found at Position " + str(ShowPos), font="Sans-serif, 20 bold", bg="#8FB9A8")
            lblSearch.pack(pady=10)

        else:

            lblSearch.config(text=str(SearchElement) + " Not Found in the Array")
            lblSearch.pack(pady=10)

    def array_insert(self):
        self.insrt = tk.Toplevel(bg="#8FB9A8")
        self.insrt.title("Insert Operation: By Value")
        self.insrt.geometry("1520x792+0+0")

        Label(self.insrt, text="\u2605 Insert Operation \u2605", font=("Times New Roman", 40, "bold"),
                 relief="raised", bg="#8FB9A8").pack(pady=30)


        self.value= tk.Button(self.insrt, text="Insert By Value", font="Sans-serif, 15", bg="#4B3832", fg="white", bd=10, relief="raised",
                  activeforeground="white", activebackground="grey", command=self.insert_with_value).place(x=100, y=150)

        self.index= tk.Button(self.insrt, text="Insert By Index No.", font="Sans-serif, 15", bg="#4B3832", fg="white", bd=10, relief="raised",
                  activeforeground="white", activebackground="grey", command=self.insert_with_index).place(x=100, y=210)

        tk.Button(self.insrt, text="Next", font="Sans-serif, 15", bg="purple", fg="white", bd=10, relief="raised",
                  activeforeground="white", activebackground="grey", command=self.array_delete).place(x=1400,
                                                                                                      y=600)
        tk.Button(self.insrt, text="Back", font="Sans-serif, 15", bg="purple", fg="white", bd=10, relief="raised",
                  activeforeground="white", activebackground="grey", command=self.insrt.destroy).place(x=50, y=600)







    def insert_with_value(self):

        tk.Label(self.insrt, text="Enter the element you want to insert: " + str(self.array),font="Sans-serif, 20 bold",
                 bg="#8FB9A8").pack(pady=10)

        self.array_insert_entry = tk.Entry(self.insrt, width="3", font="Arial 25")
        self.array_insert_entry.pack(pady=5)
        self.array_insert_entry.focus()

        tk.Button(self.insrt, text="Insert", font="Sans-serif, 15", bg="green", fg="white", bd=10, relief="raised",
                  activeforeground="white", activebackground="grey", command=self.insert_with_value2).pack(pady=10)

        # tk.Button(self.insrt, text="Next", font="Sans-serif, 15", bg="black", fg="white", bd=10, relief="raised",
        #           activeforeground="white", activebackground="grey", command=self.array_delete).place(x=1400,
        #                                                                                                     y=600)
        # tk.Button(self.insrt, text="Back", font="Sans-serif, 15", bg="black", fg="white", bd=10, relief="raised",
        #           activeforeground="white", activebackground="grey", command=self.insrt.destroy).place(x=50, y=600)



    def insert_with_value2(self):

        self.array.append(int(self.array_insert_entry.get()))
        tk.Label(self.insrt,
                 text="\nAfter inserting " + self.array_insert_entry.get() + "\n\n Updated array: " + str(self.array),
                 font="Sans-serif, 20 bold", bg="#8FB9A8").pack(pady=20)



    def insert_with_index(self):
        self.insrt_indx = tk.Toplevel(bg="#8FB9A8")
        self.insrt_indx.title("Insert Operation: By Index")
        self.insrt_indx.geometry("1520x792+0+0")

        tk.Label(self.insrt_indx, text="Array: " + str(self.array), font="Sans-serif, 20 bold", bg="#8FB9A8").pack(pady=10)

        tk.Label(self.insrt_indx, text="Enter the Index No.", font="Sans-serif, 20 bold", bg="#8FB9A8").pack(pady=10)
        self.index_entry = tk.Entry(self.insrt_indx, width="3", font="Arial 25")
        self.index_entry.pack(pady=5)
        self.index_entry.focus()

        tk.Label(self.insrt_indx, text="Enter the Value", font="Sans-serif, 20 bold", bg="#8FB9A8").pack(pady=10)
        self.index_value = tk.Entry(self.insrt_indx, width="3", font="Arial 25")
        self.index_value.pack(pady=5)

        tk.Button(self.insrt_indx, text="Insert", font="Sans-serif, 15", bg="green", fg="white", bd=10, relief="raised",
                  activeforeground="white", activebackground="grey", command=self.insert_with_index2).pack()

        tk.Button(self.insrt_indx, text="Next", font="Sans-serif, 15", bg="purple", fg="white", bd=10, relief="raised",
                  activeforeground="white", activebackground="grey", command=self.array_delete).place(x=1400,
                                                                                                      y=600)
        tk.Button(self.insrt_indx, text="Back", font="Sans-serif, 15", bg="purple", fg="white", bd=10, relief="raised",
                  activeforeground="white", activebackground="grey", command=self.insrt_indx.destroy).place(x=50, y=600)





    def insert_with_index2(self):
        self.array.insert(int(self.index_entry.get()), int(self.index_value.get()))

        tk.Label(self.insrt_indx, text="\nAfter inserting " + str(self.index_value.get()) + " at Position: "
                                       + str(self.index_entry.get()) + " (including 0)" + " \n\nUpdated array: "
                                       + str(self.array), font="Sans-serif, 20 bold", bg="#8FB9A8").pack(pady=10)





    def array_delete(self):
        self.dlt = tk.Toplevel(bg="#8FB9A8")
        self.dlt.title("Delete Operation")
        self.dlt.geometry("1520x792+0+0")

        Label(self.dlt, text="\u2605 Delete Operation \u2605", font=("Times New Roman", 40, "bold"),
                 relief="raised", bg="#8FB9A8").pack(pady=30)

        Button(self.dlt, text="Delete by Value", font="Sans-serif, 15", bg="#4B3832", fg="white", bd=10, relief="raised",
                  activeforeground="white", activebackground="grey", command=self.delete_by_value).place(x=100, y=150)

        Button(self.dlt, text="Delete by Index No.", font="Sans-serif, 15", bg="#4B3832", fg="white", bd=10, relief="raised",
                  activeforeground="white", activebackground="grey", command=self.delete_by_index).place(x=100, y=210)




        Button(self.dlt, text="Next", font="Sans-serif, 15", bg="purple", fg="white", bd=10, relief="raised",
                  activeforeground="white", activebackground="grey", command=self.update).place(x=1400, y=600)
        Button(self.dlt, text="Back", font="Sans-serif, 15", bg="purple", fg="white", bd=10, relief="raised",
                  activeforeground="white", activebackground="grey", command=self.dlt.destroy).place(x=50, y=600)

    def delete_by_value(self):

        tk.Label(self.dlt, text="Enter the value you want to delete from the Array: " + str(self.array), font="Sans-serif, 20 bold", bg="#8FB9A8").pack(pady=10)
        self.delete_value = tk.Entry(self.dlt, width="3", font="Arial 25")
        self.delete_value.pack(pady=5)
        self.delete_value.focus()

        tk.Button(self.dlt, text="Delete", font="Sans-serif, 15", bg="green", fg="white", bd=10, relief="raised",
                  activeforeground="white", activebackground="grey", command=self.delete_interface0).pack(pady=5)



    def delete_interface0(self):
        global array_label
        global value
        global dlt_value
        dlt_value = None

        value = int(self.delete_value.get())
        try:
            if value in self.array:
                self.array.remove(value)
                array_label = Label(self.dlt, text="After deleting: " + str(value)+ "\n Updated array: " +
                                                            str(self.array), font="Sans-serif, 20 bold", bg="#8FB9A8").pack(pady=10)
                tk.Button(self.dlt_by_index, text="Go to Array Home", font="Sans-serif, 15", bg="Lightsteelblue2",
                          fg="black", bd=10, relief="raised", activeforeground="white", activebackground="grey", command=self.out.destroy).pack()
            else:
                Label(self.dlt, text="Value not found.", font="Sans-serif, 20 bold", bg="#8FB9A8").pack(pady=10)
        except ValueError:
            Label(self.dlt, text="Invalid Value.", font="Sans-serif, 20 bold", bg="#8FB9A8").pack(pady=10)





    def delete_by_index(self):

        self.dlt_by_index = tk.Toplevel(bg="#8FB9A8")
        self.dlt_by_index.title("Delete Operation: By Index")
        self.dlt_by_index.geometry("1520x792+0+0")

        tk.Label(self.dlt_by_index, text="Enter the index number you want to delete from the\nArray (including 0): " + str(self.array),
                 font="Sans-serif, 20 bold", bg="#8FB9A8").pack(pady=10)
        self.array_delete_entry = tk.Entry(self.dlt_by_index, width="3", font="Arial 25")
        self.array_delete_entry.pack(pady=5)
        self.array_delete_entry.focus()

        Button(self.dlt_by_index, text="Delete", font="Sans-serif, 15", bg="green", fg="white", bd=10, relief="raised",
                  activeforeground="white", activebackground="grey", command=self.delete_interface).pack()

        Button(self.dlt_by_index, text="Next", font="Sans-serif, 15", bg="purple", fg="white", bd=10, relief="raised",
                  activeforeground="white", activebackground="grey", command=self.update).place(x=1400, y=600)
        Button(self.dlt_by_index, text="Back", font="Sans-serif, 15", bg="purple", fg="white", bd=10, relief="raised",
                  activeforeground="white", activebackground="grey", command=self.dlt_by_index.destroy).place(x=50, y=600)




    def delete_interface(self):
        self.x = int(self.array_delete_entry.get())
        self.array.__delitem__(self.x)
        tk.Label(self.dlt_by_index,
                 text="\nAfter deleting index No: " + self.array_delete_entry.get() + " (including 0)"
                      + "\n\n Updated array: " + str(self.array), font="Sans-serif, 20 bold", bg="#8FB9A8").pack(pady=20)



    def update(self):

        global old_value
        global new_value
        self.up = Toplevel(bg="#8FB9A8")
        self.up.title("Update Operation")
        self.up.geometry("1520x792+0+0")

        Label(self.up, text="\u2605 Update Operation \u2605", font=("Times New Roman", 40, "bold"),
                 relief="raised", bg="#8FB9A8").pack(pady=30)

        tk.Label(self.up, text="Array: " + str(self.array), font="Sans-serif, 30 bold", bg="#8FB9A8").pack(pady=10)

        self.old_value_label = Label(self.up, text="Enter Existing Value:", font="Sans-serif, 20 bold", bg="#8FB9A8")
        self.old_value_label.pack(pady=5)
        self.old_value_entry = Entry(self.up, width="3", font="Arial 20")
        self.old_value_entry.place(x=900, y=200)
        self.old_value_entry.focus()

        self.new_value_label = Label(self.up, text="Enter New Value:", font="Sans-serif, 20 bold", bg="#8FB9A8")
        self.new_value_label.pack()
        self.new_value_entry = Entry(self.up, width="3", font="Arial 20")
        self.new_value_entry.place(x=900, y=245)

        Button(self.up, text="Update", font="Sans-serif, 15", bg="green", fg="white", bd=10, relief="raised",
                  activeforeground="white", activebackground="grey", command=self.update_fn).pack(pady=5)


        tk.Button(self.up, text="END", font="Sans-serif, 15", bg="purple", fg="black", bd=10, relief="raised",
                  activeforeground="white", activebackground="grey", command=self.majhar.destroy).place(x=1400, y=600)
        tk.Button(self.up, text="Back", font="Sans-serif, 15", bg="purple", fg="white", bd=10, relief="raised",
                  activeforeground="white", activebackground="grey", command=self.up.destroy).place(x=50, y=600)





    def update_fn(self):

        self.uplbl = Label(self.up, text="", font="Sans-serif, 20 bold", bg="#8FB9A8")
        self.uplbl.pack(pady=10)

        old_value = int(self.old_value_entry.get())
        new_value = int(self.new_value_entry.get())

        if old_value in self.array:
            index = self.array.index(old_value)
            self.array[index] = new_value

            self.uplbl.config(text="After Updating " + self.old_value_entry.get() + " by " + self.new_value_entry.get()+
                                   "\nUpdated array: " + str(self.array))
        else:
            self.uplbl.config(text=str(self.old_value_entry.get()) + " not found in the array")




    def refresh(self):
        array.config(text="Array: " + str(self.array))



########################################################################################################################
#                                                                                                                      #
#                                         L I N K E D     L I S T                                                      #
#                                                                                                                      #
########################################################################################################################

    def llnew(self):
        LinkedListGUI()


# Node class for creating linked list nodes
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Linked List class for performing operations on the linked list
class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def search(self, data):
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False

    def delete(self, data):
        if self.head is None:
            return

        if self.head.data == data:
            self.head = self.head.next
            return

        current = self.head
        prev = None
        while current:
            if current.data == data:
                prev.next = current.next
                return
            prev = current
            current = current.next

    def update(self, old_data, new_data):
        current = self.head
        while current:
            if current.data == old_data:
                current.data = new_data
                return
            current = current.next

    def get_list_as_string(self):
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next
        return " --> ".join(elements)


# LinkedListGUI class for creating the graphical user interface
class LinkedListGUI:
    def __init__(self):
        self.linked_list = LinkedList()

        self.window = tk.Tk()
        self.window.title("Linked List Operations")
        self.window.config(bg="#8FB9A8")

        self.window.geometry("1520x792+0+0")

        Label(self.window, text="\u2744Linked List\u2744", relief="raised", font=("Times New Roman", 40, "bold"),
              bg="#8FB9A8").pack(pady=20)

        self.label = tk.Label(self.window, text="Enter values (space-separated):", font=("Times New Roman", 20, "bold"),
                              bg="#8FB9A8")
        self.label.pack()

        self.entry = tk.Entry(self.window, width="20", font="Arial 20")
        self.entry.pack()
        self.entry.focus()

        self.create_btn = tk.Button(self.window, text="Create List", command=self.create_list,
                                    font=("Times New Roman", 15, "bold"), bg="#75DF62", fg="black", bd=5,
                                    relief="raised",
                                    activeforeground="white", activebackground="grey")
        self.create_btn.place(x=705, y=182)


        self.operation_label = tk.Label(self.window, text="Perform Operation:", font=("Times New Roman", 25, "bold"),
                                        bg="#8FB9A8")
        self.operation_label.place(x=620, y=240)


        self.search_btn = tk.Button(self.window, text="Search", command=self.open_search_window,
                                    font=("Times New Roman", 15, "bold"), bg="teal", fg="white", bd=5, relief="raised",
                                    activeforeground="white", activebackground="grey")
        self.search_btn.place(x=600, y=300)
        self.insert_btn = tk.Button(self.window, text="Insert", command=self.insert,
                                    font=("Times New Roman", 15, "bold"), bg="teal", fg="white", bd=5, relief="raised",
                                    activeforeground="white", activebackground="grey")
        self.insert_btn.place(x=850, y=300)

        self.delete_btn = tk.Button(self.window, text="Delete", command=self.delete,
                                    font=("Times New Roman", 15, "bold"), bg="teal", fg="white", bd=5, relief="raised",
                                    activeforeground="white", activebackground="grey")
        self.delete_btn.place(x=600, y=400)

        self.update_btn = tk.Button(self.window, text="Update", command=self.update,
                                    font=("Times New Roman", 15, "bold"), bg="teal", fg="white", bd=5, relief="raised",
                                    activeforeground="white", activebackground="grey")
        self.update_btn.place(x=850, y=400)

        self.update_btn = tk.Button(self.window, text="HOME", command=self.window.destroy,
                                    font=("Times New Roman", 15, "bold"), bg="#CCAC93", fg="black", bd=5,
                                    relief="raised",
                                    activeforeground="white", activebackground="grey")
        self.update_btn.place(x=725, y=350)

        self.output_label = tk.Label(self.window, text="", font=("Times New Roman", 20, "bold"), bg="#8FB9A8")
        self.output_label.place(x=580, y=500)

        self.window.mainloop()

    def create_list(self):
        values = self.entry.get().split()
        for value in values:
            self.linked_list.insert(value)

        list_string = self.linked_list.get_list_as_string()
        self.output_label.config(text="Linked List: " + list_string)
        self.entry.delete(0, tk.END)  # Clear the operation entry field


    def animate(self, operation):
        self.output_label.config(text="Performing operation...")
        self.window.update()
        time.sleep(1)
        if operation == "search":
            value = self.operation_entry.get()
            result = self.linked_list.search(value)
            if result:
                self.output_label.config(text="Value found in the linked list.")
            else:
                self.output_label.config(text="Value not found in the linked list.")
        elif operation == "insert":
            value = self.operation_entry.get()
            self.linked_list.insert(value)
            self.output_label.config(text="Value inserted into the linked list.")
        elif operation == "delete":
            value = self.operation_entry.get()
            self.linked_list.delete(value)
            self.output_label.config(text="Value deleted from the linked list.")
        elif operation == "update":
            values = self.operation_entry.get().split()
            old_value = values[0]
            new_value = values[1]
            self.linked_list.update(old_value, new_value)
            self.output_label.config(text="Value updated in the linked list.")

        self.create_list()  # Display the updated list after performing the operation
        # self.operation_entry.delete(0, tk.END)  # Clear the operation entry field

    def open_search_window(self):
        search_window = tk.Toplevel(self.window)
        search_window.title("Search")
        search_window.config(bg="#8FB9A8")
        search_window.geometry("500x500+10+35")

        search_label = tk.Label(search_window, text="Enter value to search:", font=("Times New Roman", 30, "bold"),
                                bg="#8FB9A8")
        search_label.pack(pady=50)

        search_entry = tk.Entry(search_window, width="10", font="Arial 20")
        search_entry.pack(pady=5)
        search_entry.focus()

        search_btn = tk.Button(search_window, text="Search", command=lambda: self.search_value(search_entry.get()),
                               font=("Times New Roman", 15, "bold"), bg="purple", fg="white", bd=5, relief="raised",
                               activeforeground="white", activebackground="grey")
        search_btn.pack()

    def search_value(self, value):
        found = self.linked_list.search(value)
        if found:
            position = self.get_position(value)
            message = f"The value {value} is found at position {position}\n Linked List: " + self.linked_list.get_list_as_string()

        else:
            message = f"The value {value} is not found in the linked list."
        self.output_label.config(text=message)

        self.operation_entry.delete(0, tk.END)  # Clear the operation entry field

    def get_position(self, value):
        current = self.linked_list.head
        position = 1

        while current:
            if current.data == value:
                return position
            current = current.next
            position += 1

        return -1

    def insert(self):
        insert_window = tk.Toplevel(self.window)
        insert_window.title("Insert Operation")
        insert_window.config(bg="#8FB9A8")
        insert_window.geometry("500x500+10+35")

        insert_label = tk.Label(insert_window, text="Choose Insert Mode:", font=("Times New Roman", 30, "bold"),
                                bg="#8FB9A8")
        insert_label.pack(pady=50)

        direct_btn = tk.Button(insert_window, text="Insert with Value",
                               command=lambda: self.open_insert_direct(insert_window),
                               font=("Times New Roman", 15, "bold"), bg="purple", fg="white", bd=5, relief="raised",
                               activeforeground="white", activebackground="grey")
        direct_btn.pack(pady=10)

        index_btn = tk.Button(insert_window, text="Insert with Index",
                              command=lambda: self.open_insert_index(insert_window),
                              font=("Times New Roman", 15, "bold"), bg="purple", fg="white", bd=5, relief="raised",
                              activeforeground="white", activebackground="grey")
        index_btn.pack()

    def open_insert_direct(self, window):
        # window.destroy()

        insert_direct_window = tk.Toplevel(self.window)
        insert_direct_window.title("Insert with Direct Value")
        insert_direct_window.config(bg="#8FB9A8")
        insert_direct_window.geometry("500x500+10+35")

        value_label = tk.Label(insert_direct_window, text="Enter Value:", font=("Times New Roman", 20, "bold"),
                               bg="#8FB9A8")
        value_label.pack(pady=10)

        value_entry = tk.Entry(insert_direct_window, width="10", font="Arial 20")
        value_entry.pack(pady=5)
        value_entry.focus()

        insert_btn = tk.Button(insert_direct_window, text="Insert",
                               command=lambda: self.perform_insert_direct(insert_direct_window, value_entry.get()),
                               font=("Times New Roman", 15, "bold"), bg="purple", fg="white", bd=5, relief="raised",
                               activeforeground="white", activebackground="grey")
        insert_btn.pack()

    def open_insert_index(self, window):
        window.destroy()

        insert_index_window = tk.Toplevel(self.window)
        insert_index_window.title("Insert with Index")
        insert_index_window.config(bg="#8FB9A8")
        insert_index_window.geometry("500x500+10+35")

        index_label = tk.Label(insert_index_window, text="Enter Index:", font=("Times New Roman", 20, "bold"),
                               bg="#8FB9A8")
        index_label.pack(pady=10)

        index_entry = tk.Entry(insert_index_window, width="10", font="Arial 20")
        index_entry.pack(pady=5)
        index_entry.focus()

        value_label = tk.Label(insert_index_window, text="Enter Value:", font=("Times New Roman", 20, "bold"),
                               bg="#8FB9A8")
        value_label.pack(pady=10)

        value_entry = tk.Entry(insert_index_window, width="10", font="Arial 20")
        value_entry.pack(pady=5)

        insert_btn = tk.Button(insert_index_window, text="Insert",
                               command=lambda: self.perform_insert_index(insert_index_window, index_entry.get(),
                                                                         value_entry.get()),
                               font=("Times New Roman", 15, "bold"), bg="purple", fg="white", bd=5, relief="raised",
                               activeforeground="white", activebackground="grey")
        insert_btn.pack()

    def perform_insert_direct(self, window, value):
        if not value:
            self.output_label.config(text="Please enter a value to insert.", font=("Times New Roman", 20, "bold"),
                                     bg="#8FB9A8")
            return

        self.linked_list.insert(value)
        self.create_list()

        window.destroy()

    def perform_insert_index(self, window, index, value):
        if not index or not value:
            self.output_label.config(text="Please enter both index and value.")
            return

        try:
            index = int(index)
        except ValueError:
            self.output_label.config(text="Invalid index. Please enter a valid integer.")
            return

        list_length = self.get_list_length()

        if index < 0 or index > list_length:
            self.output_label.config(text=f"Invalid index. Please enter an index between 0 and {list_length}.")
            return

        self.insert_at_index(index, value)
        self.create_list()

        window.destroy()

    def get_list_length(self):
        current = self.linked_list.head
        length = 0

        while current:
            length += 1
            current = current.next

        return length

    def insert_at_index(self, index, value):
        if index == 0:
            new_node = Node(value)
            new_node.next = self.linked_list.head
            self.linked_list.head = new_node
        else:
            current = self.linked_list.head
            position = 0
            while current and position < index - 1:
                current = current.next
                position += 1
            new_node = Node(value)
            new_node.next = current.next
            current.next = new_node

    def delete(self):
        delete_window = tk.Toplevel(self.window)
        delete_window.title("Delete Operation")
        delete_window.config(bg="#8FB9A8")
        delete_window.geometry("500x500+10+35")

        delete_label = tk.Label(delete_window, text="Choose Delete Mode:", font=("Times New Roman", 30, "bold"),
                                bg="#8FB9A8")
        delete_label.pack(pady=50)

        direct_btn = tk.Button(delete_window, text="Delete by Value",
                               command=lambda: self.open_delete_direct(delete_window),
                               font=("Times New Roman", 15, "bold"), bg="purple", fg="white", bd=5, relief="raised",
                               activeforeground="white", activebackground="grey")
        direct_btn.pack(pady=10)

        index_btn = tk.Button(delete_window, text="Delete by Index",
                              command=lambda: self.open_delete_index(delete_window),
                              font=("Times New Roman", 15, "bold"), bg="purple", fg="white", bd=5, relief="raised",
                              activeforeground="white", activebackground="grey")
        index_btn.pack()

    def open_delete_direct(self, window):
        # window.destroy()

        delete_direct_window = tk.Toplevel(self.window)
        delete_direct_window.title("Delete by Value")
        delete_direct_window.config(bg="#8FB9A8")
        delete_direct_window.geometry("500x500+10+35")

        value_label = tk.Label(delete_direct_window, text="Enter Value:", font=("Times New Roman", 20, "bold"),
                               bg="#8FB9A8")
        value_label.pack(pady=10)

        value_entry = tk.Entry(delete_direct_window, width="10", font="Arial 20")
        value_entry.pack(pady=5)
        value_entry.focus()

        delete_btn = tk.Button(delete_direct_window, text="Delete",
                               command=lambda: self.perform_delete_direct(delete_direct_window, value_entry.get()),
                               font=("Times New Roman", 15, "bold"), bg="purple", fg="white", bd=5, relief="raised",
                               activeforeground="white", activebackground="grey")
        delete_btn.pack()

    def open_delete_index(self, window):
        window.destroy()

        delete_index_window = tk.Toplevel(self.window)
        delete_index_window.title("Delete by Index")
        delete_index_window.config(bg="#8FB9A8")
        delete_index_window.geometry("500x500+10+35")

        index_label = tk.Label(delete_index_window, text="Enter Index:", font=("Times New Roman", 20, "bold"),
                               bg="#8FB9A8")
        index_label.pack(pady=10)

        index_entry = tk.Entry(delete_index_window, width="10", font="Arial 20")
        index_entry.pack(pady=5)
        index_entry.focus()

        delete_btn = tk.Button(delete_index_window, text="Delete",
                               command=lambda: self.perform_delete_index(delete_index_window, index_entry.get()),
                               font=("Times New Roman", 15, "bold"), bg="purple", fg="white", bd=5, relief="raised",
                               activeforeground="white", activebackground="grey")
        delete_btn.pack()

    def perform_delete_direct(self, window, value):
        if not value:
            self.output_label.config(text="Please enter a value to delete.")
            return

        self.linked_list.delete(value)
        self.create_list()

        window.destroy()

    def perform_delete_index(self, window, index):
        if not index:
            self.output_label.config(text="Please enter an index to delete.")
            return

        try:
            index = int(index)
        except ValueError:
            self.output_label.config(text="Invalid index. Please enter a valid integer.")
            return

        list_length = self.get_list_length()

        if index < 0 or index >= list_length:
            self.output_label.config(text=f"Invalid index. Please enter an index between 0 and {list_length - 1}.")
            return

        self.delete_at_index(index)
        self.create_list()

        window.destroy()

    def delete_at_index(self, index):
        if index == 0:
            self.linked_list.head = self.linked_list.head.next
        else:
            current = self.linked_list.head
            position = 0
            while current and position < index - 1:
                current = current.next
                position += 1
            current.next = current.next.next

    def update(self):
        update_window = tk.Toplevel(self.window)
        update_window.title("Update Operation")
        update_window.config(bg="#8FB9A8")
        update_window.geometry("500x500+10+35")

        # value_label = tk.Label(update_window, text="Enter Value to Update:")
        # value_label.pack()

        # value_entry = tk.Entry(update_window)
        # value_entry.pack()

        old_label = tk.Label(update_window, text="Enter Old Value:", font=("Times New Roman", 20, "bold"), bg="#8FB9A8")
        old_label.pack(pady=10)

        old_entry = tk.Entry(update_window, width="10", font="Arial 20")
        old_entry.pack(pady=5)
        old_entry.focus()

        new_label = tk.Label(update_window, text="Enter New Value:", font=("Times New Roman", 20, "bold"), bg="#8FB9A8")
        new_label.pack(pady=10)

        new_entry = tk.Entry(update_window, width="10", font="Arial 20")
        new_entry.pack(pady=5)

        update_btn = tk.Button(update_window, text="Update",
                               command=lambda: self.perform_update(update_window, old_entry.get(),
                                                                   new_entry.get()),
                               font=("Times New Roman", 15, "bold"), bg="purple", fg="white", bd=5, relief="raised",
                               activeforeground="white", activebackground="grey")
        update_btn.pack()

    def perform_update(self, window, old_value, new_value):
        if not old_value or not new_value:
            self.output_label.config(text="Please enter all the values.")
            return

        if old_value == new_value:
            self.output_label.config(text="Old value and new value are the same.")
            return

        self.linked_list.update(old_value, new_value)
        self.create_list()

        window.destroy()





root = tk.Tk()
root.geometry("1520x792+0+0")
root.config(bg="#8FB9A8")



def primary_color():
    primary_color= colorchooser.askcolor()[1]
    if primary_color:
        root.config(bg=primary_color)

def secondary_color():
    secondary_color= colorchooser.askcolor()[1]


def highlight_color():
    highlight_color= colorchooser.askcolor()[1]

mymenu= Menu(root)
root.config(menu=mymenu)
option_menu = Menu(mymenu, tearoff=0)
mymenu.add_cascade(label="Options", menu=option_menu)
option_menu.add_command(label="Change Primary Color", command=primary_color)
option_menu.add_command(label="Change Secondary Color", command=secondary_color)
option_menu.add_command(label="Change Highlight Color", command=highlight_color)
option_menu.add_separator()
option_menu.add_command(label="Exit", command=root.quit)



credit_frame = Frame(root, bg="#8FB9A8")
credit_frame.pack(side=TOP, fill=X)

credit_label = Label(credit_frame, text="© 2023 Majharul Islam. All rights reserved.", font=("Arial", 10), fg="black", bg="#8FB9A8")
credit_label.pack(side=RIGHT, padx=5, pady=5)

contact_label = Label(credit_frame, text="Contact: majharulislamraj008@gmail.com", font=("Arial", 10), fg="black", bg="#8FB9A8")
contact_label.pack(side=LEFT, padx=5, pady=5)

app = Raj(root)
root.mainloop()
