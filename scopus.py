# https://ualibweb.github.io/UALIB_ScholarlyAPI_Cookbook/src/python/scopus.html

import pybliometrics

# import other libraries needed
from pybliometrics.scopus import ScopusSearch
import time
import numpy as np
import pandas as pd


# Scopus Author ID field (AU-ID): 55764087400, Vincent Scalfani
q1 = ScopusSearch('AU-ID(35408955300)', download=False)
q1.get_results_size()

# save to dataframe
df1 = pd.DataFrame(q1.results)

# Get a list of article titles
titles = df1.title.tolist()
titles


# now a list of the cited by count
cited_by = df1.citedby_count.tolist()
print(cited_by)