# %%
import pandas as pd
import numpy as np
import os
from pathlib import Path
import re

#Arabic quran
df_ar = pd.read_csv('quran.csv')

df_ar.head()

# %%
# surah name
df_ar['surahs_name'] = df_ar['رقم السورة'].astype(str) + ' ' + df_ar['اسم السورة انجليزي'] + ' - ' + 'سُورَةُ ' + df_ar['اسم السورة عربي']
surahs_name = df_ar['surahs_name'].unique().tolist()
surahs_name

#ayat name for .md files
df_ar['ayat_name'] = df_ar['رقم السورة'].astype(str) + '-' + df_ar['رقم الآية'].astype('Int64').astype(str) + ' ' + df_ar['نص الآية']
ayat_name = df_ar['ayat_name'].tolist()
ayat_name

# ayat text
ayat_text = df_ar['نص الآية'].tolist()

# ayat drawing
ayat_drawing = df_ar['رسم الآية'].tolist()
surahs_name

#surahs number
surahs_number = df_ar['رقم السورة'].tolist()

#juz number
juz_number = df_ar['رقم الجزء'].tolist()

# %%
# English quran
df_en = pd.read_csv('quran-en.csv')
df_en.head()

# %%
# ayat text
df_en['ayat_translation'] = df_en['translation'] + ' (' + df_en['aya'].astype(str) + ')'
ayat_translation = df_en['ayat_translation'].tolist()
ayat_translation

#ayat notes
df_en[df_en['footnotes'].isna()] = ""
ayat_notes = df_en['footnotes'].tolist()
ayat_notes


# %%
# create folders with surahs names
parent_folder = "Ayat - آيَاتُ القُرآنِ"
if not os.path.exists(parent_folder):
    os.mkdir(parent_folder)
    print(f"Parent folder '{parent_folder}' created successfully!")

# Create the subfolders inside the parent folder
for subfolder_name in surahs_name:
    subfolder_path = os.path.join(parent_folder, subfolder_name)
    if not os.path.exists(subfolder_path):
        os.mkdir(subfolder_path)
        print(f"Subfolder '{subfolder_path}' created successfully!")

# %%
# functoin to get the firts digit
def get_first_num(text):
    match = re.search(r'\d+', text)
    if match:
        first_number = int(match.group())
        return first_number
    else:
        print("No valid number found in the text.")
        return None

# %%
# juz number
juz_order_list = [
    "1 - الجُزْءُ الأَوَّلُ","2 - الجُزْءُ الثَّانِى","3 - الجُزْءُ الثَّالِثُ","4 - الجُزْءُ الرَّابِعُ","5 - الجُزْءُ الخَامِسُ","6 - الجُزْءُ السَّادِسُ","7 - الجُزْءُ السَّابِعُ","8 - الجُزْءُ الثَّامِنُ","9 - الجُزْءُ التَّاسِعُ","10 - الجُزْءُ العَاشِرُ","11 - الجُزْءُ الحَادِىَ عَشَرَ","12 - الجُزْءُ الثَّانِىَ عشَرَ",
    "13 - الجُزْءُ الثَّالِثَ عَشَرَ","14 - الجُزْءُ الرَّابِعَ عَشَرَ","15 - الجُزْءُ الخَامِسَ عَشَرَ","16 - الجُزْءُ السَّادِسَ عَشَرَ","17 - الجُزْءُ السَّابِعَ عَشَرَ","18 - الجُزْءُ الثَّامِنَ عَشَرَ","19 - الجُزْءُ التَّاسِعَ عَشَرَ","20 - الجُزْءُ العِشْرُونَ","21 - الجُزْءُ الحَادِى وَالعِشْرُونَ",
    "22 - الجُزْءُ الثَّانِى وَالعِشْرُونَ","23 - الجُزْءُ الثَّالِثُ وَالعِشْرُونَ","24 - الجُزْءُ الرَّابِعُ وَالعِشْرُونَ","25 - الجُزْءُ الخَامِسُ وَالعِشْرُونَ","26 - الجُزْءُ السَّادِسُ وَالعِشْرُونَ","27 - الجُزْءُ السَّابِعُ وَالعِشْرُونَ","28 - الجُزْءُ الثَّامِنُ وَالعِشْرُونَ",
    "29 - الجُزْءُ التَّاسِعُ وَالعِشْرُونَ","30 - الجُزْءُ الثَّلَاثُونَ"
]

# Creating the dictionary
juz_dict = {i+1: name for i, name in enumerate(juz_order_list)}

# function to return juz name
def get_juz_name(number):
    return juz_dict.get(number, "Number out of range")
get_juz_name(5)


# surah number
# Creating the dictionary
surahs_dict = {i+1: name for i, name in enumerate(surahs_name)}

# function to return juz name
def get_surah_name(number):
    return surahs_dict.get(number, "Number out of range")

# %%
#create .md files of ayat inside each surah folder
# create ayat .md files
parent_folder = "Ayat - آيَاتُ القُرآنِ"
# Create Markdown files in each subfolder
for surah_name in surahs_name:
    surah_path = os.path.join(parent_folder, surah_name)
    for i,ayah_name in enumerate(ayat_name):
        if get_first_num(ayah_name) == get_first_num(surah_name):
            
            if len(ayah_name) > 252:
                ayah_name = ayah_name[:252]

            # Write some sample content to the Markdown file
            ayah_file_path = os.path.join(surah_path, f"{ayah_name}.md")

            # Ensure the directory exists before writing the file
            os.makedirs(surah_path, exist_ok=True)
            
            with open(ayah_file_path, 'w', encoding='utf-8') as file:
                file.write("\n\n\n")
                file.write(f"###### {ayat_drawing[i]}")
                file.write("\n\n\n")
                file.write(f"{ayat_text[i]}")
                file.write("\n\n--- \n\n")
                file.write(f"###### {ayat_translation[i]}")
                file.write("\n\n")
                if ayat_notes[i] != '':
                    file.write("\n")
                    file.write(f"{ayat_notes[i]}")
                    file.write("\n\n")
                file.write("\n\n\n\n")
                file.write(f"[[{get_juz_name(juz_number[i])}]]   ->   ")
                file.write(f"[[{get_surah_name(surahs_number[i])}]]  ")
        else:
            pass

    print(f"Markdown file '{ayah_file_path}' created successfully!")
print("All Markdown files generated. Feel free to customize their content!")

# %%
# create surahs .md files
parent_folder = "Surahs - سُوَرُ القُرْآنِ"
if not os.path.exists(parent_folder):
    os.mkdir(parent_folder)
    print(f"Parent folder '{parent_folder}' created successfully!")

# Create the .md files inside the parent folder
for surah_name in surahs_name:
    surah_name = f"{surah_name}.md"
    surah_path = os.path.join(parent_folder, surah_name)
    with open(surah_path, 'w', encoding='utf-8') as file:
                file.write("")

# %%
# create juzs .md files
parent_folder = "Juz - أَجْزَاءُ القُرْآنِ"
if not os.path.exists(parent_folder):
    os.mkdir(parent_folder)
    print(f"Parent folder '{parent_folder}' created successfully!")

# Create the .md files inside the parent folder
for juz_name in juz_order_list:
    juz_name = f"{juz_name}.md"
    juz_path = os.path.join(parent_folder, juz_name)
    with open(juz_path, 'w', encoding='utf-8') as file:
                file.write("")


