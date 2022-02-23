import tkinter as tk
from tkinter import ttk
from tkinter.font import Font
import random
#!!!! IMPORTANT: Must download Pillow module for program to run.
    # to download from shell `python -m pip install --upgrade pip`, then `python -m pip install --upgrade Pillow`
from PIL import ImageTk, Image # better formatting with images

# -------------------------------------------------------------------

# Metadata just for fun why not
__author__ = "Elle Miller, Jacob Merrick, Peter Fortier"
__credits__ = ["Elle Miller", "Jacob Merrick", "Peter Fortier"]
__version__ = "0.1"
__date__ = "Date String"
__status__ = "Prototype"

# -------------------------------------------------------------------

#!! GLOBAL CONSTANTS

# Window Resolution
maxWidth = 800
#maxHeight = 400

# Map Markers
mapMarkers = {
    "loc1": (315,115),
    "loc2": (650,140),
    "loc3": (500,50),
    "loc4": (450,50),
    "loc5": (400,50),
    "loc6": (350,50),
    "loc7": (300,50),
    "loc8": (250,50),
    "loc9": (200,50),
    "loc10": (150,50),
    "loc11": (100,50),
    "loc12": (50,50),
    "loc13": (500,100),
    "loc14": (450,100),
    "loc15": (400,100),
    "loc16": (350,100),
    "loc17": (300,100),
    "loc18": (250,100),
    "loc19": (200,100),
    "loc20": (150,100),
    "loc21": (100,100),
    "loc22": (50,100)
}
# Detail Intro Note
introNote = " Click on the RED image marks to learn more about each site!"
# Detail Locations
    # {"loc": ["placeName", "imgPath", "intro", [[(x1,y1,x2,y2), "addInfo"], [(x1,y1,x2,y2), "addInfo"], [(x1,y1,x2,y2), "addInfo"]]]
