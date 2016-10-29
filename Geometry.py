#! /usr/bin/env python

########################################
#                                      #
#     Geometry Test                    #
#                                      #
#     FrB                              #
#                                      #
########################################

"""
Description
===========

"""

import numpy as np
import math as m

class Point(np.ndarray):
    """
    Class for generic 2D or 3D point based on numpy's ndarray
    """

    def __new__(cls, input_array = [0.0, 0.0], tag = None, data_type = np.float64):
        """
        Initialises and passes to numpy to set up stuff
        """
        if not 2 <= len(input_array) <= 3:
            raise AttributeError("Dimensions for input array: 2 <= dim <= 3 -> attempted: {0}".format(len(input_array)))
        obj = np.asarray(input_array, dtype = data_type).view(cls)
        obj.tag = tag
        return obj

    def __array_finalize__(self, obj):
        """
        Allows slice of Point to retain extra attributes
        """
        if obj is None: return
        self.tag = getattr(obj, "tag", None)


    # representations
    def __str__(self):
        return "Point: {0} with tag {1}".format(self.listc, self.tag)

    def __repr__(self):
        return "Point({0}, tag=\"{1}\", data_type=np.{2})".format(repr(tuple(self)), self.tag, self.dtype)

    # getters and setters
    @property
    def x(self):
        return self[0]

    @x.setter
    def x(self, value):
        self[0] = value

    @property
    def y(self):
        return self[1]

    @y.setter
    def y(self, value):
        self[1] = value

    @property
    def z(self):
        if self.size != 3:
            raise AttributeError("Point ({0}) only has x and y dimensions".format(self.tag))
        else:
            return self[2]

    @z.setter
    def z(self, value):
        if self.size != 3:
            raise AttributeError("Point ({0}) only has x and y dimensions".format(self.tag))
        else:
            self[2] = value


    # equalities
    def __eq__(self, other):
        return np.array_equal(self, other)

    def __ne__(self, other):
        return not np.array_equal(self, other)


    # useful functions
    def dist(self, other):
        return np.linalg.norm(self - other)

    def dist0(self):
        return np.linalg.norm(self)

    def listc(self):
        return [i for i in self]

    def bearing(self, other):
        """
        Returns gird north bearing of other relative to self
        """

    def _quad(self, other):
        """
        internal function to return quad of other relatiev to self
        """
        if other.x >= self.x:
            if other.y >= self.y:
                _quad = 1
            else:
                _quad = 2
        else:
            if other.y >= self.y:
                _quad = 4
            else:
                _quad = 3
       return _quad




def testPoint():
    """
    Basic assert tests for Point class
    """
    p1 = Point([1.0, 2.0], tag = "test Point 1")
    p2 = Point([2.0, 3.0], tag = "test Point 2")
    p3 = Point([1.0, 2.0, 4.0], tag = "test Point 3")

    try:
        p_fail1 = Point([1.0, 2.0, 3.0, 4.0])
    except AttributeError:
        pass


    ########
    # test area
    #
    #
    ########


    # basic gets
    assert p1.x == 1.0
    assert p1[0] == 1.0
    assert p1.x == p1[0]

    # try missing z
    try:
        p1.z = 2
    except AttributeError:
        pass

    # basic sets
    p1.x = 2.0
    assert p1.x == 2.0
    p1[0] = 1.0
    assert p1.x == 1.0

    # equality
    assert p1 == [1.0, 2.0]
    assert p1 != p2
    assert p1 != p3

    # operators
    p1 += [1.0, 2.0]
    assert p1 == [2.0, 4.0]
    p1 -= [1.0, 2.0]
    p1 *= 3
    assert p1 == [3.0, 6.0]
    p1 *= 1/3.0
    assert p1*p2 == [2.0, 6.0]

    # list comprehension
    assert p1 == [i for i in p1]
    assert p1.listc() == [1.0, 2.0]

    # distances
    assert p1.dist(p2) == m.sqrt(2)
    assert p1.dist0() == m.sqrt(5)
    try:
        p1.dist(p3)
    except ValueError:
        pass

    # slicing
    assert p3[:2] == p1
    assert p3[:2].tag == "test Point 3"

    # __repr__ and __str__
    assert eval(repr(p1)) == p1
    assert str(p1) ==  "Point: {0} with tag {1}".format(p1.listc, p1.tag)

    print "Point passed!"


def testPolygon():
    P1 = Polygon()

    

    print "Polygon Passed!"


if __name__ == "__main__":
    testPoint()
    testPolygon()


########################################
#                                      #
#     Geometry Test                    #
#                                      #
#     FrB                              #
#                                      #
########################################
