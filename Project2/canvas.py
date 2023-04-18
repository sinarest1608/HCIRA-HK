## Group 18
## Kshitij Sinha
## Hritik Baweja

import tkinter
import math
from datetime import datetime
import time
from tkinter import messagebox

# Part 1a:
# Create A Tkinter App
main = tkinter.Tk()

# Define size of Window
main.geometry("500x500")

# Part 1b:
# Define Canvas Object with a white background
drawCanvas = tkinter.Canvas(main, bg='white')

# Bind the canvas to our app with north-west as (0,0) w.r.t our Window,
# Expand, Fill enables us to use the complete window even if we desire to resize.
drawCanvas.pack(anchor='nw', expand=1, fill='both')

# To store the points while drag (Useful for next part)
points = []

# Part 1c & Part 2a:
# This helps us register the mouse click and store the pointer co-ordinates. We use event here as a parameter.

# Point class to standardize points capturing, processing and result output
class Point:
    def __init__(self, x, y):
        self.X = x
        self.Y = y

def mouseDown(event):
    global points
    points = []
    clearScreen()
    obj1 = DollarRecognizer()
    # print("mouseDown")
    # print(event.x, event.y)
    global x, y
    x = event.x
    y = event.y
    points.append(Point(x, y))


# This helps us draw a line betweem current and previous point. We use event here as a parameter.
def mouseDrag(event):
    global x, y
    drawCanvas.create_line((x, y, event.x, event.y), fill="black")
    x = event.x
    y = event.y
    points.append(Point(x, y))

# This helps us register the mouse release and store the pointer co-ordinates. We use event here as a parameter.


def mouseUp(event):
    # print("mouse up")
    # print(event.x, event.y)
    global x, y
    x = event.x
    y = event.y
    points.append(Point(x, y))
    # Unistroke(points=points, name="")
    # print(points)
    with open('forth.txt', 'w') as f:
        for point in points:
            f.write("Point(" + str(point.X) +","+ str(point.Y) + "),")


# We bind the above functions to events and triggers provided by Tkinter library
drawCanvas.bind("<Button-1>", mouseDown)
drawCanvas.bind("<B1-Motion>", mouseDrag)
drawCanvas.bind("<ButtonRelease-1>", mouseUp)

# Part 1d:


def clearScreen():
    drawCanvas.delete('all')


# Creating a button that calls the clearScreen function
clearScreenButton = tkinter.Button(
    main, text='Clear Canvas', bd='7', command=clearScreen)

# Placing the button at the very bottom of the window
clearScreenButton.pack(side='left')

# <------------------------Part 2------------------------>

# Rectangle class for Bounding box
class Rectangle:
    def __init__(self, x, y, width, height):
        self.X = x
        self.Y = y
        self.Width = width
        self.Height = height

# The unistroke class to store and preprocess templates upon initialisation
class Unistroke:
    def __init__(self, name, points):
        # print(len(points))
        # for i in range(1, len(points)):
        #     drawCanvas.create_oval((points[i-1].X, points[i-1].Y, points[i].X, points[i].Y), fill="red")
        self.Name = name
        self.Points = resample(points, 64)
        # print(len(self.Points))
        # for i in range(1, len(self.Points)):
        #     drawCanvas.create_oval((self.Points[i-1].X+100, self.Points[i-1].Y+100, self.Points[i].X+100, self.Points[i].Y+100),width= 1,fill="green")
        # print("line 102 ", self.Points)
        radians = indicativeAngle(self.Points)
        self.Points = rotateBy(self.Points, radians)
        # for i in range(1, len(self.Points)):
        #     drawCanvas.create_line((self.Points[i-1].X+200, self.Points[i-1].Y+200, self.Points[i].X+200, self.Points[i].Y+200), fill="black")
        self.Points = scaleTo(self.Points, SquareSize)
        self.Points = translateTo(self.Points, Origin)
        

# Result Class to display result in a systematic form with recognised template, Score and Time taken
class Result:
    def __init__(self, name, score, ms):
        self.Name = name
        self.Score = score
        self.Time = ms

# Function to convert angles from Degree to Radian
def Deg2Rad(d):
    d2r = d*math.pi / 180.0
    return d2r


# All the required constants declared as variables. 
NumUnistrokes = 10
NumPoints = 64
SquareSize = 250.0
Origin = Point(0, 0)
Diagonal = math.sqrt(SquareSize * SquareSize + SquareSize * SquareSize)
HalfDiagonal = 0.5 * Diagonal
AngleRange = Deg2Rad(45.0)
AnglePrecision = Deg2Rad(2.0)
Phi = 0.5 * (-1.0 + math.sqrt(5.0))

