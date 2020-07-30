# ---------------------------------------------------------------  
# IMPORT  
from pynput.keyboard import Key, Controller  
import time  
import appscript  
# ---------------------------------------------------------------  
class Music_Control:  
    # -----------------------------------------------------------  
    def __init__(self):  
        self.keyboard = Controller()  
        self.iTunes = appscript.app('iTunes')  
    # -----------------------------------------------------------  
    def playPause(self):  
        self.iTunes.playpause()  
        print "Play/Pause"  
    # -----------------------------------------------------------  
    def nextTrack(self):  
        self.iTunes.next_track()  
        self.information()  
        print "Next Track"  
    # -----------------------------------------------------------  
    def previousTrack(self):  
        self.iTunes.previous_track()  
        print "Previous Track"  
    # -----------------------------------------------------------  
    def increaseVolume(self):  
        self.iTunes.sound_volume.set(self.iTunes.sound_volume.get() + 1)  
        print "Increase Volume To " + str(self.iTunes.sound_volume.get())  
    # -----------------------------------------------------------  
    def decreaseVolume(self):  
        self.iTunes.sound_volume.set(self.iTunes.sound_volume.get() - 1)  
        print "Decrease Volume " + str(self.iTunes.sound_volume.get())  
    # -----------------------------------------------------------  
    def information(self):  
        track = self.iTunes.current_track()  
        print track.name() + " By " + track.artist()  
# ---------------------------------------------------------------  
