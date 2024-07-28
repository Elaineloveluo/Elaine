import os,time

def SavaImage(driver,errorImage):
    Rawpath = os.path.join(os.path.dirname(os.path.dirname(__file__)),'Image')
    if os.path.exists('Image') and os.path.isdir('Image'):
        pass
    else:
        os.mkdir('Image')
    NewPicture = Rawpath + '\\' + time.strftime('%Y%y%d_%H%M%S') + '_' + errorImage
    driver.get_screenshot_as_file(NewPicture)