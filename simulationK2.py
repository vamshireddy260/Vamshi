
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


class simulationK2(parent.simulationParent):

    def reset_player_position(self):
        ## randomized
        # initialPlayerPosition = self.forestgrid.getMultiRandomPositions(len(self.playerlist))

        ## diagonal
        initialPlayerPosition = self.forestgrid.getRandomDiagonalPositions()
        i = 0
        for player in self.playerlist:
            player.clearTime()
            player.setPosition(initialPlayerPosition[i])
            i = i +1

    # empty canvas, clear plot
    def reset_canvas(self):
        self.reset_player_position()
        self.ax.clear()
        self.ax.axis("off")
        self.fig.canvas.draw()

    def init_gui(self):
        self.fig, self.ax = plt.subplots(figsize=(6, 6))
        self.ax.axis("off")

        self.root = tk.Tk()

        tk.Label(self.root, text=" Grade K - 2 Forest Wander Simulation",font = 10).grid(column=0, row=0)
        tk.Label(self.root, text="Enter Square length in below box, length should be between 2- 50").grid(column=0, row=1)

        self.length_entry = tk.Entry(self.root , width = 10)
        self.length_entry.grid(column=0, row=2)

        input_button = tk.Button(self.root, text="Step 1: Set square length", command = self.input_length_button)
        input_button.grid(column=0, row=3)

        button3 = tk.Button(self.root, text="Step 2: Randomly place players (in diagonal)", command= self.place_player_button)
        button3.grid(column=0, row=4)
        #button3.place(x=0, y=30)


        button = tk.Button(self.root, text="Step 3: Push Button for simulation", command= self.animate_button)
        button.grid(column=0, row=5)
        #button.place(x=0, y=0)

        self.warning_label = tk.Label(self.root, text="",fg = 'red')
        self.warning_label.grid(column=0, row=6)

        canvas = FigureCanvasTkAgg(self.fig, master=self.root)
        canvas.get_tk_widget().grid(column=0, row=7)

        button2 = tk.Button(self.root, text="Clear all settings", command= self.reset_canvas)
        button2.grid(column=0, row=8)
        #button2.place(x=0, y=30)

        exit_button = tk.Button(self.root, text="Exit Program", bg = "#DE3163",command= self.exit_button)
        exit_button.grid(column=0, row=9)


        tk.mainloop()

    # take input by push button
    def input_length_button(self):
        try:
            length = int(self.length_entry.get())
            self.setGrid(length, length)

            if(length in range(2,51)):
                self.input_length_warning_clear()
            else:
                self.input_length_warning()
        except:
            self.input_length_warning()

        length = int(self.length_entry.get())
        self.setGrid(length, length)

        data = np.copy(self.forestgrid.emptyForestMap())
        #print(data)
        plot_data = data[::-1]
        self.ax.clear()
        plt.title('Initialize Grid')
        cmap = colors.ListedColormap(self.colorbank.getBackGroundColor())
        self.ax.pcolormesh(plot_data, cmap=cmap, edgecolors='k', linewidths=3)

        self.initialize_Player(2)
        self.reset_player_position()

        self.fig.canvas.draw()

    # control for animation
    def animate_button(self):
        self.wanderTillAllMeet()
        ani = animation.FuncAnimation(self.fig, self.animate, frames = np.arange(0, self.playerlist[0].getTotalTimes() +1, 1),
                                      interval=200, blit=False, repeat=False)
        self.fig.canvas.draw()


# simulate = simulationK2()
# simulate.init_gui()



