# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    'print "Start:", problem.getStartState()'
    'print "Is the start a goal?", problem.isGoalState(problem.getStartState())'
    'print "Start's successors:", problem.getSuccessors(problem.getStartState())'
    #print problem
    """
    #print "Start's successors:", problem.getSuccessors(problem.getStartState())
    "*** YOUR CODE HERE ***"
    #didn't really know how to start until I did a little deeper research,
    #Perhaps the teacher could discuss more on the pesudo codes and examples of implementation during courses? would help alot
    #since I am not a computer science major (Seriously, MIS differ alot from CS)and have not yet finished learning data structure and Algorithm
    #so my head is a bit more dumber than others ,lol. But I have a LOT of interest in AI and hope to perform my utmost to learn

    #  --> generating my own comments, aka annotations for later reviewing
    
#DFS Version 2
    #print problem.getSuccessors("B")
    
    stack = util.Stack()
    visited = set()

    if stack.isEmpty():
        stack.push( (problem.getStartState(), [] )  )

    while not stack.isEmpty():
        node , path = stack.pop()

        if node in visited:
            continue

        visited.add(node)

        if problem.isGoalState(node):
            return path

        for successor, action, cost in problem.getSuccessors(node):
            stack.push( (successor, path + [action]) )



    
def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""

    queue = util.Queue()
    visited = set()

    if queue.isEmpty():
        queue.push( (problem.getStartState(), [] ) )

    while not queue.isEmpty():
        node, paths = queue.pop()

        if node in visited:
            continue

        visited.add(node)

        if problem.isGoalState(node):
            return paths

        for successor, action, cost in problem.getSuccessors(node):
            queue.push( (successor, paths + [action]) )
    
    
    

  
    util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