# The template class. Each template has been made into Unistroke object with each co-ordinate as object for the Point class. 
class DollarRecognizer():
    def __init__(self):
        self.Unistrokes = [0] * 10
        self.Unistrokes[0] = Unistroke("One",  [Point(239,129),Point(239,130),Point(239,131),Point(239,132),Point(239,134),Point(239,135),Point(240,136),Point(240,137),Point(240,138),Point(240,139),Point(240,140),Point(240,141),Point(241,142),Point(241,143),Point(241,145),Point(241,147),Point(241,148),Point(241,151),Point(242,156),Point(242,160),Point(242,165),Point(242,168),Point(243,172),Point(243,175),Point(243,177),Point(245,180),Point(245,182),Point(245,185),Point(245,187),Point(245,191),Point(245,195),Point(245,199),Point(245,202),Point(245,205),Point(245,207),Point(246,209),Point(246,211),Point(246,213),Point(246,215),Point(246,217),Point(246,218),Point(246,219),Point(246,220),Point(246,222),Point(246,223),Point(246,224),Point(246,225),Point(246,227),Point(246,228),Point(246,229),Point(246,230),Point(247,231),Point(247,232),Point(247,234),Point(247,235),Point(247,237),Point(247,239),Point(247,240),Point(247,242),Point(247,243),Point(247,244),Point(247,245),Point(247,246),Point(247,247),Point(247,248),Point(247,250),Point(247,251),Point(247,252),Point(247,254),Point(247,255),Point(247,257),Point(247,258),Point(247,259),Point(247,260),Point(247,261),Point(247,262),Point(247,263),Point(247,263)])
        
        self.Unistrokes[1] = Unistroke("Two",   [Point(166,137),Point(167,136),Point(170,135),Point(172,134),Point(174,134),Point(176,133),Point(178,133),Point(178,132),Point(179,132),Point(182,132),Point(184,132),Point(185,132),Point(186,130),Point(188,130),Point(189,130),Point(190,130),Point(190,129),Point(192,129),Point(193,129),Point(194,129),Point(195,129),Point(197,129),Point(198,129),Point(199,128),Point(200,128),Point(202,127),Point(203,127),Point(204,126),Point(205,126),Point(206,126),Point(209,126),Point(210,126),Point(212,126),Point(214,126),Point(215,126),Point(217,126),Point(218,127),Point(219,128),Point(221,128),Point(222,129),Point(225,129),Point(226,131),Point(227,132),Point(229,133),Point(230,134),Point(231,135),Point(233,137),Point(234,138),Point(235,139),Point(237,141),Point(238,141),Point(239,143),Point(240,145),Point(242,147),Point(242,149),Point(242,150),Point(243,152),Point(244,153),Point(244,156),Point(244,157),Point(245,159),Point(245,161),Point(245,163),Point(245,165),Point(245,166),Point(245,168),Point(245,170),Point(245,172),Point(245,173),Point(245,176),Point(245,177),Point(244,179),Point(243,181),Point(243,183),Point(243,185),Point(242,185),Point(241,188),Point(241,189),Point(240,190),Point(239,192),Point(239,193),Point(238,194),Point(238,196),Point(237,197),Point(235,197),Point(234,200),Point(234,201),Point(234,202),Point(232,203),Point(231,205),Point(231,206),Point(230,207),Point(228,209),Point(226,212),Point(226,213),Point(226,215),Point(225,216),Point(224,218),Point(223,219),Point(222,221),Point(222,222),Point(221,224),Point(221,225),Point(219,226),Point(218,227),Point(216,229),Point(215,230),Point(214,231),Point(212,233),Point(210,233),Point(210,235),Point(207,236),Point(206,237),Point(204,238),Point(202,240),Point(200,241),Point(199,242),Point(198,245),Point(196,247),Point(193,249),Point(192,251),Point(190,253),Point(190,255),Point(189,257),Point(187,257),Point(186,259),Point(186,261),Point(185,261),Point(184,263),Point(182,264),Point(181,265),Point(179,267),Point(178,268),Point(178,269),Point(175,271),Point(174,272),Point(173,273),Point(172,273),Point(170,274),Point(170,275),Point(169,276),Point(168,277),Point(167,277),Point(166,277),Point(166,278),Point(169,278),Point(171,278),Point(175,278),Point(180,277),Point(186,276),Point(190,276),Point(194,276),Point(198,276),Point(200,276),Point(202,276),Point(205,276),Point(207,276),Point(210,276),Point(212,275),Point(214,275),Point(217,275),Point(218,275),Point(220,275),Point(222,275),Point(224,275),Point(226,275),Point(229,275),Point(230,275),Point(231,275),Point(233,275),Point(234,275),Point(236,275),Point(237,275),Point(238,275),Point(239,275),Point(240,275),Point(241,275),Point(242,275),Point(244,275),Point(245,275),Point(246,275),Point(247,275),Point(249,275),Point(250,274),Point(251,274),Point(252,274),Point(254,274),Point(255,274),Point(257,274),Point(258,274),Point(259,274),Point(261,274),Point(262,274),Point(263,274),Point(264,274),Point(266,274),Point(268,274),Point(269,274),Point(270,274),Point(271,274),Point(273,273),Point(274,273),Point(276,273),Point(278,273),Point(279,273),Point(281,273),Point(282,273),Point(283,273),Point(284,273),Point(286,273),Point(288,273),Point(289,273),Point(290,273),Point(291,273),Point(292,273),Point(293,273),Point(294,273),Point(295,273),Point(296,273),Point(297,273),Point(298,273),Point(299,273),Point(300,273),Point(301,273),Point(302,273),Point(302,273)])
        
        self.Unistrokes[2] = Unistroke("Three",   [Point(185,103),Point(185,102),Point(185,101),Point(186,100),Point(187,99),Point(188,98),Point(189,97),Point(191,96),Point(191,95),Point(192,95),Point(194,94),Point(195,93),Point(196,93),Point(197,92),Point(199,91),Point(202,91),Point(203,90),Point(204,89),Point(206,88),Point(207,87),Point(208,87),Point(209,87),Point(210,86),Point(211,85),Point(213,85),Point(214,84),Point(215,84),Point(216,83),Point(218,83),Point(219,82),Point(220,82),Point(222,82),Point(223,82),Point(224,82),Point(225,82),Point(227,82),Point(228,82),Point(229,82),Point(230,83),Point(231,83),Point(233,83),Point(234,84),Point(235,84),Point(236,84),Point(237,84),Point(239,85),Point(239,86),Point(240,86),Point(241,87),Point(242,88),Point(243,88),Point(243,89),Point(244,89),Point(244,90),Point(245,91),Point(246,91),Point(247,92),Point(247,93),Point(247,94),Point(248,94),Point(248,95),Point(249,95),Point(249,96),Point(249,98),Point(250,98),Point(250,99),Point(251,99),Point(251,100),Point(251,101),Point(251,102),Point(251,103),Point(253,103),Point(253,104),Point(253,105),Point(254,106),Point(254,107),Point(254,108),Point(254,109),Point(255,110),Point(255,111),Point(255,112),Point(255,113),Point(255,114),Point(255,115),Point(255,116),Point(255,117),Point(255,118),Point(255,119),Point(255,121),Point(255,122),Point(255,123),Point(255,124),Point(255,125),Point(255,126),Point(255,127),Point(255,128),Point(255,129),Point(255,131),Point(255,132),Point(255,133),Point(255,134),Point(255,135),Point(255,136),Point(254,136),Point(254,137),Point(253,139),Point(252,140),Point(251,141),Point(251,143),Point(250,144),Point(249,146),Point(249,147),Point(248,148),Point(247,150),Point(247,151),Point(246,151),Point(246,152),Point(245,153),Point(245,154),Point(244,154),Point(244,155),Point(243,156),Point(243,157),Point(242,158),Point(241,158),Point(241,159),Point(240,159),Point(239,160),Point(238,162),Point(236,163),Point(235,163),Point(234,163),Point(233,164),Point(231,165),Point(230,165),Point(229,166),Point(227,167),Point(226,168),Point(224,169),Point(223,169),Point(222,170),Point(221,171),Point(219,171),Point(218,172),Point(217,173),Point(216,174),Point(215,174),Point(215,175),Point(213,175),Point(212,176),Point(211,176),Point(210,177),Point(209,178),Point(209,179),Point(208,179),Point(207,179),Point(207,180),Point(206,180),Point(205,181),Point(204,181),Point(204,182),Point(203,183),Point(202,183),Point(201,183),Point(200,183),Point(199,183),Point(199,184),Point(200,184),Point(200,183),Point(201,183),Point(202,183),Point(203,183),Point(204,183),Point(204,182),Point(205,182),Point(206,182),Point(207,182),Point(208,181),Point(209,181),Point(210,180),Point(211,180),Point(211,179),Point(212,179),Point(213,179),Point(214,179),Point(215,179),Point(217,179),Point(218,179),Point(219,179),Point(220,179),Point(221,179),Point(222,179),Point(223,179),Point(223,178),Point(224,178),Point(225,178),Point(226,178),Point(227,178),Point(228,178),Point(229,178),Point(231,177),Point(232,177),Point(233,177),Point(234,177),Point(235,177),Point(236,177),Point(237,177),Point(238,177),Point(239,178),Point(240,179),Point(241,179),Point(242,180),Point(243,181),Point(244,182),Point(245,182),Point(246,183),Point(247,183),Point(247,184),Point(249,184),Point(250,185),Point(251,186),Point(251,187),Point(252,187),Point(253,188),Point(253,189),Point(254,189),Point(255,190),Point(255,191),Point(256,192),Point(257,194),Point(258,194),Point(259,195),Point(259,196),Point(260,197),Point(260,198),Point(261,199),Point(262,199),Point(262,201),Point(263,202),Point(263,203),Point(264,204),Point(265,205),Point(265,206),Point(265,207),Point(265,208),Point(265,209),Point(265,210),Point(265,211),Point(265,212),Point(265,213),Point(265,215),Point(265,216),Point(265,217),Point(265,218),Point(265,219),Point(265,220),Point(265,222),Point(265,223),Point(265,224),Point(265,225),Point(264,226),Point(263,227),Point(262,228),Point(261,229),Point(260,230),Point(259,231),Point(258,232),Point(256,233),Point(255,234),Point(254,235),Point(252,236),Point(251,237),Point(250,239),Point(247,239),Point(247,240),Point(245,242),Point(243,243),Point(242,243),Point(241,244),Point(239,245),Point(238,246),Point(237,247),Point(236,247),Point(236,248),Point(235,248),Point(235,249),Point(234,249),Point(233,249),Point(232,250),Point(231,251),Point(230,251),Point(229,251),Point(228,251),Point(227,252),Point(225,253),Point(224,254),Point(223,254),Point(221,255),Point(220,255),Point(219,255),Point(218,255),Point(216,255),Point(215,255),Point(214,255),Point(213,255),Point(212,255),Point(211,255),Point(208,256),Point(207,256),Point(205,256),Point(203,256),Point(201,256),Point(199,256),Point(196,256),Point(195,256),Point(192,256),Point(191,256),Point(190,256),Point(187,256),Point(185,256),Point(183,256),Point(182,256),Point(181,255),Point(179,255),Point(177,254),Point(175,253),Point(175,251),Point(173,251),Point(172,249),Point(171,248),Point(171,246),Point(170,246),Point(170,245),Point(169,245),Point(169,244),Point(168,243),Point(167,243),Point(167,242),Point(166,241),Point(165,240),Point(164,239),Point(163,239),Point(162,238),Point(162,237),Point(162,236),Point(161,236),Point(161,236)])
        
        self.Unistrokes[3] = Unistroke("Four",   [Point(148,122),Point(148,123),Point(147,124),Point(147,125),Point(147,126),Point(147,127),Point(147,128),Point(146,130),Point(145,133),Point(145,135),Point(145,137),Point(145,139),Point(144,142),Point(144,143),Point(144,146),Point(144,147),Point(143,149),Point(143,151),Point(141,155),Point(141,159),Point(141,163),Point(141,167),Point(141,171),Point(141,175),Point(141,178),Point(141,180),Point(141,183),Point(141,185),Point(141,187),Point(141,188),Point(141,191),Point(141,192),Point(140,195),Point(140,199),Point(140,201),Point(140,204),Point(140,207),Point(140,210),Point(140,211),Point(140,213),Point(140,215),Point(140,218),Point(140,219),Point(140,220),Point(140,222),Point(140,223),Point(140,224),Point(140,225),Point(140,227),Point(139,228),Point(139,230),Point(139,231),Point(139,233),Point(138,234),Point(138,235),Point(138,236),Point(138,238),Point(138,239),Point(138,240),Point(138,241),Point(139,241),Point(140,240),Point(141,240),Point(144,238),Point(145,237),Point(148,236),Point(153,235),Point(155,234),Point(160,233),Point(163,232),Point(169,231),Point(175,230),Point(180,229),Point(185,229),Point(190,228),Point(196,227),Point(201,227),Point(205,227),Point(211,227),Point(217,226),Point(221,226),Point(225,226),Point(231,225),Point(234,225),Point(238,225),Point(243,225),Point(245,225),Point(249,225),Point(252,225),Point(256,225),Point(257,225),Point(260,225),Point(263,225),Point(265,225),Point(266,225),Point(269,225),Point(271,225),Point(272,225),Point(273,225),Point(274,225),Point(276,225),Point(277,225),Point(278,225),Point(279,225),Point(279,223),Point(278,223),Point(278,222),Point(277,219),Point(276,215),Point(275,211),Point(274,207),Point(274,203),Point(273,199),Point(273,197),Point(273,194),Point(273,191),Point(273,189),Point(273,187),Point(273,186),Point(273,183),Point(273,180),Point(273,178),Point(273,175),Point(273,173),Point(273,170),Point(273,168),Point(273,166),Point(273,163),Point(273,162),Point(272,161),Point(272,159),Point(272,158),Point(272,157),Point(272,156),Point(272,155),Point(271,155),Point(271,156),Point(271,157),Point(271,160),Point(271,164),Point(271,168),Point(271,171),Point(271,176),Point(272,179),Point(272,184),Point(272,187),Point(273,191),Point(273,194),Point(273,199),Point(274,205),Point(274,209),Point(274,214),Point(275,218),Point(275,220),Point(276,223),Point(276,227),Point(276,231),Point(276,234),Point(276,237),Point(276,241),Point(276,243),Point(277,247),Point(277,252),Point(277,255),Point(277,256),Point(277,259),Point(277,260),Point(277,262),Point(277,264),Point(277,267),Point(277,268),Point(277,271),Point(277,274),Point(277,277),Point(277,279),Point(277,282),Point(277,284),Point(277,286),Point(277,288),Point(277,290),Point(277,291),Point(277,294),Point(277,295),Point(277,296),Point(277,297),Point(277,298),Point(277,299),Point(277,300),Point(277,301),Point(277,302),Point(277,303),Point(277,304),Point(277,305),Point(277,306),Point(278,306),Point(278,307),Point(278,308),Point(278,309),Point(279,310),Point(279,311),Point(279,312),Point(279,311),Point(279,309),Point(279,309)])
        
        self.Unistrokes[4] = Unistroke("Five",   [Point(344,120),Point(343,120),Point(342,120),Point(339,120),Point(338,120),Point(336,120),Point(333,120),Point(330,120),Point(328,120),Point(326,119),Point(325,119),Point(322,119),Point(321,119),Point(319,119),Point(318,119),Point(316,119),Point(315,119),Point(314,119),Point(313,119),Point(311,119),Point(310,119),Point(309,119),Point(307,119),Point(306,119),Point(305,119),Point(303,119),Point(302,119),Point(301,119),Point(300,119),Point(298,119),Point(296,119),Point(295,119),Point(294,119),Point(293,119),Point(290,119),Point(289,119),Point(288,119),Point(287,119),Point(286,119),Point(285,119),Point(284,119),Point(283,119),Point(282,119),Point(281,119),Point(280,119),Point(279,119),Point(278,119),Point(276,119),Point(275,119),Point(274,119),Point(273,119),Point(271,119),Point(270,119),Point(269,119),Point(268,119),Point(267,119),Point(266,119),Point(265,119),Point(264,119),Point(263,119),Point(262,119),Point(261,119),Point(260,119),Point(259,119),Point(258,119),Point(257,119),Point(256,119),Point(256,120),Point(256,121),Point(256,122),Point(256,124),Point(257,124),Point(257,125),Point(257,126),Point(258,127),Point(258,128),Point(258,129),Point(258,130),Point(258,131),Point(258,132),Point(258,134),Point(258,136),Point(258,137),Point(258,138),Point(259,140),Point(259,141),Point(259,142),Point(259,144),Point(259,145),Point(259,146),Point(259,148),Point(259,150),Point(260,151),Point(260,152),Point(260,153),Point(260,154),Point(260,156),Point(260,157),Point(260,158),Point(260,159),Point(260,160),Point(260,161),Point(260,162),Point(260,164),Point(260,165),Point(260,166),Point(260,167),Point(260,168),Point(260,170),Point(260,171),Point(260,172),Point(260,173),Point(260,175),Point(260,176),Point(260,177),Point(260,178),Point(260,180),Point(260,181),Point(260,182),Point(260,183),Point(260,184),Point(260,185),Point(260,186),Point(261,186),Point(262,186),Point(262,185),Point(263,185),Point(264,184),Point(265,184),Point(266,183),Point(266,182),Point(267,182),Point(268,182),Point(268,181),Point(269,181),Point(270,181),Point(270,180),Point(271,180),Point(272,180),Point(273,180),Point(273,179),Point(274,179),Point(275,179),Point(276,178),Point(278,178),Point(279,178),Point(281,178),Point(282,178),Point(283,178),Point(284,178),Point(285,178),Point(286,178),Point(288,178),Point(289,178),Point(290,178),Point(293,178),Point(294,178),Point(295,178),Point(297,178),Point(298,178),Point(299,178),Point(300,179),Point(301,179),Point(302,179),Point(303,179),Point(304,180),Point(305,180),Point(306,180),Point(308,181),Point(309,181),Point(310,181),Point(311,182),Point(312,182),Point(313,183),Point(314,183),Point(315,184),Point(316,184),Point(317,184),Point(318,185),Point(319,186),Point(320,187),Point(321,187),Point(321,188),Point(322,188),Point(322,189),Point(323,190),Point(323,191),Point(324,191),Point(324,192),Point(325,192),Point(325,193),Point(326,193),Point(326,194),Point(326,195),Point(326,196),Point(326,198),Point(328,199),Point(328,200),Point(328,201),Point(328,202),Point(328,203),Point(328,204),Point(329,204),Point(329,206),Point(329,207),Point(329,208),Point(329,209),Point(329,211),Point(329,212),Point(329,213),Point(329,214),Point(329,215),Point(329,216),Point(329,217),Point(329,219),Point(329,220),Point(329,221),Point(329,222),Point(329,224),Point(329,225),Point(329,226),Point(329,227),Point(328,228),Point(327,231),Point(326,232),Point(326,235),Point(325,236),Point(324,236),Point(323,237),Point(323,238),Point(322,239),Point(321,240),Point(320,241),Point(318,242),Point(318,243),Point(315,244),Point(314,244),Point(313,246),Point(311,246),Point(310,247),Point(309,248),Point(308,248),Point(306,248),Point(306,249),Point(304,250),Point(302,250),Point(302,252),Point(300,252),Point(298,252),Point(298,253),Point(296,253),Point(294,254),Point(292,254),Point(290,254),Point(287,255),Point(286,255),Point(284,255),Point(281,256),Point(279,256),Point(278,256),Point(275,256),Point(274,257),Point(273,257),Point(272,257),Point(270,257),Point(269,258),Point(268,259),Point(266,259),Point(264,260),Point(262,260),Point(261,260),Point(258,260),Point(257,260),Point(254,260),Point(251,260),Point(249,260),Point(246,260),Point(245,260),Point(242,260),Point(240,260),Point(238,260),Point(237,260),Point(234,260),Point(233,260),Point(231,260),Point(229,259),Point(228,258),Point(226,258),Point(225,258),Point(223,258),Point(222,258),Point(221,258),Point(220,258),Point(220,256),Point(219,256),Point(218,256),Point(217,256),Point(216,256),Point(215,256),Point(215,256)])
        
        self.Unistrokes[5] = Unistroke("Six",   [Point(246,99),Point(245,99),Point(243,99),Point(242,99),Point(240,99),Point(239,99),Point(238,99),Point(235,99),Point(234,99),Point(231,99),Point(229,99),Point(227,99),Point(226,99),Point(224,99),Point(222,99),Point(221,99),Point(220,99),Point(219,99),Point(218,99),Point(217,99),Point(216,99),Point(215,99),Point(214,99),Point(213,99),Point(212,100),Point(211,100),Point(210,100),Point(209,101),Point(208,102),Point(207,102),Point(206,103),Point(205,103),Point(203,104),Point(202,105),Point(201,106),Point(200,107),Point(198,109),Point(196,111),Point(194,113),Point(192,115),Point(191,117),Point(190,118),Point(189,119),Point(188,120),Point(188,122),Point(186,123),Point(186,124),Point(184,125),Point(184,126),Point(182,127),Point(182,129),Point(180,130),Point(180,131),Point(178,131),Point(178,133),Point(177,135),Point(176,136),Point(174,139),Point(174,141),Point(174,143),Point(173,144),Point(172,147),Point(171,148),Point(171,150),Point(170,151),Point(170,153),Point(169,154),Point(168,155),Point(168,156),Point(168,158),Point(168,159),Point(168,161),Point(168,163),Point(168,165),Point(169,167),Point(170,171),Point(170,174),Point(171,177),Point(172,179),Point(172,181),Point(173,184),Point(174,187),Point(174,188),Point(175,190),Point(176,191),Point(177,193),Point(177,194),Point(178,195),Point(178,197),Point(179,199),Point(179,202),Point(180,203),Point(182,205),Point(182,207),Point(182,209),Point(183,211),Point(184,213),Point(184,215),Point(186,216),Point(186,219),Point(188,220),Point(189,221),Point(190,223),Point(191,223),Point(193,225),Point(194,227),Point(195,227),Point(197,228),Point(198,229),Point(200,229),Point(201,231),Point(202,231),Point(204,231),Point(206,231),Point(208,231),Point(209,231),Point(210,231),Point(211,232),Point(213,232),Point(214,232),Point(216,232),Point(218,232),Point(219,232),Point(222,232),Point(224,232),Point(226,232),Point(228,231),Point(230,231),Point(231,231),Point(232,230),Point(234,229),Point(235,229),Point(236,229),Point(238,228),Point(239,227),Point(240,227),Point(241,227),Point(242,227),Point(242,226),Point(245,224),Point(246,223),Point(247,221),Point(248,220),Point(249,218),Point(250,217),Point(251,215),Point(251,212),Point(253,211),Point(253,210),Point(254,209),Point(255,208),Point(255,206),Point(256,206),Point(256,205),Point(257,205),Point(258,204),Point(258,203),Point(258,202),Point(259,201),Point(259,199),Point(260,199),Point(261,195),Point(261,194),Point(261,191),Point(261,188),Point(261,187),Point(261,183),Point(260,181),Point(260,180),Point(259,178),Point(258,177),Point(258,176),Point(258,175),Point(257,175),Point(256,173),Point(254,172),Point(254,171),Point(253,171),Point(252,170),Point(251,170),Point(250,170),Point(249,170),Point(248,170),Point(246,170),Point(245,170),Point(244,168),Point(243,168),Point(242,168),Point(239,167),Point(238,167),Point(237,167),Point(235,167),Point(233,167),Point(232,167),Point(230,167),Point(229,167),Point(228,167),Point(226,167),Point(224,167),Point(223,167),Point(222,167),Point(221,167),Point(220,167),Point(218,167),Point(217,167),Point(216,167),Point(215,167),Point(214,167),Point(213,166),Point(211,166),Point(210,166),Point(209,166),Point(208,166),Point(207,166),Point(206,166),Point(205,166),Point(203,166),Point(202,166),Point(201,166),Point(200,166),Point(199,166),Point(198,166),Point(197,166),Point(196,166),Point(194,166),Point(193,166),Point(192,166),Point(191,166),Point(190,166),Point(189,166),Point(188,166),Point(187,166),Point(186,166),Point(185,166),Point(184,166),Point(183,166),Point(182,167),Point(181,167),Point(180,167),Point(179,167),Point(178,167),Point(178,168),Point(178,169),Point(177,169),Point(176,169),Point(175,169),Point(174,169),Point(174,170),Point(173,170),Point(172,171),Point(171,171),Point(170,171),Point(170,171)])
        
        self.Unistrokes[6] = Unistroke("Seven",   [Point(186,107),Point(186,108),Point(188,108),Point(189,108),Point(191,109),Point(193,109),Point(195,110),Point(198,110),Point(201,110),Point(206,110),Point(209,110),Point(213,110),Point(215,110),Point(218,110),Point(220,110),Point(222,110),Point(225,110),Point(226,110),Point(227,110),Point(230,110),Point(231,110),Point(233,110),Point(235,110),Point(237,110),Point(239,110),Point(242,110),Point(245,110),Point(247,110),Point(250,110),Point(252,110),Point(254,110),Point(256,110),Point(257,110),Point(258,110),Point(260,110),Point(261,110),Point(262,110),Point(264,110),Point(266,110),Point(267,109),Point(269,109),Point(270,109),Point(271,109),Point(273,108),Point(274,108),Point(276,108),Point(277,108),Point(278,108),Point(279,108),Point(279,109),Point(279,110),Point(279,111),Point(278,113),Point(278,115),Point(276,117),Point(274,121),Point(273,123),Point(271,127),Point(270,130),Point(270,131),Point(269,134),Point(267,136),Point(266,139),Point(265,142),Point(263,145),Point(262,148),Point(261,152),Point(259,156),Point(258,159),Point(257,164),Point(255,168),Point(254,171),Point(252,174),Point(250,177),Point(250,180),Point(246,185),Point(245,187),Point(242,193),Point(240,197),Point(237,202),Point(235,205),Point(234,209),Point(233,211),Point(231,214),Point(230,216),Point(230,218),Point(229,220),Point(228,223),Point(227,227),Point(226,229),Point(224,234),Point(223,236),Point(222,240),Point(222,244),Point(222,247),Point(221,250),Point(220,251),Point(220,254),Point(219,255),Point(219,257),Point(219,258),Point(218,259),Point(218,260),Point(218,261),Point(218,262),Point(218,263),Point(218,263)])
        
        self.Unistrokes[7] = Unistroke("Eight",   [Point(216,119),Point(215,119),Point(212,119),Point(211,119),Point(209,119),Point(207,119),Point(205,119),Point(204,119),Point(201,120),Point(200,120),Point(198,120),Point(198,121),Point(197,121),Point(196,121),Point(195,122),Point(193,123),Point(193,124),Point(192,125),Point(191,125),Point(190,126),Point(190,127),Point(189,128),Point(189,129),Point(188,130),Point(188,131),Point(188,133),Point(187,133),Point(185,135),Point(185,137),Point(184,139),Point(184,141),Point(184,142),Point(184,144),Point(184,145),Point(184,146),Point(184,147),Point(184,148),Point(184,149),Point(184,150),Point(184,151),Point(184,152),Point(184,153),Point(184,155),Point(186,157),Point(187,159),Point(188,161),Point(188,162),Point(188,163),Point(189,165),Point(190,165),Point(192,167),Point(192,169),Point(193,169),Point(194,171),Point(196,172),Point(196,173),Point(199,174),Point(201,175),Point(203,176),Point(206,176),Point(208,177),Point(211,177),Point(212,177),Point(215,177),Point(217,177),Point(219,177),Point(220,177),Point(223,177),Point(224,177),Point(226,177),Point(228,177),Point(231,177),Point(232,178),Point(234,178),Point(236,178),Point(240,179),Point(242,181),Point(243,181),Point(245,181),Point(246,181),Point(247,181),Point(248,181),Point(250,182),Point(251,182),Point(251,183),Point(252,183),Point(253,184),Point(253,185),Point(255,185),Point(256,186),Point(256,187),Point(257,188),Point(257,189),Point(258,191),Point(258,193),Point(258,194),Point(258,197),Point(259,198),Point(259,201),Point(259,203),Point(259,205),Point(259,206),Point(259,208),Point(259,209),Point(259,210),Point(259,211),Point(258,212),Point(258,213),Point(257,214),Point(256,215),Point(256,216),Point(256,217),Point(255,218),Point(254,220),Point(253,221),Point(251,222),Point(249,225),Point(247,225),Point(244,227),Point(243,228),Point(240,229),Point(239,230),Point(237,232),Point(234,233),Point(233,233),Point(232,233),Point(231,234),Point(228,235),Point(227,235),Point(224,237),Point(223,237),Point(220,238),Point(216,239),Point(214,240),Point(210,241),Point(208,241),Point(204,241),Point(203,241),Point(201,241),Point(199,241),Point(197,241),Point(196,241),Point(194,241),Point(193,241),Point(192,241),Point(191,241),Point(190,241),Point(188,240),Point(187,240),Point(186,240),Point(184,239),Point(184,238),Point(183,238),Point(181,237),Point(180,236),Point(179,234),Point(178,233),Point(176,232),Point(176,230),Point(175,229),Point(174,228),Point(173,227),Point(172,225),Point(172,224),Point(172,221),Point(171,218),Point(171,216),Point(171,213),Point(171,212),Point(171,209),Point(171,207),Point(172,205),Point(172,203),Point(172,199),Point(173,197),Point(174,195),Point(175,193),Point(176,191),Point(177,189),Point(179,188),Point(179,187),Point(180,186),Point(180,185),Point(181,185),Point(184,184),Point(184,183),Point(186,182),Point(187,181),Point(189,181),Point(191,181),Point(192,180),Point(196,177),Point(198,177),Point(200,176),Point(204,175),Point(206,174),Point(208,174),Point(210,173),Point(211,173),Point(212,172),Point(214,171),Point(215,170),Point(216,170),Point(217,169),Point(218,169),Point(219,169),Point(220,168),Point(221,168),Point(223,167),Point(224,165),Point(225,165),Point(226,164),Point(227,163),Point(228,162),Point(228,161),Point(229,161),Point(230,160),Point(231,159),Point(232,158),Point(232,157),Point(234,157),Point(234,156),Point(235,155),Point(236,154),Point(236,153),Point(236,152),Point(236,150),Point(236,149),Point(236,148),Point(236,146),Point(236,145),Point(236,144),Point(236,143),Point(236,141),Point(235,140),Point(234,139),Point(233,137),Point(233,136),Point(232,135),Point(232,134),Point(232,133),Point(231,133),Point(231,132),Point(230,131),Point(229,131),Point(228,130),Point(228,129),Point(227,129),Point(226,129),Point(225,128),Point(224,127),Point(224,126),Point(223,126),Point(223,125),Point(222,125),Point(221,125),Point(220,125),Point(220,124),Point(219,123),Point(218,123),Point(218,122),Point(217,122),Point(216,122),Point(216,121),Point(215,121),Point(214,121),Point(213,121),Point(212,121),Point(212,120),Point(211,120),Point(210,120),Point(209,120),Point(209,119),Point(208,119),Point(207,119),Point(206,119),Point(206,118),Point(205,118),Point(204,118),Point(204,118)])
        
        self.Unistrokes[8] = Unistroke("Nine",   [Point(263,158),Point(262,158),Point(260,158),Point(258,158),Point(255,158),Point(253,158),Point(251,158),Point(248,158),Point(245,158),Point(243,158),Point(240,158),Point(236,158),Point(234,158),Point(230,160),Point(227,161),Point(223,162),Point(221,165),Point(217,166),Point(214,167),Point(209,169),Point(204,171),Point(199,173),Point(197,174),Point(192,176),Point(190,177),Point(187,180),Point(184,182),Point(181,184),Point(179,187),Point(177,190),Point(176,193),Point(174,194),Point(173,196),Point(171,198),Point(171,201),Point(169,203),Point(167,208),Point(167,213),Point(166,218),Point(165,222),Point(165,226),Point(165,230),Point(165,232),Point(165,234),Point(166,237),Point(167,239),Point(167,243),Point(169,246),Point(171,250),Point(172,253),Point(175,258),Point(177,261),Point(179,263),Point(181,266),Point(184,269),Point(187,272),Point(190,274),Point(193,275),Point(195,278),Point(198,278),Point(200,279),Point(202,280),Point(204,281),Point(205,281),Point(207,282),Point(209,282),Point(211,283),Point(213,284),Point(215,284),Point(217,284),Point(219,284),Point(222,284),Point(224,284),Point(227,284),Point(229,284),Point(231,283),Point(235,282),Point(238,281),Point(240,280),Point(243,279),Point(245,278),Point(248,276),Point(250,274),Point(253,272),Point(255,268),Point(257,266),Point(259,262),Point(261,261),Point(263,258),Point(265,256),Point(266,254),Point(267,253),Point(268,252),Point(269,250),Point(271,248),Point(272,246),Point(273,243),Point(275,240),Point(278,235),Point(279,233),Point(279,231),Point(281,228),Point(283,225),Point(283,222),Point(284,221),Point(285,219),Point(285,218),Point(285,215),Point(286,214),Point(286,212),Point(286,210),Point(286,208),Point(286,206),Point(286,205),Point(286,204),Point(286,202),Point(286,201),Point(286,199),Point(286,198),Point(286,197),Point(286,196),Point(286,195),Point(286,194),Point(286,193),Point(286,192),Point(285,192),Point(285,190),Point(284,190),Point(283,189),Point(283,188),Point(283,187),Point(282,186),Point(281,185),Point(280,185),Point(279,184),Point(279,183),Point(278,182),Point(277,182),Point(276,180),Point(275,180),Point(275,179),Point(274,179),Point(273,178),Point(272,177),Point(272,176),Point(271,175),Point(270,174),Point(270,173),Point(269,172),Point(269,171),Point(269,170),Point(268,170),Point(270,171),Point(270,172),Point(271,173),Point(273,174),Point(274,177),Point(275,178),Point(277,179),Point(279,182),Point(280,184),Point(283,186),Point(283,190),Point(286,193),Point(287,197),Point(287,198),Point(287,201),Point(288,203),Point(289,205),Point(290,206),Point(290,209),Point(291,212),Point(291,216),Point(291,218),Point(292,223),Point(292,227),Point(292,231),Point(292,234),Point(292,238),Point(292,240),Point(292,243),Point(292,246),Point(292,250),Point(292,254),Point(292,259),Point(292,265),Point(292,269),Point(292,274),Point(292,276),Point(291,279),Point(291,282),Point(290,286),Point(290,290),Point(289,296),Point(289,302),Point(288,309),Point(287,314),Point(287,318),Point(287,323),Point(287,326),Point(287,330),Point(287,332),Point(287,334),Point(287,338),Point(287,343),Point(287,346),Point(287,350),Point(287,352),Point(287,354),Point(287,356),Point(287,358),Point(287,359),Point(287,362),Point(287,363),Point(287,364),Point(287,365),Point(287,366),Point(287,368),Point(287,369),Point(287,370),Point(287,373),Point(287,374),Point(287,376),Point(287,377),Point(287,378),Point(287,380),Point(287,381),Point(287,382),Point(287,383),Point(287,384),Point(287,385),Point(287,386),Point(286,386),Point(286,385),Point(286,384),Point(286,384)])
        
        self.Unistrokes[9] = Unistroke("Zero",   [Point(127, 141), Point(124, 140), Point(120, 139), Point(118, 139), Point(116, 139), Point(111, 140), Point(109, 141), Point(104, 144), Point(100, 147), Point(96, 152), Point(93, 157), Point(90, 163), Point(87, 169), Point(85, 175), Point(83, 181), Point(82, 190), Point(82, 195), Point(83, 200), Point(84, 205), Point(88, 213), Point(91, 216), Point(
             96, 219), Point(103, 222), Point(108, 224), Point(111, 224), Point(120, 224), Point(133, 223), Point(142, 222), Point(152, 218), Point(160, 214), Point(167, 210), Point(173, 204), Point(178, 198), Point(179, 196), Point(182, 188), Point(182, 177), Point(178, 167), Point(170, 150), Point(163, 138), Point(152, 130), Point(143, 129), Point(140, 131), Point(129, 136), Point(126, 139)])