locations = {
    "loc1": [
        "Big Ben",
        "Big Ben.png",
        "Welcome to MUSEUM in Midtown. This building was built in YEAR and its design was inspired by the unique style of some dude.",
        [
            [(120,390), "There you are in the parking lot. I'm glad you've made it."], 
            [(300,140), "There is a lot you can see from here. Unfortunately, only service workers are allowed."], 
            [(350,350), "You've clicked on what looks like a balcony. I don't know anything about this place."],
        ]
    ],
    "loc2": [
        "Albert Memorial",
        "Albert Memorial.png",
        "Welcome to MUSEUM in Midtown. This building was built in YEAR and its design was inspired by the unique style of some dude.",
        [
            [(100,290), "There you are in the parking lot. I'm glad you've made it."], 
            [(400,20), "There is a lot you can see from here. Unfortunately, only service workers are allowed."], 
            [(300,360), "You've clicked on what looks like a balcony. I don't know anything about this place."],
        ]
    ],
    "loc3": [
        "British Museum",
        "British Museum.png",
        "British Museum"
    ],
    "loc4": [
        "Buckingham Palace",
        "Buckingham Palace.png",
        "Buckingham Palace"
    ],
    "loc5": [
        "Globe Theater",
        "Globe Theater.png",
        "Globe Theater"
    ],
    "loc6":[
        "Hampton Court Palace",
        "Hampton Court Palace.png",
        "Hampton Court Palace"
    ],
    "loc7" :[
        "Harrods",
        "Harrods.png",
        "Harrods"
    ],
    "loc8" :[
        "Hyde Park",
        "Hyde Park.png",
        "Hyde Park"
    ],
    "loc9" :[
        "Kensington Palace",
        "Kensington Palace.png",
        "Kensington Palace"
    ],
    "loc10" :[
        "Kew Garden",
        "Kew Garden.png",
        "Kew Garden"
    ],
    "loc11" :[
        "London Bridge",
        "London Bridge.png",
        "London Bridge"
    ],
    "loc12" :[
        "London Eye",
        "London Eye.png",
        "London Eye"
    ],
    "loc13" :[
        "Parliment",
        "Parliment.png",
        "Parilment"
    ],
    "loc14" :[
        "Royal Albert Hall",
        "Royal Albert Hall.png",
        "Royal Albert Hall"
    ],
    "loc15" :[
        "St. Paul's Cathedral",
        "St. Paul's Cathedral.png",
        "St. Pauls Cathedral"
    ],
    "loc16" :[
        "The National Theater",
        "The National Theater.png",
        "The National Theater"
    ],
    "loc17" :[
        "The Shard",
        "The Shard.png",
        "The Shard"
    ],
    "loc18" :[
        "Tower of London",
        "Tower of London.png",
        "Tower of London"
    ],
    "loc19" :[
        "Victoria and Albert Museum",
        "Victoria and Albert Museum.png",
        "Victoria and Albert Museum"
    ],
    "loc20" :[
        "Westminster Abbey",
        "Westminster Abbey.png",
        "Westminster Abbey"
    ],
    "loc21" :[
        "London Bus",
        "London Bus.png",
        "London Bus"
    ],
    "loc22" :[
        "London Phone Booth",
        "London Phone Booth.png",
        "London Phone Booth"
    ],
}
# Quiz Questions
quizQs = {
    "loc1": [
        ["Q1", {"option1": False, "option2": True, "option3": False}],
        ["Q2", {"option1": True, "option2": False, "option3": False}],
        ["Q3", {"option1": True, "option2": False, "option3": False}] # do something like `if option` to determine correctness
    ],
    "loc2": [
        ["Q1", {"option1": False, "option2": True, "option3": False}],
        ["Q2", {"option1": True, "option2": False, "option3": False}],
        ["Q3", {"option1": True, "option2": False, "option3": False}]
    ],
    "loc3": [
        ["Q1", {"option1": False, "option2": True, "option3": False}],
        ["Q2", {"option1": True, "option2": False, "option3": False}],
        ["Q3", {"option1": True, "option2": False, "option3": False}]
    ],
    "loc4" : [
      ["Q1", {"option1": False, "option2": True, "option3": False}],
        ["Q2", {"option1": True, "option2": False, "option3": False}],
        ["Q3", {"option1": True, "option2": False, "option3": False}]

    ],
    "loc5" :[
        ["Q1", {"option1": False, "option2": True, "option3": False}],
        ["Q2", {"option1": True, "option2": False, "option3": False}],
        ["Q3", {"option1": True, "option2": False, "option3": False}]
    ],
    "loc6" :[
        ["Q1", {"option1": False, "option2": True, "option3": False}],
        ["Q2", {"option1": True, "option2": False, "option3": False}],
        ["Q3", {"option1": True, "option2": False, "option3": False}]
    ],
    "loc7" :[
        ["Q1", {"option1": False, "option2": True, "option3": False}],
        ["Q2", {"option1": True, "option2": False, "option3": False}],
        ["Q3", {"option1": True, "option2": False, "option3": False}]
    ],
    "loc8" :[
        ["Q1", {"option1": False, "option2": True, "option3": False}],
        ["Q2", {"option1": True, "option2": False, "option3": False}],
        ["Q3", {"option1": True, "option2": False, "option3": False}]
    ],
    "loc9" :[
        ["Q1", {"option1": False, "option2": True, "option3": False}],
        ["Q2", {"option1": True, "option2": False, "option3": False}],
        ["Q3", {"option1": True, "option2": False, "option3": False}]
    ],
    "loc10" :[
        ["Q1", {"option1": False, "option2": True, "option3": False}],
        ["Q2", {"option1": True, "option2": False, "option3": False}],
        ["Q3", {"option1": True, "option2": False, "option3": False}]
    ],
    "loc11" :[
        ["Q1", {"option1": False, "option2": True, "option3": False}],
        ["Q2", {"option1": True, "option2": False, "option3": False}],
        ["Q3", {"option1": True, "option2": False, "option3": False}]
    ],
    "loc12" :[
        ["Q1", {"option1": False, "option2": True, "option3": False}],
        ["Q2", {"option1": True, "option2": False, "option3": False}],
        ["Q3", {"option1": True, "option2": False, "option3": False}]
    ],
    "loc13" :[
        ["Q1", {"option1": False, "option2": True, "option3": False}],
        ["Q2", {"option1": True, "option2": False, "option3": False}],
        ["Q3", {"option1": True, "option2": False, "option3": False}]
    ],
    "loc14" :[
        ["Q1", {"option1": False, "option2": True, "option3": False}],
        ["Q2", {"option1": True, "option2": False, "option3": False}],
        ["Q3", {"option1": True, "option2": False, "option3": False}]
    ],
    "loc15" :[
        ["Q1", {"option1": False, "option2": True, "option3": False}],
        ["Q2", {"option1": True, "option2": False, "option3": False}],
        ["Q3", {"option1": True, "option2": False, "option3": False}]
    ],
    "loc16" :[
        ["Q1", {"option1": False, "option2": True, "option3": False}],
        ["Q2", {"option1": True, "option2": False, "option3": False}],
        ["Q3", {"option1": True, "option2": False, "option3": False}]
    ],
    "loc17" :[
        ["Q1", {"option1": False, "option2": True, "option3": False}],
        ["Q2", {"option1": True, "option2": False, "option3": False}],
        ["Q3", {"option1": True, "option2": False, "option3": False}]
    ],
    "loc18" :[
        ["Q1", {"option1": False, "option2": True, "option3": False}],
        ["Q2", {"option1": True, "option2": False, "option3": False}],
        ["Q3", {"option1": True, "option2": False, "option3": False}]
    ],
    "loc19" :[
        ["Q1", {"option1": False, "option2": True, "option3": False}],
        ["Q2", {"option1": True, "option2": False, "option3": False}],
        ["Q3", {"option1": True, "option2": False, "option3": False}]
    ],
    "loc20" :[
        ["Q1", {"option1": False, "option2": True, "option3": False}],
        ["Q2", {"option1": True, "option2": False, "option3": False}],
        ["Q3", {"option1": True, "option2": False, "option3": False}]
    ],
    "loc21" :[
        ["Q1", {"option1": False, "option2": True, "option3": False}],
        ["Q2", {"option1": True, "option2": False, "option3": False}],
        ["Q3", {"option1": True, "option2": False, "option3": False}]
    ],
    "loc22" :[
        ["Q1", {"option1": False, "option2": True, "option3": False}],
        ["Q2", {"option1": True, "option2": False, "option3": False}],
        ["Q3", {"option1": True, "option2": False, "option3": False}]  
    ]
}


