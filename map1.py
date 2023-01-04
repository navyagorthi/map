import tkinter as tk
import tkintermapview

root = tk.Tk()
root.title("POI LEI e LUI e +++")
root.iconbitmap('python Wiederholung/A3_Tkinter/project/img/gui.ico')

marker_count = 0

frame_0 = tk.Frame(root, width=900, height=60, relief='raised', background="#333")
frame_1 = tk.Frame(root, width=900, height=750, relief='raised')

# =================================================================================
# search option menu and entry field
options = ["Search by Address", "Search by Coordinates"]

def get_search_option(*args):
    print(f"search option has changed to '{option_clicked.get()}'")

option_clicked = tk.StringVar(value='Search by Address')
option_clicked.set(options[0])
option_clicked.trace('w', get_search_option)

drop = tk.OptionMenu(frame_0, option_clicked, *options)
drop.config(bg='#333')
drop.config(width=20)
drop.config(height=1)
drop.config(fg="white")

searchfield = tk.Entry(frame_0)
searchfield.config(width=50)
searchfield.config(font=40)

# ==============================================================================
# Button Functions
def change_search_map():
    if option_clicked.get() == "Search by Address":
        map_widget.set_address(searchfield.get(), marker=True)
    elif option_clicked.get() == "Search by Coordinates":
        if option_clicked.get().find(","):
            sep=","
        elif option_clicked.get().find(" "):
            sep=" "
        x = float(searchfield.get().split(sep)[0])
        y = float(searchfield.get().split(sep)[1])

        map_widget.set_marker(round(x, 4), y, text=searchfield.get())
    else:
        print("not a valid entry")

# =============================================================================
# Markers and Path
def clear_map():
    map_widget.delete_all_marker()
    map_widget.delete_all_path()

marker_list = []

def add_marker(coords):
    global marker_count
    marker_count+=1
    new_marker = map_widget.set_marker(coords[0], coords[1], text="marker "+str(marker_count))
    marker_list.append(new_marker.position)
    if len(marker_list) >= 2:
       map_widget.set_path([marker_list[-2], marker_list[-1]])

def set_path():
    marker_list.append((52.57, 13.4), (52.55, 13.35))
    map_widget.set_path([marker_list[-2].position, marker_list[-1], marker_list[-2], marker_list[-1]])
def info():
    tk.messagebox.showinfo("POI LEI e LUI e +++ Usage Info", 'By clicking the Right Button\nyou can draw a Path between extra Markers.')

# ==================================================================================================
# Buttons
btn_marker = tk.Button(frame_0, text="SET POI", command=change_search_map, bg="white", fg="#333")
btn_clear = tk.Button(frame_0, text="CLEAR", command=clear_map, bg="red", fg="white")
btn_show_poi_hist = tk.Button(frame_0, text="HISTORY", bg="#333")
btn_quest = tk.Button(frame_0, text="  ?  ", bg="grey", fg="white", command=info)

map_widget = tkintermapview.TkinterMapView(frame_1, width=900, height=750, corner_radius=0)
map_widget.add_right_click_menu_command(label="Add Marker", command=add_marker, pass_coords=True)

# ==================================================================================================
# place all the stuff
searchfield.place(relx=0.21, rely=0.5, anchor=tk.W)
drop.place(relx=0.02, rely=0.5, anchor=tk.W)
btn_marker.place(relx=0.75, rely=0.5, anchor=tk.CENTER)
btn_clear.place(relx=0.94, rely=0.5, anchor=tk.E)
btn_quest.place(relx=0.98, rely=0.5, anchor=tk.E)
map_widget.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

frame_0.grid(row=0, column=0)
frame_1.grid(row=1, column=0)

# ==================================================================================================
# play as long as you can (infinitly)
root.mainloop()
