from tkinter import *
import os

dirPath = os.path.abspath(os.path.dirname(__file__) + "/Textures")
selectedPieces = []
piecesArray = []
piecesCoords = []
piecesWhiteTaken = []
piecesBlackTaken = []
whiteCount = 0
blackCount = 0
playerTurn = "White"
gameStarted = False

mainWindow = Tk()
mainWindow.geometry("620x520")
# Makes the window so it cannot be resized
mainWindow.resizable(False, False)
mainWindow.title("Pro Chess")
mainWindow.iconbitmap(dirPath + "/whitePawnIcon.ico")
container = Canvas(mainWindow, bg = "gray", highlightbackground = "black", highlightthickness = 1)
container.place(x = 0, y = 0, relheight = 1, relwidth = 1)

chessMenuCanvas = Canvas(mainWindow, bg = "#d3d3d3", relief = "sunken", highlightbackground = "black", highlightthickness = 1)

# Generates the image instances
piecePlaceholder = PhotoImage(file = dirPath + "/imagePlaceholder.gif")
whitePawn = PhotoImage(file = dirPath + "/whitePawn.gif")
blackPawn = PhotoImage(file = dirPath + "/blackPawn.gif")
whiteRook = PhotoImage(file = dirPath + "/whiteRook.gif")
blackRook = PhotoImage(file = dirPath + "/blackRook.gif")
whiteKnight = PhotoImage(file = dirPath + "/whiteKnight.gif")
blackKnight = PhotoImage(file = dirPath + "/blackKnight.gif")
whiteBishop = PhotoImage(file = dirPath + "/whiteBishop.gif")
blackBishop = PhotoImage(file = dirPath + "/blackBishop.gif")
whiteQueen = PhotoImage(file = dirPath + "/whiteQueen.gif")
blackQueen = PhotoImage(file = dirPath + "/blackQueen.gif")
whiteKing = PhotoImage(file = dirPath + "/whiteKing.gif")
blackKing = PhotoImage(file = dirPath + "/blackKing.gif")
wrongSelect = PhotoImage(file = dirPath + "/wrongSelect.gif")
correctSelect = PhotoImage(file = dirPath + "/correctSelect.gif")
chessBoard = PhotoImage(file = dirPath + "/chessBoard.gif")
menuBackground = PhotoImage(file = dirPath + "/menuBackground.gif")
verificationLineN = PhotoImage(file = dirPath + "/verificationLineN.gif")
##playButton = PhotoImage(file = dirPath + "/PlayButtonNoHover.pbm")
##playButton = playButton.subsample(2, 2)