# --- Step 1: Resampling begins ---

# Simple Eucledian distance calculation
def distance(p1, p2):
    dx = p2.X - p1.X
    dy = p2.Y - p1.Y
    dx = pow(dx, 2)
    dy = pow(dy, 2)
    return math.sqrt(dx + dy)

# Path length calculation 
def path_length(A):
    d = 0.0
    for i in range(1, len(A)):
        d = d + math.dist([A[i-1].X, A[i-1].Y], [A[i].X, A[i].Y])
    return d

# The resampling function according to the pseudocode defined in the paper
def resample(points, n):
    I = path_length(points)/(n-1)
    # print(path_length(points))
    # print(I)
    D = 0.0
    newPoints = []
    newPoints.append(Point(points[0].X, points[0].Y))
    lenPoints = len(points)
    i=1
    while i < lenPoints:
        # print("n", len(newPoints))
        # print("p", len(points))
        d = math.dist([points[i-1].X, points[i-1].Y], [points[i].X, points[i].Y])
        if ((d + D) >= I):
            qx = points[i-1].X + ((I - D)/d) * (points[i].X - points[i-1].X)
            qy = points[i-1].Y + ((I - D)/d) * (points[i].Y - points[i-1].Y)
            q = Point(qx, qy)
            newPoints.append(q)
            points.insert(i, q) 
            lenPoints = len(points)
            D = 0.0
        else:
            D = D + d
        i=i+1
    if(len(newPoints) == n-1):
        q = Point(points[len(points)-1].X, points[len(points)-1].Y)
        newPoints.append(q)
    return newPoints


