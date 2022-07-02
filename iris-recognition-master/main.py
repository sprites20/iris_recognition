from iris_recognition import *
import os
import pickle

filepath1 = r'./aeval1.bmp'
filepath2 = r'./aeval2.bmp'

folder_pair = {}
eye_arr = []

def save_data():
    names_file = open('data/names.dat', 'wb')
    global folder_pair
    pickle.dump(folder_pair, names_file)
    names_file.close()
def load_data():
    try:
        names_df_file = open('data/names.dat', 'rb')
        global folder_pair
        folder_pair = pickle.load(names_df_file)
        names_df_file.close()
    except:
        None

currentimage = ""



def get_folders(MYDIR):
    folder_nums = []
    for entry_name in os.listdir(MYDIR):
        entry_path = os.path.join(MYDIR, entry_name)
        if os.path.isdir(entry_path):
            try:
                a = int(entry_name)
                folder_nums.append(entry_name)
            except:
                None
    return folder_nums
    #print(folder_nums)
    
folder_nums = get_folders("./enrolledimages")
print(folder_nums)
load_data()
print(folder_pair)

classname = "Eye1"

def enrolleye(imgpath, eyename, side):
    #curreyefolder_main = get_folders("./enrolledimages")
    curreyenum = 0
    currpath = ""
    try:
        if os.path.isdir('./enrolledimages/' + str(folder_pair[classname])):
            curreyenum = int(folder_pair[classname])
            currpath = './enrolledimages/' + str(folder_pair[classname])
    except:
        for i in range(1,1000000000):
            if not os.path.isdir('./enrolledimages/' + str(i)):
                curreyenum = i
                os.mkdir('./enrolledimages/' + str(i))
                currpath = './enrolledimages/' + str(i)
                folder_pair[classname] = str(i)
                save_data()
                break
            else:
                curreyenum = i
                currpath = './enrolledimages/' + str(i)
    #Generate left/right folder
    if side == 0:
        if not os.path.isdir(currpath + '/left'):
            os.mkdir(currpath + '/left')
            currpath += '/left'
        else:
            currpath += '/left'
    elif side == 1:
        if not os.path.isdir(currpath + '/right'):
            os.mkdir(currpath + '/right')
            currpath += '/right'
        else:
            currpath += '/left'
    else:
        print("Invalid side!")
        return None
    #Generate Eye Folder
    for i in range(1,1000000000):
        if not os.path.isdir(currpath + '/' + str(i)):
            curreyenum = i
            os.mkdir(currpath + '/' + str(i))
            currpath += '/' + str(i)
            break

    if os.path.isdir(currpath):
        roi = load_rois_from_image(imgpath, currpath)
        return roi

"""
if os.path.isfile(filepath1) and os.path.isfile(filepath2):
    #compare_images(filepath1, filepath2)

    currentimage = filepath1
    enrolleye(currentimage, classname, 0)
    
    currentimage = filepath2
    enrolleye(currentimage, classname, 0)
    
    #getall_matches(rois_1, rois_2, 0.8, 10, 0.15, show=True)
"""