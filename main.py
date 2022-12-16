
"""
Project Title: Meet in Lost Forest
Project File Name: MeetinLostForest.py

Author: Vamshi; Vamshi@lewisu.edu
Course Number/Session Number: CPSC-60500-003
Submission Date : 12/14/2022

Project Explanation:
 Simulation for grade k-2, 3-5, 6-8

Resources referred: None

"""

import simulationK2 as sk2
import simulation35 as s35
import simulation68 as s68
import tkinter as tk


def main():
    simulationK2 = sk2.simulationK2()
    simulation35 = s35.simulation35()
    simulation68 = s68.simulation68()

    root = tk.Tk()

    row_idx = 0
    tk.Label(root, text=" Forest Wander Simulations", font=10).grid(column=0, row=row_idx)

    row_idx += 1
    tk.Label(root, text="==================================================================#").grid(column=0, row=row_idx)

    row_idx += 1
    tk.Label(root, text=" Please select your grade").grid(column=0, row=row_idx)

    row_idx += 1
    button = tk.Button(root, text="Grade K-2", command=lambda: simulationK2.init_gui())
    button.grid(column=0, row=row_idx)

    row_idx += 1
    tk.Label(root, text="--------------------------------------").grid(column=0, row=row_idx)

    row_idx += 1
    button2 = tk.Button(root, text="Grade 3-5", command=lambda: simulation35.init_gui())
    button2.grid(column=0, row=row_idx)

    row_idx += 1
    tk.Label(root, text="--------------------------------------").grid(column=0, row=row_idx)

    row_idx += 1
    button3 = tk.Button(root, text="Grade 6-8 ", command=lambda: simulation68.init_gui())
    button3.grid(column=0, row=row_idx)

    row_idx += 1
    tk.Label(root, text="==================================================================#").grid(column=0, row=row_idx)

    row_idx += 1
    tk.Label(root, text="Project Description: Multiple players are wandering in the Forest grid, trying to meet together.").grid(column=0, row=row_idx)

    row_idx += 1
    tk.Label(root, text="  This application helps you better understand their behaviors through graphical simulations  ").grid(column=0, row=row_idx)

    row_idx += 1
    tk.Label(root, text="").grid(column=0, row=row_idx)

    row_idx += 1
    button4 = tk.Button(root, text="Exit Program", command= root.destroy, bg = '#DE3163')
    button4.grid(column=0, row=row_idx)

    tk.mainloop()


if __name__ == "__main__":
    main()
