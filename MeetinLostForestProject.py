# -*- coding: utf-8 -*-
"""
HW1 Title: Meet in Lost Forest
HW1 File Name: MeetinLostForest.py

Author: vamshi; vamshi@lewisu.edu
Course Number/Session Number: CPSC-60500-003
Submission Date : 12/14/2022

"""
import numpy as np
import random as random


class ForestGrid:
    # Constraints on width and tall, ranging from 2 - 51
    MinAllowed = 2
    MaxAllowed = 50

    ## initialize a forest grid
    def __init__(self):
        self.width = 0
        self.tall = 0

    ## takes in and set dimension of the forest grid 
    def setGridDimension(self, width, tall):
        if (width in range(self.MinAllowed, self.MaxAllowed + 1) and
                tall in range(self.MinAllowed, self.MaxAllowed + 1)):
            self.width = width
            self.tall = tall
        else:
            print("Error: Width and Tall should be ranging from 2 to 50.")

    ## test if a proposed poistion is available to reach in the forest.
    def testPositionAvailability(self, positionIndices):
        if (positionIndices[0] in range(0, self.tall) and
                positionIndices[1] in range(0, self.width)):
            # print("Attempted Position is Movable")
            return True
        else:
            # print("Attempted Position is not Movable")
            return False

    ## Produce an empty forest grid, use np array
    def emptyForestMap(self):
        return (np.zeros((self.tall, self.width), dtype=int))

    def getRandomPosition(self):
        rand_x = random.randint(0, self.tall - 1)
        rand_y = random.randint(0, self.width - 1)
        return((rand_x, rand_y))

    def getMultiRandomPositions(self, num_rand):
        allRandSet = set()
        while(len(allRandSet) <= num_rand):
            allRandSet.add(self.getRandomPosition())
        #print(allRandSet)
        return(list(allRandSet))

    def getRandomDiagonalPositions(self):
        Positions_1 = [(0,0), (self.tall - 1,self.width - 1)]
        Positions_2 = [(0,self.width - 1), (self.tall - 1,0)]
        if(random.randint(0,1)):
            return(Positions_1)
        else:
            return(Positions_2)


np.zeros((3, 2), dtype=int)[2][1]


class ForestWanderer:
    ## const for all actions, representing the change of indices for an np array
    Stay = (0, 0)
    North = (-1, 0)
    South = (+1, 0)
    East = (0, +1)
    West = (0, -1)
    NorthEast = (-1, +1)
    NorthWest = (-1, -1)
    SouthEast = (+1, +1)
    SouthWest = (+1, -1)

    ## below two variables associate the actions with a moving index
    ## eg. 1 = North, 4 = West e.t.c
    AllPossibleMoveNames = ["Stay", "North", "South", "East", "West",
                            "NorthEast", "NorthWest", "SouthEast", "SouthWest"]

    AllPossibleMoves = np.array([Stay, North, South, East, West,
                                 NorthEast, NorthWest, SouthEast, SouthWest])

    def __init__(self, name, forestgrid):
        self.name = name
        self.position = ()
        self.totalTime = 0
        self.forestgrid = forestgrid
        self.AllActionNames = []
        self.AllPositions = ()

    ## Generates a random integer between 1-8 to extract actions (stay is exluded)
    def __getRandomDirection(self):
        move_idx = random.randint(1, 8)
        # print("Current position:  %s" % (self.position,))
        # print("Random Direction Picked: %s" % ( self.AllPossibleMoveNames[move_idx] ,))
        return (move_idx)

    def __getLastMoveIndex(self):
        if(self.totalTime==0):
            return(0)
        else:
            LastName = self.AllActionNames[-1]
            return(self.AllPossibleMoveNames.index(LastName))

    def __getDeterminedDirection(self):
        if(self.__getLastMoveIndex() == 0):
            return(random.randint(1, 8))
        else:
            return(self.__getLastMoveIndex())

    ## for all the moving index, proposed an new position to move
    def __getAttemptPosition(self, move_idx):
        return (np.add(self.position,
                       self.AllPossibleMoves[move_idx]))

    ## __ValidateDirection: validate if a moving index is feasible
    ## if feasible, preserve the current value, if not turn 0 (stay)
    def __ValidateDirection(self, move_idx):
        Attemp_Position = self.__getAttemptPosition(move_idx)
        ## if movable
        if (self.forestgrid.testPositionAvailability(Attemp_Position)):
            return (move_idx)
        else:
            # print("Action changed to Stay")
            return (0)

    ## move to new position by changing the self.position value
    def __movetoNewPosition(self, move_idx):
        self.position = self.__getAttemptPosition(move_idx)
        # print("Moved to new position: %s" % (self.position,))

    ## set position by public method, can be used to initialize starting position
    def setPosition(self, new_position):
        self.position = new_position
        self.AllPositions = np.array([self.position])

    ## return position
    def getPosition(self):
        return (self.position)

    ## reset time
    def clearTime(self):
        self.totalTime = 0

    ## calcuate the total time
    def getTotalTimes(self):
        return (self.totalTime)

    ## integral process for making an move: random an int, validate and correct the int
    ## make actual move after validation, update attributes accordingly
    def makeOneMove(self):
        # print("Forest Wanderer: " + self.name)
        move_idx = self.__getRandomDirection()
        corrected_move_idx = self.__ValidateDirection(move_idx)
        self.__movetoNewPosition(corrected_move_idx)

        self.AllActionNames.append(self.AllPossibleMoveNames[corrected_move_idx])
        # print(self.AllPositions)
        self.AllPositions = np.append(self.AllPositions, np.array([self.position]), axis=0)
        self.totalTime = self.totalTime + 1

    def makeDeterminedMove(self):
        move_idx = self.__getDeterminedDirection()
        corrected_move_idx = self.__ValidateDirection(move_idx)
        self.__movetoNewPosition(corrected_move_idx)

        self.AllActionNames.append(self.AllPossibleMoveNames[corrected_move_idx])
        # print(self.AllPositions)
        self.AllPositions = np.append(self.AllPositions, np.array([self.position]), axis=0)
        self.totalTime = self.totalTime + 1

    def makeNoMove(self):
        corrected_move_idx = 0
        self.__movetoNewPosition(corrected_move_idx)

        self.AllActionNames.append(self.AllPossibleMoveNames[corrected_move_idx])
        # print(self.AllPositions)
        self.AllPositions = np.append(self.AllPositions, np.array([self.position]), axis=0)
        self.totalTime = self.totalTime + 1

    ## print all the action name that the ForestWanderer taken
    def printPath(self):
        print("All actions for " + self.name + " are ...")
        print(self.AllActionNames)
        print(self.AllPositions)

    ## frequency plot calcuates the accumulate time spent in each position of the grid
    def printFrequencyPlot(self):
        freq_map = np.copy(self.forestgrid.emptyForestMap())

        for time in range(self.totalTime + 1):
            p = np.copy(self.AllPositions[time])
            # freq_map[p[0],p[1]]
            freq_map[p[0], p[1]] = freq_map[p[0]][p[1]] + 1
        print("Travel Frequency Plot for " + self.name + " is ...")
        print(freq_map)

    ## active score calculates the percentage of the times 
    ## where the ForestWanderer is making actual moves (not stay)
    def printActiveScore(self):
        activeScore = 1 - self.AllActionNames.count("Stay") / float(self.totalTime)
        print("Active score for " + self.name + " = {:.2%}".format(activeScore))