class ProChess:
    """The super class that handles eveything from board generation, to the tile screen"""

    def __init__(self):
        """Inisitalises the variables needed for the game generation"""

        self.pieceStartLocations = [[0, blackRook, "Rook", "Black"],[1, blackKnight, "Knight", "Black"],[2, blackBishop, "Bishop", "Black"],[3, blackQueen, "Queen", "Black"],[4, blackKing, "King", "Black"],
                                   [5, blackBishop, "Bishop", "Black"],[6, blackKnight, "Knight", "Black"],[7, blackRook, "Rook", "Black"],[8, blackPawn, "Pawn", "Black"],[9, blackPawn, "Pawn", "Black"],
                                   [10, blackPawn, "Pawn", "Black"],[11, blackPawn, "Pawn", "Black"],[12, blackPawn, "Pawn", "Black"],[13, blackPawn, "Pawn", "Black"],[14, blackPawn, "Pawn", "Black"],
                                   [15, blackPawn, "Pawn", "Black"],[48, whitePawn, "Pawn", "White"],[49, whitePawn, "Pawn", "White"],[50, whitePawn, "Pawn", "White"],[51, whitePawn, "Pawn", "White"],
                                   [52, whitePawn, "Pawn", "White"],[53, whitePawn, "Pawn", "White"],[54, whitePawn, "Pawn", "White"],[55, whitePawn, "Pawn", "White"],[56, whiteRook, "Rook", "White"],
                                   [57, whiteKnight, "Knight", "White"],[58, whiteBishop, "Bishop", "White"],[59, whiteQueen, "Queen", "White"],[60, whiteKing, "King", "White"],[61, whiteBishop, "Bishop", "White"],
                                   [62, whiteKnight, "Knight", "White"],[63, whiteRook, "Rook", "White"]]

        # All variables needed for the game timer
        self.gameActive = False
        self.colon = ":"
        self.whiteZero = " "
        self.whiteSeconds = 59
        self.whiteMinutes = 9
        self.blackZero = " "
        self.blackSeconds = 59
        self.blackMinutes = 9

        self.whiteKingCheck = False
        self.blackKingCheck = False

        self.createBoard("Normal")

    def createBoard(self, type):
        """Method that generates the brown and white squares of the chess board"""

        if type == "Normal":
            self.gameClock()
        else:
            # If the board is reset it rests the taken pieces section
            self.updatesPiecesTakenGrid("White")
            self.updatesPiecesTakenGrid("Black")

        container.bind("<Button-3>", lambda bind2: ProChess.getCurrentSelectedPiece())
        container.create_image("0 0", anchor = "nw", image = chessBoard)
        rowCounter = 32.5
        columnCounter = 32.5
        count = 0
        for _ in range(64):
            #Goes here if it is generating empty squares
            if count >= 16 and count <= 47:
                piecesArray.append(Placeholder(count, rowCounter, columnCounter,
                                              piecePlaceholder, "Placeholder", "None"))
                piecesCoords.append("{} {}".format(columnCounter, rowCounter))
            else:
                for i in range(len(self.pieceStartLocations)):
                    #Makes sure to grab the latest piece in the array
                    if count == self.pieceStartLocations[i][0]:
                        #Generates a chess piece at the current location identified by rowCounter and columnCounter
                        if self.pieceStartLocations[i][2] == "Pawn":
                            piecesArray.append(Pawn(self.pieceStartLocations[i][0], rowCounter, columnCounter,
                                                          self.pieceStartLocations[i][1], self.pieceStartLocations[i][2],
                                                          self.pieceStartLocations[i][3]))
                        elif self.pieceStartLocations[i][2] == "Rook":
                            piecesArray.append(Rook(self.pieceStartLocations[i][0], rowCounter, columnCounter,
                                                          self.pieceStartLocations[i][1], self.pieceStartLocations[i][2],
                                                          self.pieceStartLocations[i][3]))
                        elif self.pieceStartLocations[i][2] == "Knight":
                            piecesArray.append(Knight(self.pieceStartLocations[i][0], rowCounter, columnCounter,
                                                          self.pieceStartLocations[i][1], self.pieceStartLocations[i][2],
                                                          self.pieceStartLocations[i][3]))
                        elif self.pieceStartLocations[i][2] == "Bishop":
                            piecesArray.append(Bishop(self.pieceStartLocations[i][0], rowCounter, columnCounter,
                                                          self.pieceStartLocations[i][1], self.pieceStartLocations[i][2],
                                                          self.pieceStartLocations[i][3]))
                        elif self.pieceStartLocations[i][2] == "Queen":
                            piecesArray.append(Queen(self.pieceStartLocations[i][0], rowCounter, columnCounter,
                                                          self.pieceStartLocations[i][1], self.pieceStartLocations[i][2],
                                                          self.pieceStartLocations[i][3]))
                        elif self.pieceStartLocations[i][2] == "King":
                            piecesArray.append(King(self.pieceStartLocations[i][0], rowCounter, columnCounter,
                                                          self.pieceStartLocations[i][1], self.pieceStartLocations[i][2],
                                                          self.pieceStartLocations[i][3]))
                        piecesCoords.append("{} {}".format(columnCounter, rowCounter))
            count += 1
            columnCounter += 65
            #Moves onto the next row once the current row has been generated
            if (count % 8) == 0:
                columnCounter = 32.5
                rowCounter += 65
        self.raiseEmptySpaces()
        self.createSideMenu()

    def resetBoard(self):
        """Resets the entire chess board"""
        global playerTurn, piecesArray, piecesCoords, piecesWhiteTaken, piecesBlackTaken, gameStarted

        container.delete("all")
        try:
            winScreen.destroy()
        except: # Goes here if winScreen doesnt exist
            print()

        # Resets all the main board variables
        self.gameActive = False
        self.whiteZero = " "
        self.whiteSeconds = 59
        self.whiteMinutes = 9
        self.blackZero = " "
        self.blackSeconds = 59
        self.blackMinutes = 9
        self.whiteKingCheck = False
        self.blackKingCheck = False
        playerTurn = "White"
        gameStarted = False
        piecesArray = []
        piecesCoords = []
        piecesWhiteTaken = []
        piecesBlackTaken = []

        # Sets all pawns on the board to not have been moved before
        for i in range(len(piecesArray)):
            if piecesArray[i].getPieceType() == "Pawn":
                piecesArray[i].setFalsePieceMoved()

        self.createBoard("Reset")

    def createSideMenu(self):
        """Creates the side menu next to the chess board"""
        chessMenuCanvas.place(x = 520, y = 0, width = 100, relheight = 1)

        self.blackTurnIndicator = chessMenuCanvas.create_oval("25 -25 75 25", fill = "red", outline = "#333333")
        self.whiteTurnIndicator = chessMenuCanvas.create_oval("25 495 75 545", fill = "green", outline = "#333333")

        # Generates all the subtitles on the side-menu
        chessMenuCanvas.create_text("51 210", text = "Black", font = "Arial 10 bold italic")
        chessMenuCanvas.create_text("53 307", text = "White", font = "Arial 10 bold italic") # 53 310
        chessMenuCanvas.create_text("52 155", text = "White Taken", font = "Arial 10 bold italic")
        chessMenuCanvas.create_text("52 365", text = "Black Taken", font = "Arial 10 bold italic")
        chessMenuCanvas.create_text("52 258", text = "Reset Board", fill = "red", font = "Arial 10 bold", tag = "ResetButton")

        chessMenuCanvas.tag_bind("ResetButton", "<Button-1>", lambda reset: self.resetBoard())

    def createWinScreen(self, colour):
        """Creates a win screen showing which team won, and allowing the user to reset the board or quit"""
        global winScreen, gameStarted
        gameStarted = False
        
        # Creates a black frame that handles all of the win text and buttons
        winScreen = Frame(mainWindow, bg = "black")
        winScreen.place(relx = 0.42, rely = 0.5, relheight = 0.3, relwidth = 0.5, anchor = "center")
        winCanvas = Canvas(winScreen, bg = "black")
        winCanvas.pack(fill = "both", expand = True)
        
        # Generates win text depending on the colour
        if colour == "White":
            winCanvas.create_text("155 50", text = "White Wins!", font = "Arial 17 bold", fill = "white")
        else:
            winCanvas.create_text("155 50", text = "Black Wins!", font = "Arial 17 bold", fill = "white")

        winCanvas.create_text("67 130", text = "Reset Board", font = "Arial 14", fill = "white", tag = "ResetButton")
        winCanvas.create_text("272 130", text = "Quit", font = "Arial 14", fill = "white", tag = "LeaveButton")

        # Binds the text with the resetBoard and quit methods
        winCanvas.tag_bind("ResetButton", "<Button-1>", lambda bind: self.resetBoard())
        winCanvas.tag_bind("LeaveButton", "<Button-1>", lambda bind: self.quit())

    def quit(self):
        """Quits the entire game"""
        mainWindow.destroy()

    def updatesPiecesTakenGrid(self, colour):
        """Updates the grid of pieces that each team has taken on the side menu"""

        if colour == "Black":
            xCoordPlace = 20
            yCoordPlace = 450
            count = 0
            # Generates the pieces in the list in a 4x4 grid on the side-menu, if the index is empty it places an empty piece
            for i in range(16):
                try:
                    pieceToPlace = piecesWhiteTaken[i]
                except:
                    pieceToPlace = piecePlaceholder
                chessMenuCanvas.create_image("{} {}".format(xCoordPlace, yCoordPlace), image = pieceToPlace)

                count += 1
                xCoordPlace += 20
                if (count % 4) == 0 and count != 0:
                    xCoordPlace = 20
                    yCoordPlace -= 20
        else:
            xCoordPlace = 20
            yCoordPlace = 70
            count = 0
            for i in range(16):
                try:
                    pieceToPlace = piecesBlackTaken[i]
                except:
                    pieceToPlace = piecePlaceholder
                chessMenuCanvas.create_image("{} {}".format(xCoordPlace, yCoordPlace), image = pieceToPlace)

                count += 1
                xCoordPlace += 20
                if (count % 4) == 0 and count != 0:
                    xCoordPlace = 20
                    yCoordPlace += 20

    def raiseEmptySpaces(self):
        """Makes sure that the placeholder pieces are the lowest in the image stack"""
        for i in range(len(piecesArray)):
            if piecesArray[i].getPieceType() == "Placeholder":
                piecesArray[i].raiseImageStack()

    def getCurrentSelectedPiece(self):
        """This is used for getting the currently selected piece for it to be deselected"""
        global selectedPieces

        if len(selectedPieces) == 1:
            piecesArray[selectedPieces[0]].pieceDeSelect()
        else:
            pass

    def swapPlayerTurn(self):
        """Swaps who's turn it is; white or black"""
        global playerTurn, whiteCount, blackCount, selectedPieces

        self.turnZero = " "
        self.turnSeconds = 0
        self.turnMinutes = 0
        self.whiteKingCheck = False
        self.blackKingCheck = False
        attackingPieceCheck = None
        potentialBlockers = []
        canBeBlocked = False
        canBeTaken = False
        canMove = False
        whiteKingAttacker = None
        blackKingAttacker = None
        whiteKingSpaces = []
        blackKingSpaces = []
        selectedPieces = []

        # Goes through every piece and generates verification
        for i in range(len(piecesArray)):
            if piecesArray[i].getPieceType() != "Placeholder":
                piecesArray[i].createVerification("Check")

        if piecesArray[4].getCanMoveHere() == True:
            blackCount = 1
            blackKingAttacker = piecesArray[4].getAttackingID()
        else:
            blackCount = 0
        if piecesArray[60].getCanMoveHere() == True:
            whiteCount = 1
            whiteKingAttacker = piecesArray[60].getAttackingID()
        else:
            whiteCount = 0

        # Check
        if whiteCount == 1:
            print("White In Check!")
        if blackCount == 1:
            print("Black In Check")
        
        # Checks if the king can move out of the check
        if blackCount == 1:
            for i in range(len(piecesArray)):
                if piecesArray[i].getCanKingMoveHere() == True and piecesArray[i].getCanMoveHere() != True:
                    blackKingSpaces.append(piecesArray[i].getPieceID())
            if len(blackKingSpaces) != 0:
                canMove = True
        # Gets a list of potential blockers, which may be able to block the check
            for i in range(len(piecesArray)):
                if piecesArray[i].getCanMoveHere() == True:
                    attackingList = piecesArray[i].getAttackingID()
                    for j in range(len(attackingList)):
                        if attackingList[j] != blackKingAttacker[0]:
                            if attackingList[j] not in potentialBlockers:
                                potentialBlockers.append(attackingList[j])

            while canBeBlocked == False and len(potentialBlockers) > 0:
                    #if blackKingAttacker[0] in piecesArray[potentialBlockers[0]].getAttackingID():
                        #potentialBlockers.pop(0)
                    #else:
                        for v in range(8):
                            if v == 0:
                                nextVerificationCheck = piecesArray[potentialBlockers[0]].getNextVerification()
                            else:
                                if nextVerificationCheck != None:
                                    nextVerificationCheck = piecesArray[nextVerificationCheck].getNextVerification()
                            if len(potentialBlockers) > 0:
                                if nextVerificationCheck != None:
                                    if piecesArray[nextVerificationCheck].getPieceType() == "King":
                                        canBeBlocked = True
                                else:
                                    potentialBlockers.pop(0)
        # Checks if the attacking piece can be taken
            if piecesArray[blackKingAttacker[0]].getAttackingID() != []:
                canBeTaken = True
            print(canMove, canBeBlocked, canBeTaken)
            if canMove == True or canBeBlocked == True or canBeTaken == True:
                blackCount = 1
            else:
                blackCount = 2

        # Checks if the king can move out of the check
        if whiteCount == 1:
            for i in range(len(piecesArray)):
                if piecesArray[i].getCanKingMoveHere() == True and piecesArray[i].getCanMoveHere() != True:
                    whiteKingSpaces.append(piecesArray[i].getPieceID)
            if len(whiteKingSpaces) == 0:
                canMove = True
        # Gets a list of potential blockers, which may be able to block the check
            for i in range(len(piecesArray)):
                if piecesArray[i].getCanMoveHere() == True:
                    attackingList = piecesArray[i].getAttackingID()
                    for j in range(len(attackingList)):
                        if attackingList[j] != whiteKingAttacker[0]:
                            if attackingList[j] not in potentialBlockers:
                                potentialBlockers.append(attackingList[j])

            while canBeBlocked == False and len(potentialBlockers) > 0:
                    #if blackKingAttacker[0] in piecesArray[potentialBlockers[0]].getAttackingID():
                        #potentialBlockers.pop(0)
                    #else:
                        for v in range(8):
                            if v == 0:
                                nextVerificationCheck = piecesArray[potentialBlockers[0]].getNextVerification()
                            else:
                                if nextVerificationCheck != None:
                                    nextVerificationCheck = piecesArray[nextVerificationCheck].getNextVerification()
                            if len(potentialBlockers) > 0:
                                if nextVerificationCheck != None:
                                    if piecesArray[nextVerificationCheck].getPieceType() == "King":
                                        canBeBlocked = True
                                else:
                                    potentialBlockers.pop(0)
        # Checks if the attacking piece can be taken
            if piecesArray[whiteKingAttacker[0]].getAttackingID() != []:
                canBeTaken = True
            print(canMove, canBeBlocked, canBeTaken)
            if canMove == True or canBeBlocked == True or canBeTaken == True:
                whiteCount = 1
            else:
                whiteCount = 2
        # Checkmate
        if whiteCount == 2:
            self.createWinScreen("Black")
        if blackCount == 2:
            self.createWinScreen("White")

        if playerTurn == "White":
            # Changes (swaps) the colour of the indicator circles in the chess sub-menu
            chessMenuCanvas.itemconfig(self.blackTurnIndicator, fill = "green")
            chessMenuCanvas.itemconfig(self.whiteTurnIndicator, fill = "red")
            playerTurn = "Black"
        else:
            chessMenuCanvas.itemconfig(self.blackTurnIndicator, fill = "red")
            chessMenuCanvas.itemconfig(self.whiteTurnIndicator, fill = "green")
            playerTurn = "White"

        self.resetVerification()

    def gameClock(self):
        """Creates a timer fior both players that counts down when it is a players turn from 10 minutes"""
        global gameStarted

        if gameStarted:
            if playerTurn == "White":
                # Deletes the white game timer so it doesnt get overlay onto itself
                chessMenuCanvas.delete("GameClockWhite")
                # If the seconds is above 10 a temporary "0" is not needed (e.g
                if self.whiteSeconds < 10:
                    chessMenuCanvas.create_text("50 325", text = self.whiteZero + (str(self.whiteMinutes) + self.colon + "0" + str(self.whiteSeconds)), fill = "#333333", font = "Arial 16 italic", tags = 'GameClockWhite')
                else:
                    chessMenuCanvas.create_text("50 325", text = self.whiteZero + (str(self.whiteMinutes) + self.colon + str(self.whiteSeconds)), fill = "#333333", font = "Arial 16 italic", tags = 'GameClockWhite')

                self.whiteSeconds -= 1
                if self.whiteSeconds == 0:
                    self.whiteSeconds = 60
                    self.whiteMinutes -= 1
                if self.whiteMinutes == 10:
                    self.whiteZero = ""

                if self.whiteMinutes == -1:
                    self.whiteSeconds -= 1
                    self.createWinScreen("Black")
                    gameStarted = False
            else:
                # Deletes the black game timer so it doesnt get overlay onto itself
                chessMenuCanvas.delete("GameClockBlack")
                # If the seconds is above 10 a temporary "0" is not needed (e.g
                if self.blackSeconds < 10:
                    chessMenuCanvas.create_text("50 195", text = self.blackZero + (str(self.blackMinutes) + self.colon + "0" + str(self.blackSeconds)), fill = "#333333", font = "Arial 16 italic", tags = 'GameClockBlack')
                else:
                    chessMenuCanvas.create_text("50 195", text = self.blackZero + (str(self.blackMinutes) + self.colon + str(self.blackSeconds)), fill = "#333333", font = "Arial 16 italic", tags = 'GameClockBlack')

                self.blackSeconds -= 1
                if self.blackSeconds == 0:
                    self.blackSeconds = 60
                    self.blackMinutes -= 1
                if self.blackMinutes == 10:
                    self.blackZero = ""

                if self.blackMinutes == -1:
                    self.blackSeconds -= 1
                    self.createWinScreen("White")
                    gameStarted = False
        else:
            # If the game isnt in progress the clock defaults to 10 minutes
            chessMenuCanvas.delete("GameClockWhite")
            chessMenuCanvas.delete("GameClockBlack")
            chessMenuCanvas.create_text("50 325", text = "1" + "0" + self.colon + "0" + "0", fill = "#333333", font = "Arial 16 italic", tags = 'GameClockWhite')
            chessMenuCanvas.create_text("50 195", text = "1" + "0" + self.colon + "0" + "0", fill = "#333333", font = "Arial 16 italic", tags = 'GameClockBlack')

        # Waits for 1 seconds then recurses
        chessMenuCanvas.after(1000, self.gameClock)

    def resetVerification(self):
        """Resets so that no spaces can be moved to"""
        for i in range(len(piecesArray)):
            piecesArray[i].disablePieceMovement()

    def mainMenu(self):
        """Generates the main menu window"""
        container.create_image("0 0", image = menuBackground, anchor = "nw")
        container.create_text("260 50", text = "ProChess", font = ("Arial", 30))
