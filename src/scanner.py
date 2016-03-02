import findContours
import scaleDetection
import stitch
import gui
import determineSkew
import scannerCamera

scaleDetect = ScaleDetection()
#detSkew = DetermineSkew()
cam1Settings = ScannerCamera() #not implemented yet?
cam2Settings = ScannerCamera()

def scale_calibration(image, objx, objy):
    success = scaleDetect.calibrate(image, objx, objy)
    scaleDetect.saveConfigFile()
    return success

def scale_calibration_data():
    success = scaleDetect.loadConfigFile()
    #load other calibration data as well
    return success

def skew_calibration(calibImages):
    dst, roi, error = DetermineSkew.createSkewMatrix(calibImages)
    return dst

def skew_correction(image):
    a = 0

def stitch_images(image1, image2):
    #stitcher = Stitcher()
    return Stitcher.stitch((image1,image2)) #correct order for images?

def find_contours(image):
    #findContours = FindContours()
    contours, hierarchy, edgeImage = FindContours.find_all_contours(image)
    finalContours = findContours.select_contours(contours, hierarchy)
    return finalContours,edgeImage

def export_json(contours):
    a = 0

def gui_start_screen():
    a = 0

def gui_scale_calibration_screen():
    a = 0

def gui_skew_calibration_screen():
    a = 0

def gui_take_pictures_screen():
    a = 0

#Shows the board with contours
def gui_enter_thickness_screen(edgeImage):
    a = 0

#Is this function needed?
def gui_export_screen():
    a = 0

def main():
    gui_start_screen()

    #load calibration data
    scaleDataExists = scale_calibration_data()

    #if calibration data doesn't exist, ask user to calibrate
    if (not scaleDataExists):
        image, objx, objy = gui_scale_calibration_screen()
        scale_calibration(image, objx, objy)

    #ask user if they want to calibrate if skew calibration data doesn't exist
    calibImages1, calibImages2 = gui_skew_calibration_screen()
    dst1 = skew_calibration(calibImages1)
    dst2 = skew_calibration(calibImages2)

    image1, image2 = gui_take_pictures_screen()



    image1 = skew_correction(image1, dst1)
    image2 = skew_correction(image2, dst2)

    finalImage = stitch_images(image1, image2)
    contours, edgeImage = find_contours(finalImage)

    #what should happen if they don't like the image? Do we go back to start?
    thickness = gui_enter_thickness_screen(edgeImage)

    #scale calculation?

    export_json(contours)



if __name__ == "__main__":
    main()