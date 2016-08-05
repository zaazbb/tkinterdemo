# entry2.tcl --
#
# This demonstration script is the same as the entry1.tcl script
# except that it creates scrollbars for the entries.

##if {![info exists widgetDemo]} {
##    error "This script should be run from the \"widget\" demo."
##}
assert 'widgetDemo' in globals(), \
'This script should be run from the "widget" demo.'

##package require Tk
from tkinter import *

##set w .entry2
##catch {destroy $w}
##toplevel $w
##wm title $w "Entry Demonstration (with scrollbars)"
##wm iconname $w "entry2"
##positionWindow $w
demo_name = 'entry2'
if demo_name in globals()['demo_name']:
    globals()['demo_name'][demo_name].destroy()
w = globals()['demo_name'][demo_name] = Toplevel(root)
w.wm_title('Entry Demonstration (with scrollbars)')
w.wm_iconname('entry2')
positionWindow(w)

##label $w.msg -font $font -wraplength 5i -justify left -text "Three different entries are displayed below, with a scrollbar for each entry.  You can add characters by pointing, clicking and typing.  The normal Motif editing characters are supported, along with many Emacs bindings.  For example, Backspace and Control-h delete the character to the left of the insertion cursor and Delete and Control-d delete the chararacter to the right of the insertion cursor.  For entries that are too large to fit in the window all at once, you can scan through the entries with the scrollbars, or by dragging with mouse button2 pressed."
##pack $w.msg -side top
msg = Label(w, font=font_, wraplength='5i', justify='left', text="Three different entries are displayed below, with a scrollbar for each entry.  You can add characters by pointing, clicking and typing.  The normal Motif editing characters are supported, along with many Emacs bindings.  For example, Backspace and Control-h delete the character to the left of the insertion cursor and Delete and Control-d delete the chararacter to the right of the insertion cursor.  For entries that are too large to fit in the window all at once, you can scan through the entries with the scrollbars, or by dragging with mouse button2 pressed.")
msg.pack(side='top')

## See Code / Dismiss buttons
##set btns [addSeeDismiss $w.buttons $w]
##pack $btns -side bottom -fill x
btns = addSeeDismiss(w, demo_name)
btns.pack(side='bottom', fill='x')

##frame $w.frame -borderwidth 10
##pack $w.frame -side top -fill x -expand 1
frame = Frame(w, borderwidth=10)
frame.pack(side='top', fill='x', expand=1)

##entry $w.frame.e1 -xscrollcommand "$w.frame.s1 set"
##scrollbar $w.frame.s1 -relief sunken -orient horiz -command \
##	"$w.frame.e1 xview"
##frame $w.frame.spacer1 -width 20 -height 10
##entry $w.frame.e2 -xscrollcommand "$w.frame.s2 set"
##scrollbar $w.frame.s2 -relief sunken -orient horiz -command \
##	"$w.frame.e2 xview"
##frame $w.frame.spacer2 -width 20 -height 10
##entry $w.frame.e3 -xscrollcommand "$w.frame.s3 set"
##scrollbar $w.frame.s3 -relief sunken -orient horiz -command \
##	"$w.frame.e3 xview"
##pack $w.frame.e1 $w.frame.s1 $w.frame.spacer1 $w.frame.e2 $w.frame.s2 \
##	$w.frame.spacer2 $w.frame.e3 $w.frame.s3 -side top -fill x
e1 = Entry(frame)
s1 = Scrollbar(frame, relief='sunken', orient='horiz', command=e1.xview)
e1['xscrollcommand'] = s1.set
spacer1 = Frame(frame, width=20, height=10)
e2 = Entry(frame)
s2 = Scrollbar(frame, relief='sunken', orient='horiz', command=e2.xview)    
e2['xscrollcommand'] = s2.set
spacer2 = Frame(frame, width=20, height=10)
e3 = Entry(frame)
s3 = Scrollbar(frame, relief='sunken', orient='horiz', command=e3.xview)    
e3['xscrollcommand'] = s3.set
for w in [e1, s1, spacer1, e2, s2, spacer2, e3, s3]:
    w.pack(side='top', fill='x')

##$w.frame.e1 insert 0 "Initial value"
##$w.frame.e2 insert end "This entry contains a long value, much too long "
##$w.frame.e2 insert end "to fit in the window at one time, so long in fact "
##$w.frame.e2 insert end "that you'll have to scan or scroll to see the end."
e1.insert(0, "Initial value")
e2.insert('end', "This entry contains a long value, much too long ")
e2.insert('end', "to fit in the window at one time, so long in fact ")
e2.insert('end', "that you'll have to scan or scroll to see the end.")