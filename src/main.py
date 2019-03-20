import io
from tendo import singleton
from PIL import Image

from VideoCapture import VideoCapture
from ROI import ROI
from GUI import GUI

me = singleton.SingleInstance()

videoCapture = VideoCapture()

gui = GUI('LightMouseGun')

start_capture = False
show_preview = False
positions = ['top_left', 'top_center', 'top_right',
             'middle_left', 'middle_center', 'middle_right',
             'bottom_left', 'bottom_center', 'bottom_right']
roi = ROI(positions[7])     #bottom_center

while True:
    button, values = gui.window.Read(timeout=0)

    if button is 'START':
        videoCapture.prepare_camera()
        if videoCapture.cam_is_available():
            gui.popup('No camera detected')
            break
        videoCapture.start()
        start_capture = not start_capture
        gui.disable('START').enable('STOP').enable('PREVIEW')
    elif button is 'STOP':
        videoCapture.stop()
        start_capture = False
        show_preview = False
        gui.window.Element('OUTPUT').Update(filename='', size=gui.elSize)
        gui.enable('START').disable('STOP').disable('PREVIEW')
    elif button is 'PREVIEW':
        show_preview = not show_preview
    elif button in positions:
        index = positions.index(button)
        roi.position = positions[index]
    elif button is None:
        videoCapture.stop()
        break

    if start_capture:
        frame = videoCapture.frame
        processedFrame = roi.process(frame)
        if show_preview:
            img = Image.fromarray(processedFrame)  # create PIL image from frame
            bio = io.BytesIO()  # a binary memory resident stream
            img.save(bio, format='PNG')  # save image as png to it
            imgbytes = bio.getvalue()
            gui.window.Element('OUTPUT').Update(data=imgbytes)
        else:
            gui.window.Element('OUTPUT').Update(filename='', size=gui.elSize)
gui.window.Close()