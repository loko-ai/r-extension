import rpy2.robjects as robjects
from rpy2.robjects.numpy2ri import rpy2py

res = robjects.r['pi']

print(rpy2py(res))
