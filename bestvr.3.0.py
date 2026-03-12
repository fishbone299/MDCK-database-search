#this code is for finding similar compounds in two different datasets 
#exit()
#you must exit python environment and download pandas in bash (pip3 comand), then enter python environment (python3 comand)
#pip3 install pandas
#python3
import pandas as pd
MDCK_df = pd.read_csv("/Users/teaguemr/project/mdck/MDCK databse search/MDCK studies copy.csv")
C1_df = pd.read_csv("/Users/teaguemr/project/mdck/MDCK databse search/C1 MDCK-AUTO-2026-02.csv")
#this comand allows you to see column names which is important for setting up "Sample" vs "Compound"
print(MDCK_df.columns)
print(C1_df.columns)
#code format must be .isin function, regular Boolian task will not compair two columns from different datasets
matches = MDCK_df[MDCK_df["Compound"].isin(C1_df["Sample"])]
#you can change the location where the file saves, mine is set to Desktop
matches.to_csv("/Users/teaguemr/Desktop/filternocontrols.csv")
C2_df = pd.read_csv("/Users/teaguemr/project/mdck/MDCK databse search/C2 MDCK-AUTO-2026-02.csv")
print(C2_df.columns)
matches2 = MDCK_df[MDCK_df["Compound"].isin(C2_df["Sample"])]
matches2.to_csv("/Users/teaguemr/Desktop/C2_filternocontrols.csv")
#for single compound search via the user
variable = input("Enter Compound ID: ")
results = MDCK_df[MDCK_df["Compound"] == variable]
results.to_csv("/Users/teaguemr/Desktop/C2_filternocontrols.csv")


