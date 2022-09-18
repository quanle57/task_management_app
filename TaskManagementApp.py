import psycopg2
import tkinter as tk
from tkinter import END, ttk


class Database:
    def __init__(self):
        self.hostname = 'localhost'
        self.database = 'JOBSYSTEM'
        self.username = 'postgres'
        self.pwd      = '2511'
        self.port_id  = 5432
        
    def connect(self):
        ''' Connect to Database
            return: connection, cursor'''
        
        try:
            # Create connection to database
            conn = psycopg2.connect(
                        host = self.hostname,
                        dbname = self.database,
                        user = self.username,
                        password = self.pwd,
                        port = self.port_id)

            # Create the cursor
            cur = conn.cursor()
        except Exception as e:
            print(e)
            conn = None
            cur = None
        
        return conn, cur

    def get_all_data(self, conn, cur):
        
        if conn != None and cur != None:
            return self.fetch_data(cur, 'job')
        else:
            return []
    
    def fetch_data(self, cursor, database_name):
        ''' Select all records from database'''

        try: 
            cursor.execute('SELECT * FROM {}'.format(database_name)) 
        
        except: 
            print('error !') 
        
        # Store the results in data
        data = cursor.fetchall()

        return data

  
class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('1600x800')
        self.resizable(1,1)
        self.iconbitmap('D:\Pyfile\icon.ico')
        self.title('JOB SYSTEM')

        # Variables
        self.search_job_id = tk.StringVar()
        self.job_id = tk.StringVar()
        self.name = tk.StringVar()
        self.kind = tk.StringVar()
        self.status = tk.StringVar()
        self.worker_id = tk.StringVar()
        self.excution_time = tk.StringVar()
        self.start_time = tk.StringVar()
        self.end_time = tk.StringVar()
        self.job_output = tk.StringVar()

        # Create Insert data
        self.insert_data = [self.search_job_id, self.job_id, self.name, self.kind, self.status, self.worker_id, 
                self.excution_time, self.start_time, self.end_time, self.job_output]
        self.insert_data = self.create_insert_data(self)
        
        # Create TreeView
        self.tree = self.create_tree_widget()
        
        # Create button
        tk.Button(self, text="Add", font='arial 10 bold',command = self.add, height=2, width= 15).place(x=250, y=50)
        tk.Button(self, text="Update", font='arial 10 bold', command = self.update, height=2, width= 15).place(x=500, y=50)
        tk.Button(self, text="Delete", font='arial 10 bold',command = self.delete, height=2, width= 15).place(x=750, y=50)
        tk.Button(self, text="Reload", font='arial 10 bold',command = self.reload, height=2, width= 15).place(x=1000, y=50)
        tk.Button(self, text="Search", font='arial 10 bold',command = self.search, height=2, width= 10).place(x=1470, y=50)
        
        # Close the App
        tk.Button(self, font = 'arial 13 bold', text = 'EXIT'  ,padx =5,bg ='grey' ,command = self.exit).place(x=1500,y=750)     

    def create_insert_data(self, root):

        # search_job_id   = data[0]
        # job_id          = data[1]
        # name            = data[2]
        # kind            = data[3]
        # status          = data[4]
        # worker_id       = data[5]
        # excution_time   = data[6]
        # start_time      = data[7]
        # end_time        = data[8]
        # job_output      = data[9]
        search_job_id   = tk.StringVar()
        job_id          = tk.StringVar()
        name            = tk.StringVar()
        kind            = tk.StringVar()
        status          = tk.StringVar()
        worker_id       = tk.StringVar()
        excution_time   = tk.StringVar()
        start_time      = tk.StringVar()
        end_time        = tk.StringVar()
        job_output      = tk.StringVar()
        
        # Label for Search Job as job_id
        tk.Label(root, text = 'SEARCH as job_id' , font='arial 15 bold').place(x = 1250, y=50)
        self.e0 = tk.Entry(root, font = 'arial 10 bold', bg ='white',width = 30)
        self.e0.place(x=1250, y = 75)
        
        tk.Label(root, text = 'INSERT id' , font='arial 15 bold').place(x = 20, y=50)
        self.e1 = tk.Entry(root, font = 'arial 10 bold', bg ='white',width = 30,)
        self.e1.place(x=20, y = 80)

        # Label for INSERT job_id
        tk.Label(root, text = 'INSERT job_id' , font='arial 15 bold').place(x = 20, y=120)
        self.e2 = tk.Entry(root, font = 'arial 10 bold', bg ='white',width = 30,)
        self.e2.place(x=20, y = 150)

        # Label for INSERT name
        tk.Label(root, text = 'INSERT name' , font='arial 15 bold').place(x = 20, y=190)
        self.e3 = tk.Entry(root, font = 'arial 10 bold', bg ='white',width = 30,)
        self.e3.place(x=20, y = 220)

        # Label for INSERT kind
        tk.Label(root, text = 'INSERT kind' , font='arial 15 bold').place(x = 20, y=260)
        self.e4 = tk.Entry(root, font = 'arial 10 bold', bg ='white',width = 30,)
        self.e4.place(x=20, y = 290)

        # Label for INSERT status
        tk.Label(root, text = 'INSERT status' , font='arial 15 bold').place(x = 20, y=330)
        self.e5 = tk.Entry(root, font = 'arial 10 bold', bg ='white',width = 30,)
        self.e5.place(x=20, y = 360)

        # Label for INSERT worker_id
        tk.Label(root, text = 'INSERT worker_id' , font='arial 15 bold').place(x = 20, y=400)
        self.e6 = tk.Entry(root, font = 'arial 10 bold', bg ='white',width = 30,)
        self.e6.place(x=20, y = 430)

        # Label for INSERT excution_time
        tk.Label(root, text = 'INSERT excution_time' , font='arial 15 bold').place(x = 20, y=470)
        self.e7 = tk.Entry(root, font = 'arial 10 bold', bg ='white',width = 30,)
        self.e7.place(x=20, y = 500)

        # Label for INSERT start_time
        tk.Label(root, text = 'INSERT start_time' , font='arial 15 bold').place(x = 20, y=540)
        self.e8 = tk.Entry(root, font = 'arial 10 bold', bg ='white',width = 30,)
        self.e8.place(x=20, y = 570)

        # Label for INSERT end_time
        tk.Label(root, text = 'INSERT end_time' , font='arial 15 bold').place(x = 20, y=610)
        self.e9 = tk.Entry(root, font = 'arial 10 bold', bg ='white',width = 30,)
        self.e9.place(x=20, y = 640)

        # Label for INSERT job_output
        tk.Label(root, text = 'INSERT job_output' , font='arial 15 bold').place(x = 20, y=680)
        self.e10 = tk.Entry(root, font = 'arial 10 bold', bg ='white',width = 30,)
        self.e10.place(x=20, y = 710)

    def exit(self):
        '''
        Close the Application
        '''
        self.destroy()
        
    def create_tree_widget(self):
        
        # Define columns
        columns = ('id', 'job_id', 'name', 'kind', 'status', 'worker_id', 'excution_time', 'start_time', 'end_time', 'job_output')

        tree = ttk.Treeview(self, columns=columns, show='headings')

        # Define Headings
        tree.heading('id', text='ID')
        tree.heading('job_id', text='Job_ID')
        tree.heading('name', text='Name')
        tree.heading('kind', text='Kind')
        tree.heading('status', text='Status')
        tree.heading('worker_id', text='Worker_ID')
        tree.heading('excution_time', text='Excution_time')
        tree.heading('start_time', text='Start_Time')
        tree.heading('end_time', text='End_Time')
        tree.heading('job_output', text='Job_Output')

        # Modify column of TreeView
        tree.column('id', width=100, anchor=tk.CENTER)
        tree.column('job_id', width=100, anchor=tk.CENTER)
        tree.column('name', width=150, anchor=tk.CENTER)
        tree.column('kind', width=150, anchor=tk.CENTER)
        tree.column('status', width=100, anchor=tk.CENTER)
        tree.column('worker_id', width=100, anchor=tk.CENTER)
        tree.column('excution_time', width=100, anchor=tk.CENTER)
        tree.column('start_time', width=200, anchor=tk.CENTER)
        tree.column('end_time', width=200, anchor=tk.CENTER)
        tree.column('job_output', width=125, anchor=tk.CENTER)
        
        tree.bind('<<TreeviewSelect>>', self.item_selected)
        
        return tree

    def show_data(self, records):
        
        for selected_item in self.tree.get_children():
            self.tree.delete(selected_item)
        
        # Add data to the treeview
        for job in records:
            self.tree.insert('', tk.END, values=job)
        
        self.tree.grid(row=0, column=0, sticky='nsew', padx=250, pady=120)
        
    def item_selected(self, event):
        
        self.e1.delete(0, END)
        self.e2.delete(0, END)
        self.e3.delete(0, END)
        self.e4.delete(0, END)
        self.e5.delete(0, END)
        self.e6.delete(0, END)
        self.e7.delete(0, END)
        self.e8.delete(0, END)
        self.e9.delete(0, END)
        self.e10.delete(0, END)
        if len(self.tree.selection()) > 0:
            row_id = self.tree.selection()[0]
            select = self.tree.set(row_id)
            self.e1.insert(0, select['id'])
            self.e2.insert(0, select['job_id'])
            self.e3.insert(0, select['name'])
            self.e4.insert(0, select['kind'])
            self.e5.insert(0, select['status'])
            self.e6.insert(0, select['worker_id'])
            self.e7.insert(0, select['excution_time'])
            self.e8.insert(0, select['start_time'])
            self.e9.insert(0, select['end_time'])
            self.e10.insert(0, select['job_output'])
    
    def add(self):
        
        # Connect to database
        try:
            # Create connection to database
            conn = psycopg2.connect(
                        host = 'localhost',
                        dbname = 'JOBSYSTEM',
                        user = 'postgres',
                        password = '2511',
                        port = 5432)

            # Create the cursor
            cur = conn.cursor()
        except Exception as e:
            print(e)
            conn = None
            cur = None
        
        # INSEERT INTO Database
        if conn != None and cur != None:
            
            insert_script = 'INSERT INTO JOB (id, job_id, name, kind, status, worker_id, execution_time, start_time, end_time, job_output) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
            
            new_record = (self.e1.get(), self.e2.get(), self.e3.get(), self.e4.get(), self.e5.get(), 
                          self.e6.get(), self.e7.get(), self.e8.get(), self.e9.get(), self.e10.get())
            cur.execute(insert_script, new_record)

            conn.commit()

            cur.close()
            conn.close()
        
    
    def update(self):
        # Connect to database
        try:
            # Create connection to database
            conn = psycopg2.connect(
                        host = 'localhost',
                        dbname = 'JOBSYSTEM',
                        user = 'postgres',
                        password = '2511',
                        port = 5432)

            # Create the cursor
            cur = conn.cursor()
        except Exception as e:
            print(e)
            conn = None
            cur = None
        
        # Alter Database
        if conn != None and cur != None:
            # UPDATE Tên_bảng SET Tên_cột .WRITE('Chuỗi_thay_thế', Vị_trí, Số_lượng) WHERE Điều_kiện;

            script = "UPDATE job SET id= %s, job_id= %s, name= %s,kind= %s,status= %s,worker_id= %s, execution_time= %s, \
                    start_time= %s, end_time= %s, job_output= %s where job_id= %s;"
            
            val = (self.e1.get(), self.e2.get(), self.e3.get(), self.e4.get(), self.e5.get(), 
                          self.e6.get(), self.e7.get(), self.e8.get(), self.e9.get(), self.e10.get(), self.e2.get())
            cur.execute(script, val)

            conn.commit()

            cur.close()
            conn.close()
            
            self.e1.delete(0, END)
            self.e2.delete(0, END)
            self.e3.delete(0, END)
            self.e4.delete(0, END)
            self.e5.delete(0, END)
            self.e6.delete(0, END)
            self.e7.delete(0, END)
            self.e8.delete(0, END)
            self.e9.delete(0, END)
            self.e10.delete(0, END)
    
    def delete(self):
        # Connect to database
        try:
            # Create connection to database
            conn = psycopg2.connect(
                        host = 'localhost',
                        dbname = 'JOBSYSTEM',
                        user = 'postgres',
                        password = '2511',
                        port = 5432)

            # Create the cursor
            cur = conn.cursor()
        except Exception as e:
            print(e)
            conn = None
            cur = None
        
        # Alter Database
        if conn != None and cur != None:
            # DELETE FROM Tên_bảng WHERE Điều_kiện;

            script = 'DELETE FROM Job WHERE job_id = %s;'
            
            val = (self.e2.get(),)
            
            cur.execute(script, val)

            conn.commit()

            cur.close()
            conn.close()
            
            self.e1.delete(0, END)
            self.e2.delete(0, END)
            self.e3.delete(0, END)
            self.e4.delete(0, END)
            self.e5.delete(0, END)
            self.e6.delete(0, END)
            self.e7.delete(0, END)
            self.e8.delete(0, END)
            self.e9.delete(0, END)
            self.e10.delete(0, END)
    
    def reload(self):
        database = Database()
        conn, cur = database.connect()
        records = database.get_all_data(conn, cur)
        
        conn.commit()

        cur.close()
        conn.close()
        
        self.show_data(records)
    
    def search(self):
        print('search')
        # Search in Treeview
        for child in self.tree.get_children():
            if len(self.tree.item(child)['values']) >= 10:
                if self.tree.item(child)['values'][1] == self.e0.get():
                    self.e1.delete(0, END)
                    self.e2.delete(0, END)
                    self.e3.delete(0, END)
                    self.e4.delete(0, END)
                    self.e5.delete(0, END)
                    self.e6.delete(0, END)
                    self.e7.delete(0, END)
                    self.e8.delete(0, END)
                    self.e9.delete(0, END)
                    self.e10.delete(0, END)
                    
                    self.e1.insert(0, self.tree.item(child)['values'][0])
                    self.e2.insert(0, self.tree.item(child)['values'][1])
                    self.e3.insert(0, self.tree.item(child)['values'][2])
                    self.e4.insert(0, self.tree.item(child)['values'][3])
                    self.e5.insert(0, self.tree.item(child)['values'][4])
                    self.e6.insert(0, self.tree.item(child)['values'][5])
                    self.e7.insert(0, self.tree.item(child)['values'][6])
                    self.e8.insert(0, self.tree.item(child)['values'][7])
                    self.e9.insert(0, self.tree.item(child)['values'][8])
                    self.e10.insert(0, self.tree.item(child)['values'][9])
               
