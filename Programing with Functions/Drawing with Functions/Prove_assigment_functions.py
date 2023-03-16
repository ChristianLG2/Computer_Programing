# Christian Lira 2022 - Last Revision Winter 2023 
# 
from draw2d import \
    start_drawing, draw_line, draw_oval, draw_arc, \
    draw_rectangle, draw_polygon, draw_text, finish_drawing


def main():
    scene_width = 800
    scene_height = 500

  
    canvas = start_drawing("Scene", scene_width, scene_height)
    draw_sky(canvas, scene_width, scene_height)
    draw_ground(canvas, scene_width, scene_height)
    draw_house (canvas, scene_width, scene_height)
    finish_drawing(canvas)


def draw_sky(canvas, scene_width, scene_height):
    draw_rectangle(canvas, 0, scene_height / 3,
        scene_width, scene_height, width=0, fill="blue4")
    def draw_stars():
     draw_oval(canvas, 45, 400, 50, 405, width=1 ,outline= "yellow2", fill="yellow2")
     draw_oval(canvas, 200, 490, 195, 495, width=1 ,outline= "yellow2", fill="yellow2")
     draw_oval(canvas, 180, 420, 175, 425, width=1 ,outline= "yellow2", fill="yellow2")
     draw_oval(canvas, 400, 318, 405, 323, width=1 ,outline= "yellow2", fill="yellow2")
     draw_oval(canvas, 290, 375, 285, 380, width=1 ,outline= "yellow2", fill="yellow2")
     draw_oval(canvas, 210, 395, 205, 400, width=1 ,outline= "yellow2", fill="yellow2")
     draw_oval(canvas, 70, 445, 75, 450, width=1 ,outline= "yellow2", fill="yellow2")
     draw_oval(canvas, 30, 369, 35, 364, width=1 ,outline= "yellow2", fill="yellow2")
     draw_oval(canvas, 150, 300, 155, 295, width=1 ,outline= "yellow2", fill="yellow2")
     draw_oval(canvas, 116, 295, 121, 300, width=1 ,outline= "yellow2", fill="yellow2")
     draw_oval(canvas, 750, 250, 755, 255, width=1 ,outline= "yellow2", fill="yellow2")
     draw_oval(canvas, 300, 275, 295, 280, width=1 ,outline= "yellow2", fill="yellow2")
     draw_oval(canvas, 560, 280, 565, 285, width=1 ,outline= "yellow2", fill="yellow2")
     draw_oval(canvas, 624, 400, 629, 405, width=1 ,outline= "yellow2", fill="yellow2")
     draw_oval(canvas, 700, 450, 695, 455, width=1 ,outline= "yellow2", fill="yellow2")
     draw_oval(canvas, 650, 460, 655, 465, width=1 ,outline= "yellow2", fill="yellow2")
     draw_oval(canvas, 540, 445, 545, 450, width=1 ,outline= "yellow2", fill="yellow2")
     draw_oval(canvas, 642, 415, 647, 420, width=1 ,outline= "yellow2", fill="yellow2")
     draw_oval(canvas, 525, 365, 530, 370, width=1 ,outline= "yellow2", fill="yellow2")
    draw_stars()
    def draw_clouds():
     draw_oval(canvas, 700, 250, 800, 300, width=1 ,outline= "azure2", fill="azure2")
     draw_oval(canvas, 500, 220, 590, 300, width=1 ,outline= "azure2", fill="azure2")
     draw_oval(canvas, 20, 180, 95, 215, width=1 ,outline= "azure2", fill="azure2")
     draw_oval(canvas, 150, 235, 299, 190, width=1 ,outline= "azure2", fill="azure2")
     draw_oval(canvas, 642, 300, 548, 380, width=1 ,outline= "azure2", fill="azure2")
     draw_oval(canvas, 525, 380, 590, 400, width=1 ,outline= "azure2", fill="azure2")
    draw_clouds()

def draw_ground(canvas, scene_width, scene_height):
    
    draw_rectangle(canvas, 0, 0,
        scene_width, scene_height / 3, width=0, fill="paleGreen4")
    def draw_tree():
        draw_rectangle(canvas, 100, 50, 105, 270, width= 10, outline= "saddleBrown")
        draw_polygon(canvas, 100, 400, 80, 355, 120, 355, width = 1, outline= "paleGreen4", fill="paleGreen4")
        draw_polygon(canvas, 100, 380, 65, 310, 130, 310, width = 1, outline= "paleGreen4", fill="paleGreen4")
        draw_polygon(canvas, 100, 350, 50, 270, 150, 270, width = 1, outline= "paleGreen4", fill="paleGreen4")
        draw_rectangle(canvas, 600, 50, 605, 170, width= 10, outline= "saddleBrown")
        draw_polygon(canvas, 600, 300, 580, 255, 620, 255, width = 1, outline= "paleGreen4", fill="paleGreen4")
        draw_polygon(canvas, 600, 280, 565, 210, 630, 210, width = 1, outline= "paleGreen4", fill="paleGreen4")
        draw_polygon(canvas, 600, 250, 550, 170, 650, 170, width = 1, outline= "paleGreen4", fill="paleGreen4")
    draw_tree()


def draw_house(canvas, scene_width, scene_height):
    draw_rectangle(canvas, 300, 100, 400, 150, width= 200, outline="antiquewhite3")
    def draw_door():
     draw_rectangle(canvas, 250, 0,
     280, 60, width=50, outline="khaki4")
    draw_door()
    def draw_window():
     draw_rectangle(canvas, 250, 150, 450, 180, width= 50, outline= "lightblue1")   
    draw_window()
    def draw_garage():
     draw_rectangle(canvas, 390, 0, 420, 0, width = 100, outline= "ivory4")
    draw_garage()

main()