""" Self-contained London Interactive Guide program """

# --IMPORT MODULES---------------------------------------------------

import tkinter as tk
from tkinter import ttk
from tkinter.font import Font

#!!!! IMPORTANT: User must install Pillow module for program to run.
from PIL import ImageTk, Image

import random


# --METADATA---------------------------------------------------------

__title__ = "London Interactive Guide"
__author__ = "Elle Miller, Jacob Merrick, Peter Fortier"
__credits__ = ["Elle Miller", "Jacob Merrick", "Peter Fortier"]
__profession__ = ["Student", "Student", "Student"]
__college__ = "St. Olaf College"
__location__ = "MN"
__course__ = "CSCI 121: Principles of Computer Science"
__professor__ = "Elizabeth Jensen"
__version__ = "3902u84538.09210rt3hds^134e8237w8r"
__status__ = "Production"
__date__ = "05/24/2021"
__vibe__ = "coolio beans"


# --NOTES------------------------------------------------------------

# lambda is a small anonymous function; `lambda arg1=arg1, arg2=arg2 : [expression using arg1 and arg2]`
# lambda is useful as a shorthand work-around for passing args inside `command=` function calls


# --GLOBAL RESOURCES-------------------------------------------------

# Window x-dimension resolution
maxWidth = 800

# Guide's map page text
mapNote = "\nNote: Use the '<<' and '>>' buttons at the right to navigate through this guide text."
mapGuideSays = [
    "Welcome to London! I'll be your guide today. Click on a map pin to visit one of the city's many wonderful sites.",
    "If you are feeling smart, visit a few locations and complete their quizzes to level me up!",
    "You'll be able to return back to this map page as many times as you'd like, so don't be afraid to click around.",
    "If you'd like to choose another guide, I wont be offended, but you will lose my current level progress. When you're sure, click the 'Reselect' button to the right to return to the guide select page."
]
# Supplimentary guide location detail text
introNote = " Use the '<<' and '>>' buttons below to navigate through location details."

# List of map marker coordinants/tuples
mapMarkers = { # Note: same keys as 'locations' and 'quizQs' dictionaries (except for dual locs, read below)
    "loc1loc13": (345,285), 
    "loc2loc14": (190,280), 
    "loc3": (340,170),
    "loc4": (300,293),
    "loc5": (515,245),
    "loc6": (25,325),
    "loc7": (240,290),
    "loc8": (238,220),
    "loc9": (140,225),
    "loc10": (25,200),
    "loc11": (600,235),
    "loc12": (390,260),
    "loc15": (505,115),
    "loc16": (420,235),
    "loc17": (570,255),
    "loc18": (585,215),
    "loc19": (200,300),
    "loc20": (335,305),
    "loc21": (75,75),
    "loc22": (50,100)
}

# General location information dictionary, key-value template given in line below
    # "locN": ["Place Name", "base-image-path", [info list]]