#!! GLOBAL FUNCTIONS
# Guide Selected Resource

selectedGuide = 1 # intialize
def guideGet(side):
    path = "./photos/guide" + str(selectedGuide) + ".png"
    inImg = Image.open(path)
    inImg = inImg.resize((side, side), Image.ANTIALIAS) # image resize
    tkimage = ImageTk.PhotoImage(inImg)
    return tkimage

# Progress Bar Resources
progress = 90 # intialize
def addProgBar(frame, actCols, actRow):
    global progress
    frame.progress_frame = ttk.LabelFrame(frame, text="Guide Level")
    frame.progress_frame.grid(column=1, columnspan=actCols, row=actRow)
    frame.progress_frame.grid_columnconfigure(0, weight=1)
    frame.progress_bar = ttk.Progressbar(frame.progress_frame, orient="horizontal", length=600, mode="determinate")
    frame.progress_bar["value"] = progress
    frame.progress_bar.grid(column=0, row=0, padx= 10)
# to update progress use `self.progress_bar["value"] = [some int 0 <= x <= 100]`

# Active Detail
activeDetail = "loc1"

# -------------------------------------------------------------------

# FULL APPLICATION CLASS
class Application(tk.Tk):  # class produces tk.Tk window

    def __init__(self):
        tk.Tk.__init__(self) # constructing tk.Tk window for Application
        self.title("Interactive Guide") # set tk.Tk window title bar

        self.container = tk.Frame(self)  # initiating parent container for all pages
        self.container.pack(side="top", fill="both", expand=True) # setting full window stretch

        self.container.grid_rowconfigure(0, weight=1) # allowing stretch fit
        self.container.grid_columnconfigure(0, weight=1) # allowing stretch fit

        self.frames = {} # initiate frames

        # producing every frame (page)
        self.renderFrames([LandingPage, GuideSelectPage, MapPage, LocationDetails]) # Render all first time (except Traveling)
        self.new_frame(LandingPage) # initial frame set to LandingPage
    
    def renderFrames(self, frameList):
        for aFrame in frameList:
            frame = aFrame(self.container, self) # creating frame in Application()'s self.container with value of aFrame
            self.frames[aFrame] = frame # adding key aFrame with value frame for each page
            frame.grid(row=0, column=0, sticky="nsew") # covering full window w/ each frame (each frame is stacked over same space)

    def new_frame(self, controller):
        frame = self.frames[controller] # seleting frame value from frames based on controller key
        frame.tkraise() # pushes selected frame to top of stack

