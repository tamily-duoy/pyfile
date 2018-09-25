step_sizes=[100,10,1,0.1,0.01,0.001,0.0001,0.00001]
def safe(f):
    """return a new function that's the same as f,
        except that it outputs infinity whenever f produces an error"""
    def safe_f(*args,**kwargs):
        try:
            return f(*args,**kwargs)
        except:
            return float('inf')
        return safe_f
