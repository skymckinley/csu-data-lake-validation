import pandas as pd
import numpy as np

testfiles = {
        "Application by Student": "application_by_student.csv",
        "Student": "student.csv",
        "Student by Class": "student_by_class.csv",
        "Student by Degree": "student_by_degree.csv",
        "Student by Term": "student_by_term.csv",
	"Class by Section": "class_by_section.csv"
        }

for t in testfiles:
    df = pd.read_csv(testfiles[t], low_memory = False)
    # empty_cols = [col for col in df.columns if ( df[col].replace(r'^\s*$', np.nan, regex=True).isnull().all() )]
    empty_cols = [col for col in df.columns if ( df[col].isnull().all() )]
    print(t + " has the following empty columns:")
    for col in empty_cols:
        print(col)
    print()
