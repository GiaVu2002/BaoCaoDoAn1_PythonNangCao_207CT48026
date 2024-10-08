import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Tạo cửa sổ
win = tk.Tk()
win.title("Quản lý thông tin người dùng")

#Thay icon
win.iconbitmap('download-icon-vscode+icons+type+vscode+opened-1324451628093987556_16.ico')

# Tạo các nhãn và ô nhập liệu
tk.Label(win, text="Tên:").grid(row=0, column=0, padx=10, pady=5)
name_entry = ttk.Entry(win, width=30)
name_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(win, text="Tuổi:").grid(row=1, column=0, padx=10, pady=5)
age_entry = ttk.Entry(win, width=30)
age_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(win, text="Giới tính:").grid(row=2, column=0, padx=10, pady=5)
gender_combobox = ttk.Combobox(win, width=27, values=["Nam", "Nữ", "Khác"])
gender_combobox.grid(row=2, column=1, padx=10, pady=5)
gender_combobox.set("Chọn giới tính")  # Đặt giá trị mặc định

tk.Label(win, text="Chiều cao (cm):").grid(row=3, column=0, padx=10, pady=5)
height_entry = ttk.Entry(win, width=30)
height_entry.grid(row=3, column=1, padx=10, pady=5)

tk.Label(win, text="Cân nặng (kg):").grid(row=4, column=0, padx=10, pady=5)
weight_entry = ttk.Entry(win, width=30)
weight_entry.grid(row=4, column=1, padx=10, pady=5)

# Tạo Treeview để hiển thị danh sách người dùng
tree = ttk.Treeview(win, columns=("Tên", "Tuổi", "Giới tính", "Chiều cao", "Cân nặng"), show="headings")
tree.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

# Đặt tiêu đề cho các cột
tree.heading("Tên", text="Tên")
tree.heading("Tuổi", text="Tuổi")
tree.heading("Giới tính", text="Giới tính")
tree.heading("Chiều cao", text="Chiều cao (cm)")
tree.heading("Cân nặng", text="Cân nặng (kg)")

# Hàm thêm người dùng
def add_person():
    name = name_entry.get()
    age = age_entry.get()
    gender = gender_combobox.get()
    height = height_entry.get()
    weight = weight_entry.get()

    if name and age and gender in ["Nam", "Nữ", "Khác"] and height and weight:
        tree.insert("", tk.END, values=(name, age, gender, height, weight))
        clear_entries()
    else:
        messagebox.showwarning("Cảnh báo", "Vui lòng nhập đầy đủ và hợp lệ thông tin")

# Hàm sửa thông tin người dùng
def edit_person():
    selected_item = tree.selection()
    if selected_item:
        name = name_entry.get()
        age = age_entry.get()
        gender = gender_combobox.get()
        height = height_entry.get()
        weight = weight_entry.get()

        if name and age and gender in ["Nam", "Nữ", "Khác"] and height and weight:
            tree.item(selected_item, values=(name, age, gender, height, weight))
            clear_entries()
        else:
            messagebox.showwarning("Cảnh báo", "Vui lòng nhập đầy đủ và hợp lệ thông tin")
    else:
        messagebox.showwarning("Cảnh báo", "Vui lòng chọn người để sửa")

# Hàm xóa người dùng khỏi danh sách
def delete_person():
    selected_item = tree.selection()
    if selected_item:
        tree.delete(selected_item)
    else:
        messagebox.showwarning("Cảnh báo", "Vui lòng chọn người để xóa")

# Hàm xóa nội dung trong các ô nhập liệu
def clear_entries():
    name_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)
    gender_combobox.set("Chọn giới tính")
    height_entry.delete(0, tk.END)
    weight_entry.delete(0, tk.END)

# Tạo các nút Thêm, Sửa, Xóa
add_button = ttk.Button(win, text="Thêm", command=add_person)
add_button.grid(row=6, column=0, padx=10, pady=10)

edit_button = ttk.Button(win, text="Sửa", command=edit_person)
edit_button.grid(row=6, column=1, padx=10, pady=10)

delete_button = ttk.Button(win, text="Xóa", command=delete_person)
delete_button.grid(row=7, column=0, padx=10, pady=10)

# Chạy ứng dụng
win.mainloop()