##        container.create_image("260 100", image = playButton, anchor = "nw")


class ChessPiece:
    """Object class for each chess piece, this stores the piece type, location and available moves"""
    def __init__(self, id, xCoord, yCoord, imageVar, piece, pieceColour):
        """Inisisation class that sets up the attributes for the chess piece"""

        self.id = id
        self.attackingID = []
        self.nextVerification = None
        self.castleVerification = False
        self.piece = piece
        self.pieceColour = pieceColour
        self.imageVar = imageVar
        self.selectionImage = imageVar.subsample(2, 2) # Image used when the piece is selected
        self.takenImage = imageVar.subsample(3, 3) # Image used when the piece is taken and moved to the side-menu
        self.xCoord = xCoord
        self.yCoord = yCoord
        self.motionTrack = 0
        self.canMoveHere = False
        self.kingCanMoveHere = False

        #Generates the piece image
        self.pieceImage = container.create_image(yCoord, xCoord, image = self.imageVar,
                                                 anchor = "center", tag = str(self.id))
        #Binds the chess piece image with left mouse click so the player can select it
        container.tag_bind(self.pieceImage, "<Button-1>", lambda bind: self.pieceSelect())

    def getPieceColour(self):
        """Returns the current pieceColour"""
        return self.pieceColour

    def getPieceImage(self):
        """Returnms the variable storing this pieces image"""
        return self.pieceImage

    def getPieceID(self):
        """Returns the ID of this piece"""
        return self.id

    def getAttackingID(self):
        """Returns the ID of the piece that can move to this square"""
        return self.attackingID

    def getNextVerification(self):
        """Gets the id of the peice next in the route"""
        return self.nextVerification

    def getPieceCoords(self):
        """Returns the coordinates of the chess piece"""
        return (self.yCoord, self.xCoord)

    def getPieceType(self):
        """Returns the piece type"""
        return self.piece

    def getCanMoveHere(self):
        """Returns if any peice is able to move here"""
        return self.canMoveHere

    def getCanKingMoveHere(self):
        """Returns if the king can move here"""
        return self.kingCanMoveHere

    def allowKingMovement(self, attackingID):
        """Allows a king to move to this space, this makes sure
        that king verification does not mix with piece verification"""
        self.kingCanMoveHere = True

        self.setAttackingID(attackingID)

    def allowPieceMovement(self, attackingID):
        """Allows a chess piece to be able to move to this square"""
        self.canMoveHere = True
        self.kingCanMoveHere = False

        self.setAttackingID(attackingID)

    def disablePieceMovement(self):
        """Disables chess pieces being able to move to this square"""
        self.canMoveHere = False
        self.kingCanMoveHere = False

    def createVerificationSquare(self):
        """Generates a blue square around this location showing that you can move here"""
        global selectedPieces

        try:
            # If the piece is white the line generates at the top of the piece
            # If the piece is black the line generates at the bottom of the piece 
            if piecesArray[selectedPieces[0]].getPieceColour() == "White":
                container.create_image(self.yCoord, self.xCoord - 27, image = verificationLineN, tag = "VerificationLine")
            else:
                container.create_image(self.yCoord, self.xCoord + 27, image = verificationLineN, tag = "VerificationLine")
        except: # Just in case no colour is passed through it defaults to white
            container.create_image(self.yCoord, self.xCoord - 27, image = verificationLineN, tag = "VerificationLine")

    def setPieceID(self, id):
        """Sets the piece id to the id so it matches the square its on"""
        self.id = id

    def setAttackingID(self, id):
        """Sets the piece id of the piece that is attacking this square"""
        self.attackingID.append(id)

    def setPieceCoords(self, xCoords, yCoords):
        """Sets the coordinates of the chess piece"""
        self.yCoords = yCoords
        self.xCoords = xCoords

    def setNextVerification(self, id):
        """Sets the id of the next piece in the route"""
        self.nextVerification = id

    def setCastleVerification(self):
        """This sets the castleVerification to True when a king can castle with this piece (rook)"""
        self.castleVerification = True

    def raiseImageStack(self):
        container.tag_raise(self.pieceImage)

    def destroyImage(self):
        """Deletes this peice of the board"""
        container.delete(self.pieceImage)

    def pieceSelect(self):
        """Validation for when 2 peices are selected,
           to see which pieces they are to go to the correct method"""
        global selectedPieces

        selectedPieces.append(self.id)
        self.listLocation = selectedPieces[0]

        if self.kingCanMoveHere == True and self.castleVerification == True:
            if self.id == 0 or self.id == 56: # Long castle
                rookID = selectedPieces.pop(1)
                container.unbind("<Motion>")
                # First the king piece is swapped
                kingCurrentCoords = piecesArray[self.listLocation].getPieceCoords() # Gets the coords of the king that is castling
                verificationIDX = kingCurrentCoords[0] - 130

                verificationID = piecesCoords.index("{} {}".format(verificationIDX, kingCurrentCoords[1]))
                selectedPieces.append(verificationID)
                self.pieceSwap("Castle")

                # Second the Rook is swapped to complete the castle
                selectedPieces = [rookID]
                kingCurrentCoords = piecesArray[self.listLocation].getPieceCoords() # Gets the coords of the king after it has moved
                verificationIDX = kingCurrentCoords[0] + 65

                self.listLocation = selectedPieces[0]
                verificationID = piecesCoords.index("{} {}".format(verificationIDX, kingCurrentCoords[1]))
                selectedPieces.append(verificationID)
                self.pieceSwap("Normal")
                ProChess.resetVerification()
                container.delete("VerificationLine")
                self.castleVerification = False

            elif self.id == 7 or self.id == 63: # Short castle
                rookID = selectedPieces.pop(1)
                container.unbind("<Motion>")
                # First the king piece is swapped
                kingCurrentCoords = piecesArray[self.listLocation].getPieceCoords() # Gets the coords of the king that is castling
                verificationIDX = kingCurrentCoords[0] + 130

                verificationID = piecesCoords.index("{} {}".format(verificationIDX, kingCurrentCoords[1]))
                selectedPieces.append(verificationID)
                self.pieceSwap("Castle")

                # Second the Rook is swapped to complete the castle
                selectedPieces = [rookID]
                kingCurrentCoords = piecesArray[self.listLocation].getPieceCoords() # Gets the coords of the king after it has moved
                verificationIDX = kingCurrentCoords[0] - 65

                self.listLocation = selectedPieces[0]
                verificationID = piecesCoords.index("{} {}".format(verificationIDX, kingCurrentCoords[1]))
                selectedPieces.append(verificationID)
                self.pieceSwap("Normal")
                ProChess.resetVerification()
                container.delete("VerificationLine")
                self.castleVerification = False

        #Goes here when the first piece is selected so the image tracks the cursor
        elif len(selectedPieces) == 1 and self.getPieceType() != "Placeholder" and self.getPieceColour() == playerTurn and self.castleVerification == False:
            self.createVerification("Normal")
            self.raiseImageStack() # Makes the selected piece higher in the image stack so it appears higher than the other images
            self.motionTrack = 1
            container.itemconfig(self.pieceImage, image = self.selectionImage)
            container.bind("<Motion>", self.pieceCursor)
        elif len(selectedPieces) == 1 and self.getPieceColour() != playerTurn:
            selectedPieces = []
            self.createWrongSelect()
            print("Guitar")
        #Goes here when the second piece is selected
        elif len(selectedPieces) == 2 and self.canMoveHere == True or self.kingCanMoveHere == True:
            # Checks if the piece to move to is an empty space and the same colour,
            # if this is the case the selected pieces will be reset
            if self.getPieceType() != "Placeholder" and self.getPieceColour() == piecesArray[self.listLocation].getPieceColour():
                selectedPieces = [selectedPieces[0]]
                self.createWrongSelect()
                print("Chicken")
            else:
                container.delete("VerificationLine")
                # Checks if the this piece is not an empty square and its the opposite colour of the peice that wants to move here
                # If it is this piece will be reset to an empty square
                if self.pieceColour != piecesArray[self.listLocation].getPieceColour() and self.pieceColour != "None":
                    self.removePiece()
                self.motionTrack = 1
                container.unbind("<Motion>") # De-links the piece icon from the cursor
                ProChess.resetVerification() # Resets all squares on the board to where no piece can move
                self.pieceSwap("Normal")
        elif len(selectedPieces) == 2 and self.canMoveHere != True:
            selectedPieces = [selectedPieces[0]]
            self.createWrongSelect()
            print("Weasel")

    def pieceDeSelect(self):
        """Deselects this piece if it is currently selected"""
        global selectedPieces

        self.motionTrack = 0
        container.unbind("<Motion>")
        self.updateImage()
        # Moves back the piece to its orginal spot
        container.coords(self.pieceImage, self.yCoord, self.xCoord)

        container.delete("VerificationLine")
        ProChess.resetVerification()
        selectedPieces = []

        if self.getPieceType() == "King":
            self.resetCastlingAttributes()

    def createWrongSelect(self):
        container.create_image(self.yCoord, self.xCoord, image = wrongSelect,
                               anchor = "center", tag = "WrongSelect")
        #Deletes the red sqaure border after 500 ms
        container.after(500, lambda: container.delete("WrongSelect"))

    def pieceSwap(self, mode):
        """Method for swapping two selected pieces"""
        global selectedPieces, gameStarted

        gameStarted = True
        container.delete("CorrectSelect")   
        if piecesArray[self.listLocation].getPieceType() == "Pawn":
            piecesArray[self.listLocation].setPieceMoved()

        # Checking for promotion
        if piecesArray[self.listLocation].getPieceType() == "Pawn":
            print(piecesArray[selectedPieces[1]].getPieceCoords())
            if (piecesArray[selectedPieces[1]].getPieceCoords())[1] == 32.5 or (piecesArray[selectedPieces[1]].getPieceCoords())[1] == 422.5:
                # id, xCoord, yCoord, imageVar, piece, pieceColour
                piecesArray[self.listLocation].destroyImage()
                piecesArray.append(Queen(piecesArray[self.listLocation].getPieceID(), (piecesArray[selectedPieces[1]].getPieceCoords())[1], (piecesArray[selectedPieces[1]].getPieceCoords())[0], whiteQueen, "Queen", piecesArray[self.listLocation].getPieceColour()))

        piecesArray[self.listLocation].updateImage()
        #Gets the coordiantes of the second selected piece
        pieceNewLocation = piecesArray[selectedPieces[1]].getPieceCoords()
        #Gets the coordinates of the first selected piece
        pieceOldLocation = piecesArray[self.listLocation].getPieceCoords()
        piecesArray[self.listLocation].moveChessPiece(pieceNewLocation)
        piecesArray[selectedPieces[1]].moveChessPiece(pieceOldLocation)
        piecesArray[selectedPieces[1]].arraySwap()
        if mode == "Normal":
            ProChess.swapPlayerTurn()

    def arraySwap(self):
        """Swaps the coordinates of the 2 selected pieces in the piecesCoords array"""

        originalArrayIndex = piecesArray[self.listLocation].getPieceID()
        temp = piecesCoords[self.getPieceID()]
        piecesCoords[self.getPieceID()] = piecesCoords[originalArrayIndex]
        piecesCoords[originalArrayIndex] = temp

    def moveChessPiece(self, newCoords):
        """Method for actually moving the pieces"""

        # Moves the image to the coordinates that are passed through
        container.coords(self.pieceImage, newCoords)
        self.yCoord = newCoords[0]
        self.xCoord = newCoords[1]

    def removePiece(self):
        """Sets the piece to an empty square"""
        global piecesWhiteTaken, piecesBlackTaken

        # Puts the taken piece into the taken list so it can be placed on the side-menu
        if self.getPieceColour() == "White":
            piecesBlackTaken.append(self.takenImage)
        else:
            piecesWhiteTaken.append(self.takenImage)
        ProChess.updatesPiecesTakenGrid(self.getPieceColour())


        #Sets the attributes to an empty pieces
        self.piece = "Placeholder"
        self.pieceColour = "None"
        self.imageVar = piecePlaceholder
        # Updates the image once the attributes have been changed
        self.updateImage()

    def updateImage(self):
        """Updates the image associated with the ChessPiece object"""
        container.itemconfig(self.pieceImage, image = self.imageVar)

    def pieceCursor(self, event):
        """Sets the pices location to that of the cursor"""
        container.coords(self.pieceImage, event.x + 20, event.y - 12)
        # Can only stay in a loop if the motionTrack is set to 1
        if self.motionTrack == 0:
            container.after(0.1, self.pieceCursor)

