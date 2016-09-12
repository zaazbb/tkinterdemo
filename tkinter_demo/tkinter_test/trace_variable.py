#! /usr/bin/env python
# -*- python -*-
# Generated by PAGE version 4.0
# In conjuction with Tcl version 8.6
#    May. 17, 2013 01:30:13 PM
import sys

py2 = py30 = py31 = False
version = sys.hexversion
if version >= 0x020600F0 and version < 0x03000000 :
    py2 = True    # Python 2.6 or 2.7
    from Tkinter import *
    import ttk
elif version >= 0x03000000 and version < 0x03010000 :
    py30 = True
    from tkinter import *
    import ttk
elif version >= 0x03010000:
    py31 = True
    from tkinter import *
    import tkinter.ttk as ttk
else:
    print ("""
    You do not have a version of python supporting ttk widgets..
    You need a version >= 2.6 to execute PAGE modules.
    """)
    sys.exit()



def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    root.title('New_Toplevel_1')
    root.geometry('600x450+650+150')
    set_Tk_var()
    w = New_Toplevel_1 (root)
    init()
    root.mainloop()

w = None
def create_New_Toplevel_1 (root):
    '''Starting point when module is imported by another program.'''
    global w, w_win
    if w: # So we have only one instance of window.
        return
    w = Toplevel (root)
    w.title('New_Toplevel_1')
    w.geometry('600x450+650+150')
    set_Tk_var()
    w_win = New_Toplevel_1 (w)
    init()
    return w_win

def destroy_New_Toplevel_1 ():
    global w
    w.destroy()
    w = None


def set_Tk_var():
    # These are Tk variables used passed to Tkinter and must be
    # defined before the widgets using them are created.
    global myentry
    myentry = StringVar()
    
    global myvar
    myvar = StringVar()

def init():
    pass


def ButtonClicked():
        print ('ButtonClicked')
        sys.stdout.flush()
        myvar.set('222')

def button1clicked():
        print ('button1clicked')
        sys.stdout.flush()
        myentry.set(myentry.get() + '\naaa')


class New_Toplevel_1:
    def __init__(self, master=None):
        _bgcolor = 'SystemButtonFace'  # X11 color: #d4d0c8
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = 'SystemButtonFace' # X11 color: #d4d0c8
        _ana1color = 'SystemButtonFace' # X11 color: #d4d0c8 
        _ana2color = 'SystemButtonFace' # X11 color: #d4d0c8 
        TkDefaultFont = "-family Tahoma -size 8 -weight normal -slant roman -underline 0 -overstrike 0"
        TkTextFont = "-family Tahoma -size 8 -weight normal -slant roman -underline 0 -overstrike 0"
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font=TkDefaultFont)
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])
        master.configure(highlightcolor="black")


        self.TButton1 = ttk.Button (master)
        self.TButton1.place(relx=0.25,rely=0.11,height=24,width=77)
        self.TButton1.configure(command=ButtonClicked)
        self.TButton1.configure(takefocus="")
        self.TButton1.configure(text='''Tbutton''')

        self.Scrolledtext1 = ScrolledText (master)
        self.Scrolledtext1.place(relx=0.07,rely=0.27,relheight=0.5
                ,relwidth=0.34)
        self.Scrolledtext1.configure(background="white")
        self.Scrolledtext1.configure(font=TkTextFont)
        self.Scrolledtext1.configure(foreground="black")
        self.Scrolledtext1.configure(highlightcolor="black")
        self.Scrolledtext1.configure(insertbackground="black")
        self.Scrolledtext1.configure(insertborderwidth="3")
        self.Scrolledtext1.configure(selectbackground="#bfbbb4")
        self.Scrolledtext1.configure(selectforeground="black")
        self.Scrolledtext1.configure(width=10)

        self.TButton2 = ttk.Button (master)
        self.TButton2.place(relx=0.55,rely=0.11,height=24,width=77)
        self.TButton2.configure(command=button1clicked)
        self.TButton2.configure(takefocus="")
        self.TButton2.configure(text='''Tbutton''')

        self.TEntry1 = ttk.Entry (master)
        self.TEntry1.place(relx=0.47,rely=0.29,relheight=0.25,relwidth=0.21)
        self.TEntry1.configure(textvariable=myentry)
        self.TEntry1.configure(width=128)
        self.TEntry1.configure(takefocus="")
        self.TEntry1.configure(cursor="ibeam")

        self.Text1 = Text (master)
        self.Text1.place(relx=0.47,rely=0.6,relheight=0.14,relwidth=0.21)
        self.Text1.configure(background="white")
        self.Text1.configure(font=TkTextFont)
        self.Text1.configure(foreground="black")
        self.Text1.configure(highlightcolor="black")
        self.Text1.configure(insertbackground="black")
        self.Text1.configure(selectbackground="#bfbbb4")
        self.Text1.configure(selectforeground="black")
        self.Text1.configure(width=124)
        self.Text1.configure(wrap="word")

        self.Label1 = Label (master)
        self.Label1.place(relx=0.72,rely=0.29,height=59,width=141)
        self.Label1.configure(anchor="nw")
        self.Label1.configure(disabledforeground="#9f9c96")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='''Label''')
        self.Label1.configure(width=141)

        self.Message2 = Message (master)
        self.Message2.place(relx=0.73,rely=0.51,relheight=0.22,relwidth=0.17)
        self.Message2.configure(foreground="#000000")
        self.Message2.configure(highlightcolor="black")
        self.Message2.configure(text='''Message''')
        self.Message2.configure(width=104)
        

        myvar.trace_variable('w', lambda a,b,c:self.Scrolledtext1.insert(1.0, myvar.get()+'\n'))