# --- Step 2: Rotation ---

# Calculation of the Centroid 
def Centroid(points):
    x = 0.0
    y = 0.0
    for i in range(0, len(points)):
        # print("line 246", points[i])
        # print("line 247 ", points)
        # print("line 248 ", type(points[i]))
        # print("line 249 ", type(points[i].X))
        x = x + points[i].X
        y = y + points[i].Y

    x = x/len(points)
    y = y/len(points)

    return Point(x, y)

# Calculating Indicative Angle
def indicativeAngle(points):
    # print("line 258", type(points))
    # print("line 259 ", points[0])
    # print("line 260 ", type(points[0].X))
    c = Centroid(points)
    theta = math.atan2(c.Y - points[0].Y, c.X - points[0].X)
    return theta

# The rotate to 0,0 function
def rotateToZero(points):
    c = Centroid(points)
    theta = math.atan(c.Y - points[0].Y, c.X - points[0].X)
    newPoints = rotateBy(points, -theta)
    return newPoints

# The function used to rotate the gesture by the angle provided
def rotateBy(points, theta):
    c = Centroid(points)
    cos = math.cos(theta)
    sin = math.sin(theta)
    newPoints = []
    for i in range(0, len(points)):
        qx = (points[i].X - c.X)*cos - (points[i].Y - c.Y)*sin + c.X
        qy = (points[i].X - c.X)*sin + (points[i].Y - c.Y) * cos + c.Y
        newPoints.append(Point(qx, qy))
    return newPoints