locations = { # Note: same keys as 'quizQs' dictionary
    "loc1": [
        "Big Ben",
        "big-ben",
        [
			"Welcome to Big Ben! Located at the Palace of Westminster, Big Ben is one of London’s most iconic landmarks. It was completed in 1859 and built in honor of Queen Victoria.",
			"The origin of its nickname is unknown but the most popular theories include Sir Benjamin Hall, who oversaw the installation of the bell, or Benjamin Caunt, a heavyweight boxing champion at that time.",
			"Big Ben remains one of the most popular attractions in London to this day.",
		]
    ],
    "loc2": [
        "Albert Memorial",
        "albert-memorial",
		[
			"Welcome to The Albert Memorial! It was commissioned by Queen Victoria in memory of her husband, Prince Albert.",
			"It took over ten years to complete and cost over £120,000. The Albert Memorial is located in Kensington Gardens on Albert Memorial Road opposite the Royal Albert Hall.",
			"It is one of London's most ornate monuments, designed by George Gilbert Scott.",
		]
    ],
    "loc3": [
        "British Museum",
        "british-museum",
		[
			"The British Museum, with a permanent collection of around eight million works, is one of the largest and most comprehensive museums in existence.",
			"It was established in 1753 by Irish physician and scientist Sir Hans Sloane making it the first public national museum in the world.",
			"The British Museum’s ownership of some of its most famous artifacts originating in other countries have been the source of international controversy, especially in the case of the Rosetta Stone of Egypt.",
		]        
    ],
    "loc4": [
        "Buckingham Palace",
        "buckingham-palace",
		[
			"Featuring an impressive 775 rooms and 39 acres of grounds, Buckingham Palace is the official residence and administrative headquarters of the British monarchy.",
			"Built in 1703 the palace was originally constructed for Duke Buckingham before being purchased by King George III in 1761 as a private residence for Queen Charlotte.",
			"Be sure to stop by to see the Changing of the Guard, which happens outside the palace at 10:45 and usually lasts around 45 minutes!",
		]
    ],
    "loc5": [
        "Globe Theatre",
        "globe-theatre",
		[
			"Welcome to the Globe Theater, home of Shakespeare’s plays!",
			"The original building burned down during a performance of Henry VIII due to a theatrical cannon misfiring and igniting the wooden beams and thatching. It was rebuilt the following year.",
			"The current Globe was built based off of the design of the original and is located approximately 750 feet from the site of the original theatre.",
			"Be sure to get tickets to the next performance!"
		]
    ],
    "loc6":[
        "Hampton Court Palace",
        "hampton-court-palace",
		[
			"Originally built in 1514 for Cardinal Thomas Woolsey, the Palace was then passed to King Henry VIII who saw it as one of his favorite residences.",
			"King George II was the last member of royalty to live in the Palace before it was opened up to the public.",
			"Today it’s one of London’s most popular tourist attractions, offering a wide variety of tours of the Palace and its gardens.",
			"With a variety of events happening here year-round, you’re sure to find an activity to enjoy!"
		]
    ],
    "loc7" :[
        "Harrods",
        "harrods",
		[
			"Welcome to Harrods, one of the largest and most famous departments in Europe! It is located on Brompton Road and occupies an area covering 1.1 million square feet.",
			"The shop has 330 departments and 23 restaurants. Up to 300,000 customers visit the shop on peak days and it is run by more than 5,000 staff members from over 50 different countries.",
			"Harrods is owned by the state of Qatar through the nation's sovereign wealth fund.",
			"The store previously held a number of royal warrants before the owner burned them, claiming that they were a curse."
		]
    ],
    "loc8" :[
        "Hyde Park",
        "hyde-park",
		[
			"Hyde Park is the largest of the four Royal Parks that form a chain from the entrance of Kensington Palace through past the Entrance to Buckingham Palace.",
			"The Park was established by Henry VIII in 1536. It was opened to the public in 1637 and quickly became incredibly popular.",
			"The park is known for the protests held there including suffragettes and the Stop The War Coalition. Be sure to check out the Winter Wonderland hosted annually since 2007!"
		]
    ],
    "loc9" :[
        "Kensington Palace",
        "kensington-palace",
		[
			"Welcome to Kensington Palace, residence of the British Royal Family since the 17th century! Today the State Rooms are open to the public and all profits go toward Historic Royal palaces, a nonprofit dedicated to managing the UK’s unoccupied palaces.",
			"King William III and Queen Mary II were the first royalty to live there, purchasing the palace in 1689. Since then a number of other royalty have lived there including Queen Anne, King George I, and King George II.",
			"The Palace displays many paintings and other objects from the Royal Collection.",
			"The Palace is an excellent tourist attraction offering 4 routes through the Palace, interactive experiences, and exhibits about the people who have lived there."
		]
    ],
    "loc10" :[
        "Kew Gardens",
        "kew-gardens",
		[
			"Welcome to Kew Gardens! This is a beautiful botanical garden featuring an Arboretum, cafes, and an incredible plant collection that is among the most diverse in the world.",
			"Founded in 1840, the garden has a living collection of around 27,000 species and 8.5 million preserved plant and fungi specimens.",
			"Additionally, the library contains more than 750,000 volumes and more than 175,000 prints and drawings of plants.",
			"The Gardens are one of London’s top tourist attractions and a World Heritage Site."
		]
    ],
    "loc11" :[
        "London Bridge",
        "london-bridge",
		[
			"Welcome to the Tower Bridge, frequently confused with the London Bridge! Built in 1894 across the River Thames, the Bridge has become a world-famous landmark of London.",
			"The bridge deck is free to access while the bridge’s twin towers, high-level walkways, and Victorian engine rooms have an admission charge.",
			"Construction of the Bridge took eight years, 432 construction workers, and around £1,184,000.",
		]
    ],
    "loc12" :[
        "London Eye",
        "london-eye",
		[
			"Welcome to London Eye, a giant observation wheel that quickly became one of London’s most iconic attractions when it opened in 2000!",
			"At 443 feet high, the London Eye is currently the fourth-largest Ferris wheel in the world.",
			"The Eye has 32 capsules (one for each of the city's 32 boroughs) but they’re numbered 1-33 to avoid the unlucky number 13.",
			"Be sure to take a ride on the London Eye which takes 30 minutes, and it travels at a speed of about 0.6 miles per hour!"
		]
    ],
    "loc13" :[
        "Parliament",
        "parliament",
		[
			"Welcome to the seat of the UK government, Parliament.",
			"The Houses of Parliament are the official meeting place for parliament, but as the UK is a constitutional monarchy, they are technically owned by the reigning monarch.",
			"The Houses of Parliament has over 100 staircases and 3 miles of corridors to explore. Parliament is also home of the infamous clock tower Big Ben.",
		]
    ],
    "loc14" :[
        "Royal Albert Hall",
        "royal-albert-hall",
		[
			"The Royal Albert Albert Hall is a concert hall that can seat 5,272 people.",
			" The Hall was opened in 1871 by Queen Victoria and has hosted the world's leading artists from a variety of performance genres.",
			"It was originally supposed to be called the Central Hall of Arts and Sciences but the name was changed to the Royal Albert Hall of Arts and Sciences in memory of the Queen’s husband, Prince Albert, who had died 6 years earlier.",
			"It’s the venue for the Proms concert, which has been held annually since 1941, along with more than 390 shows held in the main auditorium annually. An additional 400 events are held annually in the non-auditorium spaces."
		]
    ],
    "loc15" :[
        "St. Paul's Cathedral",
        "st-pauls-cathedral",
		[
			"St. Paul’s Cathedral is an Anglican cathedral located on Ludgate Hill, the highest point in the city.",
			"It was designed by Sir Christopher Wren as part of the major rebuilding program after the Great Fire of London.",
			"Services held at St. Paul’s Cathedral have included the funerals of Winston Churchill and Margaret Thatcher, jubilee celebrations for Queen Victoria, and the wedding between Prince Charles and Lady Diana Spencer.",
			"The Cathedral is open to the public and hosts hourly prayer and daily services. The tourist entry fee at the door is £20 for adults, but no charge is made to worshippers attending advertised services."
		]
    ],
    "loc16" :[
        "The National Theatre",
        "the-national-theatre",
		[
			"The National Theatre is one of the UK’s three most prominent publicly funded performing arts venues, along with the Royal Opera House and the Royal Shakespeare Company.",
			"The Theatre was founded in 1963 by Laurence Oliver and given permission to add the prefix Royal in 1988 though the full name is rarely used.",
			"Until 1976, the Theatre was located in the Old Vic theatre in Waterloo. The current building is next to the Thames in the South Bank area of London.",
			"The National Theatre's foyers are open to the public, with a large theatrical bookshop, restaurants, bars and exhibition spaces."
		]
    ],
    "loc17" :[
        "The Shard",
        "the-shard",
		[
			"Welcome to The Shard, also known as the Shard of Glass, is a 72-story skyscraper located in Southwark, London.",
			"It was designed by the Italian architect Renzo Piano and forms part of the Shard Quarter development.",
			"It is 1,016 feet tall, the tallest building in the UK, and the seventh tallest building in Europe.",
			"The Shard’s construction took place from 2009 to 2012 and it’s observation deck was opened February 1, 2013."
		]
    ],
    "loc18" :[
        "Tower of London",
        "tower-of-london",
		[
			"Welcome to the Tower of London, a popular site rich with history and attractions! The Tower has been a tourist destination since at least the Elizabethan period and continues to attract millions of visitors each year.",
			"It was originally built by William the Conqueror at the centre of his London fortress in the 1070s and over time it’s purpose has changed to suit the times.",
			"So far that has included a prison, fortress, palace, Royal Mint, the Royal Armouries and even a zoo.",
			"The Tower is currently home to the Crown Jewels, Yeomen Warders and its legendary guardians, and the six ravens which the kingdom is rumored to fall without."
		]
    ],
    "loc19" :[
        "Victoria and Albert Museum",
        "victoria-and-albert-museum",
		[
			"Welcome to the Victoria and Albert Museum, often abbreviated to V&A. It is the world’s largest museum of applied and decorative arts and design and sculpture, housing over 2.27 million objects.",
			"The museum covers 12.5 acres of land and 145 galleries. The collection spans 5,000 years of art and contains works from a variety of cultures including Europe, North America, North Africa, and Asia.",
			"Additionally, the museum has the world’s largest collection of Italian Renaissance pieces outside of Italy.",
		]
    ],
    "loc20" :[
        "Westminster Abbey",
        "westminster-abbey",
		[
			"Westminster Abbey is a mainly gothic abbey church and one of the UK’s most notable religious buildings.",
			"Originally the building was used as a Benedictine monastic church until 1539 when it was dissolved. Construction of the current church began in 1245 on the orders of King Henry III.",
			"A total of 16 royal weddings have happened inside Westminster Abbey as well as every coronation since William the Conqueror in 1066.",
		]
    ],
    "loc21" :[
        "London Bus",
        "london-bus",
		[
			"You found the London Bus! Nicely done. Come take a ride. You've earned it.",
			"In 1941, Miss Phyllis Thompson became the first woman licensed to drive a double-decker vehicle in the United Kingdom.",
			"The majority of buses in London are double-deckers and they have become a national symbol for England.",
			"The majority of double-decker buses in the UK are between 31 ft 2 in and 36 ft 5 in long, the latter being more common since the mid-1990s."
		]
    ],
    "loc22" :[
        "London Phone Booth",
        "london-phone-booth",
		[
			"Fantastic! You've stubbled upon an old London Phone Booth. Let's take a look!",
			"The red phone box was originally designed by Sir Giles Gilbert Scott.",
			"Starting in 1926, phone booths were emblazoned with a prominent crown, representing the British government.",
			"The production of them ended in 1985 but many still stand in Britain today."
		]
    ]
}