class Pawn(ChessPiece):
    def __init__(self, id, xCoord, yCoord, imageVar, piece, pieceColour):
        ChessPiece.__init__(self, id, xCoord, yCoord, imageVar, piece, pieceColour)
        # This is required for the pawn chess piece as it can move 2 spaces from the start
        self.pieceMoved = False
        # This is the amount that the Pawn piece type can move up and down (row)
        self.amountCanMoveRow = 65
        # This is the amount that the Pawn piece type can move left and right (column)
        self.amountCanMoveCol = 65

    def createVerification(self, type):
        veriNormalCheck = True
        veriNECheck = True
        veriNWCheck = True
        currentCoords = self.getPieceCoords()
        if self.pieceMoved == False:
            if self.getPieceColour() == "White":
                # Gets the coordinates of all of the pieces nearby that it could move to
                verificationIDClose = currentCoords[1] - self.amountCanMoveCol
                verificationIDFar = currentCoords[1] - (self.amountCanMoveCol * 2) # Because the piece hasnt moved before the pawn can move 2 spaces infront
                verificationIDNEY = currentCoords[1] - self.amountCanMoveCol
                verificationIDNEX = currentCoords[0] - self.amountCanMoveRow
                verificationIDNWY = currentCoords[1] - self.amountCanMoveCol
                verificationIDNWX = currentCoords[0] + self.amountCanMoveRow
            else:
                verificationIDClose = currentCoords[1] + self.amountCanMoveCol
                verificationIDFar = currentCoords[1] + (self.amountCanMoveCol * 2)
                verificationIDNEY = currentCoords[1] + self.amountCanMoveCol
                verificationIDNEX = currentCoords[0] + self.amountCanMoveRow
                verificationIDNWY = currentCoords[1] + self.amountCanMoveCol
                verificationIDNWX = currentCoords[0] - self.amountCanMoveRow
            try: # Gets the ID of the North East diagonal piece, if this doesnt exist then it moves onto the next
                verificationIDNE = piecesCoords.index("{} {}".format(verificationIDNEX, verificationIDNEY))
            except:
                veriNECheck = False
                verificationIDNE = 0
            try: # Gets the ID of the North West diagonal piece, if this doesnt exist then it moves onto the next
                verificationIDNW = piecesCoords.index("{} {}".format(verificationIDNWX, verificationIDNWY))
            except:
                veriNWCheck = False
                verificationIDNW = 0
            if veriNormalCheck == False and veriNECheck == False and veriNWCheck == False:
                pass
            # Using the ID of the pieces it sets that pieces canMoveHere to true and generates a verification line there
            # If the ID get failed before it will not attempt to set the piece attributes here
            if piecesArray[verificationIDNE].getPieceType() != "Placeholder" and piecesArray[verificationIDNE].getPieceColour() != self.getPieceColour():
                piecesArray[verificationIDNE].allowPieceMovement(self.getPieceID())
                if type == "Normal":
                    piecesArray[verificationIDNE].createVerificationSquare()
            if piecesArray[verificationIDNW].getPieceType() != "Placeholder" and piecesArray[verificationIDNW].getPieceColour() != self.getPieceColour():
                piecesArray[verificationIDNW].allowPieceMovement(self.getPieceID())
                if type == "Normal":
                    piecesArray[verificationIDNW].createVerificationSquare()

            verificationIDClose = piecesCoords.index("{} {}".format(currentCoords[0], verificationIDClose))
            verificationIDFar = piecesCoords.index("{} {}".format(currentCoords[0], verificationIDFar))
            if piecesArray[verificationIDClose].getPieceType() == "Placeholder":
                piecesArray[verificationIDClose].allowPieceMovement(self.getPieceID())
                if type == "Normal":
                    piecesArray[verificationIDClose].createVerificationSquare()
            if piecesArray[verificationIDFar].getPieceType() == "Placeholder":
                if type == "Normal":
                    piecesArray[verificationIDFar].createVerificationSquare()
                piecesArray[verificationIDFar].allowPieceMovement(self.getPieceID())
        else:
            if self.getPieceColour() == "White":
                # Gets the coordinates of the nearby pieces when the Pawn has already moved
                verificationIDNormal = currentCoords[1] - self.amountCanMoveCol
                verificationIDNEY = currentCoords[1] - self.amountCanMoveCol
                verificationIDNEX = currentCoords[0] - self.amountCanMoveRow
                verificationIDNWY = currentCoords[1] - self.amountCanMoveCol
                verificationIDNWX = currentCoords[0] + self.amountCanMoveRow
            else:
                verificationIDNormal = currentCoords[1] + self.amountCanMoveCol
                verificationIDNEY = currentCoords[1] + self.amountCanMoveCol
                verificationIDNEX = currentCoords[0] + self.amountCanMoveRow
                verificationIDNWY = currentCoords[1] + self.amountCanMoveCol
                verificationIDNWX = currentCoords[0] - self.amountCanMoveRow
            try:
                verificationIDNormal = piecesCoords.index("{} {}".format(currentCoords[0], verificationIDNormal))
            except:
                veriNormalCheck = False
                verificationIDNormal = 0
            try:
                verificationIDNE = piecesCoords.index("{} {}".format(verificationIDNEX, verificationIDNEY))
            except:
                veriNECheck = False
                verificationIDNE = 0
            try:
                verificationIDNW = piecesCoords.index("{} {}".format(verificationIDNWX, verificationIDNWY))
            except:
                veriNWCheck = False
                verificationIDNW = 0
            if veriNormalCheck == False and veriNECheck == False and veriNWCheck == False:
                pass
            if piecesArray[verificationIDNormal].getPieceType() == "Placeholder":
                piecesArray[verificationIDNormal].allowPieceMovement(self.getPieceID())
                if type == "Normal":
                    piecesArray[verificationIDNormal].createVerificationSquare()
            if piecesArray[verificationIDNE].getPieceType() != "Placeholder" and piecesArray[verificationIDNE].getPieceColour() != self.getPieceColour():
                piecesArray[verificationIDNE].allowPieceMovement(self.getPieceID())
                if type == "Normal":
                    piecesArray[verificationIDNE].createVerificationSquare()
            if piecesArray[verificationIDNW].getPieceType() != "Placeholder" and piecesArray[verificationIDNW].getPieceColour() != self.getPieceColour():
                piecesArray[verificationIDNW].allowPieceMovement(self.getPieceID())
                if type == "Normal":
                    piecesArray[verificationIDNW].createVerificationSquare()

    def setPieceMoved(self):
        """Sets pieceMoved to True"""
        self.pieceMoved = True

    def setFalsePieceMoved(self):
        """Resets the pieceMoved to False, for when the board resets"""
        self.pieceMoved = False

