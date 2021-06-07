import rotatescreen
import time
screen = rotatescreen.get_primary_display()
for i in range(1, 13):
    time.sleep(1)
    screen.rotate_to(i*90%360)
## Press Alt + F2 when the original position comes to stop rotating