# Quiz questions for every location dictionary, key-value template given in line below
    # "locN": [ ["Q1", {"a1": [bool], "a2": [bool], "a3": [bool]}] ]
quizQs = { # Note: same keys as 'locations' dictionary
    "loc1": [
        ["Who was Big Ben named after?", {"King Benjamin": False, "Unknown": True, "Duke of Benjamin": False}],
        ["When was Big Ben Built?", {"1859": True, "1873": False, "1881": False}],
        ["Where is Big Ben located?", {"the Palace of Westminster": True, "Carnaby Street": False, "Oxford Street": False}] # do something like `if option` to determine correctness
    ],
    "loc2": [
        ["Who designed the Memorial?", {"option1": False, "George Gilbert Scott": True, "option3": False}],
        ["How much did it cost to build?", {"£120,000": True, "£90,000": False, "£200,000": False}],
        ["Where is the Memorial located?", {"Kensington Gardens": True, "Botanic Gardens": False, "Wrest Park": False}]
    ],
    "loc3": [
        ["Which artifact can be found in the British Museum?", {"Terracotta Army": False, "The Rosetta Stone": True, "Dead Sea Scrolls": False}],
        ["Who established the British Museum?", {"Sir Hans Sloane": True, "Sir Percival": False, "The Duke of Hastings": False}],
        ["How many works are in the collection?", {"eight million": True, "five million": False, "two million": False}]
    ],
    "loc4" : [
        ["Who was the palace originally built for?", {"King Henry": False, "Duke Buckingham": True, "Lady Whistledown": False}],
        ["What event happens outside the palace?", {"Changing of the Guard": True, "Royal Gardens Tour": False, "Art Festival": False}],
        ["How many rooms does the palace have?", {"775": True, "760": False, "755": False}]

    ],
    "loc5" :[
        ["How many Globe Theaters have existed?", {"Two": False, "Three": True, "Five": False}],
        ["How did the original burn down?", {"Canon misfiring": True, "Candle fire": False, "It didn't": False}],
        ["Who’s plays are staged in the Globe Theater?", {"Shakespeare": True, "Aristophanes": False, "William Kemp": False}]
    ],
    "loc6" :[
        ["Who was the last member of royalty to live at the Palace?", {"Queen Elizabeth": False, "King George II": True, "Queen Charlotte": False}],
        ["Who was the Palace originally built for", {"Cardinal Thomas Woolsey": True, "The Pope": False, "option3": False}],
        ["Is it currently open to the public?", {"Yes": True, "No": False, "Unsure": False}]
    ],
    "loc7" :[
        ["How many restaurants are in Harrods?", {"33": False, "23": True, "43": False}],
        ["What state owns the department store?", {"Qatar": True, "Germany": False, "United States": False}],
        ["How much space does Harrods take up?", {"1.1 million sq ft": True, "300,000 sq ft": False, "900,000 sq ft": False}]
    ],
    "loc8" :[
        ["Who established the Park?", {"James II": False, "Henry VIII": True, "Mary II": False}],
        ["When was the Park opened to the public?", {"1637": True, "1536": False, "1598": False}],
        ["What event is hosted annually?", {"Winter Wonderland": True, "Winter Carnival": False, "Winter Fair": False}]
    ],
    "loc9" :[
        ["Who was the first Queen to live in Kensington Palace?", {"Queen Anne": False, "Queen Mary II": True, "Queen Elizabeth I": False}],
        ["How many different routes are available for visitors to walk through?", {"4": True, "5": False, "6": False}],
        ["Who manages the Palace?", {"A nonprofit": True, "The Royal Family": False, "Parliament": False}]
    ],
    "loc10" :[
        ["How many preserved plant and fungal specimens does the Gardens have?", {"8 million": False, "8.5 million": True, "7.5 million": False}],
        ["When was it established?", {"1840": True, "1850": False, "1860": False}],
        ["How big is the living collection?", {"27,000": True, "30,000": False, "35,000": False}]
    ],
    "loc11" :[
        ["Which part of the Bridge is accessible for free?", {"Twin towers": False, "The bridge deck": True, "Victorian engine rooms": False}],
        ["How many workers did it take to build?", {"432": True, "433": False, "434": False}],
        ["How long did it take to build?", {"8 years": True, "A decade": False, "9 years": False}]
    ],
    "loc12" :[
        ["What rank is the London Eye in terms of largest Ferris wheel?", {"Second": False, "Fourth": True, "Third": False}],
        ["How many capsules are there?", {"32": True, "42": False, "52": False}],
        ["How long does a ride take?", {"30 minutes": True, "45 minutes": False, "1 hour": False}]
    ],
    "loc13" :[
        ["What other iconic British landmark is located here?", {"London Eye": False, "Big Ben": True, "The Shard": False}],
        ["Who owns Parliament?", {"The monarchy": True, "The public": False, "The government": False}],
        ["How many staircases are there?", {"100": True, "150": False, "200": False}]
    ],
    "loc14" :[
        ["How many people can the Hall seat?", {"4,636": False, "5,272": True, "6,989": False}],
        ["How many total events are held annually?", {"790": True, "690": False, "590": False}],
        ["What was the Hall’s original name?", {"Central Hall of Arts and Sciences": True, "Orchestra Hall": False, "Christiansen Hall of Music": False}]
    ],
    "loc15" :[
        ["Where is the Cathedral located?", {"Blackheath Ridge": False, "Ludgate Hill": True, "Stanmore Hill": False}],
        ["What denomination is the Cathedral affiliated with?", {"Anglican": True, "Catholic": False, "Lutheran": False}],
        ["How much does it cost for worshippers to attend services?", {"Free": True, "£40": False, "£20": False}]
    ],
    "loc16" :[
        ["Who founded the theatre?", {"Queen Victoria": False, "Laurence Oliver": True, "Winston Churchill": False}],
        ["When was the prefix added?", {"1988": True, "1977": False, "1966": False}],
        ["Where was the original Theatre located?", {"Waterloo": True, "Brent": False, "Harrow": False}]
    ],
    "loc17" :[
        ["How many stories does The Shard have?", {"62": False, "72": True, "52": False}],
        ["Who was it designed by?", {"Renzo Piano": True, "Frank Wright": False, "Zaha Hadid": False}],
        ["What rank is it for height in Europe?", {"7th": True, "5th": False, "9th": False}]
    ],
    "loc18" :[
        ["Who built the Tower of London?", {"John the Conqueror": False, "William the Conqueror": True, "James the Conqueror": False}],
        ["When was the Tower originally built?", {"1070s": True, "1270s": False, "1080s": False}],
        ["According to legend, how many ravens must stay at the Tower?", {"Six": True, "Seven": False, "One": False}]
    ],
    "loc19" :[
        ["What abbreviation is commonly used?", {"V&AM": False, "V&A": True, "There is no abbreviation": False}],
        ["How many galleries are there?", {"145": True, "95": False, "125": False}],
        ["How many years of art does it span?", {"5,000": True, "6,000": False, "7,000": False}]
    ],
    "loc20" :[
        ["What was the building originally used for?", {"It's always been an abbey": False, "Benedictine monastic church": True, "option3": False}],
        ["How many royal weddings have happened at the Abbey?", {"16": True, "15": False, "14": False}],
        ["Since what year have all royal coronations been held in the Abbey?", {"1066": True, "1265": False, "1156": False}]
    ],
    "loc21" :[
        ["What color is associated with the buses?", {"Yellow": False, "Red": True, "Blue": False}],
        ["In what year did the first woman drive a double-decker vehicle?", {"1941": True, "1901": False, "1889": False}],
        ["Approximetly how long are the buses on average?", {"36ft 5in": True, "36ft": False, "37ft": False}]
    ],
    "loc22" :[
        ["What symbol was emblazoned onto the phone booths?", {"Rose": False, "Crown": True, "Swan": False}],
        ["What color is associated with them?", {"Red": True, "Black": False, "Blue": False}],
        ["Who designed them?", {"Sir Giles Gilbert Scott": True, "Benjamin Franklin": False, "Queen Victoria": False}]  
    ]
}