class Knight(ChessPiece):
    def __init__(self, id, xCoord, yCoord, imageVar, piece, pieceColour):
        ChessPiece.__init__(self, id, xCoord, yCoord, imageVar, piece, pieceColour)
        self.maxCanMoveRow = 130
        self.maxCanMoveCol = 130

    def createVerification(self, type):
        doingUpLeft = True
        doingUpRight = False
        doingDownLeft = False
        doingDownRight = False
        currentCoords = self.getPieceCoords()

        for i in range(4):
            canDoClose = True
            canDoFar = True
            if doingUpLeft == True:
                if self.getPieceColour() == "White":
                    # Gets the coordinates of the possible 2 moves the knight could make in the top left portion
                    verificationIDCloseY = currentCoords[1] - self.maxCanMoveRow
                    verificationIDCloseX = currentCoords[0] - 65
                    verificationIDFarY = verificationIDCloseY + 65
                    verificationIDFarX = verificationIDCloseX - 65
                else:
                    verificationIDCloseY = currentCoords[1] + self.maxCanMoveRow
                    verificationIDCloseX = currentCoords[0] + 65
                    verificationIDFarY = verificationIDCloseY - 65
                    verificationIDFarX = verificationIDCloseX + 65
                try:
                    verificationIDClose = piecesCoords.index("{} {}".format(verificationIDCloseX, verificationIDCloseY))
                except:
                    canDoClose = False
                    verificationIDClose = 0
                try:
                    verificationIDFar = piecesCoords.index("{} {}".format(verificationIDFarX, verificationIDFarY))
                except:
                    canDoFar = False
                    verificationIDFar = 0
                # If the IDs exist then these pieces are changed to canMoveHere and a verification line is generated there
                if canDoClose == True and piecesArray[verificationIDClose].getPieceType() == "Placeholder" or piecesArray[verificationIDClose].getPieceColour() != self.getPieceColour():
                    piecesArray[verificationIDClose].allowPieceMovement(self.getPieceID())
                    if type == "Normal":
                        piecesArray[verificationIDClose].createVerificationSquare()
                if canDoFar == True and piecesArray[verificationIDFar].getPieceType() == "Placeholder" or piecesArray[verificationIDFar].getPieceColour() != self.getPieceColour():
                    piecesArray[verificationIDFar].allowPieceMovement(self.getPieceID())
                    if type == "Normal":
                        piecesArray[verificationIDFar].createVerificationSquare()
                doingUpLeft = False
                doingUpRight = True

            if doingUpRight == True:
                if self.getPieceColour() == "White":
                    # Also grabs the coordinates but of the 2 pieces in the top right portion
                    verificationIDCloseY = currentCoords[1] - self.maxCanMoveRow
                    verificationIDCloseX = currentCoords[0] + 65
                    verificationIDFarY = verificationIDCloseY + 65
                    verificationIDFarX = verificationIDCloseX + 65
                else:
                    verificationIDCloseY = currentCoords[1] + self.maxCanMoveRow
                    verificationIDCloseX = currentCoords[0] - 65
                    verificationIDFarY = verificationIDCloseY - 65
                    verificationIDFarX = verificationIDCloseX - 65
                try:
                    verificationIDClose = piecesCoords.index("{} {}".format(verificationIDCloseX, verificationIDCloseY))
                except:
                    canDoClose = False
                    verificationIDClose = 0
                try:
                    verificationIDFar = piecesCoords.index("{} {}".format(verificationIDFarX, verificationIDFarY))
                except:
                    canDoFar = False
                    verificationIDFar = 0
                if canDoClose == True and piecesArray[verificationIDClose].getPieceType() == "Placeholder" or piecesArray[verificationIDClose].getPieceColour() != self.getPieceColour():
                    piecesArray[verificationIDClose].allowPieceMovement(self.getPieceID())
                    if type == "Normal":
                        piecesArray[verificationIDClose].createVerificationSquare()
                if canDoFar == True and piecesArray[verificationIDFar].getPieceType() == "Placeholder" or piecesArray[verificationIDFar].getPieceColour() != self.getPieceColour():
                    piecesArray[verificationIDFar].allowPieceMovement(self.getPieceID())
                    if type == "Normal":
                        piecesArray[verificationIDFar].createVerificationSquare()
                doingUpRight = False
                doingDownLeft = True

            if doingDownLeft == True:
                if self.getPieceColour() == "White":
                    # Also grabs the coordinates but of the 2 pieces in the bottom left portion
                    verificationIDCloseY = currentCoords[1] + self.maxCanMoveRow
                    verificationIDCloseX = currentCoords[0] - 65
                    verificationIDFarY = verificationIDCloseY - 65
                    verificationIDFarX = verificationIDCloseX - 65
                else:
                    verificationIDCloseY = currentCoords[1] - self.maxCanMoveRow
                    verificationIDCloseX = currentCoords[0] + 65
                    verificationIDFarY = verificationIDCloseY + 65
                    verificationIDFarX = verificationIDCloseX + 65
                try:
                    verificationIDClose = piecesCoords.index("{} {}".format(verificationIDCloseX, verificationIDCloseY))
                except:
                    canDoClose = False
                    verificationIDClose = 0
                try:
                    verificationIDFar = piecesCoords.index("{} {}".format(verificationIDFarX, verificationIDFarY))
                except:
                    canDoFar = False
                    verificationIDFar = 0
                if canDoClose == True and piecesArray[verificationIDClose].getPieceType() == "Placeholder" or piecesArray[verificationIDClose].getPieceColour() != self.getPieceColour():
                    piecesArray[verificationIDClose].allowPieceMovement(self.getPieceID())
                    if type == "Normal":
                        piecesArray[verificationIDClose].createVerificationSquare()
                if canDoFar == True and piecesArray[verificationIDFar].getPieceType() == "Placeholder" or piecesArray[verificationIDFar].getPieceColour() != self.getPieceColour():
                    piecesArray[verificationIDFar].allowPieceMovement(self.getPieceID())
                    if type == "Normal":
                        piecesArray[verificationIDFar].createVerificationSquare()
                doingDownLeft = False
                doingDownRight = True

            if doingDownRight == True:
                if self.getPieceColour() == "White":
                    # Also grabs the coordinates but of the 2 pieces in the bottom right portion
                    verificationIDCloseY = currentCoords[1] + self.maxCanMoveRow
                    verificationIDCloseX = currentCoords[0] + 65
                    verificationIDFarY = verificationIDCloseY - 65
                    verificationIDFarX = verificationIDCloseX + 65
                else:
                    verificationIDCloseY = currentCoords[1] - self.maxCanMoveRow
                    verificationIDCloseX = currentCoords[0] - 65
                    verificationIDFarY = verificationIDCloseY + 65
                    verificationIDFarX = verificationIDCloseX - 65
                try:
                    verificationIDClose = piecesCoords.index("{} {}".format(verificationIDCloseX, verificationIDCloseY))
                except:
                    canDoClose = False
                    verificationIDClose = 0
                try:
                    verificationIDFar = piecesCoords.index("{} {}".format(verificationIDFarX, verificationIDFarY))
                except:
                    canDoFar = False
                    verificationIDFar = 0
                if canDoClose == True and piecesArray[verificationIDClose].getPieceType() == "Placeholder" or piecesArray[verificationIDClose].getPieceColour() != self.getPieceColour():
                    piecesArray[verificationIDClose].allowPieceMovement(self.getPieceID())
                    if type == "Normal":
                        piecesArray[verificationIDClose].createVerificationSquare()
                if canDoFar == True and piecesArray[verificationIDFar].getPieceType() == "Placeholder" or piecesArray[verificationIDFar].getPieceColour() != self.getPieceColour():
                    piecesArray[verificationIDFar].allowPieceMovement(self.getPieceID())
                    if type == "Normal":
                        piecesArray[verificationIDFar].createVerificationSquare()
                doingDownRight = False

class Rook(ChessPiece):
    def __init__(self, id, xCoord, yCoord, imageVar, piece, pieceColour):
        ChessPiece.__init__(self, id, xCoord, yCoord, imageVar, piece, pieceColour)
        self.maxSpacesCanMove = 8

    def createVerification(self, type):
        doingNorth = True
        doingEast = False
        doingSouth = False
        doingWest = False
        loopCompleted = False
        verificationFullyCreated = False
        lastVerification = None

        while verificationFullyCreated == False:
            # Because the rook can move as far as possible in the vertical and horizontal directions
            # The verificationID is used from the last iteration only if doing the same direction
            if loopCompleted == True:
                currentCoords = piecesArray[verificationID].getPieceCoords()
                lastVerification = verificationID
            else:
                currentCoords = self.getPieceCoords()
                lastVerification = None
            loopCompleted = True
            
            if doingNorth == True:
                if self.getPieceColour() == "White":
                    # Gets the coordniates of 1 infront or 1 behind if colour is black
                    verificationID = currentCoords[1] - 65
                else:
                    verificationID = currentCoords[1] + 65
                try:
                    # Gets the ID of this coordinate
                    verificationID = piecesCoords.index("{} {}".format(currentCoords[0], verificationID))
                except:
                    doingNorth = False
                    doingEast = True
                    loopCompleted = False
                if doingNorth == True:
                    if piecesArray[verificationID].getPieceType() == "Placeholder": 
                    # Carries on iterating if its an empty space, whilst allowing the peice to move here
                        if lastVerification != None:
                            piecesArray[lastVerification].setNextVerification(verificationID)
                        piecesArray[verificationID].allowPieceMovement(self.getPieceID())
                        if type == "Normal":
                            piecesArray[verificationID].createVerificationSquare()
                    elif piecesArray[verificationID].getPieceType() != "Placeholder" and piecesArray[verificationID].getPieceColour() != self.getPieceColour():
                    # If the current piece is of a diffrent colour but no an empty sqaure then genereate verification on the piece but stop iterating    
                        piecesArray[verificationID].allowPieceMovement(self.getPieceID())
                        if lastVerification != None:
                            piecesArray[lastVerification].setNextVerification(verificationID)
                        if type == "Normal":
                            piecesArray[verificationID].createVerificationSquare()
                        doingNorth = False
                        doingEast = True
                        loopCompleted = False
                    elif piecesArray[verificationID].getPieceType() != "Placeholder" and piecesArray[verificationID].getPieceColour() == self.getPieceColour():
                    # If the current piece is of the same colour then iterating stops    
                        doingNorth = False
                        doingEast = True
                        loopCompleted = False

            elif doingEast == True:
                if self.getPieceColour() == "White":
                    # Gets the coordinate of the piece to the left, right if its black
                    verificationID = currentCoords[0] + 65
                else:
                    verificationID = currentCoords[0] - 65
                try:
                    verificationID = piecesCoords.index("{} {}".format(verificationID, currentCoords[1]))
                except:
                    doingEast = False
                    doingSouth = True
                    loopCompleted = False
                if doingEast == True:
                    if piecesArray[verificationID].getPieceType() == "Placeholder":
                        piecesArray[verificationID].allowPieceMovement(self.getPieceID())
                        if lastVerification != None:
                            piecesArray[lastVerification].setNextVerification(verificationID)
                        if type == "Normal":
                            piecesArray[verificationID].createVerificationSquare()
                    elif piecesArray[verificationID].getPieceType() != "Placeholder" and piecesArray[verificationID].getPieceColour() != self.getPieceColour():
                        piecesArray[verificationID].allowPieceMovement(self.getPieceID())
                        if lastVerification != None:
                            piecesArray[lastVerification].setNextVerification(verificationID)
                        if type == "Normal":
                            piecesArray[verificationID].createVerificationSquare()
                        doingEast = False
                        doingSouth = True
                        loopCompleted = False
                    elif piecesArray[verificationID].getPieceType() != "Placeholder" and piecesArray[verificationID].getPieceColour() == self.getPieceColour():
                        doingEast = False
                        doingSouth = True
                        loopCompleted = False

            elif doingSouth == True:
                if self.getPieceColour() == "White":
                    # Gets the coordinate of the piece 1 down, or 1 up if black
                    verificationID = currentCoords[1] + 65
                else:
                    verificationID = currentCoords[1] - 65
                try:
                    verificationID = piecesCoords.index("{} {}".format(currentCoords[0], verificationID))
                except:
                    doingSouth = False
                    doingWest = True
                    loopCompleted = False
                if doingSouth == True:
                    if piecesArray[verificationID].getPieceType() == "Placeholder":
                        piecesArray[verificationID].allowPieceMovement(self.getPieceID())
                        if lastVerification != None:
                            piecesArray[lastVerification].setNextVerification(verificationID)
                        if type == "Normal":
                            piecesArray[verificationID].createVerificationSquare()
                    elif piecesArray[verificationID].getPieceType() != "Placeholder" and piecesArray[verificationID].getPieceColour() != self.getPieceColour():
                        piecesArray[verificationID].allowPieceMovement(self.getPieceID())
                        if lastVerification != None:
                            piecesArray[lastVerification].setNextVerification(verificationID)
                        if type == "Normal":
                            piecesArray[verificationID].createVerificationSquare()
                        doingSouth = False
                        doingWest = True
                        loopCompleted = False
                    elif piecesArray[verificationID].getPieceType() != "Placeholder" and piecesArray[verificationID].getPieceColour() == self.getPieceColour():
                        doingSouth = False
                        doingWest = True
                        loopCompleted = False

            elif doingWest == True:
                if self.getPieceColour() == "White":
                    # Gets the coordinates of the piece 1 to the right, or left if black
                    verificationID = currentCoords[0] - 65
                else:
                    verificationID = currentCoords[0] + 65
                try:
                    verificationID = piecesCoords.index("{} {}".format(verificationID, currentCoords[1]))
                except:
                    doingWest = False
                    loopCompleted = False
                if doingWest == True:
                    if piecesArray[verificationID].getPieceType() == "Placeholder":
                        piecesArray[verificationID].allowPieceMovement(self.getPieceID())
                        if lastVerification != None:
                            piecesArray[lastVerification].setNextVerification(verificationID)
                        if type == "Normal":
                            piecesArray[verificationID].createVerificationSquare()
                    elif piecesArray[verificationID].getPieceType() != "Placeholder" and piecesArray[verificationID].getPieceColour() != self.getPieceColour():
                        piecesArray[verificationID].allowPieceMovement(self.getPieceID())
                        if lastVerification != None:
                            piecesArray[lastVerification].setNextVerification(verificationID)
                        if type == "Normal":
                            piecesArray[verificationID].createVerificationSquare()
                        doingWest = False
                        loopCompleted = False
                    elif piecesArray[verificationID].getPieceType() != "Placeholder" and piecesArray[verificationID].getPieceColour() == self.getPieceColour():
                        doingWest = False
                        loopCompleted = False
            else:
                # If all directions are done then it comes out of the while loop
                verificationFullyCreated = True
                