##        myvar.trace('w', lambda a,b,c:self.Scrolledtext1.insert(1.0, myvar.get()+'\n'))


# The following code is added to facilitate the Scrolled widgets you specified.
class AutoScroll(object):
    '''Configure the scrollbars for a widget.'''

    def __init__(self, master):
        vsb = ttk.Scrollbar(master, orient='vertical', command=self.yview)
        hsb = ttk.Scrollbar(master, orient='horizontal', command=self.xview)

        self.configure(yscrollcommand=self._autoscroll(vsb),
            xscrollcommand=self._autoscroll(hsb))
        self.grid(column=0, row=0, sticky='nsew')
        vsb.grid(column=1, row=0, sticky='ns')
        hsb.grid(column=0, row=1, sticky='ew')

        master.grid_columnconfigure(0, weight=1)
        master.grid_rowconfigure(0, weight=1)

        # Copy geometry methods of master  (took from ScrolledText.py)
        if py31:
            methods = Pack.__dict__.keys() | Grid.__dict__.keys() \
                  | Place.__dict__.keys()
        else:
            methods = Pack.__dict__.keys() + Grid.__dict__.keys() \
                  + Place.__dict__.keys()

        for meth in methods:
            if meth[0] != '_' and meth not in ('config', 'configure'):
                setattr(self, meth, getattr(master, meth))

    @staticmethod
    def _autoscroll(sbar):
        '''Hide and show scrollbar as needed.'''
        def wrapped(first, last):
            first, last = float(first), float(last)
            if first <= 0 and last >= 1:
                sbar.grid_remove()
            else:
                sbar.grid()
            sbar.set(first, last)
        return wrapped

    def __str__(self):
        return str(self.master)

def _create_container(func):
    '''Creates a ttk Frame with a given master, and use this new frame to
    place the scrollbars and the widget.'''
    def wrapped(cls, master, **kw):
        container = ttk.Frame(master)
        return func(cls, container, **kw)
    return wrapped

class ScrolledText(AutoScroll, Text):
    '''A standard Tkinter Text widget with scrollbars that will
    automatically show/hide as needed.'''
    @_create_container
    def __init__(self, master, **kw):
        Text.__init__(self, master, **kw)
        AutoScroll.__init__(self, master)

if __name__ == '__main__':
    vp_start_gui()