# Guide select resources
selectedGuide = 1 # globally intialize
def guideGet(side):
    ''' Returns active guide image '''
    path = "./photos/guide" + str(selectedGuide) + ".png"
    inImg = Image.open(path)
    inImg = inImg.resize((side, side), Image.ANTIALIAS) # image resize
    tkimage = ImageTk.PhotoImage(inImg)
    return tkimage

# Progress bar resources
progress = 0 # globally intialize
guideLevel = 0 # globally intialize
def addProgBar(root, actCols, actRow):
    ''' Displays progress bar at desired grid position '''
    global progress
    root.progress_frame = ttk.LabelFrame(root, text="Guide: Level " + str(guideLevel))
    root.progress_frame.grid(column=1, columnspan=actCols, row=actRow)
    root.progress_frame.grid_columnconfigure(0, weight=1)
    root.progress_bar = ttk.Progressbar(root.progress_frame, orient="horizontal", length=600, mode="determinate")
    root.progress_bar["value"] = progress
    root.progress_bar.grid(column=0, row=0, padx= 10)

# Active location
activeLoc = "loc1" # globally intialized (intiated with usable key for first render)


# --APPLICATION SUBCLASS---------------------------------------------

class Application(tk.Tk):
    ''' This class acts as the full Application. 
        Application is a subclass of the tk.Tk class. '''

    def __init__(self):
        ''' Application constructor. '''

        # Constructor/intializor for parent tk.Tk class. Note: super() is an equivalent option to tk.Tk
        tk.Tk.__init__(self)

        # Set window title
        self.title("London Interactive Guide")

        # Creating full application container frame (spans window)
        self.container = tk.Frame(self)
        self.container.pack(side="top", fill="both", expand=True)
        self.container.grid_rowconfigure(0, weight=1) # allowing complete stretch fit
        self.container.grid_columnconfigure(0, weight=1) # allowing complete stretch fit

        # Initiate frames dictionary
        self.pages = {}
        # Rendering every frame (page) except Traveling
        self.renderPages([LandingPage, GuideSelectPage, MapPage, LocationDetails])
        # Set intial page to LandingPage
        self.viewPage(LandingPage)
    

    def renderPages(self, pageList):
        ''' Renders passed pages (pageList). '''

        for pageClass in pageList: 
            # classInstance = className(root frame, root frame's parent--also tk window in this case)
            pageInstance = pageClass(self.container, self)
            # classDictionary[className] = classInstance
            self.pages[pageClass] = pageInstance
            # classInstance fitting full self.container frame
            pageInstance.grid(row=0, column=0, sticky="nsew") # covering full window w/ each frame (Note: each frame is stacked over same space)


    def viewPage(self, page):
        ''' Navigates to new page (frame). '''

        activePage = self.pages[page]
        # Push selected frame to top of stack
        activePage.tkraise()


# --GLOBAL FOR FRAMES------------------------------------------------

def manageGridBorder(self, activeCols, activeRows):
    ''' Sets page grid with weighted margins; Centers relevant content in middle of frame. '''

    self.grid(row=0, column=0, sticky="nsew")
    numGridCols = activeCols + 2 # + 2 for margin left and right
    numGridRows = activeRows + 2 # + 2 for margin top and bottom
    # Add weight to edge columns and borders to center frame content in window
    self.grid_columnconfigure(0, weight=1)
    self.grid_columnconfigure(numGridCols-1, weight=1) # last column
    self.grid_rowconfigure(0, weight=1)
    self.grid_rowconfigure(numGridRows-1, weight=1) # last row


# ----LANDINGPAGE SUBCLASS-------------------------------------------

