import pandas as pd
import streamlit as st
import openpyxl
from pathlib import Path





def run():

    brands = set()
    models = set()
    Combined = set()
    combined_DD=set()                                                             ##### Required data structures
    brands_count=[]
    models_count=[]
    combined_count=[]
    Combined_DD_count=[]

    brands_removed = set()
    models_removed = set()
    Combined_removed = set()
    combined_DD_removed=set()                                                   
    brands_count_removed=[]
    models_count_removed=[]
    combined_count_removed=[]
    Combined_DD_count_removed=[]

    st.header("Initial Data Analysis")
    st.write('-------------------------------------------------')
    st.header("This website gives us overall data knowledge like what is the shape of the data provided in the current build. We can compare how many new brands, models added.")



    oldfile=st.file_uploader("Choose a file")
    newfile=st.file_uploader("Choose a second file")

    if oldfile and newfile:
        old_file=pd.read_csv(oldfile)
        new_file=pd.read_csv(newfile)
        st.write("Old build file size ",old_file.shape[0])
        st.write('New build file size',new_file.shape[0])
        old_file.fillna('None',inplace=True)
        new_file.fillna('None',inplace=True)
        old_file['Combined'] = old_file['BrandName'].astype('str') + old_file['Model'].astype('str')
        new_file['Combined'] = new_file['BrandName'].astype('str') + new_file['Model'].astype('str')
        old_file['Combined_DD']=old_file['BrandName'].astype('str') + old_file['SubDevice_DisplayName'].astype('str')
        new_file['Combined_DD']=new_file['BrandName'].astype('str') + new_file['SubDevice_DisplayName'].astype('str')

        if old_file.shape[0] > new_file.shape[0]:
            st.write("Total number of records removed in the current build :", old_file.shape[0]- new_file.shape[0])
            for value1 in old_file['BrandName']:
                brands.add(value1)
            for value2 in new_file['BrandName'].unique():
                if value2 not in brands:
                    brands_count.append(value2)
            your_output_list = [item.replace(":", " :") for item in brands_count]
            st.write(your_output_list)

            st.write("Total number of brands:",len(brands_count))

            for value1 in old_file['Model']:
                models.add(value1)
            for value2 in new_file['Model'].unique():
                if value2 not in models:
                    models_count.append(value2)
            your_output_list = [item.replace(":", " :") for item in models_count]
            st.write(your_output_list)

            st.write("Total number of Models:",len(models_count))

            for value1 in old_file['Combined']:
                Combined.add(value1)
            for value2 in new_file['Combined'].unique():
                if value2 not in Combined:
                    combined_count.append(value2)
            your_output_list = [item.replace(":", " :") for item in combined_count]
            st.write("Total number of of brand and model",your_output_list)

            for value1 in old_file['Combined_DD']:
                combined_DD.add(value1)
            for value2 in new_file['Combined_DD'].unique():
                if value2 not in combined_DD:
                    Combined_DD_count.append(value2)
            your_output_list = [item.replace(":", " :") for item in Combined_DD_count]
            st.write("Total number of brand and display device",your_output_list)

            workbook = openpyxl.Workbook()

            # Create a new sheet in the workbook
            sheet = workbook.active

            # Write data to the sheet
            sheet['A1'] = "New brands added"
            sheet['A2'] = len(brands_count)
            sheet['A3'] = "Brands"
            sheet['A4'] = str(brands_count)

            sheet['B1'] = "New models added"
            sheet['B2'] = len(models_count)
            sheet['B3'] = "Models"
            sheet['B4'] = str(models_count)

            sheet['C1'] = "Total number of brand and model combination present"
            sheet['C2'] = len(combined_count)
            sheet['C3'] = "Brand and model"
            sheet['C4'] = str(combined_count)

            sheet['D1'] = "Total number of brand and Display_Device combination present"
            sheet['D2'] = len(Combined_DD_count)
            sheet['D3'] = "Brand and Display_Device"
            sheet['D4'] = str(Combined_DD_count)

            sheet['E1']='Delta added removed'
            sheet['E2']= old_file.shape[0] - new_file.shape[0]

            for value2 in new_file['BrandName']:
                brands_removed.add(value2)
            for value1 in old_file['BrandName'].unique():
                if value1 not in brands_removed:
                    brands_count_removed.append(value1)
            your_output_list = [item.replace(":", " :") for item in brands_count_removed]
            st.write("Brands removed",your_output_list)

            for value2 in new_file['Model']:
                models_removed.add(value2)
            for value1 in old_file['Model'].unique():
                if value1 not in models_removed:
                    models_count_removed.append(value1)
            your_output_list = [item.replace(":", " :") for item in models_count_removed]
            st.write("Models removed",your_output_list)

            for value2 in new_file['Combined']:
                Combined_removed.add(value2)
            for value1 in old_file['Combined'].unique():
                if value1 not in Combined_removed:
                    combined_count_removed.append(value1)
            your_output_list = [item.replace(":", " :") for item in combined_count_removed]
            st.write("Brand and model removed",your_output_list)
            

            for value2 in new_file['Combined_DD']:
                combined_DD_removed.add(value2)
            for value1 in old_file['Combined_DD'].unique():
                if value1 not in combined_DD_removed:
                    Combined_DD_count_removed.append(value1)
            your_output_list = [item.replace(":", " :") for item in Combined_DD_count_removed]
            st.write("Brand and display device removed",your_output_list)




            # Write data to the sheet
            sheet['F1'] = "brands Removed"
            sheet['F2'] = len(brands_count_removed)
            sheet['F3'] = "Brands"
            sheet['F4'] = str(brands_count_removed)

            sheet['G1'] = "models Removed"
            sheet['G2'] = len(models_count_removed)
            sheet['G3'] = "Models"
            sheet['G4'] = str(models_count_removed)

            sheet['H1'] = "Total number of brand and model combination removed"
            sheet['H2'] = len(combined_count_removed)
            sheet['H3'] = "Brand and model"
            sheet['H4'] = str(combined_count_removed)

            sheet['I1'] = "Total number of brand and Display_Device combination removed"
            sheet['I2'] = len(Combined_DD_count_removed)
            sheet['I3'] = "Brand and Display_Device"
            sheet['I4'] = str(Combined_DD_count_removed)


            # Save the workbook to a file

            outPath = Path('C:/Projects')
            outPath.mkdir(parents=True, exist_ok=True)
            workbook.save(str(outPath/ 'Results.xlsx'))
    
        else:
            st.write("Total number of records added in current build",new_file.shape[0] - old_file.shape[0])
            for value1 in old_file['BrandName']:
                    brands.add(value1)
            for value2 in new_file['BrandName'].unique():
                if value2 not in brands:
                    brands_count.append(value2)
            your_output_list = [item.replace(":", " :") for item in brands_count]
            st.write(your_output_list)

            st.write("Total number of brands added:",brands_count)

            for value1 in old_file['Model']:
                models.add(value1)
            for value2 in new_file['Model'].unique():
                if value2 not in models:
                    models_count.append(value2)
            your_output_list = [item.replace(":", " :") for item in models_count]
            st.write(your_output_list)

            st.write("Total number of Models:",models_count)

            for value1 in old_file['Combined']:
                Combined.add(value1)
            for value2 in new_file['Combined'].unique():
                if value2 not in Combined:
                    combined_count.append(value2)
            your_output_list = [item.replace(":", " :") for item in combined_count]
            st.write("Total number of brand and model added",your_output_list)

            for value1 in old_file['Combined_DD']:
                combined_DD.add(value1)
            for value2 in new_file['Combined_DD'].unique():
                if value2 not in combined_DD:
                    Combined_DD_count.append(value2)
            your_output_list = [item.replace(":", " :") for item in Combined_DD_count]
            st.write("Total number of brand and display device added",your_output_list)

            workbook = openpyxl.Workbook()

            # Create a new sheet in the workbook
            sheet = workbook.active

            # Write data to the sheet
            sheet['A1'] = "New brands added"
            sheet['A2'] = len(brands_count)
            sheet['A3'] = "Brands"
            sheet['A4'] = str(brands_count)

            sheet['B1'] = "New models added"
            sheet['B2'] = len(models_count)
            sheet['B3'] = "Models"
            sheet['B4'] = str(models_count)

            sheet['C1'] = "Total number of brand and model combination present"
            sheet['C2'] = len(combined_count)
            sheet['C3'] = "Brand and model"
            sheet['C4'] = str(combined_count)

            sheet['D1'] = "Total number of brand and Display_Device combination present"
            sheet['D2'] = len(Combined_DD_count)
            sheet['D3'] = "Brand and Display_Device"
            sheet['D4'] = str(Combined_DD_count)

            sheet['E1']='Delta added removed'
            sheet['E2']= old_file.shape[0] - new_file.shape[0]

            for value2 in new_file['BrandName']:
                brands_removed.add(value2)
            for value1 in old_file['BrandName'].unique():
                if value1 not in brands_removed:
                    brands_count_removed.append(value1)
            your_output_list = [item.replace(":", " :") for item in brands_count_removed]
            st.write("Brands removed",your_output_list)

            for value2 in new_file['Model']:
                models_removed.add(value2)
            for value1 in old_file['Model'].unique():
                if value1 not in models_removed:
                    models_count_removed.append(value1)
            your_output_list = [item.replace(":", " :") for item in models_count_removed]
            st.write("Models removed",your_output_list)

            for value2 in new_file['Combined']:
                Combined_removed.add(value2)
            for value1 in old_file['Combined'].unique():
                if value1 not in Combined_removed:
                    combined_count_removed.append(value1)
            your_output_list = [item.replace(":", " :") for item in combined_count_removed]
            st.write("Brand and model removed",your_output_list)
            

            for value2 in new_file['Combined_DD']:
                combined_DD_removed.add(value2)
            for value1 in old_file['Combined_DD'].unique():
                if value1 not in combined_DD_removed:
                    Combined_DD_count_removed.append(value1)
            your_output_list = [item.replace(":", " :") for item in Combined_DD_count_removed]
            st.write("Brand and Display device removed",your_output_list)




            # Write data to the sheet
            sheet['F1'] = "brands Removed"
            sheet['F2'] = len(brands_count_removed)
            sheet['F3'] = "Brands"
            sheet['F4'] = str(brands_count_removed)

            sheet['G1'] = "models Removed"
            sheet['G2'] = len(models_count_removed)
            sheet['G3'] = "Models"
            sheet['G4'] = str(models_count_removed)

            sheet['H1'] = "Total number of brand and model combination removed"
            sheet['H2'] = len(combined_count_removed)
            sheet['H3'] = "Brand and model"
            sheet['H4'] = str(combined_count_removed)

            sheet['I1'] = "Total number of brand and Display_Device combination removed"
            sheet['I2'] = len(Combined_DD_count_removed)
            sheet['I3'] = "Brand and Display_Device"
            sheet['I4'] = str(Combined_DD_count_removed)


            # Save the workbook to a file
            outPath = Path('C:/Projects')
            outPath.mkdir(parents=True, exist_ok=True)
            workbook.save(str(outPath/ 'Results.xlsx'))
            
            
if __name__=='__main__':
    run()



        