# -------------------------------------------------------------------

# GLOBAL for frames
def frame_management(self, activeCols, activeRows):
    self.grid(row=0, column=0, sticky="nsew")
    numGridCols = activeCols + 2 # + 2 for margin left and right
    numGridRows = activeRows + 2 # + 2 for margin top and bottom
        # weighted sides to center actual content in center of window
    self.grid_columnconfigure(0, weight=1)
    self.grid_columnconfigure(numGridCols-1, weight=1) # last column
    self.grid_rowconfigure(0, weight=1)
    self.grid_rowconfigure(numGridRows-1, weight=1) # last row

# -------------------------------------------------------------------

class LandingPage(tk.Frame): # class produces tk.Frame frame

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent) # constructing tk.Frame frame for LandingPage

        # Frame Grid Management
        activeGridCols = 4
        activeGridRows = 2
        frame_management(self, activeGridCols, activeGridRows) # remember to start all grid positions from 1 not standard 0

        self.configure(bg="#ccc") # set full landing background color

        self.landing_widgets(controller) # passing page controller

    def landing_widgets(self, controller): # recieving page controller
        # Title Image
        self.wValue = maxWidth # set width here
        self.titlePhoto = Image.open("./photos/surreal.jpg") # import photo
        self.wPercent = (self.wValue / float(self.titlePhoto.size[0])) # calc ratio of desired width from original width
        self.hValue = int((float(self.titlePhoto.size[1]) * float(self.wPercent))) # calc appropriate height to preserve aspect ratio
        self.titlePhoto = self.titlePhoto.resize((self.wValue, self.hValue), Image.ANTIALIAS) # applying desired resize and antialiasing
        self.tkTitlePhoto = ImageTk.PhotoImage(self.titlePhoto) # applying resized photo to PIL format
            # Image Canvas
        self.title_c = tk.Canvas(self, width=self.wValue, height=self.hValue, highlightthickness=0) # creating canvas same size as image
        self.title_c.grid(column=1, columnspan=4, row=1) # assigning grid position
        self.title_c.create_image(0, 0, image=self.tkTitlePhoto, anchor=tk.NW) # place image covering canvas

        # Title Message
        self.title_c.create_text(self.wValue/2 + 2, self.hValue/2 + 1.5, fill="black", font="Arial 40 bold", text="Interactive Guide") # adding text shadow
        self.title_c.create_text(self.wValue/2, self.hValue/2, fill="white", font="Arial 40 bold", text="Interactive Guide") # adding text to center
        # Subtitle Message
        self.title_c.create_text(self.wValue/2 + 1, self.hValue*3/5 - 1, fill="black", font="Arial 16", text="Elle, Jacob, Peter") # adding text shadow
        self.title_c.create_text(self.wValue/2, self.hValue*3/5, fill="white", font="Arial 16", text="Elle, Jacob, Peter") # adding text slightly off center

        # Enter Button
            # lambda: small anonymous function; `lambda arguments : expression`
            # lambda: useful as shorthand passing args inside `command=`
        self.enter = tk.Button(self, text="Enter", bg="white", pady=2, padx=10, cursor="hand2", command=lambda: controller.new_frame(GuideSelectPage))
        self.enter.grid(column=2, row=2, pady=10)

        # Quit Button
        self.quit_button = tk.Button(self, text="Quit", fg="red", bg="white", pady=2, padx=10, cursor="hand2", command=self.quit)
        self.quit_button.grid(column=3, row=2, pady=10)

# -------------------------------------------------------------------