# Creating the bounding box that returns as rectangle as the oject of the Rectangle class
def boundingBox(points):
    minX = math.inf
    maxX = -math.inf
    minY = math.inf
    maxY = -math.inf
    for i in range(0, len(points)):
        minX = min(minX, points[i].X)
        maxX = max(maxX, points[i].X)
        minY = min(minY, points[i].Y)
        maxY = max(maxY, points[i].Y)
    return Rectangle(minX, minY, maxX-minX, maxY-minY)

# --- Step 3: Scaling & Translating --- 
def scaleTo(points, size):
    b = boundingBox(points)
    # print("b ", b.X, b.Y, b.Width, b.Height)
    newPoints = []
    for i in range(0, len(points)):
        qx = points[i].X * (size/b.Width)
        qy = points[i].Y * (size/b.Height)
        newPoints.append(Point(qx, qy))
    return newPoints

def translateTo(points, pt):
    c = Centroid(points)
    newPoints = []
    for i in range(0, len(points)):
        qx = points[i].X + pt.X - c.X
        qy = points[i].Y + pt.Y - c.Y
        newPoints.append(Point(qx, qy))
    return newPoints

# --- Step 4: Recognize ---

# Calculating the distance at best angle 
def distanceAtBestAngle(points, T, thetaA, thetaB, thetaD):
    phi = (math.sqrt(5) - 1)/2
    x1 = phi*thetaA + (1 - phi)*thetaB
    f1 = distanceAtAngle(points, T, x1)
    x2 = (1 - phi)*thetaA + phi*thetaB
    f2 = distanceAtAngle(points, T, x2)

    while abs(thetaB - thetaA) > thetaD:
        if f1 < f2:
            thetaB = x2
            x2 = x1
            f2 = f1
            x1 = phi*thetaA + (1 - phi)*thetaB
            f1 = distanceAtAngle(points, T, x1)
        else:
            thetaA = x1
            x1 = x2
            f1 = f2
            x2 = (1 - phi)*thetaA + phi*thetaB
            f2 = distanceAtAngle(points, T, x2)
    return min(f1, f2)

