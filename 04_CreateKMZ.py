import os, simplekml, datetime as dt, pyexiv2 as pex
import warnings
warnings.filterwarnings("ignore")

path = r'T:\Planning\02_KPI_GIS\09_Photos\Ground\20161115\LQ'
OutputFile = r'T:\Planning\02_KPI_GIS\09_Photos\Ground\20161115\Test.kmz'
print path
print OutputFile

def GetLatLong(fn):
    metadata = pex.ImageMetadata(fn)
    metadata.read()
    Lat = metadata['Exif.GPSInfo.GPSLatitude'].human_value
    Long = metadata['Exif.GPSInfo.GPSLongitude'].human_value
    Alt = metadata['Exif.GPSInfo.GPSAltitude'].human_value
    DateTime = metadata['Exif.Image.DateTime'].human_value #string
    DT = dt.datetime.strptime(DateTime, '%Y:%m:%d %H:%M:%S') #Datetime object
    return (Lat, Long, Alt, DT)

def FormatLatLong(LatLongString):
    d = LatLongString.find('deg')
    Degrees = float(LatLongString[:d])
    m = LatLongString.find("'")
    Minutes = float(LatLongString[d+4:m])
    if LatLongString.find('"') >= 0:
        s = LatLongString.find('"')
        print LatLongString[m+2:s]
        Seconds = float(LatLongString[m+2:s])
        decCoords = Degrees + Minutes/60.00 + Seconds/3600.0
    else:
        decCoords = Degrees + Minutes/60.00
    print decCoords
    return decCoords


kml = simplekml.Kml()
for (dirpath, dirnames, filenames) in os.walk(path):
    for filename in filenames:
        fullpath = os.path.join(dirpath, filename)
        try:
            Lat, Long, Alt, DT = GetLatLong(fullpath)
        except:
            Lat, Long, Alt, DT = (None, None, None, None)
        print '%s: Lat: %s, Long: %s, Alt: %s' % (fullpath, Lat, Long, Alt)
        if Lat:
            x, y = (FormatLatLong(Lat), FormatLatLong(Long))
            point = kml.newpoint(name = filename , coords = [(-y,x)])
            picpath = kml.addfile(fullpath)
            print picpath
            fn = 'files/'+ os.path.splitext(filename)[0] + '.jpg' #Note: will not work if .JPG is used, must be lower case.
            balstylestring = "<![CDATA[ <p><b>Image: </b>" + filename + "<p><b>Date: </b>" + DT.strftime('%a, %B %d, %Y') + "<br/></br><b>Time: </b>" + DT.strftime("%I:%M:%S %p")+ "<br/></br><hr></p><table width=500 cellpadding=0 cellspacing=0> <tbody><tr><td><img width=100% src='" + fn + "' /></td></tr></tbody></table>]]>"
##            balstylestring = "< ![CDATA[<p><b>Date:</b> " + DT.strftime('%a, %B %d, %Y') + " <b>Time:</b> " + DT.strftime("%I:%M:%S %p") + "</p> <table width="500" cellspacing="0" cellpadding="0">  <tbody><tr><td><img width="100%" src='" + fn + "'></td></tr></tbody></table>]] >"
            point.style.balloonstyle.text = balstylestring
            point.style.iconstyle.icon.href = "C:/Users/Peter/AppData/LocalLow/Google/GoogleEarth/view_9.png"
            headingcalc = 45
            point.style.iconstyle.icon.heading = headingcalc

kml.savekmz(OutputFile, format = False)
print 'done!'
