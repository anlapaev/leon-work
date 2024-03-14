
import PySimpleGUI as sg

FL_top = [[sg.Image(sg.EMOJI_BASE64_BLANK_STARE, subsample= 2, background_color= "#C1C1C1"), 
           sg.Text("Hackathone 15-17 y.o.", background_color= "#C1C1C1", text_color= "#000000"), 
           sg.Image(sg.EMOJI_BASE64_BLANK_STARE, subsample= 2, background_color= "#C1C1C1") ]]

FL_readed = [[sg.Text("???", size= (5, 1), pad= 0, background_color= "#C1C1C1", text_color= "#000000", enable_events= True, key= "-A-"), 
              sg.Text("???", size= (5, 1), pad= 0, background_color= "#C1C1C1", text_color= "#000000", enable_events= True, key= "-F-"),
              sg.Text("???", size= (5, 1), pad= 0, background_color= "#C1C1C1", text_color= "#000000", enable_events= True, key= "-B-"), 
              sg.Text("=", size= (5, 1), pad= 0, background_color= "#C1C1C1", text_color= "#000000"), 
              sg.Text("???", size= (5, 1), pad= 0, background_color= "#C1C1C1", text_color= "#000000", enable_events= True, key= "-R-")]]

FL_logicKiller = [[sg.In(size= (31, 1), pad= 0, enable_events= True, key= "-IN-")]]

FL_kill_me = [[sg.Button("Solve!", size= (27, 1), pad= 0, key= "-Solve-")]]

layout = [[sg.Frame("", FL_top, pad= 0, background_color= "#C1C1C1", border_width= 5)],
          [sg.Frame("", FL_readed, pad= 0, background_color= "#C1C1C1", border_width= 5)],
          [sg.Frame("", FL_logicKiller, pad= 0, background_color= "#C1C1C1", border_width= 5)],
          [sg.Frame("", FL_kill_me, pad= 0, background_color= "#C1C1C1", border_width= 5)]]

# FL_input = [[sg.Text("0", size= (35, 3), enable_events= True, key= "-Value-")]]

# FL_erasers = [[sg.Button("C", size= [8, 3], pad= 0), ]]
# FL_keyboard = [[sg.Button("7", size= [8, 3], pad= 0), sg.Button("8", size=[8,3], pad= 0), sg.Button("9", size=[8,3], pad= 0)],
#                [sg.Button("4", size=[8,3], pad= 0), sg.Button("5", size=[8,3], pad= 0), sg.Button("6", size=[8,3], pad= 0)],
#                [sg.Button("1", size=[8,3], pad= 0), sg.Button("2", size=[8,3], pad= 0), sg.Button("3", size=[8,3], pad= 0)],
#                [sg.Button(" ", size=[8,3], pad= 0), sg.Button("0", size=[8,3], pad= 0), sg.Button(",", size=[8,3], pad= 0)]
#                ]

# FL_operators = [[sg.Button("/", size= (8, 3), pad= 0)],
#                 [sg.Button("*", size= (8, 3), pad= 0)],
#                 [sg.Button("+", size= (8, 3), pad= 0)],
#                 [sg.Button("=", size= (8, 3), pad= 0)]
# ]

# l_top = [[sg.Frame("", FL_top, pad= 0, background_color= "#C1C1C1", border_width= 5)],
#          [sg.Frame("", FL_input, pad= 0, background_color= "#C1C1C1")],
#          [sg.Frame("", FL_erasers, pad= 0, background_color= "#C1C1C1")],
#          [sg.Frame("", FL_keyboard, background_color= "#C1C1C1", border_width= 5, pad= 0), sg.Frame("", FL_operators, background_color= "#C1C1C1", border_width= 5, pad= 0)] ]

