import pandas as pd
import numpy as np
import argparse

# In order to process the CSV files exported from Pentaho you should copy them 
# to this directory and rename them according to the dataset you exported.

def main():
        testfiles = {
                "Application by Student": "application_by_student.csv",
                "Student": "student.csv",
                "Student by Class": "student_by_class.csv",
                "Student by Degree": "student_by_degree.csv",
                "Student by Term": "student_by_term.csv",
                "Class by Section": "class_by_section.csv"
                }

        parser = argparse.ArgumentParser(description = "Find blank columns in datasets.")
        parser.add_argument("-f","--outputfile", help = "File to direct output to.")

        args = parser.parse_args()

        if args.outputfile:
            try:
                output_file = open(args.outputfile, "x");
            except:
                print("The specified file could not be created.")

        # TODO: Allow for an optional filename argument where this output will be 
        #       written to.

        for t in testfiles:
            df = pd.read_csv(testfiles[t], low_memory = False)

            # According to Angela Williams at the Chancellor's Office, any column which contains only null values or
            # fields with a single space, " ", is considered to be empty for the purposes of this validation.

            empty_cols = [col for col in df.columns if ( df[col].replace(r'^\s*$', np.nan, regex=True).isnull().all() )]
            output_file.write(t + " has the following empty columns:")
            for col in empty_cols:
                output_file.write(col + "\n")

            output_file.write("\n")

        output_file.close()

if __name__ == "__main__":
        main()
