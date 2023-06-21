# Array & Linked list project by using tkinter(GUi)


import tkinter as tk   # import tkinter library for (GUI)
from tkinter import *
from tkinter import messagebox
import subprocess   # Button based sound for MacOS



# Node class for Creating individual node
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

# Linked list class for linked list back end
class LinkedList:
    def __init__(self):
        self.head = None

    # Add element at the beginning in a linked list 
    def add_begin(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    
    # Add an element at the end of a linked list 
    def add_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.next is not None:
                n = n.next
            n.next = new_node

    # Add node after a particular node
    def add_after_x(self, data, x):
        n = self.head
        while n is not None:
            if x == n.data:
                break
            n = n.next

        if n is None:
            messagebox.showerror("Error", "Node is not found in the linked list!")
        else:
            new_node = Node(data)
            new_node.next = n.next
            n.next = new_node

    # Add node after a particular node
    def add_before_x(self, data, x):
        if self.head is None:
            messagebox.showerror("Error", "Linked list is empty, So we can't add before any nodes!")
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
            messagebox.showerror("Error", "Node is not present in the linked list!")
        else:
            new_node = Node(data)
            new_node.next = n.next
            n.next = new_node
            
    # Delete a particular node
    def delete_node(self, data):
        curr_node = self.head
        prev_node = None

        if curr_node is None:
            messagebox.showerror("Error", "Linked list is empty, So we can't delete node!")


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

    # Delete the first node of the linked list
    def delete_begin(self):
        if self.head is None:
            messagebox.showerror("Error", "Linked list is empty, So we can't delete nodes!")
        else:
            self.head = self.head.next

    
    # Delete the last node of the linked list
    def delete_end(self):
        if self.head is None:
            messagebox.showerror("Error", "Linked list is empty, So we can't delete nodes!")
        elif self.head.next is None:
            self.head = None

        else:
            n = self.head
            while n.next.next is not None:
                n = n.next
            n.next = None
   
    # For searching element
    def search_element(self, data):
        n = self.head
        loc = 0
        while n is not None:
            if n.data == data:
                return n
            n = n.next
            loc += 1
        return None
    
    # For update element
    def update_element(self, old_data, new_data):
        n = self.head
        while n is not None:
            if n.data == old_data:
                n.data = new_data
                return True
            n = n.next
        return False

    # Display linked list
    def display_list(self):
        n = self.head
        while n is not None:
            print(n.data)
            n = n.next


# Inherit the Linked list class
class Ssd(LinkedList):

    #For array Back_end and Front_end
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

    # Button based sound play method for the Home Window (Array, Linked list) button
    def play_sound(self):

        sound_file = "/System/Library/Sounds/Glass.aiff"
        subprocess.call(["afplay", sound_file])

    # Home page backend
    def home_interface(self):

        self.current_interface = 0
        self.ssd.title("Basic Data Structures")
        tk.Label(self.ssd, text="Choose a Data Structure", relief="solid", font="Arial, 40 bold", fg='black', padx=10, bg="azure4").pack(pady=50)

        tk.Button(self.ssd, text="Array", font="Sans-serif, 20 bold", fg="black", highlightbackground='deep sky blue', relief="raised", bd=5, activeforeground="white",
                  command=self.array_interface).pack(pady=5)

        tk.Button(self.ssd, text="Linked list", font="Sans-serif, 20 bold", fg="dodger blue", highlightbackground='chocolate', relief="raised", bd=3,
                  command=self.linkedlist).pack(pady=5)

        tk.Button(self.ssd, text="X", fg="red", relief="groove", bd=1, command=self.ssd.destroy).place(x=860, y=0)

    # GUI functionality
    def array_interface(self):

        self.ary = tk.Toplevel(bg="rosy brown")
        self.ary.title("Array")
        self.ary.geometry("900x600+300+80")

        tk.Label(self.ary, text="Enter the size of array:", font="Sans-serif, 20 bold", bg="rosy brown").pack(pady=10)

        self.array_size_entry = tk.Entry(self.ary, width="3", font="Arial 25", bg="white", fg="black")
        self.array_size_entry.pack(pady=5)

        tk.Button(self.ary, text="Next", fg="chocolate", highlightbackground='chocolate', command=self.create_array).place(x=455, y=115)
        tk.Button(self.ary, text="Back", fg="green", highlightbackground='green', command=self.ary.destroy).place(x=375, y=115)
        self.play_sound()

    # Array Size
    def create_array(self):

        self.array_size = int(self.array_size_entry.get())
        self.array_interface_2()

    # Array element
    def array_interface_2(self):

        self.current_interface = 2
        tk.Label(self.ary, text="Enter array elements:", font="Sans-serif, 20 bold", bg="rosy brown").place(x=320, y=230)

        self.array_entries = []
        for i in range(self.array_size):
            entry = tk.Entry(self.ary, width="3", font="Arial 25", bg="white", fg="black")
            entry.place(x=300 + (i * 50), y=280)
            self.array_entries.append(entry)

        tk.Button(self.ary, text="Next", fg="chocolate", highlightbackground='chocolate', command=self.show_array).place(x=440, y=350)
        tk.Button(self.ary, text="Back", fg="green", highlightbackground='green', command=self.ary.destroy).place(x=360, y=350)

    # Show Array Functionality for GUI
    def show_array(self):

        self.out = tk.Toplevel(bg="rosy brown")
        self.out.title("Arrays: Operations")
        self.out.geometry("900x600+300+80")

        self.array = []
        for entry in self.array_entries:
            self.array.append(int(entry.get()))
        tk.Label(self.out, text="Array: " + str(self.array), font="Sans-serif, 30 bold", bg="rosy brown").pack(pady=30)

        tk.Button(self.out, text="Insert", highlightbackground='DarkOliveGreen4', fg="green",
                  activeforeground="red", activebackground="grey", command=self.array_insert).pack(pady=10)

        tk.Button(self.out, text="Delete", highlightbackground='SlateBlue1', fg="blue",
                  activeforeground="red", activebackground="grey", command=self.array_delete).pack(pady=10)

        tk.Button(self.out, text="Search", fg="black", highlightbackground='salmon',
                  activeforeground="red", activebackground="grey", command=self.array_search).pack(pady=10)

        tk.Button(self.out, text="Update", fg="dodger blue", highlightbackground='dodger blue',
                  activeforeground="red", activebackground="grey", command=self.array_update).pack(pady=10)

        tk.Button(self.out, text="<", fg="green", relief="groove", bd=1, command=self.out.destroy).place(x=0, y=0)
        tk.Button(self.out, text="X", fg="red", relief="groove", bd=1, command=self.ssd.destroy).place(x=860, y=0)


    def array_insert(self):

        self.insrt = tk.Toplevel(bg="azure4")
        self.insrt.title("Insert Operation")
        self.insrt.geometry("900x600+300+80")

        tk.Label(self.insrt, text="Enter the element you want to insert:", font="Sans-serif, 20 bold", bg="azure4").pack(pady=10)
        self.array_insert_entry = tk.Entry(self.insrt, width="3", font="Arial 25", bg="white", fg="black")
        self.array_insert_entry.pack(pady=5)

        tk.Label(self.insrt, text="Enter the position where you want to insert the element:", font="Sans-serif, 20 bold", bg="azure4").pack(pady=10)
        self.insert_position_entry = tk.Entry(self.insrt, width="3", font="Arial 25", bg="white", fg="black")
        self.insert_position_entry.pack(pady=5)

        tk.Button(self.insrt, text="Next", fg="chocolate", highlightbackground='chocolate',
                  activeforeground="red", activebackground="grey", command=self.insert_interface).pack(pady=5)
        tk.Button(self.insrt, text="Back", fg="green", highlightbackground='green',
                  activeforeground="red", activebackground="grey", command=self.insrt.destroy).pack()

    def insert_interface(self):

        element = int(self.array_insert_entry.get())
        position = int(self.insert_position_entry.get())
        self.array.insert(position, element)

        tk.Label(self.insrt, text=f"\nAfter inserting {element} at position {position}:\n\nUpdated array: {str(self.array)}",
                 font="Sans-serif, 20 bold", bg="azure4").pack(pady=20)

        tk.Button(self.insrt, text="Go to Array Home", highlightbackground='deep sky blue', fg="black",
                  activeforeground="red", activebackground="grey", command=self.insrt.destroy).pack()

    def array_delete(self):

        self.dlt = tk.Toplevel(bg="azure4")
        self.dlt.title("Delete Operation")
        self.dlt.geometry("900x600+300+80")

        tk.Label(self.dlt, text="Choose the delete option:", font="Sans-serif, 20 bold", bg="azure4").pack(pady=10)

        tk.Button(self.dlt, text="Delete by Index", fg="black", highlightbackground='dodger blue',
                  activeforeground="red", activebackground="grey", command=self.delete_by_index).pack(pady=5)
        tk.Button(self.dlt, text="Delete by Value", fg="black", highlightbackground='blue',
                  activeforeground="red", activebackground="grey", command=self.delete_by_value).pack()

        tk.Button(self.dlt, text="<", fg="green", relief="groove", bd=1, command=self.dlt.destroy).place(x=0, y=0)
        tk.Button(self.dlt, text="X", fg="red", relief="groove", bd=2, command=self.ssd.destroy).place(x=860, y=0)

    def delete_by_index(self):

        self.dlt.destroy()
        self.dlt_idx = tk.Toplevel(bg="azure4")
        self.dlt_idx.title("Delete by Index")
        self.dlt_idx.geometry("900x600+300+80")

        tk.Label(self.dlt_idx, text="Enter the index number you want to delete:", font="Sans-serif, 20 bold", bg="azure4").pack(pady=10)

        self.array_delete_entry = tk.Entry(self.dlt_idx, width="3", font="Arial 25", bg="white", fg="black")
        self.array_delete_entry.pack(pady=5)

        tk.Button(self.dlt_idx, text="Next", fg="chocolate", highlightbackground='chocolate',
                  activeforeground="red", activebackground="grey", command=self.delete_by_index_interface).pack(pady=5)
        tk.Button(self.dlt_idx, text="Back", fg="green", highlightbackground='green',
                  activeforeground="red", activebackground="grey", command=self.dlt_idx.destroy).pack()

    def delete_by_index_interface(self):

        index = int(self.array_delete_entry.get())

        if index >= 0 and index < len(self.array):
            self.array.pop(index)

            tk.Label(self.dlt_idx, text="\nAfter deleting index No. " + str(index) + "\n\n Updated array: " + str(self.array),
                     font="Sans-serif, 20 bold", bg="azure4").pack(pady=20)

            tk.Button(self.dlt_idx, text="Go to Array Home", highlightbackground='deep sky blue', fg="black",
                      activeforeground="red", activebackground="grey", command=self.dlt_idx.destroy).pack()
        else:
            tk.Label(self.dlt_idx, text="Invalid index. Please enter a valid index.", font="Sans-serif, 20 bold",
                     bg="azure4").pack()

    def delete_by_value(self):

        self.dlt.destroy()
        self.dlt_val = tk.Toplevel(bg="azure4")
        self.dlt_val.title("Delete by Value")
        self.dlt_val.geometry("900x600+300+80")

        tk.Label(self.dlt_val, text="Enter the value you want to delete:", font="Sans-serif, 20 bold", bg="azure4").pack(pady=10)

        self.array_delete_entry = tk.Entry(self.dlt_val, width="3", font="Arial 25", bg="white", fg="black")
        self.array_delete_entry.pack(pady=5)

        tk.Button(self.dlt_val, text="Next", fg="chocolate", highlightbackground='chocolate',
                  activeforeground="red", activebackground="grey", command=self.delete_by_value_interface).pack(pady=5)

        tk.Button(self.dlt_val, text="Back", fg="green", highlightbackground='green',
                  activeforeground="red", activebackground="grey", command=self.dlt_val.destroy).pack()

    def delete_by_value_interface(self):

        value = int(self.array_delete_entry.get())

        if value in self.array:
            self.array = [x for x in self.array if x != value]
            tk.Label(self.dlt_val, text="\nAfter deleting value " + str(value) + "\n\n Updated array: " + str(self.array),
                     font="Sans-serif, 20 bold", bg="azure4").pack(pady=20)
            tk.Button(self.dlt_val, text="Go to Array Home", highlightbackground='deep sky blue', fg="black",
                      activeforeground="red", activebackground="grey", command=self.dlt_val.destroy).pack()
        else:
            tk.Label(self.dlt_val, text="Value not found in the array. Please enter a valid value.",
                     font="Sans-serif, 20 bold", bg="azure4").pack()


    def array_search(self):

        self.src = tk.Toplevel(bg="azure4")
        self.src.title("Search Operation")
        self.src.geometry("900x600+300+80")

        tk.Label(self.src, text="Enter the element you want to search: " + str(self.array), font="Sans-serif, 20 bold",
                 bg="azure4").pack(pady=10)
        self.array_search_element = tk.Entry(self.src, width="3", font="Arial 25", bg="white", fg="black")
        self.array_search_element.pack(pady=5)

        tk.Button(self.src, text="Next", fg="chocolate", highlightbackground='chocolate', command=self.search_interface).pack(pady=5)
        tk.Button(self.src, text="Back", fg="green",  highlightbackground='green', command=self.src.destroy).pack()

    def search_interface(self):

        global s_e
        global z
        global pos
        s_e= int(self.array_search_element.get())

        if s_e in self.array:
            pos= self.array.index(s_e)

            tk.Label(self.src, text=self.array_search_element.get() + " found in the Array at position " + str(pos),
                     font="Sans-serif, 20 bold", bg="azure4").pack(pady=5)

        else:
            tk.Label(self.src, text=self.array_search_element.get() + " not found in the Array:" + str(self.array),
                     font="Sans-serif, 20 bold", bg="azure4").pack(pady=5)

    def array_update(self):

        self.updt = tk.Toplevel(bg="azure4")
        self.updt.title("Update Operation")
        self.updt.geometry("900x600+300+80")

        tk.Label(self.updt, text="Enter the index no. and value respectively: " + str(self.array), font="Sans-serif, 20 bold", bg="azure4").pack(pady=10)

        self.current_value_index = tk.Entry(self.updt, width="3", font="Arial 25", bg="white", fg="black")
        self.current_value_index.pack(pady=2)
        self.updated_value = tk.Entry(self.updt, width="3", font="Arial 25", bg="white", fg="black")
        self.updated_value.pack()

        tk.Button(self.updt, text="Next",  fg="chocolate", highlightbackground='chocolate', command=self.update_interface).pack(pady=5)
        tk.Button(self.updt, text="Back", fg="green", highlightbackground='green', command=self.updt.destroy).pack()

    def update_interface(self):

        index = int(self.current_value_index.get())
        value = int(self.updated_value.get())

        if index >= 0 and index < len(self.array):
            self.array[index] = value
            tk.Label(self.updt, text="After updating the element\nUpdated array: " + str(self.array),
                     font="Sans-serif, 20 bold", bg="azure4").pack()
        else:
            tk.Label(self.updt, text="Invalid index. Please enter a valid index.",
                     font="Sans-serif, 20 bold", bg="azure4").pack()



    # Linked list GUI window started here
    def linkedlist(self):

        self.window = Toplevel(bg="gray20")
        self.window.title("Singly Linked List Operations")
        self.window.geometry("900x670+300+20")
        self.play_sound()


        def add_begin():

            data = entryBox.get()
            if data.isdigit():
                links.add_begin(int(data))
                resultList.delete(0, END)
                resultList.insert(END, "Data added: " + data)
            else:
                resultList.delete(0, END)
                messagebox.showerror("Error", "Invalid input !")


        def add_end():

            data = entryBox.get()
            if data.isdigit():
                links.add_end(int(data))
                resultList.delete(0, END)
                resultList.insert(END, "Data added: " + data)
            else:
                resultList.delete(0, END)
                messagebox.showerror("Error", "Invalid input !")


        def add_after_x():

            data = entryBox.get()
            x = entryX.get()
            if data.isdigit() and x.isdigit():
                if links.search_element(int(x)):
                    links.add_after_x(int(data), int(x))
                    resultList.delete(0, END)
                    resultList.insert(END, "Data added: " + data + " after " + x)
                else:
                    resultList.delete(0, END)
                    resultList.insert(END, "Data: " + str(x) + " is not found in the linked list, So can't add.")
            else:
                resultList.delete(0, END)
                messagebox.showerror("Error", "Invalid input !")


        def add_before_x():

            data = entryBox.get()
            x = entryX.get()
            if data.isdigit() and x.isdigit():
                if links.search_element(int(x)):
                    links.add_before_x(int(data), int(x))
                    resultList.delete(0, END)
                    resultList.insert(END, "Data added: " + data + " before " + x)
                else:
                    resultList.delete(0, END)
                    resultList.insert(END, "Data: " + str(x) + " is not found in the linked list, So can't add.")
            else:
                resultList.delete(0, END)
                messagebox.showerror("Error", "Invalid input !")


        def delete_node():

            data = entryBox.get()
            if data.isdigit():
                if links.delete_node(int(data)):
                    resultList.delete(0, END)
                    resultList.insert(END, "Node deleted: " + data)
                else:
                    resultList.delete(0, END)
                    resultList.insert(END, "Data: " + data + " not found in the Linked list.")
            else:
                resultList.delete(0, END)
                messagebox.showerror("Error", "Invalid input !")


        def delete_begin():
            links.delete_begin()
            display_list()

        def delete_end():
            links.delete_end()
            display_list()


        def search_element():

            data = entryBox.get()
            if data.isdigit():
                result = links.search_element(int(data))
                if result is not None:
                    resultList.delete(0, END)
                    resultList.insert(END, "Data " + data + " is found at location: " + str(result))
                else:
                    resultList.delete(0, END)
                    resultList.insert(END, "Data not found: " + data)
            else:
                resultList.delete(0, END)
                messagebox.showerror("Error", "Invalid input !")


        def update_element():

            new_data = entryBox.get()
            old_data = entryX.get()
            if old_data.isdigit() and new_data.isdigit():
                if links.update_element(int(old_data), int(new_data)):
                    resultList.delete(0, END)
                    resultList.insert(END, "Data updated: " + old_data + " to " + new_data)
                else:
                    resultList.delete(0, END)
                    resultList.insert(END, "Data not found: " + old_data)
            else:
                resultList.delete(0, END)
                messagebox.showerror("Error", "Invalid input !")


        def display_list():

            resultList.delete(0, END)
            curr_node = links.head
            if curr_node is None:
                resultList.insert(END, "NONE")
            else:
                resultList.insert(END, "List contents:")
                while curr_node is not None:
                    resultList.insert(END, curr_node.data)
                    curr_node = curr_node.next
                if curr_node is None:
                    resultList.insert(END, "NONE")


        def clear_placeholder(event, entry_widget, placeholder_text):

            current_text = entry_widget.get()
            if current_text == placeholder_text:
                entry_widget.delete(0, END)


        def set_placeholder(event, entry_widget, placeholder_text):

            current_text = entry_widget.get()
            if current_text == "":
                entry_widget.insert(END, placeholder_text)

        # Initialize the linked list
        links = LinkedList()

        # Create the GUI interface


        titleLabel = Label(self.window, text="Singly Linked List Operation", fg="black", padx=10, relief="solid", font="Arial, 36 bold", bg="azure4")
        titleLabel.pack(pady=30)

        entryBox = Entry(self.window, width=30)
        entryBox.pack()
        placeholder_text_data = "Entry for data"
        entryBox.insert(END, placeholder_text_data)  # Placeholder for data entry
        entryBox.bind("<FocusIn>", lambda event: clear_placeholder(event, entryBox, placeholder_text_data))
        entryBox.bind("<FocusOut>", lambda event: set_placeholder(event, entryBox, placeholder_text_data))

        entryX = Entry(self.window, width=30)
        entryX.pack()
        placeholder_text_position = "Entry for position"
        entryX.insert(END, placeholder_text_position)  # Placeholder for position entry
        entryX.bind("<FocusIn>", lambda event: clear_placeholder(event, entryX, placeholder_text_position))
        entryX.bind("<FocusOut>", lambda event: set_placeholder(event, entryX, placeholder_text_position))

        # Keyboard layout design for buttons
        buttonLayout = [
            ["7", "8", "9", "Delete"],
            ["4", "5", "6", "Search"],
            ["1", "2", "3", "Update"],
            ["0", "Delete Begin", "Delete End", "Display"],
            ["Add After X", "Add Before X", "Add Begin", "Add End"]
        ]

        # Function for handling the button clicks
        def button_click(data):

            if data.isdigit():
                if entryBox.focus_get() == entryBox:
                    entryBox.insert(END, data)
                elif entryX.focus_get() == entryX:
                    entryX.insert(END, data)
            elif data == "Add Begin":
                add_begin()
                clear_entries()
            elif data == "Add End":
                add_end()
                clear_entries()
            elif data == "Add After X":
                add_after_x()
                clear_entries()
            elif data == "Add Before X":
                add_before_x()
                clear_entries()
            elif data == "Delete Begin":
                delete_begin()
                clear_entries()
            elif data == "Delete End":
                delete_end()
                clear_entries()
            elif data == "Search":
                search_element()
                clear_entries()
            elif data == "Update":
                update_element()
                clear_entries()
            elif data == "Delete":
                delete_node()
                clear_entries()
            elif data == "Display":
                display_list()
                clear_entries()

        
        # When entry box Clicked then clear the entry placeholder
        def clear_entries():
            entryBox.delete(0, END)
            entryX.delete(0, END)
            entryBox.focus_set()

        # for creating the buttons layout, looks like a keyboard
        for row in buttonLayout:
            buttonFrame = Frame(self.window)
            buttonFrame.pack()
            for buttonData in row:
                button = Button(buttonFrame, text=buttonData, width=15, highlightbackground="midnight blue",activeforeground="red", activebackground="gray20")
                button.pack(side=LEFT)
                button.configure(command=lambda btn=buttonData: button_click(btn))

        resultList = Listbox(self.window, width=62, height=18, font=("arial 18 bold"), bg="midnight blue")
        resultList.pack(pady=5)


        tk.Button(self.window, text="<", fg="green", relief="groove", bd=1, command=self.window.destroy).place(x=0, y=0)

        tk.Button(self.window, text="X", fg="red", relief="groove", bd=1,command=self.ssd.destroy).place(x=860, y=0)


root = tk.Tk()
root.geometry("900x600+300+80")
root.config(bg="PaleVioletRed4")
app = Ssd(root)
root.mainloop()