class LandingPage(tk.Frame):
    ''' The landing page for an instance of Application().
        LandingPage is a subclass of the tk.Frame class. '''

    def __init__(self, rootContainer, appReference):
        ''' Landing page constructor. '''

        # Constructor/intializor for parent tk.Frame class. Note: super() is an equivalent option to tk.Frame
        tk.Frame.__init__(self, rootContainer) 

        # Frame grid management
        activeGridCols = 4
        activeGridRows = 2
        manageGridBorder(self, activeGridCols, activeGridRows)
        # Note: remember to start all grid positions from 1 not standard 0

        # Render default widgets
        self.landing_widgets(appReference)


    def landing_widgets(self, appReference):
        ''' Renders default landing page widgets. '''

        # Title Image
            # Image
        self.wValue = maxWidth # set width here
        self.titlePhoto = Image.open("./photos/londonskyline.png") # import
        self.wPercent = (self.wValue / float(self.titlePhoto.size[0])) # calc new height percentage for maintaining aspect ratio from defined new width
        self.hValue = int((float(self.titlePhoto.size[1]) * float(self.wPercent))) # calc new height to preserve aspect ratio
        self.titlePhoto = self.titlePhoto.resize((self.wValue, self.hValue), Image.ANTIALIAS) # applying desired resize and antialiasing
        self.tkTitlePhoto = ImageTk.PhotoImage(self.titlePhoto) # applying resized photo to PIL format for use with tkinter
            # Text Image
        self.titleText = Image.open("./photos/londonskyline-text.png")
        self.wTPercent = (self.wValue / float(self.titleText.size[0])) # calc new height percentage for maintaining aspect ratio from defined new width
        self.hTValue = int((float(self.titleText.size[1]) * float(self.wTPercent))) # calc new height to preserve aspect ratio
        self.titleText = self.titleText.resize((self.wValue, self.hTValue), Image.ANTIALIAS) # applying desired resize and antialiasing
        self.tkTitleText = ImageTk.PhotoImage(self.titleText) # applying resized photo to PIL format for use with tkinter
            # Canvas
        self.title_c = tk.Canvas(self, width=self.wValue, height=self.hTValue, highlightthickness=0) # creating canvas same size as image
        self.title_c.grid(column=1, columnspan=4, row=1)
        self.title_c.create_image(0, 0, image=self.tkTitlePhoto, anchor="nw")
        self.title_c.create_image(0, 0, image=self.tkTitleText, anchor="nw")
        
        # Enter Button
        self.enter = tk.Button(self, text="Enter", bg="white", pady=2, padx=10, cursor="hand2", command=lambda: appReference.viewPage(GuideSelectPage))
        self.enter.grid(column=2, row=2, pady=10)

        # Quit Button
        self.quit_button = tk.Button(self, text="Quit", fg="red", bg="white", pady=2, padx=10, cursor="hand2", command=self.quit)
        self.quit_button.grid(column=3, row=2, pady=10)


# --GUIDESELECTPAGE SUBCLASS-----------------------------------------

class GuideSelectPage(tk.Frame): # class produces tk.Frame frame
    ''' The guide select page for an instance of Application(). 
        GuideSelectPage is a subclass of the tk.Frame class. '''

    def __init__(self, rootContainer, appReference):
        ''' Guide select page constructor. First action is constructing self as a reference to a new tkinter frame. '''

        # Constructor/intializor for parent tk.Frame class. Note: super() is an equivalent option to tk.Frame
        tk.Frame.__init__(self, rootContainer)

        # Frame grid management
        self.activeGridCols = 1
        self.activeGridRows = 4
        manageGridBorder(self, self.activeGridCols, self.activeGridRows)
        # remember to start all grid positions from 1 not standard 0

        # Render default widgets
        self.guide_select_widgets(appReference)


    def guideWasChoosen(self, guideNum, appReference):
        ''' Updates selected guide. '''

        global selectedGuide
        selectedGuide = guideNum
        appReference.renderPages([Traveling]) # render/execute Traveling (starts .after() countdown)
        appReference.viewPage(Traveling) # lift Traveling frame


    def guide_select_widgets(self, appReference):
        ''' Renders default guide select page widgets. '''

        # Title
        self.titleFont = Font(family='Courier', size=20, weight='bold')
        self.title = tk.Label(self, text="Guide Select", font=self.titleFont)
        self.title.grid(column=1, row=1)
        self.subtitleFont = Font(family='Courier', size=12, weight='normal')
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
            if i < 4: # first row
                self.guide_option.grid(column=i, row=0, pady=5, padx=5)
            else: # second row
                self.guide_option.grid(column=i-4, row=1, pady=5, padx=5)
            self.guide_img = tk.Label(self.guide_option, image=self.guideImages[i])
            self.guide_img.grid(column=0, row=0)
            self.guide_select_btn = tk.Button(self.guide_option, text="Select", bg="white", pady=2, padx=10, cursor="hand2", command=lambda i=i: self.guideWasChoosen((i+1), appReference)) # `i=i` necessary to get correct varaible reference
            self.guide_select_btn.grid(column=0, row=1, pady=5, padx=5)

        # Return to Landing
        self.return_to = tk.Button(self, text="Return", bg="white", pady=2, padx=10, cursor="hand2", command=lambda: appReference.viewPage(LandingPage))
        self.return_to.grid(column=1, row=4, pady=5, padx=5)


# --TRAVELING SUBCLASS-----------------------------------------------

class Traveling(tk.Frame): # class produces tk.Frame frame
    ''' The traveling animation transition/page for an instance of Application(). 
        Traveling is a subclass of the tk.Frame class. '''

    def __init__(self, rootContainer, appReference):
        ''' Traveling transition/page constructor. '''

        # Constructor/intializor for parent tk.Frame class. Note: super() is an equivalent option to tk.Frame
        tk.Frame.__init__(self, rootContainer)

        # Frame Grid Management
        self.activeGridCols = 1
        self.activeGridRows = 1
        manageGridBorder(self, self.activeGridCols, self.activeGridRows) # remember to start all grid positions from 1 not standard 0

        self.appReferenceAlias = appReference # Allows non-argument use of appReference

        # Render default widgets
        self.traveling_widgets()


    def arrived(self):
        ''' Invokes change to map page after animation completes. '''

        self.appReferenceAlias.renderPages([MapPage]) # render map page
        self.appReferenceAlias.viewPage(MapPage) # lift map page


    def animate(self, t, y):
        ''' Handles animating the london bus. '''

        # Clear canvas
        self.travel_c.delete("all")
        # Create image
        self.travel_c.create_image((t/3)-60, 200+y, image=self.tkBusImg, anchor="nw")
        # Increase time elapsed
        t += 30
        # Determine bumpiness
        if y != 0:
            y = random.choice([0,y])
        else:
            y = random.choice([0,0,0,0,0,0,0,0,3,-3])
        # Handle endpoint
        if t < 3000:
            self.after(30, lambda t=t, y=y : self.animate(t, y))
        else:
            self.after(30, self.arrived)


    def traveling_widgets(self):
        ''' Renders default traveling animation slide/page widgets. '''

        # Bus image processing
        self.wValue = 200
        self.busImg = Image.open("./photos/london-bus-traveling.png")
        self.wPercent = (self.wValue / float(self.busImg.size[0])) # calc new height percentage for maintaining aspect ratio from defined new width
        self.hValue = int((float(self.busImg.size[1]) * float(self.wPercent))) # calc new height to preserve aspect ratio
        self.busImg = self.busImg.resize((self.wValue, self.hValue), Image.ANTIALIAS) # applying desired resize and antialiasing
        self.tkBusImg = ImageTk.PhotoImage(self.busImg)

        # Canvas initializing
        self.travel_c = tk.Canvas(self, width=800, height=400, highlightthickness=0)
        self.travel_c.grid(column=1, row=1)

        # Bus driving loop started
        self.animate(0, 0)


