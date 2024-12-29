import cv2 
import os 

def capture_frames():
    cam = cv2.VideoCapture("raw_data/Rickroll_data.mp4") 
    
    try: 
        if not os.path.exists('frame_data'): 
            os.makedirs('frame_data') 
    
    except OSError: 
        print ('Error: Creating directory of data') 
    
    currentframe = 0
    
    while(True): 

        ret, frame = cam.read() 
    
        if ret: 
            name = './frame_data/frame' + str(currentframe) + '.jpg'
            print ('Creating...' + name) 

            frame = cv2.resize(frame, (64, 48))
            cv2.imwrite(name, frame) 
    
            currentframe += 1
        else: 
            break
    
    print('Done')