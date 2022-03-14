import math



viewNormal = (-0.00255832, -0.0081181, 0.999964)
focus = (0.0117188, 0.00585938, -0.0683594)
viewUp = (0.00201308, 0.999965, 0.00812326)
viewAngle = 30
parallelScale = 78665.2
nearPlane = -157330
farPlane = 157330
imagePan = (0, 0)
imageZoom = 21.1138
perspective = 1
eyeAngle = 2
centerOfRotationSet = 0
centerOfRotation = (0.0117188, 0.00585938, -0.0683594)
axis3DScaleFlag = 0
axis3DScales = (1, 1, 1)
shear = (0, 0, 1)
windowValid = 1

#Script for capturing timelapse of all datapoints and keeping camera with it
def AnimateInTime():
    Pat = View3DAttributes()
    Pat.SetViewNormal(0.000000, 0.000000, 1.000000)
    Pat.SetFocus(0.011719, 0.005859, -0.068359)
    Pat.SetViewUp(0.000000, 1.000000, 0.000000)
    Pat.SetNearPlane(-157330.411114)
    Pat.SetFarPlane(157330.411114)
    Pat.SetImagePan(0.000000, 0.000000)
    Pat.SetImageZoom(66.264076)
    Pat.SetParallelScale(78665.205557)
    Pat.SetPerspective(1)
    imagezoom = 66.264076
    for i in range(6,100):
        if (i >= 6 and i < 11):
            imagezoom = imagezoom - 5.7719466
        elif (i >= 11 and i < 16):
            imagezoom = imagezoom - 2.3713346
        elif (i >= 16 and i < 21):
            imagezoom = imagezoom - 1.6196536
        elif (i >= 21 and i < 26):
            imagezoom = imagezoom - 0.6056816
        elif (i >= 26 and i < 31):
            imagezoom = imagezoom - 0.5005634
        elif (i >= 31 and i < 36):
            imagezoom = imagezoom - 0.4136888
        elif (i >= 36 and i < 41):
            imagezoom  = imagezoom - 0.3418916
        elif (i >= 41 and i < 56):
            imagezoom = imagezoom - 0.094185
        elif (i >= 56 and i < 61:
            imagezoom = imagezoom - 0.2335166
        elif (i >= 61 and i < 71):
            imagezoom = imagezoom - 0.0964944
        elif (i >= 71 and i < 86):
            imagezoom = imagezoom - 0.053165
        Pat.SetImageZoom(imagezoom)
        TimeSliderSetState(i)

AnimateInTime()
#Script for flying into vector plot
def fly():
    Pat = View3DAttributes()
    Pat.SetViewNormal(0.437808, -0.860044, -0.262006)
    Pat.SetFocus(0.000000, 0.029297, -0.032227)
    Pat.SetViewUp(0.039855, 0.309699, -0.949999)
    Pat.SetNearPlane(-94879.786788)
    Pat.SetFarPlane(94879.786788)
    Pat.SetImagePan(0.000000, 0.000000)
    Pat.SetImageZoom(1.210000)
    Pat.SetParallelScale(47439.893394)
    Pat.SetPerspective(1)
    Pat1 = View3DAttributes()
    Pat1.SetViewNormal(-0.939537, -0.338851, 0.049509)
    Pat1.SetFocus(0.000000, 0.029297, -0.032227)
    Pat1.SetViewUp(-0.342411, 0.931690, -0.121278)
    Pat1.SetNearPlane(-94879.786788)
    Pat1.SetFarPlane(94879.786788)
    Pat1.SetImagePan(0.000000, 0.000000)
    Pat1.SetImageZoom(1.000000)
    Pat1.SetParallelScale(47439.893394)
    Pat1.SetPerspective(1)
    vpts = (Pat,Pat1)
    x = [0,1]
    nsteps = 100
    for i in range (nsteps):
        t = float(i) / float(nsteps - 1)
        c = EvalCubicSpline(t, x , vpts)
        SetView3D(c)

fly()

def AnimateInTime():
    Pat = View3DAttributes()
    Pat.SetViewNormal(0.000000, 0.000000, 1.000000)
    Pat.SetFocus(0.000000, 0.029297, -0.032227)
    Pat.SetViewUp(0.000000, 1.000000, 0.000000)
    Pat.SetNearPlane(-94879.786788)
    Pat.SetFarPlane(94879.786788)
    Pat.SetImagePan(0.000000, 0.000000)
    Pat.SetImageZoom(37.404343)
    Pat.SetParallelScale(47439.893394)
    Pat.SetPerspective(1)
    Pat1 = View3DAttributes()
    Pat1.SetViewNormal(0.000000, 0.000000, 1.000000)
    Pat1.SetFocus(0.000000, 0.029297, -0.032227)
    Pat1.SetViewUp(0.000000, 1.000000, 0.000000)
    Pat1.SetNearPlane(-94879.786788)
    Pat1.SetFarPlane(94879.786788)
    Pat1.SetImagePan(0.000000, 0.000000)
    Pat1.SetImageZoom(1.771561)
    Pat1.SetParallelScale(47439.893394)
    Pat1.SetPerspective(1)
    vpts = (Pat,Pat1)
    nsteps = 378
    for i in range (2):
        x = x + [float(i) / float(6.)]
    for i in range (21,400):
        t = float(i) / float(nsteps - 1)
        c = EvalCubicSpline(t,x,vpts)
        SetView3D(c)
        TimerSliderSetState(i)
        SaveWindow()
AnimateInTime()


#Scripting for going around the volume box and adding time to it
def AnimateInTime():
    Pat = View3DAttributes()
    Pat.SetViewNormal(0.000000, 0.000000, 1.000000)
    Pat.SetFocus(-0.019531, 0.011719, -0.030273)
    Pat.SetViewUp(0.000000, 1.000000, 0.000000)
    Pat.SetNearPlane(-91251.627485)
    Pat.SetFarPlane(91251.627485)
    Pat.SetImagePan(0.000000, 0.000000)
    Pat.SetImageZoom(30.912681)
    Pat.SetParallelScale(45625.813743)
    Pat.SetPerspective(1)
    Pat1 = View3DAttributes()
    Pat1.SetViewNormal(0.997997, -0.020198, -0.059951)
    Pat1.SetFocus(-0.019531, 0.011719, -0.030273)
    Pat1.SetViewUp(0.023596, 0.998123, 0.056522)
    Pat1.SetNearPlane(-91251.627485)
    Pat1.SetFarPlane(91251.627485)
    Pat1.SetImagePan(0.000000, 0.000000)
    Pat1.SetImageZoom(30.912681)
    Pat1.SetParallelScale(45625.813743)
    Pat1.SetPerspective(1)
    Pat2 = View3DAttributes()
    Pat2.SetViewNormal(0.022804, 0.121275, -0.992357)
    Pat2.SetFocus(-0.019531, 0.011719, -0.030273)
    Pat2.SetViewUp(-0.025634, 0.992360, 0.120687)
    Pat2.SetNearPlane(-91251.627485)
    Pat2.SetFarPlane(91251.627485)
    Pat2.SetImagePan(0.000000, 0.000000)
    Pat2.SetImageZoom(30.912681)
    Pat2.SetParallelScale(45625.813743)
    Pat2.SetPerspective(1)
    Pat3 = View3DAttributes()
    Pat3.SetViewNormal(-0.989820, 0.132409, 0.052196)
    Pat3.SetFocus(-0.019531, 0.011719, -0.030273)
    Pat3.SetViewUp(0.133617, 0.990824, 0.020351)
    Pat3.SetNearPlane(-91251.627485)
    Pat3.SetFarPlane(91251.627485)
    Pat3.SetImagePan(0.000000, 0.000000)
    Pat3.SetImageZoom(30.912681)
    Pat3.SetParallelScale(45625.813743)
    Pat3.SetPerspective(1)
    Pat4 = View3DAttributes()
    Pat4.SetViewNormal(0.000000, 0.000000, 1.000000)
    Pat4.SetFocus(-0.019531, 0.011719, -0.030273)
    Pat4.SetViewUp(0.000000, 1.000000, 0.000000)
    Pat4.SetNearPlane(-91251.627485)
    Pat4.SetFarPlane(91251.627485)
    Pat4.SetImagePan(0.000000, 0.000000)
    Pat4.SetImageZoom(30.912681)
    Pat4.SetParallelScale(45625.813743)
    Pat4.SetPerspective(1)
    vpts = (Pat,Pat1,Pat2,Pat3,Pat4)
    x = []
    nsteps = 2790
    timestep = 7
    imagezoom = 30.912681
    for i in range (5):
        x = x + [float(i) / float(6.)]
    for i in range (nsteps):
        if (i % 30 == 0):
                TimeSliderSetState(timestep)
                timestep += 1
        imagezoom = imagezoom - 0.01171478853
        t = float(i) / float(nsteps - 1)
        c = EvalCubicSpline(t, x , vpts)
        c.SetImageZoom(imagezoom)
        #SaveWindow()
#Scripting for velocity fly around (last scene)
def fly():
    Pat = View3DAttributes()
    Pat.SetViewNormal(-0.015257, 0.999606, -0.023563)
    Pat.SetFocus(0.000000, 0.029297, -0.032227)
    Pat.SetViewUp(-0.010367, -0.023723, -0.999665)
    Pat.SetNearPlane(-94879.786788)
    Pat.SetFarPlane(94879.786788)
    Pat.SetImagePan(0.000000, 0.000000)
    Pat.SetImageZoom(0.826446)
    Pat.SetParallelScale(47439.893394)
    Pat.SetPerspective(1)
    Pat1 = View3DAttributes()
    Pat1.SetViewNormal(0.977569, 0.122738, -0.171154)
    Pat1.SetFocus(0.000000, 0.029297, -0.032227)
    Pat1.SetViewUp(-0.181556, 0.079195, -0.980186)
    Pat1.SetNearPlane(-94879.786788)
    Pat1.SetFarPlane(94879.786788)
    Pat1.SetImagePan(0.000000, 0.000000)
    Pat1.SetImageZoom(0.826446)
    Pat1.SetParallelScale(47439.893394)
    Pat1.SetPerspective(1)
    Pat2 = View3DAttributes()
    Pat2.SetViewNormal(0.954277, -0.171446, -0.244872)
    Pat2.SetFocus(0.000000, 0.029297, -0.032227)
    Pat2.SetViewUp(-0.230038, 0.101925, -0.967829)
    Pat2.SetNearPlane(-94879.786788)
    Pat2.SetFarPlane(94879.786788)
    Pat2.SetImagePan(0.000000, 0.000000)
    Pat2.SetImageZoom(1.771561)
    Pat2.SetParallelScale(47439.893394)
    Pat2.SetPerspective(1)
    Pat3 = View3DAttributes()
    Pat3.SetViewNormal(0.641378, -0.521879, 0.562385)
    Pat3.SetFocus(0.000000, 0.029297, -0.032227)
    Pat3.SetViewUp(0.362922, -0.439444, -0.821692)
    Pat3.SetNearPlane(-94879.786788)
    Pat3.SetFarPlane(94879.786788)
    Pat3.SetImagePan(0.000000, 0.000000)
    Pat3.SetImageZoom(1.771561)
    Pat3.SetParallelScale(47439.893394)
    Pat3.SetPerspective(1)
    Pat4 = View3DAttributes()
    Pat4.SetViewNormal(0.421464, -0.142742, 0.895540)
    Pat4.SetFocus(0.000000, 0.029297, -0.032227)
    Pat4.SetViewUp(0.712417, -0.558905, -0.424367)
    Pat4.SetNearPlane(-94879.786788)
    Pat4.SetFarPlane(94879.786788)
    Pat4.SetImagePan(0.000000, 0.000000)
    Pat4.SetImageZoom(2.593742)
    Pat4.SetParallelScale(47439.893394)
    Pat4.SetPerspective(1)
    Pat5 = View3DAttributes()
    Pat5.SetViewNormal(-0.442856, -0.784906, 0.433362)
    Pat5.SetFocus(0.000000, 0.029297, -0.032227)
    Pat5.SetViewUp(0.872186, -0.265128, 0.411094)
    Pat5.SetNearPlane(-94879.786788)
    Pat5.SetFarPlane(94879.786788)
    Pat5.SetImagePan(0.000000, 0.000000)
    Pat5.SetImageZoom(1.771561)
    Pat5.SetParallelScale(47439.893394)
    Pat5.SetPerspective(1)
    Pat6 = View3DAttributes()
    Pat6.SetViewNormal(-0.625152, -0.745658, -0.230604)
    Pat6.SetFocus(0.000000, 0.029297, -0.032227)
    Pat6.SetViewUp(-0.446916, 0.099757, 0.888996)
    Pat6.SetNearPlane(-94879.786788)
    Pat6.SetFarPlane(94879.786788)
    Pat6.SetImagePan(0.000000, 0.000000)
    Pat6.SetImageZoom(1.771561)
    Pat6.SetParallelScale(47439.893394)
    Pat6.SetPerspective(1)
    Pat7 = View3DAttributes()
    Pat7.SetViewNormal(-0.075503, 0.997141, 0.003088)
    Pat7.SetFocus(0.000000, 0.029297, -0.032227)
    Pat7.SetViewUp(-0.996869, -0.075555, 0.023296)
    Pat7.SetNearPlane(-94879.786788)
    Pat7.SetFarPlane(94879.786788)
    Pat7.SetImagePan(0.000000, 0.000000)
    Pat7.SetImageZoom(0.826446)
    Pat7.SetParallelScale(47439.893394)
    Pat7.SetPerspective(1)
    Pat8 = View3DAttributes()
    Pat8.SetViewNormal(-0.075503, 0.997141, 0.003088)
    Pat8.SetFocus(0.000000, 0.029297, -0.032227)
    Pat8.SetViewUp(-0.996869, -0.075555, 0.023296)
    Pat8.SetNearPlane(-94879.786788)
    Pat8.SetFarPlane(94879.786788)
    Pat8.SetImagePan(0.000000, 0.000000)
    Pat8.SetImageZoom(0.015091)
    Pat8.SetParallelScale(47439.893394)
    Pat8.SetPerspective(1)
    vpts = (Pat,Pat1,Pat2,Pat3,Pat4,Pat5,Pat6,Pat7,Pat8)
    x = []
    nsteps = 4200
    for i in range (9):
        x = x + [float(i) / float(8.)]


    for i in range (nsteps):
        t = float(i) / float(nsteps - 1)
        c = EvalCubicSpline(t,x,vpts)
        SetView3D(c)
        SaveWindow()
fly()