# Calculating Distance at a particular angle
def distanceAtAngle(points, T, theta):
    newPoints = rotateBy(points, theta)
    # print("line 338 ", len(points))
    # print("line 339 ", len(T.Points))
    d = pathDistance(newPoints, T.Points)
    return d

# Calculating Path distance using the Eucledian distance function defined previously.
def pathDistance(A, B):
    d = 0
    for i in range(0, len(A)):
        d += distance(A[i], B[i])
    return d/len(A)

# The actual recognize function
def recognize(points, templates, size):
    s = time.time()
    # print("Points passed in recognise, ", points)
    # Represents Infinity
    b = math.inf

    theta = Deg2Rad(45)
    thetaD = Deg2Rad(2)
    Tprime = ""
    for T in templates:
        # print("T len ", len(T.Points))
        # print("points Le, ", len(points))
        
        d = distanceAtBestAngle(points, T, -1*theta, theta, thetaD)
        if d < b:
            b = d
            Tprime = T
        print("T ", T.Name, " TPrime ", Tprime.Name)
    # sizePrime = math.sqrt(2*size*size)
    score = 1 - (b/(0.5*(math.sqrt(size**2 + size**2))))
    
    e =  time.time()
    executionTime = e-s
    return [Tprime, score, executionTime*1000]

# Displaying the result on button click using an information box
def displayResult(template, score, timeTaken):
    messagebox.showinfo("Result", "Result: " + template + " \nScore: " + str(round(score*100)) + "\n Time take: "+str(round(timeTaken)) + "ms")

# Calcualting the result and identifying gesture. This function is called on the "Recognize" function and returns the result to the displayResult function
def result():
    Points = resample(points=points, n=64)
    print("points ",len(Points))
    r = indicativeAngle(Points)
    Points = rotateBy(Points, r)
    Points = scaleTo(Points, SquareSize)
    Points = translateTo(Points, Origin)
    print("points ",len(Points))
    resName = recognize(points=Points, templates=DollarRecognizer().Unistrokes, size=SquareSize)
    print("line 386 ", resName[0].Name, resName[1], resName[2])
    displayResult(resName[0].Name, resName[1], resName[2])

# Defining a recognize button for the window
recognizeScreenButton = tkinter.Button(
    main, text='Recognize Gesture', bd='7', command=result)

# Placing the button at the very bottom of the window
recognizeScreenButton.pack(side='left')

# Put the Tkinter App in loop so it keeps running until terminated explicitly using Ctrl+C
main.mainloop()