class GuideSelectPage(tk.Frame): # class produces tk.Frame frame
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent) # constructing tk.Frame frame for LandingPage

        # Frame Grid Management
        self.activeGridCols = 1
        self.activeGridRows = 4
        frame_management(self, self.activeGridCols, self.activeGridRows) # remember to start all grid positions from 1 not standard 0

        self.guide_select_widgets(controller)

    def guideWasChoosen(self, guideNum, controller):
        global selectedGuide
        selectedGuide = guideNum
        controller.renderFrames([Traveling]) # render/execute Traveling (starts .after() countdown)
        controller.new_frame(Traveling) # lift Traveling frame

    def guide_select_widgets(self, controller):
        # Title
        self.titleFont = Font(family='Helvetica', size=20, weight='bold')
        self.title = tk.Label(self, text="Guide Select", font=self.titleFont)
        self.title.grid(column=1, row=1)
        self.subtitleFont = Font(family='Helvetica', size=12, weight='normal')
        self.subtitle = tk.Label(self, text="Chose a personal guide from the options below", font=self.subtitleFont)
        self.subtitle.grid(column=1, row=2)

        # Guide Select Options
        self.guide_options = ttk.LabelFrame(self, text="Guide options")
        self.guide_options.grid(column=1, row=3)
        # Creating Guide Select Image List
        self.guideImages = [] # initiate guide img list
        for i in range(8): # range(numIntendedGuides)
            path = "./photos/guide" + str(i+1) + ".png"
            inImg = Image.open(path)
            inImg = inImg.resize((120, 120), Image.ANTIALIAS) # image resize
            tkimage = ImageTk.PhotoImage(inImg)
            self.guideImages.append(tkimage)
        # Rendering Guide Options
        for i in range(len(self.guideImages)):
            self.guide_option = ttk.LabelFrame(self.guide_options, text="Guide " + str(i+1))
            if i < 4:
                self.guide_option.grid(column=i, row=0, pady=5, padx=5)
            else:
                self.guide_option.grid(column=i-4, row=1, pady=5, padx=5)
            self.guide_img = tk.Label(self.guide_option, image=self.guideImages[i])
            self.guide_img.grid(column=0, row=0)
            self.guide_select_btn = tk.Button(self.guide_option, text="Select", bg="white", pady=2, padx=10, cursor="hand2", command=lambda i=i: self.guideWasChoosen((i+1), controller)) # `i=i` necessary to get correct varaible reference
            self.guide_select_btn.grid(column=0, row=1, pady=5, padx=5)

        # Return to Landing
        self.return_to = tk.Button(self, text="Return", bg="white", pady=2, padx=10, cursor="hand2", command=lambda: controller.new_frame(LandingPage))
        self.return_to.grid(column=1, row=4, pady=5, padx=5)

# -------------------------------------------------------------------

class Traveling(tk.Frame): # class produces tk.Frame frame
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent) # constructing tk.Frame frame for Traveling

        # Frame Grid Management
        self.activeGridCols = 1
        self.activeGridRows = 1
        frame_management(self, self.activeGridCols, self.activeGridRows) # remember to start all grid positions from 1 not standard 0

        self.traveling_widgets(controller) # Apply widgets to frame

        self.varController = controller # Allows pass on of controller

        self.after(2000, self.arrived) # Wait 2 seconds before "arriving" at MapPage

    def arrived(self):
        self.varController.renderFrames([MapPage]) # render Map Page
        self.varController.new_frame(MapPage) # lift Map Page

    def traveling_widgets(self, controller):
        self.spaceship = tk.Label(self, text="london bus moves across the screen from left to right")
        self.spaceship.grid(column=1, row=1)


# -------------------------------------------------------------------

