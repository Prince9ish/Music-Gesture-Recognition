# -------------------------------------------------------------------------------  
# Import  
import Leap, sys, thread, time, math  
from Leap import CircleGesture, KeyTapGesture, ScreenTapGesture, SwipeGesture  
from Music_Control import*  
# -------------------------------------------------------------------------------  
class Leap_Listener(Leap.Listener):  
    # ---------------------------------------------------------------------------  
    finger_names = ['Thumb', 'Index', 'Middle', 'Ring', 'Pinky']  
    bone_names = ['Metacarpal', 'Proximal', 'Intermediate', 'Distal']  
    state_names = ['STATE_INVALID', 'STATE_START', 'STATE_UPDATE', 'STATE_END']  
    # ---------------------------------------------------------------------------  
    def on_init(self, controller):  
        print("Init")  
    # ---------------------------------------------------------------------------  
    # Check  
    def isClockwise(self,number):  
        if (number <= Leap.PI / 2):  
            return True  
        else:  
            return False  
 
    @staticmethod  
    def swipeDirection(Xnumber,Ynumber):  
        if Xnumber > 0 and math.fabs(Xnumber) > math.fabs(Ynumber) :  
            return "Right"  
        if Xnumber < 0 and math.fabs(Xnumber) > math.fabs(Ynumber) :  
            return "Left"  
        elif Ynumber > 0 and math.fabs(Xnumber) < math.fabs(Ynumber) :  
            return "Up"  
        elif Ynumber < 0 and math.fabs(Xnumber) < math.fabs(Ynumber):  
            return "Down"  
    # ---------------------------------------------------------------------------  
    def on_connect(self, controller):  
        # Enable gestures  
        controller.enable_gesture(Leap.Gesture.TYPE_CIRCLE)  
        controller.enable_gesture(Leap.Gesture.TYPE_SCREEN_TAP)  
        controller.enable_gesture(Leap.Gesture.TYPE_SWIPE)  
    # ---------------------------------------------------------------------------  
    def on_frame(self, controller):  
        music = Music_Control()  
        frame = controller.frame()  
        for gesture in frame.gestures():  
            # -----------------------------------------------------------------------  
            if gesture.type == Leap.Gesture.TYPE_CIRCLE:  
                circle = CircleGesture(gesture)  
                if self.isClockwise(circle.pointable.direction.angle_to(circle.normal)):  
                    music.increaseVolume()  
                else:  
                    music.decreaseVolume()  
            # -----------------------------------------------------------------------  
            if gesture.type is Leap.Gesture.TYPE_SWIPE:  
                swipe = Leap.SwipeGesture(gesture)  