def main():
    WidthA = int(input("Please input Width A (2 <= A <= 50): "))
    TallB = int(input("Please input Tall B (2 <= B <= 50): "))

    while (WidthA not in range(2, 51) or TallB not in range(2, 51)):
        print("Error:Incorrect input on Width or Tall, please check range and reenter!")
        WidthA = int(input("Please input Width A (2 <= A <= 50): "))
        TallB = int(input("Please input Tall B (2 <= A <= 50): "))

    forestgrid = ForestGrid()
    forestgrid.setGridDimension(WidthA, TallB)

    Pat = ForestWanderer("Pat", forestgrid)
    Pat.setPosition((0, 0))  # top right

    Chris = ForestWanderer("Chris", forestgrid)
    Chris.setPosition((TallB - 1, WidthA - 1))  # bottom left

    Final_Situation = "B"
    Final_Meet_Location = ()
    Final_Times = 0
    Max_TimeOut = 1000000

    ## loop thru maximum allowed time
    for times in range(Max_TimeOut):
        Pat.makeOneMove()
        Chris.makeOneMove()

        # if Pat adn Chris meet, change the situation value,
        if (np.array_equal(Pat.getPosition(), Chris.getPosition())):
            Final_Situation = "A"
            Final_Meet_Location = Pat.getPosition()
            Final_Times = Pat.getTotalTimes()
            break

    input("Press Enter to Show Results...")
    if (Final_Situation == "A"):
        print("####################################################")
        print("Situation A! Pat and Chris meet at %s" % (Final_Meet_Location,))
        print("Total time spent is : " + str(Final_Times))
        print("####################################################")

        # Pat.printPath()
        Pat.printActiveScore()
        Pat.printFrequencyPlot()
        print("====================================================")
        # Chris.printPath()
        Chris.printActiveScore()
        Chris.printFrequencyPlot()
        print("====================================================")

    else:
        print("Situation B: Pat and Chris didn't meet each other.")
        print("Max Time out at " + Max_TimeOut)
        # Pat.printPath()
        Pat.printActiveScore()
        Pat.printFrequencyPlot()
        print("====================================================")

        # Chris.printPath()
        Chris.printActiveScore()
        Chris.printFrequencyPlot()
        print("====================================================")


def additionalExperiments():
    experiment_id = 0
    Results = np.zeros(6, dtype=int).reshape(1, 6)

    for repeat in range(5):

        for length in range(5, 51, 5):
            experiment_id += 1

            WidthA = length
            TallB = length

            forestgrid = ForestGrid()
            forestgrid.setGridDimension(WidthA, TallB)

            Pat = ForestWanderer("Pat", forestgrid)
            Pat.setPosition((0, 0))  # top right

            Chris = ForestWanderer("Chris", forestgrid)
            Chris.setPosition((TallB - 1, WidthA - 1))  # bottom left

            Final_Situation = 0  # = B = miss
            Final_Times = 0
            Max_TimeOut = 1000000

            ## loop thru maximum allowed time
            for times in range(Max_TimeOut):
                Pat.makeOneMove()
                Chris.makeOneMove()

                # if Pat adn Chris meet, change the situation value,
                if (np.array_equal(Pat.getPosition(), Chris.getPosition())):
                    Final_Situation = 1  # = A = meet
                    Final_Times = Pat.getTotalTimes()
                    break
            result = (experiment_id, int(repeat), WidthA, TallB, Final_Situation, Final_Times)
            Results = np.append(Results, np.array(result).reshape(1, 6), axis=0)

        # print(Results)
    np.savetxt("Experiment.csv", Results, delimiter=",", fmt='%10.0f')
    print("Experiments results saved!")


if __name__ == "__main__":
    ## for iterative user input
    main()

    ## for experiment.
    run_experiment = False

    if (run_experiment):
        additionalExperiments()