if __name__ == '__main__':

    records = []
    # if conn != None and cur != None:
    #     # cur.execute('DROP TABLE IF EXISTS JOB')

    #     create_script = ''' CREATE TABLE IF NOT EXISTS JOB(
    #                             id      int,
    #                             job_id  varchar(20) PRIMARY KEY,
    #                             name    varchar(40) NOT NULL,
    #                             kind    varchar(40) NOT NULL,
    #                             status  varchar(40) NOT NULL,
    #                             worker_id  varchar(40) NOT NULL,
    #                             execution_time  int,
    #                             start_time  timestamp,
    #                             end_time  timestamp,
    #                             job_output  varchar(40))'''

    #     cur.execute(create_script)
        
    #     insert_script = 'INSERT INTO JOB (id, job_id, name, kind, status, worker_id, execution_time, start_time, end_time, job_output) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
        
        # insert_values = [(1, 'Quan', 1000), (2, 'Duy', 1000), (3, 'Le', 2511)]
        # for record in insert_values:
        #     cur.execute(insert_script, record)
        # cur.execute(insert_script, (1, 'j57', 'DE', 'IT', 'In Process', '19', 12, '2022-04-05 19:10:25-07', '2022-04-05 19:10:25-07', 'ahihi'))
        # cur.execute(insert_script, (2, 'j579', 'DE2', 'IT', 'dONE', '19', 12, '2022-04-05 19:10:25-07', '2022-04-05 19:10:25-07', 'ahihi'))
        
        # cur.execute("UPDATE JOB SET name = 'lelele', kind = 'Dev' WHERE job_id = 'j57'")
        
        # records = fetch_data(cur, 'job')

        # conn.commit()

        # cur.close()
        # conn.close()
        
    database = Database()
    conn, cur = database.connect()
    records = database.get_all_data(conn, cur)
    
    conn.commit()

    cur.close()
    conn.close()
        
    app =  App()
    app.show_data(records)
    app.mainloop()

    # Search in Treeview
    # for child in tree.get_children():
    #     if tree.item(child)['values'][0] == 2:
    #         print(tree.item(child)['values'][1])

    # Modify in TreeView
    # Modify full a item (a record)
    # for child in tree.get_children():
    #     if tree.item(child)['values'][0] == 2:
    #         tree.item(child, values=('IT', 'TI'))

    # Show data when treeview is selected
    # def item_selected(event):
    #     for selected_item in tree.selection():
    #         item = tree.item(selected_item)
    #         record = item['values']
    #         print(record)

    
    
    