class Bishop(ChessPiece):
    def __init__(self, id, xCoord, yCoord, imageVar, piece, pieceColour):
        ChessPiece.__init__(self, id, xCoord, yCoord, imageVar, piece, pieceColour)

    def createVerification(self, type):
        doingNorth = True
        doingEast = False
        doingSouth = False
        doingWest = False
        loopCompleted = False
        verificationFullyCreated = False

        while verificationFullyCreated == False:
            # Because the bishop can move as far as possible in all diagonal directions
            # The verificationID is used from the last iteration only if doing the same direction
            if loopCompleted == True:
                currentCoords = piecesArray[verificationID].getPieceCoords()
                lastVerification = verificationID
            else:
                currentCoords = self.getPieceCoords()
                lastVerification = None
            loopCompleted = True
            
            if doingNorth == True:
                if self.getPieceColour() == "White":
                    # Gets the coordinates of the piece diagonally to up, or down if black
                    verificationIDX = currentCoords[0] + 65
                    verificationIDY = currentCoords[1] - 65
                else:
                    verificationIDX = currentCoords[0] - 65
                    verificationIDY = currentCoords[1] + 65
                # Gets the ID of the coordinate gotten
                try:
                    verificationID = piecesCoords.index("{} {}".format(verificationIDX, verificationIDY))
                except:
                    doingNorth = False
                    doingEast = True
                    loopCompleted = False
                if doingNorth == True:
                    if piecesArray[verificationID].getPieceType() == "Placeholder":
                    # If the piece is an empty square then iteration continues, and creates verification here
                        piecesArray[verificationID].allowPieceMovement(self.getPieceID())
                        if lastVerification != None:
                            piecesArray[lastVerification].setNextVerification(verificationID)
                        if type == "Normal":
                            piecesArray[verificationID].createVerificationSquare()
                    elif piecesArray[verificationID].getPieceType() != "Placeholder" and piecesArray[verificationID].getPieceColour() != self.getPieceColour():
                    # If the piece colour is the opposite and its not an empty square, iteration stops but verification is created here    
                        piecesArray[verificationID].allowPieceMovement(self.getPieceID())
                        if lastVerification != None:
                            piecesArray[lastVerification].setNextVerification(verificationID)
                        if type == "Normal":
                            piecesArray[verificationID].createVerificationSquare()
                        doingNorth = False
                        doingEast = True
                        loopCompleted = False
                    elif piecesArray[verificationID].getPieceType() != "Placeholder" and piecesArray[verificationID].getPieceColour() == self.getPieceColour():
                    # If the piece colour is the same and its not an empty square, then iteration stops    
                        doingNorth = False
                        doingEast = True
                        loopCompleted = False

            elif doingEast == True:
                if self.getPieceColour() == "White":
                    # Gets the coordinates of the piece diagonally down to the right, left if black
                    verificationIDX = currentCoords[0] + 65
                    verificationIDY = currentCoords[1] + 65
                else:
                    verificationIDX = currentCoords[0] - 65
                    verificationIDY = currentCoords[1] - 65
                try:
                    verificationID = piecesCoords.index("{} {}".format(verificationIDX, verificationIDY))
                except:
                    doingEast = False
                    doingSouth = True
                    loopCompleted = False
                if doingEast == True:
                    if piecesArray[verificationID].getPieceType() == "Placeholder":
                        piecesArray[verificationID].allowPieceMovement(self.getPieceID())
                        if lastVerification != None:
                            piecesArray[lastVerification].setNextVerification(verificationID)
                        if type == "Normal":
                            piecesArray[verificationID].createVerificationSquare()
                    elif piecesArray[verificationID].getPieceType() != "Placeholder" and piecesArray[verificationID].getPieceColour() != self.getPieceColour():
                        piecesArray[verificationID].allowPieceMovement(self.getPieceID())
                        if lastVerification != None:
                            piecesArray[lastVerification].setNextVerification(verificationID)
                        if type == "Normal":
                            piecesArray[verificationID].createVerificationSquare()
                        doingEast = False
                        doingSouth = True
                        loopCompleted = False
                    elif piecesArray[verificationID].getPieceType() != "Placeholder" and piecesArray[verificationID].getPieceColour() == self.getPieceColour():
                        doingEast = False
                        doingSouth = True
                        loopCompleted = False

            elif doingSouth == True:
                if self.getPieceColour() == "White":
                    # Gets the coordinate of the piece diagonally to the right, left if black
                    verificationIDX = currentCoords[0] - 65
                    verificationIDY = currentCoords[1] + 65
                else:
                    verificationIDX = currentCoords[0] + 65
                    verificationIDY = currentCoords[1] - 65
                try:
                    verificationID = piecesCoords.index("{} {}".format(verificationIDX, verificationIDY))
                except:
                    doingSouth = False
                    doingWest = True
                    loopCompleted = False
                if doingSouth == True:
                    if piecesArray[verificationID].getPieceType() == "Placeholder":
                        piecesArray[verificationID].allowPieceMovement(self.getPieceID())
                        if lastVerification != None:
                            piecesArray[lastVerification].setNextVerification(verificationID)
                        if type == "Normal":
                            piecesArray[verificationID].createVerificationSquare()
                    elif piecesArray[verificationID].getPieceType() != "Placeholder" and piecesArray[verificationID].getPieceColour() != self.getPieceColour():
                        piecesArray[verificationID].allowPieceMovement(self.getPieceID())
                        if lastVerification != None:
                            piecesArray[lastVerification].setNextVerification(verificationID)
                        if type == "Normal":
                            piecesArray[verificationID].createVerificationSquare()
                        doingSouth = False
                        doingWest = True
                        loopCompleted = False
                    elif piecesArray[verificationID].getPieceType() != "Placeholder" and piecesArray[verificationID].getPieceColour() == self.getPieceColour():
                        doingSouth = False
                        doingWest = True
                        loopCompleted = False

            elif doingWest == True:
                if self.getPieceColour() == "White":
                    # Gets the coordinate of the peice diagonally up to the left, right if black
                    verificationIDX = currentCoords[0] - 65
                    verificationIDY = currentCoords[1] - 65
                else:
                    verificationIDX = currentCoords[0] + 65
                    verificationIDY = currentCoords[1] + 65
                try:
                    verificationID = piecesCoords.index("{} {}".format(verificationIDX, verificationIDY))
                except:
                    doingWest = False
                    loopCompleted = False
                if doingWest == True:
                    if piecesArray[verificationID].getPieceType() == "Placeholder":
                        piecesArray[verificationID].allowPieceMovement(self.getPieceID())
                        if lastVerification != None:
                            piecesArray[lastVerification].setNextVerification(verificationID)
                        if type == "Normal":
                            piecesArray[verificationID].createVerificationSquare()
                    elif piecesArray[verificationID].getPieceType() != "Placeholder" and piecesArray[verificationID].getPieceColour() != self.getPieceColour():
                        piecesArray[verificationID].allowPieceMovement(self.getPieceID())
                        if lastVerification != None:
                            piecesArray[lastVerification].setNextVerification(verificationID)
                        if type == "Normal":
                            piecesArray[verificationID].createVerificationSquare()
                        doingWest = False
                        loopCompleted = False
                    elif piecesArray[verificationID].getPieceType() != "Placeholder" and piecesArray[verificationID].getPieceColour() == self.getPieceColour():
                        doingWest = False
                        loopCompleted = False
            else:
                # If all directions are done, it comes out of the while loop
                verificationFullyCreated = True

