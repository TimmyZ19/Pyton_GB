import view
import csv_create as csv_file
import xml_create as xml_file


def Selection_processing():
    selection = view.User_selection()
    if selection == 1:
        Import_processing(view.User_data_entry())
    else:
        Export_processing()


def Export_processing():
    csv_file.File_reading()
    xml_file.File_reading()



def Import_processing(data):
    csv_file.File_recording(data)
    xml_file.File_recording(data)
