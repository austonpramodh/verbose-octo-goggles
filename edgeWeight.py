class GraphEdgeWeight:
    '''Represents abstract class representing graph edge weight
       with abstract addition and product operations;
       (i) These operations are associative and commutative
       (ii) product operation distributes over addition operation
       (iii) they also have identities
    '''
    addId = None
    multId = None
    
    def aIdent(self):
        pass

    def mIdent(self):
        pass
    
    def __add__(self,other):
        pass

    def __mul__(self,other):
        pass

    def __eq__(self,other):
        pass

    def closure(self):
        '''Computes closure in semi-ring'''
        result = self.mIdent()
        prod = self
        while True:
            prod = prod * self
            result1 = result + prod
            if result == result1:
                break
            result = result1
        return result
    
class EdgeCost(GraphEdgeWeight):
    '''Edge weight semi-ring for min distance paths'''
    def addIdent():
        if EdgeCost.addId is None:
            EdgeCost.addId = EdgeCost(float("inf"))
        return EdgeCost.addId
    
    def aIdent(self):
        return EdgeCost.addIdent()

    def multIdent():
        if EdgeCost.multId is None:
            EdgeCost.multId = EdgeCost(0.0)
        return EdgeCost.multId

    def mIdent(self):
        return EdgeCost.multIdent()
    
    def __init__(self,w):
        '''weight representing a number'''
        if w < 0:
            raise ValueError('Invalid edge cost : ' + str(w))
        self.w = float(w)
        
    def __add__(self,other):
        return EdgeCost(min(self.w,other.w))

    def __mul__(self,other):
        return EdgeCost(self.w + other.w)

    def __str__(self):
        return str(self.w)

    def __eq__(self,other):
        if not isinstance(other,EdgeCost):
            return False
        return self.w == other.w

class EdgeProbability(GraphEdgeWeight):
    '''Edge weight semi-ring for max probability paths'''
    def addIdent():
        if EdgeProbability.addId is None:
            EdgeProbability.addId = EdgeProbability(0.0)
        return EdgeProbability.addId

    def aIdent(self):
        return EdgeProbability.addIdent()

    def multIdent():
        if EdgeProbability.multId is None:
            EdgeProbability.multId = EdgeProbability(1.0)
        return EdgeProbability.multId

    def mIdent(self):
        return EdgeProbability.multIdent()
    
    def __init__(self,w):
        '''weight representing a number'''
        if w < 0 or w > 1.0:
            raise ValueError('Invalid edge probability : ' + str(w))
        self.w = float(w)
        
    def __add__(self,other):
        return EdgeProbability(max(self.w,other.w))

    def __mul__(self,other):
        return EdgeProbability(self.w * other.w)

    def __str__(self):
        return str(self.w)

    def __eq__(self,other):
        if not isinstance(other,EdgeProbability):
            return False
        return self.w == other.w

    
    
    
    
