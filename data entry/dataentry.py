import PySimpleGUI as sg
import pandas as pd

sg.theme("Darkgreen")

Excel_file = "dataentry.xlsx"

df = pd.read_excel(Excel_File)

layout=[
    [sg.text('Masukan Data Kamu')]
    [sg.text('Masukan umur kamu ')]
]