class Queen(ChessPiece):
    def __init__(self, id, xCoord, yCoord, imageVar, piece, pieceColour):
        ChessPiece.__init__(self, id, xCoord, yCoord, imageVar, piece, pieceColour)

    def createVerification(self, type):
        doingNorth = True
        doingNE = False
        doingEast = False
        doingSE = False
        doingSouth = False
        doingSW = False
        doingWest = False
        doingNW = False
        loopCompleted = False
        verificationFullyCreated = False

        while verificationFullyCreated == False:
            # Because the queen can move as far as possible in the vertical, horizontal, and diagonal directions
            # The verificationID is used from the last iteration only if doing the same direction
            if loopCompleted == True:
                currentCoords = piecesArray[verificationID].getPieceCoords()
                lastVerification = verificationID
            else:
                currentCoords = self.getPieceCoords()
                lastVerification = None
            loopCompleted = True
            
            if doingNorth == True:
                if self.getPieceColour() == "White":
                    # Gets the coordinates of the piece 1 up, or down if black
                    verificationID = currentCoords[1] - 65
                else:
                    verificationID = currentCoords[1] + 65
                # Gets the ID of the gotten coordinates
                try:
                    verificationID = piecesCoords.index("{} {}".format(currentCoords[0], verificationID))
                except:
                    doingNorth = False
                    doingNE = True
                    loopCompleted = False
                if doingNorth == True:
                    if piecesArray[verificationID].getPieceType() == "Placeholder":
                    # If the piece is an empty square then iteration continues, and verification is generated here
                        piecesArray[verificationID].allowPieceMovement(self.getPieceID())
                        if lastVerification != None:
                            piecesArray[lastVerification].setNextVerification(verificationID)
                        if type == "Normal":
                            piecesArray[verificationID].createVerificationSquare()
                    elif piecesArray[verificationID].getPieceType() != "Placeholder" and piecesArray[verificationID].getPieceColour() != self.getPieceColour():
                    # If the piece is the oppoiste colour and is not an empty square then iteration stops, but verification if created     
                        piecesArray[verificationID].allowPieceMovement(self.getPieceID())
                        if lastVerification != None:
                            piecesArray[lastVerification].setNextVerification(verificationID)
                        if type == "Normal":
                            piecesArray[verificationID].createVerificationSquare()
                        doingNorth = False
                        doingNE = True
                        loopCompleted = False
                    elif piecesArray[verificationID].getPieceType() != "Placeholder" and piecesArray[verificationID].getPieceColour() == self.getPieceColour():
                    # If the piece is the same colour and is not an empty square, iteration stops and moves onto the next direction    
                        doingNorth = False
                        doingNE = True
                        loopCompleted = False

            elif doingNE == True:
                if self.getPieceColour() == "White":
                    # Gets the coordinates of the piece diagonally 1 up, or down if black
                    verificationIDX = currentCoords[0] + 65
                    verificationIDY = currentCoords[1] - 65
                else:
                    verificationIDX = currentCoords[0] - 65
                    verificationIDY = currentCoords[1] + 65
                try:
                    verificationID = piecesCoords.index("{} {}".format(verificationIDX, verificationIDY))
                except:
                    doingNE = False
                    doingEast = True
                    loopCompleted = False
                if doingNE == True:
                    if piecesArray[verificationID].getPieceType() == "Placeholder":
                        piecesArray[verificationID].allowPieceMovement(self.getPieceID())
                        if lastVerification != None:
                            piecesArray[lastVerification].setNextVerification(verificationID)
                        if type == "Normal":
                            piecesArray[verificationID].createVerificationSquare()
                    elif piecesArray[verificationID].getPieceType() != "Placeholder" and piecesArray[verificationID].getPieceColour() != self.getPieceColour():
                        piecesArray[verificationID].allowPieceMovement(self.getPieceID())
                        if lastVerification != None:
                            piecesArray[lastVerification].setNextVerification(verificationID)
                        if type == "Normal":
                            piecesArray[verificationID].createVerificationSquare()
                        doingNE = False
                        doingEast = True
                        loopCompleted = False
                    elif piecesArray[verificationID].getPieceType() != "Placeholder" and piecesArray[verificationID].getPieceColour() == self.getPieceColour():
                        doingNE = False
                        doingEast = True
                        loopCompleted = False

            elif doingEast == True:
                if self.getPieceColour() == "White":
                    # Gets the coordinates of the piece 1 right, or left if black
                    verificationID = currentCoords[0] + 65
                else:
                    verificationID = currentCoords[0] - 65
                try:
                    verificationID = piecesCoords.index("{} {}".format(verificationID, currentCoords[1]))
                except:
                    doingEast = False
                    doingSE = True
                    loopCompleted = False
                if doingEast == True:
                    if piecesArray[verificationID].getPieceType() == "Placeholder":
                        piecesArray[verificationID].allowPieceMovement(self.getPieceID())
                        if lastVerification != None:
                            piecesArray[lastVerification].setNextVerification(verificationID)
                        if type == "Normal":
                            piecesArray[verificationID].createVerificationSquare()
                    elif piecesArray[verificationID].getPieceType() != "Placeholder" and piecesArray[verificationID].getPieceColour() != self.getPieceColour():
                        piecesArray[verificationID].allowPieceMovement(self.getPieceID())
                        if lastVerification != None:
                            piecesArray[lastVerification].setNextVerification(verificationID)
                        if type == "Normal":
                            piecesArray[verificationID].createVerificationSquare()
                        doingEast = False
                        doingSE = True
                        loopCompleted = False
                    elif piecesArray[verificationID].getPieceType() != "Placeholder" and piecesArray[verificationID].getPieceColour() == self.getPieceColour():
                        doingEast = False
                        doingSE = True
                        loopCompleted = False

            elif doingSE == True:
                if self.getPieceColour() == "White":
                    # Gets the coordinates of the piece diagonally 1 down right, or left if black
                    verificationIDX = currentCoords[0] + 65
                    verificationIDY = currentCoords[1] + 65
                else:
                    verificationIDX = currentCoords[0] - 65
                    verificationIDY = currentCoords[1] - 65
                try:
                    verificationID = piecesCoords.index("{} {}".format(verificationIDX, verificationIDY))
                except:
                    doingSE = False
                    doingSouth = True
                    loopCompleted = False
                if doingSE == True:
                    if piecesArray[verificationID].getPieceType() == "Placeholder":
                        piecesArray[verificationID].allowPieceMovement(self.getPieceID())
                        if lastVerification != None:
                            piecesArray[lastVerification].setNextVerification(verificationID)
                        if type == "Normal":
                            piecesArray[verificationID].createVerificationSquare()
                    elif piecesArray[verificationID].getPieceType() != "Placeholder" and piecesArray[verificationID].getPieceColour() != self.getPieceColour():
                        piecesArray[verificationID].allowPieceMovement(self.getPieceID())
                        if lastVerification != None:
                            piecesArray[lastVerification].setNextVerification(verificationID)
                        if type == "Normal":
                            piecesArray[verificationID].createVerificationSquare()
                        doingSE = False
                        doingSouth = True
                        loopCompleted = False
                    elif piecesArray[verificationID].getPieceType() != "Placeholder" and piecesArray[verificationID].getPieceColour() == self.getPieceColour():
                        doingSE = False
                        doingSouth = True
                        loopCompleted = False

            elif doingSouth == True:
                if self.getPieceColour() == "White":
                    # Gets the coordinates of the piece 1 down, or up if black
                    verificationID = currentCoords[1] + 65
                else:
                    verificationID = currentCoords[1] - 65
                try:
                    verificationID = piecesCoords.index("{} {}".format(currentCoords[0], verificationID))
                except:
                    doingSouth = False
                    doingSW = True
                    loopCompleted = False
                if doingSouth == True:
                    if piecesArray[verificationID].getPieceType() == "Placeholder":
                        piecesArray[verificationID].allowPieceMovement(self.getPieceID())
                        if lastVerification != None:
                            piecesArray[lastVerification].setNextVerification(verificationID)
                        if type == "Normal":
                            piecesArray[verificationID].createVerificationSquare()
                    elif piecesArray[verificationID].getPieceType() != "Placeholder" and piecesArray[verificationID].getPieceColour() != self.getPieceColour():
                        piecesArray[verificationID].allowPieceMovement(self.getPieceID())
                        if lastVerification != None:
                            piecesArray[lastVerification].setNextVerification(verificationID)
                        if type == "Normal":
                            piecesArray[verificationID].createVerificationSquare()
                        doingSouth = False
                        doingSW = True
                        loopCompleted = False
                    elif piecesArray[verificationID].getPieceType() != "Placeholder" and piecesArray[verificationID].getPieceColour() == self.getPieceColour():
                        doingSouth = False
                        doingSW = True
                        loopCompleted = False

            elif doingSW == True:
                if self.getPieceColour() == "White":
                    # Gets the coordinates of the piece diagonally 1 down left, or right if black
                    verificationIDX = currentCoords[0] - 65
                    verificationIDY = currentCoords[1] + 65
                else:
                    verificationIDX = currentCoords[0] + 65
                    verificationIDY = currentCoords[1] - 65
                try:
                    verificationID = piecesCoords.index("{} {}".format(verificationIDX, verificationIDY))
                except:
                    doingSW = False
                    doingWest = True
                    loopCompleted = False
                if doingSW == True:
                    if piecesArray[verificationID].getPieceType() == "Placeholder":
                        piecesArray[verificationID].allowPieceMovement(self.getPieceID())
                        if lastVerification != None:
                            piecesArray[lastVerification].setNextVerification(verificationID)
                        if type == "Normal":
                            piecesArray[verificationID].createVerificationSquare()
                    elif piecesArray[verificationID].getPieceType() != "Placeholder" and piecesArray[verificationID].getPieceColour() != self.getPieceColour():
                        piecesArray[verificationID].allowPieceMovement(self.getPieceID())
                        if lastVerification != None:
                            piecesArray[lastVerification].setNextVerification(verificationID)
                        if type == "Normal":
                            piecesArray[verificationID].createVerificationSquare()
                        doingSW = False
                        doingWest = True
                        loopCompleted = False
                    elif piecesArray[verificationID].getPieceType() != "Placeholder" and piecesArray[verificationID].getPieceColour() == self.getPieceColour():
                        doingSW = False
                        doingWest = True
                        loopCompleted = False

            elif doingWest == True:
                if self.getPieceColour() == "White":
                    # Gets the coordinates of the piece 1 left, or right if black
                    verificationID = currentCoords[0] - 65
                else:
                    verificationID = currentCoords[0] + 65
                try:
                    verificationID = piecesCoords.index("{} {}".format(verificationID, currentCoords[1]))
                except:
                    doingWest = False
                    doingNW = True
                    loopCompleted = False
                if doingWest == True:
                    if piecesArray[verificationID].getPieceType() == "Placeholder":
                        piecesArray[verificationID].allowPieceMovement(self.getPieceID())
                        if lastVerification != None:
                            piecesArray[lastVerification].setNextVerification(verificationID)
                        if type == "Normal":
                            piecesArray[verificationID].createVerificationSquare()
                    elif piecesArray[verificationID].getPieceType() != "Placeholder" and piecesArray[verificationID].getPieceColour() != self.getPieceColour():
                        piecesArray[verificationID].allowPieceMovement(self.getPieceID())
                        if lastVerification != None:
                            piecesArray[lastVerification].setNextVerification(verificationID)
                        if type == "Normal":
                            piecesArray[verificationID].createVerificationSquare()
                        doingWest = False
                        doingNW = True
                        loopCompleted = False
                    elif piecesArray[verificationID].getPieceType() != "Placeholder" and piecesArray[verificationID].getPieceColour() == self.getPieceColour():
                        doingWest = False
                        doingNW = True
                        loopCompleted = False

            elif doingNW == True:
                if self.getPieceColour() == "White":
                    # Gets the coordinates of the piece diagonally up left, or right if black
                    verificationIDX = currentCoords[0] - 65
                    verificationIDY = currentCoords[1] - 65
                else:
                    verificationIDX = currentCoords[0] + 65
                    verificationIDY = currentCoords[1] + 65
                try:
                    verificationID = piecesCoords.index("{} {}".format(verificationIDX, verificationIDY))
                except:
                    doingNW = False
                    loopCompleted = False
                if doingNW == True:
                    if piecesArray[verificationID].getPieceType() == "Placeholder":
                        piecesArray[verificationID].allowPieceMovement(self.getPieceID())
                        if lastVerification != None:
                            piecesArray[lastVerification].setNextVerification(verificationID)
                        if type == "Normal":
                            piecesArray[verificationID].createVerificationSquare()
                    elif piecesArray[verificationID].getPieceType() != "Placeholder" and piecesArray[verificationID].getPieceColour() != self.getPieceColour():
                        piecesArray[verificationID].allowPieceMovement(self.getPieceID())
                        if lastVerification != None:
                            piecesArray[lastVerification].setNextVerification(verificationID)
                        if type == "Normal":
                            piecesArray[verificationID].createVerificationSquare()
                        doingNW = False
                        loopCompleted = False
                    elif piecesArray[verificationID].getPieceType() != "Placeholder" and piecesArray[verificationID].getPieceColour() == self.getPieceColour():
                        doingNW = False
                        loopCompleted = False

            else:
                # If all directions have been done then it comes out of the while loop
                verificationFullyCreated = True

