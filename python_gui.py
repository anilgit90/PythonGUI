#Library For GUI wxDesktop.
import wx
#Library For Connection to MSSQL instance.
import pymssql
#Initialize the wxFrame Inside Class Constructor.
class MyFrame(wx.Frame):
#Initialize the frame and panel for GUI    
    def __init__(self):
        super().__init__(parent=None, title='Sample SQL GUI Python')
        #All GUI elements are contained inside a panel, and parent is frame.
        panel = wx.Panel(self)        
        my_sizer = wx.BoxSizer(wx.VERTICAL)
        #Initialize the text Box control
        self.text_ctrl = wx.TextCtrl(panel)
        self.text_load = wx.TextCtrl(panel)
        #Added code for dynamic resizing.
        #Added 2 buttons and two text boxes
        my_sizer.Add(self.text_ctrl, 0, wx.ALL | wx.EXPAND, 5)
        my_btn = wx.Button(panel, label='Insert')
        my_btn.Bind(wx.EVT_BUTTON, self.on_press)
        my_sizer.Add(my_btn, 0, wx.ALL | wx.CENTER, 5)
        
        my_sizer.Add(self.text_load, 0, wx.ALL | wx.EXPAND, 5)
        my_btn2 = wx.Button(panel, label='Load')
        my_btn2.Bind(wx.EVT_BUTTON, self.on_press2)
        my_sizer.Add(my_btn2, 0, wx.ALL | wx.CENTER, 5)

        panel.SetSizer(my_sizer)        
        self.Show()
    #Button press event.
    def on_press(self, event):
        #Initialize Database Connection
        userName = 'sa'
        passWord = 'a'
        serverName = 'ANIL-RB-PC\\SQLEXPRESS'
        conn = pymssql.connect(serverName , userName , passWord, "testPython")
        cursor = conn.cursor()
        value = self.text_ctrl.GetValue()
        if not value:
            #Display on screen using alertbox
            wx.MessageBox("You didn't enter anything!")
            conn.close()
        else:
            wx.MessageBox(f'You typed: "{value}"')
            #Example Insert Statement.
            query = "INSERT INTO  TestTable(Value) VALUES(%s)"
            cursor.execute(query,(value))
            conn.commit()
            conn.close()
            
    def on_press2(self, event):
        #Initialize Database Connection
        userName = 'sa'
        passWord = 'a'
        serverName = 'ANIL-RB-PC\\SQLEXPRESS'
        conn = pymssql.connect(serverName , userName , passWord, "testPython")
        cursor = conn.cursor()
        #Example Select Statement
        cursor.execute("Select Value From TestTable")
        row = cursor.fetchone()
        value = row[0]
        conn.close()
        if not value:
            #Display on screen using alertbox
            wx.MessageBox("You didn't enter anything!")
        else:
            wx.MessageBox(f'Your fetched value is : "{value}"')
            #Write fetched value to TextBox
            self.text_load.write(value)
#Application logic starts here runs inifinitely.
if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame()
    app.MainLoop()
