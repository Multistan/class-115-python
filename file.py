import os
import shutil

import time
import random

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir="C:/Users/arvin/Downloads"
to_dir="C:/Users.arvin/OneDrive/Desktop/Nethra/code/class 115/move folder"
dir_tree = { "Image_Files": ['.jpg', '.jpeg', '.png', '.gif', '.jfif'], "Video_Files": ['.mpg', '.mp2', '.mpeg', '.mpe', '.mpv', '.mp4', '.m4p', '.m4v', '.avi', '.mov'], "Document_Files": ['.ppt', '.xls', '.xlsx' '.csv', '.pdf', '.txt'], "Setup_Files": ['.exe', '.bin', '.cmd', '.msi', '.dmg'] }
#user defined class
class FileMoveHandler(FileSystemEventHandler):
    def on_created(self,event):
        name,extention=os.path.splitext(event.src_path)
        time.sleep(1)

        for key,value in dir_tree.items():
            time.sleep(1)

            if extention in value:
                file_name= os.path.basename(event.src_path)
                print("downloading files....")

                path1= from_dir+"/"+file_name
                path2= to_dir+"/"+key
                path3=to_dir+"/"+key+"/"+file_name

                if(os.path.exists(path2)):
                    print("directory files....")
                    print("moving"+file_name+"......")
                    shutil.move(path1,path3)
                    time.sleep(1)
                else:
                    print("making new directory")
                    os.makedirs(path2)
                    print("moving"+file_name+"......")
                    shutil.move(path1,path3)
                    time.sleep(1)


event_handler= FileMoveHandler()

observer=Observer()

#schudle obsrver
observer.schedule(event_handler,from_dir,recursive=True)

observer.start()

try:
    while True:
        time.sleep(1)
        print("Runnning.........")

except KeyboardInterrupt:
    print("stopped")
    observer.stop()