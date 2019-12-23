import pandas as pd
import numpy as np
import argparse
import datetime

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

        parser = argparse.ArgumentParser(description = "Find blank columns in \
            datasets.")
        parser.add_argument("-f","--outputfile", 
            help = "File to direct output to.")

        args = parser.parse_args()

        # Get the runtime for creating filenames.
        runtime = datetime.datetime.today()

        if args.outputfile:
            try:
                output_file = open(args.outputfile, "x")
            except:
                filename = "empty_columns_" + \
                    runtime.strftime("%Y%m%d%H%m") + \
                    ".csv"
                output_file = open(filename, "x")
                print("The specified file could not be created. \
                    Using " + filename)
        else:
            filename = "empty_columns_" + \
                runtime.strftime("%Y%m%d%H%M") + \
                ".csv"
            output_file = open(filename, "x")

        # Create a dataframe to hold the blank columns and the file they came
        # from.
        output_df = pd.DataFrame(data = {'dataset':[], 'column':[]})

        for t in testfiles:
            df = pd.read_csv(testfiles[t], low_memory = False)

            # According to Angela Williams at the Chancellor's Office, any 
            # column which contains only null values or fields with a single
            # space, " ", is considered to be empty for the purposes of this
            # validation.

            empty_cols = [col for col in df.columns 
                if ( 
                    df[col].replace(r'^\s*$', np.nan, regex=True).isnull().all()
                    )]
            for col in empty_cols:
                # Insert the dataset and column name into the dataframe.
                output_df.loc[len(output_df.index)] = [t, col]

        output_df.to_csv(path_or_buf=output_file, header=True)
        output_file.close()

if __name__ == "__main__":
        main()