class King(ChessPiece):
    def __init__(self, id, xCoord, yCoord, imageVar, piece, pieceColour):
        ChessPiece.__init__(self, id, xCoord, yCoord, imageVar, piece, pieceColour)

        # Attributes to check which type of castle can be performed
        self.canCastleShort = False
        self.canCastleLong = False

    def createVerification(self, type):
        doingUp = True
        doingLeft = False
        doingDown = False
        doingRight = False
        currentCoords = self.getPieceCoords()

        for i in range(4):
            canDoClose = True
            canDoFar = True
            if doingUp == True:
                if self.getPieceColour() == "White":
                    # Gets the coordinates of the pieces 1 up and 1 to the left of that, or down if black
                    verificationIDCloseY = currentCoords[1] - 65
                    verificationIDCloseX = currentCoords[0]
                    verificationIDFarY = verificationIDCloseY 
                    verificationIDFarX = verificationIDCloseX - 65
                else:
                    verificationIDCloseY = currentCoords[1] + 65
                    verificationIDCloseX = currentCoords[0]
                    verificationIDFarY = verificationIDCloseY
                    verificationIDFarX = verificationIDCloseX + 65
                # Gets the IDs of the pieces of the coordinates gotten
                try:
                    verificationIDClose = piecesCoords.index("{} {}".format(verificationIDCloseX, verificationIDCloseY))
                except:
                    canDoClose = False
                    verificationIDClose = 0
                try:
                    verificationIDFar = piecesCoords.index("{} {}".format(verificationIDFarX, verificationIDFarY))
                except:
                    canDoFar = False
                    verificationIDFar = 0
                # If the IDs were gotten the pieces are set to canMoveHere and verfication is generated there
                if canDoClose == True and piecesArray[verificationIDClose].getPieceType() == "Placeholder" or piecesArray[verificationIDClose].getPieceColour() != self.getPieceColour():
                    piecesArray[verificationIDClose].allowKingMovement(self.getPieceID())
                    if type == "Normal":
                        piecesArray[verificationIDClose].createVerificationSquare()
                if canDoFar == True and piecesArray[verificationIDFar].getPieceType() == "Placeholder" or piecesArray[verificationIDFar].getPieceColour() != self.getPieceColour():
                    piecesArray[verificationIDFar].allowKingMovement(self.getPieceID())
                    if type == "Normal":
                        piecesArray[verificationIDFar].createVerificationSquare()
                doingUp = False
                doingRight = True

            if doingRight == True:
                if self.getPieceColour() == "White":
                    # Gets the coordinates of the pieces 1 right and 1 down of that, or left and up if black
                    verificationIDCloseY = currentCoords[1]
                    verificationIDCloseX = currentCoords[0] + 65
                    verificationIDFarY = verificationIDCloseY - 65
                    verificationIDFarX = verificationIDCloseX
                else:
                    verificationIDCloseY = currentCoords[1]
                    verificationIDCloseX = currentCoords[0] - 65
                    verificationIDFarY = verificationIDCloseY + 65
                    verificationIDFarX = verificationIDCloseX
                try:
                    verificationIDClose = piecesCoords.index("{} {}".format(verificationIDCloseX, verificationIDCloseY))
                except:
                    canDoClose = False
                    verificationIDClose = 0
                try:
                    verificationIDFar = piecesCoords.index("{} {}".format(verificationIDFarX, verificationIDFarY))
                except:
                    canDoFar = False
                    verificationIDFar = 0
                if canDoClose == True and piecesArray[verificationIDClose].getPieceType() == "Placeholder" or piecesArray[verificationIDClose].getPieceColour() != self.getPieceColour():
                    piecesArray[verificationIDClose].allowKingMovement(self.getPieceID())
                    if type == "Normal":
                        piecesArray[verificationIDClose].createVerificationSquare()
                if canDoFar == True and piecesArray[verificationIDFar].getPieceType() == "Placeholder" or piecesArray[verificationIDFar].getPieceColour() != self.getPieceColour():
                    piecesArray[verificationIDFar].allowKingMovement(self.getPieceID())
                    if type == "Normal":
                        piecesArray[verificationIDFar].createVerificationSquare()
                doingRight = False
                doingDown = True

            if doingDown == True:
                if self.getPieceColour() == "White":
                    # Gets the coordinates of the pieces 1 down and 1 to the left of that, or up and right if black
                    verificationIDCloseY = currentCoords[1] + 65
                    verificationIDCloseX = currentCoords[0]
                    verificationIDFarY = verificationIDCloseY
                    verificationIDFarX = verificationIDCloseX - 65
                else:
                    verificationIDCloseY = currentCoords[1] - 65
                    verificationIDCloseX = currentCoords[0]
                    verificationIDFarY = verificationIDCloseY
                    verificationIDFarX = verificationIDCloseX + 65
                try:
                    verificationIDClose = piecesCoords.index("{} {}".format(verificationIDCloseX, verificationIDCloseY))
                except:
                    canDoClose = False
                    verificationIDClose = 0
                try:
                    verificationIDFar = piecesCoords.index("{} {}".format(verificationIDFarX, verificationIDFarY))
                except:
                    canDoFar = False
                    verificationIDFar = 0
                if canDoClose == True and piecesArray[verificationIDClose].getPieceType() == "Placeholder" or piecesArray[verificationIDClose].getPieceColour() != self.getPieceColour():
                    piecesArray[verificationIDClose].allowKingMovement(self.getPieceID())
                    if type == "Normal":
                        piecesArray[verificationIDClose].createVerificationSquare()
                if canDoFar == True and piecesArray[verificationIDFar].getPieceType() == "Placeholder" or piecesArray[verificationIDFar].getPieceColour() != self.getPieceColour():
                    piecesArray[verificationIDFar].allowKingMovement(self.getPieceID())
                    if type == "Normal":
                        piecesArray[verificationIDFar].createVerificationSquare()
                doingDown = False
                doingLeft = True

            if doingLeft == True:
                # Gets the coordinates of the pieces 1 left and 1 up of that, or right and down if black
                if self.getPieceColour() == "White":
                    verificationIDCloseY = currentCoords[1]
                    verificationIDCloseX = currentCoords[0] - 65
                    verificationIDFarY = verificationIDCloseY - 65
                    verificationIDFarX = verificationIDCloseX
                else:
                    verificationIDCloseY = currentCoords[1]
                    verificationIDCloseX = currentCoords[0] + 65
                    verificationIDFarY = verificationIDCloseY + 65
                    verificationIDFarX = verificationIDCloseX
                try:
                    verificationIDClose = piecesCoords.index("{} {}".format(verificationIDCloseX, verificationIDCloseY))
                except:
                    canDoClose = False
                    verificationIDClose = 0
                try:
                    verificationIDFar = piecesCoords.index("{} {}".format(verificationIDFarX, verificationIDFarY))
                except:
                    canDoFar = False
                    verificationIDFar = 0
                if canDoClose == True and piecesArray[verificationIDClose].getPieceType() == "Placeholder" or piecesArray[verificationIDClose].getPieceColour() != self.getPieceColour():
                    piecesArray[verificationIDClose].allowKingMovement(self.getPieceID())
                    if type == "Normal":
                        piecesArray[verificationIDClose].createVerificationSquare()
                if canDoFar == True and piecesArray[verificationIDFar].getPieceType() == "Placeholder" or piecesArray[verificationIDFar].getPieceColour() != self.getPieceColour():
                    piecesArray[verificationIDFar].allowKingMovement(self.getPieceID())
                    if type == "Normal":
                        piecesArray[verificationIDFar].createVerificationSquare()
                doingLeft = False

        verificationID = currentCoords[0]
        flagLong = False
        flagShort = False
        if type == "Normal":
            while self.canCastleLong == False and flagLong == False:
                # Checks the left side of the kng to see if it can castle long
                verificationID = verificationID - 65
                # Gets the ID of the piece one to the left of the last checked piece
                try:
                    verificationCheck = piecesCoords.index("{} {}".format(verificationID, currentCoords[1]))
                except:
                # If the rook has moved then the verification will go out of the board so it will have to go here
                    flagLong = True
                if flagLong == False:
                    if piecesArray[verificationCheck].getPieceType() == "Rook":
                        self.canCastleLong = True
                        piecesArray[verificationCheck].allowKingMovement(self.getPieceID())
                        piecesArray[verificationCheck].setCastleVerification()
                        if type == "Normal":
                            piecesArray[verificationCheck].createVerificationSquare()
                    elif piecesArray[verificationCheck].getPieceType() != "Placeholder":
                        flagLong = True

            verificationID = currentCoords[0]
            while self.canCastleShort == False and flagShort == False:
                # Checks the left side of the kng to see if it can castle long
                verificationID = verificationID + 65
                # Gets the ID of the piece one to the left of the last checked piece
                try:
                    verificationCheck = piecesCoords.index("{} {}".format(verificationID, currentCoords[1]))
                except:
                # If the rook has moved then the verification will go out of the board so it will have to go here
                    flagShort = True
                if flagShort == False:
                    if piecesArray[verificationCheck].getPieceType() == "Rook":
                        self.canCastleShort = True
                        piecesArray[verificationCheck].allowKingMovement(self.getPieceID())
                        piecesArray[verificationCheck].setCastleVerification()
                        if type == "Normal":
                            piecesArray[verificationCheck].createVerificationSquare()
                    elif piecesArray[verificationCheck].getPieceType() != "Placeholder":
                        flagShort = True

    def resetCastlingAttributes(self):
        """Resets all atributes to do with castling for if the king is placed back down"""
        self.canCastleLong = False
        self.canCastleShort = False 

class Placeholder(ChessPiece):
    def __init__(self, id, xCoord, yCoord, imageVar, piece, pieceColour):
        ChessPiece.__init__(self, id, xCoord, yCoord, imageVar, piece, pieceColour)

    def createVerification(self, type):
        # Returns as empty squares do not support verification
        return   

# This makes sure that the game will not run if it is imported into another module
if __name__ == "__main__":
    ProChess = ProChess()
    mainWindow.mainloop()