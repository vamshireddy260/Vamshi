import simulationParent as parent
import MeetinLostForestProject as fg
import colorBank as cb
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors
import matplotlib.animation as animation
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import tkinter as tk
import time
from statistics import mean

class simulation35(parent.simulationParent):

    def init_gui(self):
        self.fig, self.ax = plt.subplots(figsize=(6, 6))
        self.ax.axis("off")

        self.root = tk.Tk()

        row_idx = 0
        tk.Label(self.root, text=" Grade 3 - 5: Forest Wander Simulation",font = 10).grid(column=1, row=row_idx)

        row_idx += 1
        tk.Label(self.root, text="Enter width A and tall B in below boxes, both length should be between 2- 50").grid(column=1, row=row_idx)

        row_idx += 1
        self.width_entry = tk.Entry(self.root , width = 10)
        self.width_entry.grid(column=1, row=row_idx)

        row_idx += 1
        self.tall_entry = tk.Entry(self.root , width = 10)
        self.tall_entry.grid(column=1, row=row_idx)

        row_idx += 1
        l3 = tk.Label(self.root, text=" Enter number of players below, the number should be between 2 - 4")
        l3.grid(column=1, row= row_idx)

        row_idx += 1
        self.num_player_entry = tk.Entry(self.root , width = 10)
        self.num_player_entry.grid(column=1, row=row_idx)

        row_idx += 1
        input_button = tk.Button(self.root, text="Step 1: Set the width A and tall B, configure number of players", command = self.input_length_button)
        input_button.grid(column=1, row=row_idx)

        row_idx += 2
        button3 = tk.Button(self.root, text="Step 2: Randomly place all players", command= self.place_player_button)
        button3.grid(column=1, row=row_idx)
        #button3.place(x=0, y=30)

        row_idx += 1
        button = tk.Button(self.root, text="Step 3: Push Button for simulation", command= self.animate_button)
        button.grid(column=1, row=row_idx)
        #button.place(x=0, y=0)

        row_idx += 1
        self.warning_label = tk.Label(self.root, text='', fg = 'red')
        self.warning_label.grid(column=1, row=row_idx)

        row_idx += 1
        canvas = FigureCanvasTkAgg(self.fig, master=self.root)
        canvas.get_tk_widget().grid(column=1, row = row_idx)


        row_idx += 1
        self.stat_label1 = tk.Label(self.root, text='Total Number of Experiments: ' + self.calculateMeetStatistics()[0] + ' | ' + \
                                               'Average Meet Time: ' + self.calculateMeetStatistics()[3])
        self.stat_label1.grid(column=1, row=row_idx)

        row_idx += 1
        self.stat_label2 = tk.Label(self.root, text='Minimum Meet Time: ' + self.calculateMeetStatistics()[1] + ' | ' + \
                                                    'Maximum Meet Time: ' + self.calculateMeetStatistics()[2])
        self.stat_label2.grid(column=1, row=row_idx)


        row_idx += 1
        tk.Label(self.root, text='').grid(column=1, row=row_idx)

        row_idx += 2
        pause_button = tk.Button(self.root, text="**Optional: Skip simulation and show results", bg = '#6495ED', command= self.pause_animation)
        pause_button.grid(column=1, row=row_idx)


        #button.place(x=0, y=0)
        button2 = tk.Button(self.root, text="Clear Results", bg = '#9FE2BF',command= self.reset_canvas)
        button2.grid(column=0, row=row_idx)
        #button2.place(x=0, y=30)

        exit_button = tk.Button(self.root, text="Exit Program", bg = "#DE3163",command= self.exit_button)
        exit_button.grid(column=2, row=row_idx)


        tk.mainloop()

    def reset_canvas(self):
        self.meetTime = []
        self.reset_player_position()
        self.ax.clear()
        self.ax.axis("off")
        self.fig.canvas.draw()
        self.updateStatLabels()


    def calculateMeetStatistics(self):
        if(len(self.meetTime) ==0 ):
            return ['0']*4
        else:
            stats =[len(self.meetTime),
                    min(self.meetTime),
                    max(self.meetTime),
                    round(mean(self.meetTime))]

            return([str(i) for i in stats])


    def input_length_button(self):
        try:
            # length = int(self.length_entry.get())
            # self.setGrid(length, length)

            width = int(self.width_entry.get())
            tall = int(self.tall_entry.get())
            num_player = int(self.num_player_entry.get())

            self.setGrid(width, tall)

            if(width in range(2,51) and tall in range(2,51) and num_player in range(2,5)):
                self.input_length_warning_clear()
            else:
                self.input_length_warning()
        except:
            self.input_length_warning()

        data = np.copy(self.forestgrid.emptyForestMap())
        #print(data)
        plot_data = data[::-1]
        self.ax.clear()
        plt.title('Initialize Grid')
        cmap = colors.ListedColormap(self.colorbank.getBackGroundColor())
        self.ax.pcolormesh(plot_data, cmap=cmap, edgecolors='k', linewidths=3)

        self.initialize_Player(num_player)
        self.reset_player_position()

        self.fig.canvas.draw()


    def updateStatLabels(self):
        self.stat_label1['text'] ='Total Number of Experiments: ' + self.calculateMeetStatistics()[0] + ' | ' + \
                                               'Average Meet Time: ' + self.calculateMeetStatistics()[3]

        self.stat_label2['text'] ='Minimum Meet Time: ' + self.calculateMeetStatistics()[1] + ' | ' + \
                                  'Maximum Meet Time: ' + self.calculateMeetStatistics()[2]

    def animate_button(self):
        self.wanderTillAllMeet()
        self.ani = animation.FuncAnimation(self.fig, self.animate, frames = np.arange(0, self.playerlist[0].getTotalTimes() +1, 1),
                                      interval=100, blit=False, repeat=False)
        self.fig.canvas.draw()
        # print("update stat")
        # print(self.calculateMeetStatistics())

        self.updateStatLabels()


# simulate = simulation35()
# simulate.init_gui()