class MapPage(tk.Frame): # class produces tk.Frame frame
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent) # constructing tk.Frame frame for LandingPage

        # Frame Grid Management
        self.activeGridCols = 2
        self.activeGridRows = 4
        frame_management(self, self.activeGridCols, self.activeGridRows) # remember to start all grid positions from 1 not standard 0

        self.map_widgets(controller)

        self.varController = controller # necessary to pass controller for mapLocClick
		
    def drawMarkers(self):
        self.markerPhoto = Image.open("./photos/pin2.png")
        self.markerPhoto = self.markerPhoto.resize((40, 40), Image.ANTIALIAS)
        self.tkMarkerPhoto = ImageTk.PhotoImage(self.markerPhoto)
        for key in mapMarkers:
            mark = mapMarkers[key]
            self.map_c.create_image(mark[0]-20, mark[1]-20, image=self.tkMarkerPhoto, anchor=tk.NW) # place image covering canvas
			
    def mapLocClick(self, event):
        global activeDetail
        clickX = event.x
        clickY = event.y
        for key in mapMarkers:
            mark = mapMarkers[key]
            insideX = (clickX >= mark[0]-15) and (clickX <= mark[0]+15)
            insideY = (clickY >= mark[1]-15) and (clickY <= mark[1]+15)
            if insideX and insideY:
                activeDetail = key
                self.varController.renderFrames([LocationDetails])
                self.varController.new_frame(LocationDetails)

    def map_widgets(self, controller):
        # Place Title
        self.titleFont = Font(family='Helvetica', size=20, weight='bold')
        self.title = tk.Label(self, text="Welcome to the 9th Circle of Hell", font=self.titleFont)
        self.title.grid(column=1, columnspan=2, row=1)

        # Progress Bar
        addProgBar(self, self.activeGridCols, 2) # global function (frame, actCols, actRow)

        # Map
        self.wValue = 800  # set width here
        self.mapPhoto = Image.open("./photos/fake-map2.jpg") # import photo
        #self.wPercent = (self.wValue / float(self.titlePhoto.size[0])) # calc ratio of desired width from original width
        #self.hValue = int((float(self.titlePhoto.size[1]) * float(self.wPercent))) # calc appropriate height to preserve aspect ratio
        self.hValue = 300
        self.mapPhoto = self.mapPhoto.resize((self.wValue, self.hValue), Image.ANTIALIAS) # applying desired resize and antialiasing
        self.tkMapPhoto = ImageTk.PhotoImage(self.mapPhoto) # applying resized photo to PIL format
            # Image Canvas
        self.map_c = tk.Canvas(self, width=self.wValue, height=self.hValue, highlightthickness=0, cursor="dotbox") # creating canvas same size as image
        self.map_c.grid(column=1, columnspan=2, row=3, pady=5) # assigning grid position
        self.map_c.create_image(0, 0, image=self.tkMapPhoto, anchor="nw") # place image covering canvas
            # Map Locations
        self.map_c.bind("<Button-1>", self.mapLocClick)
        self.drawMarkers()
        
        # Dialogue Box
        self.dialogue = ttk.LabelFrame(self, text="Guide")
        self.dialogue.grid(column=1, columnspan=2, row=4)
            # Guide Image
        self.guideRef = guideGet(100) # need guide_ref to maintain reference, single function call gets trashed after
        self.guide = tk.Label(self.dialogue, image=self.guideRef)
        self.guide.grid(column=0, row=0, pady=5, padx=5)
            # Text
        self.guide_says = tk.Text(self.dialogue, width=50, height=5)
        self.guide_message = "Placeholder text that this mad lad could say. It's going to go on and on because I need to test text wrap so this looks ok. This length should do I think."
        self.guide_says.insert("end", self.guide_message)
        self.guide_says.config(wrap="word", state="disabled")
        self.guide_says.grid(column=1, row=0)
            # Options
        self.options = ttk.LabelFrame(self.dialogue, text="Options")
        self.options.grid(column=2, row=0, pady=5, padx=5)
                # Next Button
        self.next_button = tk.Button(self.options, text="Continue", bg="white", pady=2, padx=10, cursor="hand2")
        self.next_button.grid(column=0, row=0, pady=0, padx=4)
                # Return Button
        self.reselect = tk.Button(self.options, text="Reselect", bg="white", pady=2, padx=10, cursor="hand2", command=lambda: controller.new_frame(GuideSelectPage))
        self.reselect.grid(column=0, row=1, pady=4, padx=4)

# -------------------------------------------------------------------

