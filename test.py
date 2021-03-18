#!/usr/bin/env python3
import os
import sys
VTK_BUILD_DIR = os.path.join(os.getcwd(), 'build')
sys.path.append(os.path.join(VTK_BUILD_DIR, 'lib', 'python3.9', 'site-packages'))
import vtk

# Text Mapper
mapper = vtk.vtkTextMapper()
mapper.SetInput("Testing...")

# 2D Actor
actor = vtk.vtkActor2D()
actor.SetMapper(mapper)

# Create a rendering window and renderer.
ren = vtk.vtkRenderer()
ren.AddActor(actor)

# Window
renWin = vtk.vtkRenderWindow()
renWin.SetSize(1000, 1000)
renWin.AddRenderer(ren)
#renWin.Update()
print(renWin)
#renWin.Render()

window_filter = vtk.vtkWindowToImageFilter()
window_filter.SetInput(renWin)
window_filter.Update()

# Write it
writer = vtk.vtkPNGWriter()
writer.SetFileName('test.png')
writer.SetInputData(window_filter.GetOutput())
writer.Write()
