from ast import literal_eval

# Edit these parameters as you please, though d > 3 runs slow, and we probably should start with 2

empty = ' ' # Empty space when printing shape
full = 'X' # Shaded in space when printing shape
d = 3 # Dimension of problem

def neighbors(d = 2):
    """List of lists, representing the change in coors for neighbors in dimension d. Assumes d >= 1"""
    #assert(isinstance(d, int) and d > 0)
    if d == 1:
        return [[1], [-1]]
    else:
        neighs = neighbors(d-1)
        new_neighs = [[0] + neigh for neigh in neighs]
        new_neighs.append([1] + [0]*(d-1))
        new_neighs.append([-1] + [0]*(d-1))
        return new_neighs

def grid(n, d = 2):
    """Returns an (2n+1) X (2n+1) X (2n+1) ... X (2n+1) d times"""
    #assert(isinstance(d, int) and d > 0 and isinstance(n, int) and n >= 0)
    if d == 1:
        return [[i] for i in xrange(-n, n+1)]
    else:
        flat = grid(n, d-1)
        return [f + [i] for f in flat for i in xrange(-n, n+1)]

def add(v1, v2):
    """Adds two lists/tuples and returns a list of their sum"""
    #assert (isinstance(v1, list) or isinstance(v1, tuple)) and (isinstance(v2, list) or isinstance(v2, tuple))
    dim = len(v1)
    #assert(dim == len(v2))
    result = []
    return [v1[i] + v2[i] for i in xrange(dim)]

class Growth:
    """A representation of the grid as steps increase"""
    global directions
    directions = neighbors(d)
    #print directions

    def __init__(self, readIn = False):
        """Initializes object, starting at iteration 1000 if readIn is True"""
        if readIn:
            self.iteration = 500
            self.size = 0
            self.len = 2 * 500 + 1
            self.edges = []
            self.shape = {}
            file = open("threedim_500.txt", "r") # Read in shape coordinates
            for line in file:
                c = literal_eval(line)
                self.shape[c] = full
                self.size += 1
            file.close()

            file = open("threedim_edge_500.txt", "r") # Read in edges of shape
            for line in file:
                c = literal_eval(line)
                self.edges.append(c)
            file.close()
        else:
            self.iteration = 0
            self.edges = [tuple([0]*d)] #, (5,5)] # Set to be one point
            #self.edges.append((0,1)) # Remove in general
	    self.shape = {}
            for edge in self.edges:
                self.shape[edge] = '0'
            self.size = 1
            self.len = 1

    def get_iteration(self):
        """Returns what iteration we are on, indexed at 0"""
        return self.iteration

    def num_edges(self):
        """Returns the number points that were added on the last iteration"""
        return len(self.edges)

    def get_size(self):
        """Returns the number of 'filled' points at this time"""
        return self.size

    def get_density(self, n=-1):
        """Returns the density of X in a square of size 2n+1"""
        if n == -1:
            n = self.iteration
        #assert(isinstance(n, int) and n >= 0)
        if n >= self.iteration:
            return float(self.size)/ ((2 * self.iteration + 1)**(float(d)))
        else:
            count = 0
            coors = grid(n, d) # Edit as needed
            for coor in coors:
                if self.shape.get(tuple(coor), empty) != empty:
                    count += 1
            return float(count) / ((2 * n + 1) ** float(d))

    def grow(self):
        """Performs one iteration of the process. That is, we add all points not in the current set that would have precisely one neighbor with it"""
        self.iteration += 1
        new_edges = []
        for edge in self.edges:
            for change in directions:
                count = 0
                for direction in directions:
                    possible = add(add(edge, change), direction)
                    if self.shape.get(tuple(possible), empty) != empty:
                        count += 1
                if count == 1:
                    new_edges.extend([tuple(add(edge, change))])
        for edge in new_edges:
            self.shape[edge] = full
        self.len += 2
        self.size += len(new_edges)
        self.edges = new_edges

    def show(self, size = -1):
        """For the two-dimensional case, gives a (2*size + 1) by (2*size + 1) square representation of the shape"""
        if size == -1:
            size = self.iteration
        #assert(isinstance(size, int) and size >= 0)
        if d != 2:
            return
        grid = ""
        for x in xrange(-size, size + 1):
            for y in xrange(-size, size + 1):
                grid += self.shape.get((x,y), empty)
            grid += "\n"
        print grid

    def coors(self, size = -1):
        """Returns an unordered list of filled coordinates of the shape"""
        if size == -1:
            size = self.iteration
        #assert(isinstance(size, int) and size >= 0)
        crs = grid(size, d)
	
	def first_quadrant(coor):
	    for x in coor:
		if x < 0:
		    return False
	    return True
	
	def increasing(coor):
	    m = coor[0]
	    for x in coor:
		if x < m:
		    return False
		else:
		    m = x
	    return True
	
	all = ""
        for coor in crs:
	    coor = tuple(coor)
            if self.shape.get(coor, 0) != 0 and increasing(coor) and first_quadrant(coor):
                all += str(coor) + ", "
	print all
        

test = Growth()
print "Done"
desired_iteration = 100
for i in xrange(desired_iteration):
    test.grow()
    #test.show(10)
    #print
    if i % 25 == 0:
        print i
    #print str(i) + ": " + str(test.num_edges() - 1) + " " + str(4*3**(-1 + bin(i+1).count("1")))
    #Numerical evidence for my conjecture^
test.show(30)
#print test.get_iteration(), test.num_edges(), test.get_size()
#print test.get_density(0), test.get_density()
test.coors(16)
#for i in xrange(30):
#    print str(10*(i+1)) + ": " + str(test.get_density(10*(i+1))) # Seems to converge to 2/3 for d = 2, maybe 6-10% for d = 3?
#test.show()
print test.iteration
    
def write():
    file = open("threedim_500.txt", "w")
    for coors in test.shape:
        file.write(str(coors) + "\n")
    file.close()

    file = open("threedim_edge_500.txt", "w")
    for edge in test.edges:
        file.write(str(edge) + "\n")
    file.close()

#write()

#print (18,34) in test.shape