class LocationDetails(tk.Frame): # class produces tk.Frame frame
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent) # constructing tk.Frame frame for LandingPage

        # Frame Grid Management
        self.activeGridCols = 3
        self.activeGridRows = 2
        frame_management(self, self.activeGridCols, self.activeGridRows) # remember to start all grid positions from 1 not standard 0
        
        # Setting Active Location
        self.activeLocation = locations[activeDetail]
        self.activeQuiz = quizQs[activeDetail]
        self.addInfoList = self.activeLocation[3]

        # Widgets
        self.location_details_widgets(controller)

        self.varController = controller # necessary to pass controller for mapLocClick

    def imgLocClick(self, event):
        clickX = event.x
        clickY = event.y
        for i in range(len(self.addInfoList)):
            insideX = (clickX >= self.addInfoList[i][0][0]-7) and (clickX <= self.addInfoList[i][0][0]+7)
            insideY = (clickY >= self.addInfoList[i][0][1]-7) and (clickY <= self.addInfoList[i][0][1]+7)
            if insideX and insideY:
                self.guide_says.config(state="normal")
                self.guide_says.delete("1.0", "end")
                self.guide_says.insert("end", self.addInfoList[i][1])
                self.guide_says.config(state="disabled")

    def setIntroText(self):
        self.guide_says.config(state="normal")
        self.guide_says.delete("1.0", "end")
        self.guide_says.insert("end", self.activeLocation[2] + introNote)
        self.guide_says.config(state="disabled")
                
    def location_details_widgets(self, controller):
        # Progress Bar
        addProgBar(self, self.activeGridCols, 1) # global function (frame, actCols, actRow)

        # Location Image
        self.wValue = 450 # set width here
        self.hValue = 450 # set height here
        self.locPhoto = Image.open("./photos/" + self.activeLocation[1]) # import photo
        self.locPhoto = self.locPhoto.resize((self.wValue, self.hValue), Image.ANTIALIAS) # applying desired resize and antialiasing
        self.tkLocPhoto = ImageTk.PhotoImage(self.locPhoto) # applying resized photo to PIL format
            # Image Canvas
        #self.title_c = tk.Canvas(self, width=self.wValue, height=self.hValue, highlightthickness=0) # creating canvas same size as image
        self.loc_c = tk.Canvas(self, width=self.wValue, height=self.hValue, highlightthickness=0, cursor="tcross") # creating canvas same size as image
        self.loc_c.grid(column=1, columnspan=2, row=2, pady=10, padx=10) # assigning grid position
        self.loc_c.create_image(0, 0, image=self.tkLocPhoto, anchor=tk.NW) # place image covering canvas
        # Title Message
        self.loc_c.create_text(self.wValue/2 + 2, 40 + 1.5, fill="black", font="Arial 30 bold", text=self.activeLocation[0]) # adding text shadow to canvas
        self.loc_c.create_text(self.wValue/2, 40, fill="white", font="Arial 30 bold", text=self.activeLocation[0]) # adding title to canvas

        # Additional Info Points
        for addInfo in self.addInfoList:
            point = addInfo[0]
            self.loc_c.create_rectangle(point[0]-7, point[1]-7, point[0]+7, point[1]+7, fill="red", outline="white", width=2)
        self.loc_c.bind("<Button-1>", self.imgLocClick)
        
        # Dialogue Box
        self.dialogue = ttk.LabelFrame(self, text="Guide")
        self.dialogue.grid(column=3, row=2)
            # Guide Image
        self.guide_ref = guideGet(150) # need guide_ref to maintain reference, single function call gets trashed after
        self.guide = tk.Label(self.dialogue, image=self.guide_ref)
        self.guide.grid(column=0, row=0, pady=5, padx=5)
           # Options
        self.options = ttk.LabelFrame(self.dialogue, text="Options")
        self.options.grid(column=1, row=0, pady=5, padx=5)
                # Intro Button
        self.intro_button = tk.Button(self.options, text="Intro", bg="white", pady=2, padx=10, cursor="hand2", command=self.setIntroText)
        self.intro_button.grid(column=0, row=0, pady=(0,4), padx=4)
                # Quiz Button
        self.next_button = tk.Button(self.options, text="Take\nQuiz", bg="white", pady=2, padx=10, cursor="hand2")
        self.next_button.grid(column=0, row=1, pady=0, padx=4)
                # Return Button
        self.reselect = tk.Button(self.options, text="Return\nto Map", bg="white", pady=2, padx=10, cursor="hand2", command=lambda: controller.new_frame(MapPage))
        self.reselect.grid(column=0, row=2, pady=4, padx=4)
            # Text
        self.guide_says = tk.Text(self.dialogue, width=30, height=15)
        self.guide_says.insert("end", self.activeLocation[2] + introNote)
        self.guide_says.config(wrap="word", state="disabled")
        self.guide_says.grid(column=0, columnspan=2, row=1, pady=10, padx=10)

# -------------------------------------------------------------------

def main():
    program = Application() # create gui program
    program.mainloop() # start gui event loop

if __name__ == "__main__":
    main()
