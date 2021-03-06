import cv2
import numpy as np
import pyautogui
import time
import datetime
import keyboard


def main():
    SCREEN_SIZE = (1024, 600)

    fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
    time_stamp = datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')
    file_name = f'{time_stamp}.mp4'
    print(file_name)

    out = cv2.VideoWriter(file_name,
                          fourcc, 20.0, (SCREEN_SIZE))

    waitKey_value = 1
    fps = 240
    prev = 0

    print('Recording... Press [F10] to stop')

    while True:
        time_elapsed = time.time() - prev
        img = pyautogui.screenshot()

        if time_elapsed > 1.0 / fps:
            prev = time.time()
            frame = np.array(img)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            out.write(frame)
        if keyboard.is_pressed('F10'):
            break

        cv2.waitKey(waitKey_value)

    cv2.destroyAllWindows()
    out.release()
    print('Recording Finished...')


print('Press [F10] to start recording')
keyboard.wait('F10')
main()
