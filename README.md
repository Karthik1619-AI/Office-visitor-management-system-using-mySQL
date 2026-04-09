# Office-visitor-management-system-using-mySQL
A desktop-based Office Visitor Management System built using Python (Tkinter) and MySQL Workbench to efficiently manage and track visitor records.

# 🏢 Office Visitor Management System  

## 📌 Description  
The Office Visitor Management System is a desktop-based application designed to efficiently manage visitor entries in an organization. It replaces traditional manual logbooks with a digital system using Python and MySQL Workbench for accurate and organized record-keeping.  

---

## 🚀 Features  
- 📝 Add visitor details (Name & Employee ID)  
- ⏱️ Automatic entry time recording  
- 📊 View visitor records in table format  
- 🔄 Refresh visitor list  
- ❌ Clear input fields  
- ✔️ Pop-up confirmation on successful entry  

---

## 🛠️ Technologies Used  
- Python (Tkinter GUI)  
- MySQL (Database)  
- MySQL Workbench  
- mysql-connector-python  

---

### 🖥️ Application UI  
![UI](ui.png)  

### 🗃️ Database (MySQL Workbench)  
![Database](database.png)  

---

## 🗄️ Database Structure  

### Table: visitors  
- **id** (Primary Key)  
- **visitor_name**  
- **emp_id**  
- **entry_time**  

---

## ▶️ How to Run  

1. Install dependency  
   ```bash
   pip install mysql-connector-python
2. Open MySQL Workbench
3. Create database
SQL
CREATE DATABASE visitor_db;
USE visitor_db;
4. Update database credentials in main.py
5. Run the application
Bash
python main.py