# --MAPPAGE SUBCLASS-------------------------------------------------

class MapPage(tk.Frame): # class produces tk.Frame frame
    ''' The map page for an instance of Application(). 
        MapPage is a subclass of the tk.Frame class. '''

    def __init__(self, rootContainer, appReference):
        ''' Map page constructor.  '''

        # Constructor/intializor for parent tk.Frame class. Note: super() is an equivalent option to tk.Frame
        tk.Frame.__init__(self, rootContainer)

        # Frame Grid Management
        self.activeGridCols = 2
        self.activeGridRows = 4
        manageGridBorder(self, self.activeGridCols, self.activeGridRows) # remember to start all grid positions from 1 not standard 0

        # Initiate activeInfo index at zero (first)
        self.activeInfo = 0

        self.appReferenceAlias = appReference # Allows non-argument use of appReference

        # Initiate multi-option pin location attributes
        self.between = False
        self.betweenOpt = [None, None]

        # Render default widgets
        self.map_widgets()
		

    def drawMarkers(self):
        ''' Draws pin markers on map canvas. '''

        self.markerPhoto = Image.open("./photos/pin4.png")
        self.markerPhoto = self.markerPhoto.resize((30, 30), Image.ANTIALIAS)
        self.tkMarkerPhoto = ImageTk.PhotoImage(self.markerPhoto)
        for key in mapMarkers:
            if (key == "loc21" or key == "loc22") and (guideLevel < 1):
                # Doesn't render london bus or london phone booth until guide level 1
                continue
            mark = mapMarkers[key]
            if (key == "loc10" or key == "loc6"):
                # Add rect if outlying location
                self.map_c.create_rectangle(mark[0]-18, mark[1]-22, mark[0]+22, mark[1]+18, fill="black", width=3)
                self.map_c.create_rectangle(mark[0]-20, mark[1]-20, mark[0]+20, mark[1]+20, fill="white", width=3)
            self.map_c.create_image(mark[0]-15, mark[1]-15, image=self.tkMarkerPhoto, anchor="nw") # place image covering canvas


    def mapLocClick(self, event):
        ''' Event handler for user map clicks. Under the right conditions, this function opens a location details page. '''

        global activeLoc

        # assign event's x and y coordinate attributes to vars
        clickX = event.x
        clickY = event.y

        # For between two options condition
        if self.between:
            if clickX < 400: # left side of canvas
                activeLoc = self.betweenOpt[0]
            else: # right side of canvas
                activeLoc = self.betweenOpt[1]
            self.appReferenceAlias.renderPages([MapPage, LocationDetails]) # rerender map page to default
            self.appReferenceAlias.viewPage(LocationDetails)
            self.between = False # reset
            return # exit/terminate method

        # For between all pins condition
        for key in mapMarkers: # check each marker with event coordinates
            mark = mapMarkers[key]
            insideX = (clickX >= mark[0]-15) and (clickX <= mark[0]+15)
            insideY = (clickY >= mark[1]-15) and (clickY <= mark[1]+15)
            if insideX and insideY:

                # Do for multi-location pins
                if key == "loc1loc13" or key == "loc2loc14":
                    self.between = True # on next event fire between will be True
                    self.betweenOpt = [key[:4], key[4:]] # set betweenOpt attribute to slices of dual-location key
                    self.map_c.delete("all") # clear canvas
                    xDisplace = [25, 425] # set second location image displacement to the right
                    # Initialize image attributes
                    self.opt1 = None
                    self.opt2 = None
                    # Create image variables
                    for i in [0,1]:
                        optImg = Image.open("./photos/" + locations[self.betweenOpt[i]][1] + ".png")
                        optImg = optImg.resize((350, 350), Image.ANTIALIAS)
                        if i == 0:
                            self.opt1 = ImageTk.PhotoImage(optImg)
                        else:
                            self.opt2 = ImageTk.PhotoImage(optImg)
                    # Place on canvas
                    self.map_c.create_image(xDisplace[0], 0, image=self.opt1, anchor="nw")
                    self.map_c.create_image(xDisplace[1], 0, image=self.opt2, anchor="nw")
                    self.map_c.create_text(400, 175, font="Courier 20 bold", text="or")
                    # Update guide box text
                    self.guide_says.config(state="normal")
                    self.guide_says.delete("1.0", "end")
                    self.guide_says.insert("end", locations[self.betweenOpt[0]][0] + " and " + locations[self.betweenOpt[1]][0] + " are both located here. Click one of the images above to pick which destination you'd like to visit.")
                    self.guide_says.config(state="disabled")

                # Do for all other pins
                else: 
                    activeLoc = key
                    self.appReferenceAlias.renderPages([LocationDetails])
                    self.appReferenceAlias.viewPage(LocationDetails)


    def navTextL(self, e=None):
        ''' Navigate map guide info to previous text. The `e=None` is included to account for non-event-binded (button click) execution. '''

        if self.activeInfo == 0:
            self.activeInfo = len(mapGuideSays)-1
        else:
            self.activeInfo -= 1
        self.guide_says.config(state="normal")
        self.guide_says.delete("1.0", "end")
        self.guide_says.insert("end", mapGuideSays[self.activeInfo])
        self.guide_says.config(state="disabled")
        

    def navTextR(self, e=None):
        ''' Navigate map guide info to next text. The `e=None` is included to account for non-event-binded (button click) execution. '''

        if self.activeInfo == len(mapGuideSays)-1:
            self.activeInfo = 0
        else:
            self.activeInfo += 1
        self.guide_says.config(state="normal")
        self.guide_says.delete("1.0", "end")
        self.guide_says.insert("end", mapGuideSays[self.activeInfo])
        self.guide_says.config(state="disabled")


    def switchGuide(self):
        ''' Resets progress and guide level then opens guide select page. '''

        global progress, guideLevel
        self.appReferenceAlias.viewPage(GuideSelectPage)
        progress = 0
        guideLevel = 0


    def map_widgets(self):
        ''' Renders default map page widgets. '''

        # Progress Bar
        addProgBar(self, self.activeGridCols, 2) # global function (frame, actCols, actRow)

        # Map
            # Image
        self.wValue = 800  # set width here
        self.mapPhoto = Image.open("./photos/london-map-close4.png") # import photo
        self.hValue = 350
        self.mapPhoto = self.mapPhoto.resize((self.wValue, self.hValue)) # applying desired resize and antialiasing
        self.tkMapPhoto = ImageTk.PhotoImage(self.mapPhoto) # applying resized photo to PIL format
            # Map Text
        self.mapText = Image.open("./photos/london-map-text.png")
        self.tWidth = int(900/2.7)
        self.tHeight = int(400/2.7)
        self.mapText = self.mapText.resize((self.tWidth, self.tHeight))
        self.tkMapText = ImageTk.PhotoImage(self.mapText)
            # Image Canvas
        self.map_c = tk.Canvas(self, width=self.wValue, height=self.hValue, highlightthickness=0, cursor="dotbox") # creating canvas same size as image
        self.map_c.grid(column=1, columnspan=2, row=3, pady=5) # assigning grid position
        self.map_c.create_image(0, 0, image=self.tkMapPhoto, anchor="nw") # place image covering canvas
        self.map_c.create_image(50, 0, image=self.tkMapText, anchor="nw")
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
        self.guide_says.insert("end", mapGuideSays[0] + mapNote)
        self.guide_says.config(wrap="word", state="disabled")
        self.guide_says.grid(column=1, row=0)
            # Options
        self.options = ttk.LabelFrame(self.dialogue, text="Options")
        self.options.grid(column=2, row=0, pady=5, padx=5)
                # Prev Button
        self.next_button = tk.Button(self.options, text="<<", bg="white", pady=2, padx=6, cursor="hand2", command=self.navTextL)
        self.next_button.grid(column=0, row=0, pady=0, padx=4)
                # Next Button
        self.next_button = tk.Button(self.options, text=">>", bg="white", pady=2, padx=6, cursor="hand2", command=self.navTextR)
        self.next_button.grid(column=1, row=0, pady=0, padx=4)
                # Return Button
        self.reselect = tk.Button(self.options, text="Reselect", bg="white", pady=2, padx=10, cursor="hand2", command=self.switchGuide)
        self.reselect.grid(column=0, columnspan=2, row=1, pady=4, padx=4)

        # Arrow Key Binds
        self.master.master.bind("<Left>", self.navTextL) # self=[[LocationDetails() frame]].master=[[LocationDetails()]].master=[[Application() window]]
        self.master.master.bind("<Right>", self.navTextR)


