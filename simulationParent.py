
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

class simulationParent:

    colorbank = cb.colorBank()
    Max_TimeOut = 1000000
    meetTime = []

    def __init__(self):
        self.forestgrid = fg.ForestGrid()
        self.playerlist = []
        self.meetTime = []

    # set grid of the forest
    def setGrid(self, WidthA ,TallB):

        self.forestgrid = fg.ForestGrid()
        self.forestgrid.setGridDimension(WidthA,TallB)

    # initialize player
    def initialize_Player(self, number_players):
        self.playerlist = []
        for i in range(number_players):
            self.playerlist.append(
                fg.ForestWanderer(self.colorbank.getPlayerColor(i+1), self.forestgrid)
            )

    # place players in random positions on the grid (no overlapping)
    def reset_player_position(self):
        # randomized
        initialPlayerPosition = self.forestgrid.getMultiRandomPositions(len(self.playerlist))

        ## diagonal
        # initialPlayerPosition = self.forestgrid.getRandomDiagonalPositions()
        i = 0
        for player in self.playerlist:
            player.clearTime()
            player.setPosition(initialPlayerPosition[i])
            i = i +1

    ##  all take random step to meet
    def wanderTillAllMeet(self):
        Max_TimeOut = self.Max_TimeOut

        ## loop thru maximum allowed time
        for times in range(Max_TimeOut):
            TotalPosition = set()
            for player in self.playerlist:
                player.makeOneMove()
                #print(tuple(player.getPosition()))
                TotalPosition.add(tuple(player.getPosition()))

            # if meet, one position,
            if (len(TotalPosition)==1):
                self.meetTime.append(self.playerlist[0].getTotalTimes())
                break

    # initialize GUI page
    def init_gui(self):
        self.fig, self.ax = plt.subplots(figsize=(6, 6))
        self.ax.axis("off")

        self.root = tk.Tk()

        tk.mainloop()


    def exit_button(self):
        self.root.quit()
        self.root.destroy()

    def input_length_warning(self):
        self.warning_label['text'] = "Invalid input, please re-enter"

    def input_length_warning_clear(self):
        self.warning_label['text'] = ""


    def place_player_button(self):
        self.reset_player_position()
        self.plot_static_placement(0)

    # utility function to get plot.
    def get_plot_data(self, time):
        data = np.copy(self.forestgrid.emptyForestMap())
        for i in range(len(self.playerlist)):
            player = self.playerlist[i]
            p = player.AllPositions[time]
            data[p[0], p[1]] = i + 1

        plot_data = data[::-1]
        return(plot_data)

    # plot static plot
    def plot_static_placement(self,time):
        plot_data = self.get_plot_data(time)
        if(time == self.Max_TimeOut):
            plt.title('Failed to Meet in the maximum allowed time  ' + str(self.Max_TimeOut))
        else:
            plt.title('Wandering at Time = ' + str(time))
        cmap = colors.ListedColormap(self.colorbank.getListedColormap(len(self.playerlist)))
        plot = self.ax.pcolormesh(plot_data, cmap=cmap, edgecolors='k', linewidths=3)
        self.fig.canvas.draw()
        return(plot)

    ## push for animation
    def animate(self, i):
        while(i < self.playerlist[0].getTotalTimes()):
            plot_data = self.get_plot_data(i)
            plt.title('Wandering at Time = ' + str(i))
            cmap = colors.ListedColormap(self.colorbank.getListedColormap(len(self.playerlist)))
            plot = self.ax.pcolormesh(plot_data, cmap=cmap, edgecolors='k', linewidths=3)
            return (plot)
            #self.plot_static_placement(i)

        if (i == self.playerlist[0].getTotalTimes() and i!=0 ):
            plot_data = self.get_plot_data(i)
            plt.title('Meet at Time = ' + str(i))
            plot = self.ax.pcolormesh(plot_data, cmap= colors.ListedColormap(self.colorbank.getColorMeet()), edgecolors='k', linewidths=3)
            return (plot)

        if(i == self.Max_TimeOut):
            plot_data = self.get_plot_data(i)
            plt.title('Failed to Meet in the maximum allowed time  ' + str(self.Max_TimeOut))
            return (self.plot_static_placement(i))

    # pause for animation
    def pause_animation(self):
        self.ani.event_source.stop()

        finalTime = self.playerlist[0].getTotalTimes()

        plot_data = self.get_plot_data(finalTime)
        plt.title('Meet at Time = ' + str(finalTime))
        plot = self.ax.pcolormesh(plot_data, cmap= colors.ListedColormap(self.colorbank.getColorMeet()), edgecolors='k', linewidths=3)
        self.fig.canvas.draw()
        return (plot)





