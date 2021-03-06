import json
import numpy as np

class jsonCreator:
    '''
    A class to construct a json object for exportation
    '''
    def __init__(self, logger = None):
        '''
        Initialize a new jsonCreator object.  This will call the resetJson function to set all values to None.
        Args:
            logger (logger object): Logger object to debug this class, will be set to None if no object is specified.
        '''

        self.logger = logger
        self.resetJson()

    def addUnits(self, units):
        '''
        This function will add the scale to the json object
        Args:
            x (float): The scale of the x axis
            y (float): The scale of the y axis
        '''
        if not isinstance(units, basestring):
            if self.logger is not None:
                self.logger.debug("Units must be a string")
            raise TypeError
        self.__json["units"] = units

    def addScale(self, x, y):
        '''
        This function will add the scale to the json object
        Args:
            x (float): The scale of the x axis
            y (float): The scale of the y axis
        '''
        '''
        try:
            if type(x) is not float:
                print type(x)
                raise TypeError
            if type(y) is not float:
                raise TypeError
        except TypeError:
            if self.logger is not None:
                self.logger.debug("X and Y must be floats")
            raise TypeError
        '''
        self.__json["scale"] = (str(x),str(y))

    def addContours(self, contours):
        '''
        This function will add the scale to the json object
        Args:
            contour (list): the contour(s) to be added this can be a list of vertices or a list of contours (list of lists)
        '''
        try:
            if type(contours) is not list:
                raise TypeError
        except TypeError:
            if self.logger is not None:
                self.logger.debug("Contour must be of type list")
            raise TypeError

        if type(contours) is list:
            for contour in contours:
                contour = contour.tolist()
            contourdict = [[[{"x":a[0], "y":a[1]} for a in b] for b in c] for c in contours]
            self.__json["contours"].append(contourdict)
        else:
            for contour in contours:
                #contourdict = [{"x":c[0], "y":c[1]} for c in contour]
                contour = contour.tolist()
            contourdict = [[[{"x":a[0], "y":b[1]} for a in b] for b in c] for c in contours]
            self.__json["contours"].append(contour.tolist())

    def getJson(self):
        '''
        Returns: A dict containing the added information.
        '''
        return self.__json

    def exportJson(self, filename = "final.json"):
        '''
        This function exports the json object to the specified filename
        Args:
            filename (str): The filename that the json should be exported to
        '''
        with open(filename, 'w') as fp:
            fp.write(json.dumps(self.__json))

    def resetJson(self):
        '''
        Resets the JSON object to empty all variables
        '''
        self.__json = {}
        self.__json["scale"] = None
        self.__json["units"] = None
        self.__json["contours"] = []