# --LOCATIONDETAILS SUBCLASS-----------------------------------------

class LocationDetails(tk.Frame): # class produces tk.Frame frame
    ''' The location details page for an instance of Application().
        Rerendered when different location is selected. 
        LandingPage is a subclass of the tk.Frame class. '''

    def __init__(self, rootContainer, appReference):
        ''' Location details page constructor. '''

        # Constructor/intializor for parent tk.Frame class. Note: super() is an equivalent option to tk.Frame
        tk.Frame.__init__(self, rootContainer)

        # Frame Grid Management
        self.activeGridCols = 3
        self.activeGridRows = 2
        manageGridBorder(self, self.activeGridCols, self.activeGridRows) # remember to start all grid positions from 1 not standard 0
        
        # Setting active location and relative location variables
        self.location = locations[activeLoc]
        self.activeQuiz = quizQs[activeLoc]
        self.addInfoList = self.location[2]

        # Keep track of initial progress when entered. Used to decide whether to rerender map page.
        self.initProg = progress+0 # +0 to prevent aliasing
        self.initLevel = guideLevel+0 # +0 to prevent aliasing

		# Guide says state
        self.activeInfo = 0

		# Initiate quiz variables
        self.allLocQs = quizQs[activeLoc]
        self.selectedQs = []
		
        self.appReferenceAlias = appReference # Allows non-argument use of appReference

		# Rendering default widgets
        self.location_details_widgets()

    
    def mapPageReturn(self):
        ''' Returns user to map page frame. Rerenders map page if progress has changed. '''

        if self.initProg != progress or self.initLevel != guideLevel:
            self.appReferenceAlias.renderPages([MapPage]) # render/execute Traveling (starts .after() countdown)
        self.appReferenceAlias.viewPage(MapPage)
    

    def textNavRender(self):
        ''' Renders the text navigator bar. '''

        self.text_nav = tk.Frame(self.guide_interaction)
        self.text_nav.grid(column=0, row=1, pady=0, padx=10)
        self.text_nav.columnconfigure(1, minsize=120) # buffer middle column for spacing
        self.buffer = tk.Label(self.text_nav)
        self.buffer.grid(column=1)
            # Left
        self.left_button = tk.Button(self.text_nav, text="<<", bg="white", pady=2, padx=15, cursor="hand2", command=self.navTextL)
        self.left_button.grid(column=0, row=0, pady=(4,10))
            # Right
        self.right_button = tk.Button(self.text_nav, text=">>", bg="white", pady=2, padx=15, cursor="hand2", command=self.navTextR)
        self.right_button.grid(column=2, row=0, pady=(4,10))


    def navTextL(self, e=None):
        ''' Navigate map guide info to previous text. The `e=None` is included to account for non-event-binded (button click) execution. '''

        if self.activeInfo == 0:
            self.activeInfo = len(self.addInfoList)-1
        else:
            self.activeInfo -= 1
        self.guide_says.config(state="normal")
        self.guide_says.delete("1.0", "end")
        self.guide_says.insert("end", self.addInfoList[self.activeInfo])
        self.guide_says.config(state="disabled")

        
    def navTextR(self, e=None):
        ''' Navigate map guide info to next text. The `e=None` is included to account for non-event-binded (button click) execution. '''

        if self.activeInfo == len(self.addInfoList)-1:
            self.activeInfo = 0
        else:
            self.activeInfo += 1
        self.guide_says.config(state="normal")
        self.guide_says.delete("1.0", "end")
        self.guide_says.insert("end", self.addInfoList[self.activeInfo])
        self.guide_says.config(state="disabled")


    def quizOpen(self):
        ''' Activates quiz. Updates guidebox GUI to adjust for quiz. '''

        # Prevent leaving or restarting quiz
        self.quiz_button.config(state="disabled", cursor="no")
        self.return_map.config(state="disabled", cursor="no")
        # Temporarily destroy text navigation
        self.text_nav.destroy()
        # Initialize score and reset selected questions
        self.numCorrect = 0
        self.selectedQs = []
        mutableAllLocQs = self.allLocQs[:] # make copy of location questions; don't edit original allLocQs attribute
        # Randomly select questions, add them to selected questions, and remove them from possible questions pool
        for i in range(3):
            selectIndex = random.randrange(0, len(mutableAllLocQs))
            addQ = mutableAllLocQs[selectIndex]
            mutableAllLocQs.pop(selectIndex)
            self.selectedQs.append(addQ)
        self.guide_says.config(height=5) # resize guidebox
        self.quizHandler(0) # open first question


    def quizHandler(self, q): # (self, quiz question index)
        ''' Renders appropriate quiz widgets. Updates the output for each question and, over the course of user completion, the state of quiz progress. '''

        # Update guide text box
        self.guide_says.config(state="normal")
        self.guide_says.delete("1.0", "end")
        self.guide_says.insert("end", self.selectedQs[q][0])
        self.guide_says.config(state="disabled")
        # Render buttons
        self.question_frame = tk.Frame(self.guide_interaction) # necessary frame meant to be destroyed later
        self.question_frame.grid(column=0, row=1)
        letters = ["A.", "B.", "C."]
        answerIndex = 0
        # Shuffle answer keys to create random answer order
        answerKeys = []
        for key in self.selectedQs[q][1]:
            answerKeys.append(key)
        random.shuffle(answerKeys)
        # Render each answer
        for answer in answerKeys:
            answer_frame = tk.Frame(self.question_frame)
            answer_frame.grid(column=0, row=answerIndex, pady=(10,0))
            answer_frame.grid_columnconfigure(1, weight=1)
            optionLetter = letters[answerIndex]
            answerIndex += 1
            answer_select = tk.Button(answer_frame, text=optionLetter, bg="white", pady=4, padx=4, cursor="hand2", command=lambda q=q, a=answer : self.answerHandler(q,a))
            answer_select.grid(column=0, row=0, padx=(0,10))
            answer_text = tk.Label(answer_frame, text=answer, width=24, anchor="w", wraplength=180)
            answer_text.grid(column=1, row=0)
    

    def answerHandler(self, q, a):
        ''' Determines answer correctness. Moves user on to next question or finishes quiz based on quiz progress. When this function identifies the end of the quiz, it displays a special completion message. '''

        global progress, guideLevel
        lastQ = (q == 2) # bool var
        self.question_frame.destroy()
        if self.selectedQs[q][1][a]:
            self.numCorrect += 1
            progress += 10 # Add ten points
            if progress >= 100:
                progress -= 100
                guideLevel += 1
        if lastQ:
			# Quiz completion message
            self.guide_says.config(state="normal")
            self.guide_says.delete("1.0", "end")
            self.guide_says.insert("end", "You scored a " + str(self.numCorrect) + " out of 3.")
            self.guide_says.config(state="disabled")
			# Exit quiz button
            self.exit_quiz = tk.Button(self.guide_interaction, text="Exit Quiz", bg="white", pady=2, padx=10, cursor="hand2", command=self.exitQuiz)
            self.exit_quiz.grid(column=0, row=2, pady=10, padx=4)
        else:
            self.quizHandler(q+1)

            
    def exitQuiz(self):
        ''' Leaves the quiz and resets to appropriate default widgets. Rerenders progress bar to updated progress.'''

        self.exit_quiz.destroy()
        self.guide_says.config(height=12)
        # Rerender progress bar
        self.progress_frame.destroy()
        addProgBar(self, self.activeGridCols, 1)
        # Guide says
        self.guide_says.config(state="normal")
        self.guide_says.delete("1.0", "end")
        self.guide_says.insert("end", self.location[2][self.activeInfo])
        self.guide_says.config(state="disabled")
        # Text Nav Render
        self.textNavRender()
        # Reactivate Option Buttons
        self.quiz_button.config(state="normal", cursor="hand2")
        self.return_map.config(state="normal", cursor="hand2")
                
    
    def location_details_widgets(self):
        ''' Renders all default location details page widgets. '''

        # Progress Bar
        addProgBar(self, self.activeGridCols, 1) # global function (frame, actCols, actRow)

        # Location Image
        self.wValue = 450 # set width here
        self.hValue = 450 # set height here
            # Image
        self.locPhoto = Image.open("./photos/" + self.location[1] + ".png") # import photo
        self.locPhoto = self.locPhoto.resize((self.wValue, self.hValue)) # applying desired resize
        self.tkLocPhoto = ImageTk.PhotoImage(self.locPhoto) # applying resized photo to PIL format
            # Image Text
        self.locTitle = Image.open("./photos/" + self.location[1] + "-text.png") # import text photo
        self.locTitle = self.locTitle.resize((self.wValue, self.hValue)) # applying desired resize and anti-aliasing
        self.tkLocTitle = ImageTk.PhotoImage(self.locTitle) # applying resized photo to PIL format
            # Image Canvas
        #self.title_c = tk.Canvas(self, width=self.wValue, height=self.hValue, highlightthickness=0) # creating canvas same size as image
        self.loc_c = tk.Canvas(self, width=self.wValue, height=self.hValue, highlightthickness=0) # creating canvas same size as image
        self.loc_c.grid(column=1, columnspan=2, row=2, pady=10, padx=10) # assigning grid position
        self.loc_c.create_image(0, 0, image=self.tkLocPhoto, anchor=tk.NW) # place image covering canvas
        self.loc_c.create_image(0, 0, image=self.tkLocTitle, anchor=tk.NW) # place text image on canvas
        
        # Guide Box
        self.guide_box = ttk.LabelFrame(self, text="Guide")
        self.guide_box.grid(column=3, row=2)
        self.guide_box.grid_rowconfigure(1, minsize=250) # establish constant guide_box column height
            # Guide Image
        self.guideRef = guideGet(150) # need guideRef to maintain reference, single function call gets trashed after
        self.guide = tk.Label(self.guide_box, image=self.guideRef)
        self.guide.grid(column=0, row=0, pady=5, padx=5)
           # Options
        self.options = ttk.LabelFrame(self.guide_box, text="Options")
        self.options.grid(column=1, row=0, pady=5, padx=5)
                # Quiz Button
        self.quiz_button = tk.Button(self.options, text="Take\nQuiz", bg="white", pady=2, padx=10, cursor="hand2", command=self.quizOpen)
        self.quiz_button.grid(column=0, row=0, pady=0, padx=4)
                # Return Button
        self.return_map = tk.Button(self.options, text="Return\nto Map", bg="white", pady=2, padx=10, cursor="hand2", command=self.mapPageReturn)
        self.return_map.grid(column=0, row=1, pady=4, padx=4)
            # Guide Interaction
        self.guide_interaction = tk.Frame(self.guide_box)
        self.guide_interaction.grid(column=0, columnspan=2, row=1, sticky="N")
                # Text
        self.guide_says = tk.Text(self.guide_interaction, width=30, height=12)
        self.guide_says.insert("end", self.location[2][self.activeInfo] + introNote)
        self.guide_says.config(wrap="word", state="disabled")
        self.guide_says.grid(column=0, row=0, pady=(10,0), padx=10)
                # Text Nav
        self.textNavRender()
        # Arrow Key Binds
        self.master.master.bind("<Left>", self.navTextL) # self=[[LocationDetails() frame]].master=[[LocationDetails()]].master=[[Application() window]]
        self.master.master.bind("<Right>", self.navTextR)


# --GLOBAL MAIN FUNCTION---------------------------------------------

def main():
    ''' Executes program. '''

    # Set variable to instance of application class
    program = Application()

    # Set default font
    def_font = tk.font.nametofont("TkDefaultFont")
    def_font.config(family="Courier")

    # Execute main tkinter program loop
    program.mainloop()


if __name__ == "__main__":
    main()
