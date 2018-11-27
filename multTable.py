from tkinter import *
import time

class multiplicationTable():


    def __init__(self):

        self.btnList = []

        '''initialize window/table to receive user input
        '''
        self.tableRange = Tk()
        # tableRange.geometry('550x550')
        self.tableRange.title("Multiplication Table Range")
        Label(self.tableRange, text="Table Range: ").grid(column=0, row=0)

        self.e1 = Entry(self.tableRange)
        self.submitBtn = Button(self.tableRange, text="Submit", command=self.getInput)

        self.e1.grid(row=1, column=0)
        self.submitBtn.grid(row=2, column=0)


        #loop to display the input window for multiplication table size
        self.tableRange.mainloop()



    def getInput(self):
        '''This method is used to get the user input value
        We can't call the createTable method directly from inside the button because if we use the syntax of createTable(), the function
        will be called on button intialization. We want the function to be called when the submit button is clicked
        '''
        #get value in input
        inputRange = self.e1.get()
        print('===')
        print(inputRange)

        #try/catch to check if user input is a number
        try:
            inputRange = int(inputRange)
            self.createTable(inputRange)
        except ValueError:
            errorLabel = Label(self.tableRange, text="The value you entered was not a number, please try again.", background="red", wraplength="100")
            errorLabel.grid(column=0, row=3)


    def enter(self, event):
        '''function to handle event when cursor enters any of the inner buttons
        '''
        btnEnter = event.widget
        if btnEnter['bg'] == 'blue':
            print("------!")
            btnColumn = btnEnter.grid_info()['column']
            btnRow = btnEnter.grid_info()['row']

            for btn in self.btnList:

                #if a button is in the same row, or in  the same column, change the background to orange
                if (btn.grid_info()['row'] == btnRow and btn.grid_info()['column'] < btnColumn) or (btn.grid_info()['column'] == btnColumn and btn.grid_info()['row'] < btnRow):
                    btn['bg'] = 'orange'

            btnEnter['activebackground'] = 'white'


    def leaveBtn(self, event):
        '''function to reset all inner buttons of styling when cursor leaves any of the inner
        buttons
        '''

        #loop through all buttons and reset background color to blue
        for btn in self.btnList:
            btn['bg'] = 'blue'



    def createTable(self, inputRange):
        """This method is used to create a multiplication table of variable size depending
        on the input value from user
        """

        #destroy/close the user input window
        self.tableRange.destroy()

        #initialize a new window for the multiplication table
        window = Tk()

        #create title for window
        window.title("multiplication Table")

        # window.geometry('350x350')

        # two loopps, outer (i) loop keeps track of which row in table we are on
        # inner loop (j) keeps track of which column in the table we are on
        for i in range(inputRange+1):

            for j in range(inputRange+1):
                #on non 'header' rows or columns, value for each cell is calculated by multiplying every value in the row by the row index in decending order (from top)

                # this is to ensure top row creates the 'header' for 1,2,3,4...n
                if i ==0:
                    #make outside label along top(x axis)
                    btn = Button(window, text=(j), bg="red", width='3')
                    btn.grid(column=j, row=i)


                else:
                    # this is to ensure the first entry for ever row in the first column is a 'header' for 1,2,3,4...n
                    if j == 0:
                        #make outside label along left side (y axis)
                        btn = Button(window, text=(i), bg="red", width='3')
                        btn.grid(column=j, row=i)

                    else:
                        #this section creates all the inner multiplication value buttons
                        valueBtn = Button(window, text=(j*i), width='3', background="blue")
                        valueBtn.grid(column=j, row=i)

                        #bind mouse enter event
                        valueBtn.bind("<Enter>", self.enter)
                        #bind mouse leave event
                        valueBtn.bind("<Leave>", self.leaveBtn)
                        #append buttons to master list of all inner buttons
                        self.btnList.append(valueBtn)




        #loop to display the multiplication table
        window.mainloop()




multiplicationTable()
