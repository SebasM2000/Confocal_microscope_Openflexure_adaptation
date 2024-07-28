<h1 align="center"> Confocal Microscope: an adaptation of the V7 Openflexure's Microscope </h1>

<p>
  <img src="https://img.shields.io/github/languages/top/SebasM2000/Confocal_microscope_Openflexure_adaptation?style=flat&logo=python&color=green&logoColor=yellow&link=https%3A%2F%2Fwww.python.org" alt="GitHub top language">
  <img src="https://img.shields.io/github/license/SebasM2000/Confocal_microscope_Openflexure_adaptation?label=License&labelColor=gray&color=yellow" alt="GitHub License" >
  <img src="https://img.shields.io/badge/Status-In%20Development-blue" alt="Status: In Development">
</p>

<p> This document is also available in [Spanish](README_es.md). </p>

<p> In this project, version 7 of the Openflexure high-resolution microscope was adapted to a confocal microscope, which is controlled from an interface developed in Python. This microscope has the ability to form two-dimensional and volumetric images, thanks to the fact that the code performs image processing that stores them in a folder specified by the user. This project was carried out as an undergraduate thesis in Physics at the Interdisciplinary Institute of Sciences (IIC) of the University of Quindío, so all the documentation and the thesis itself (in Spanish) are provided in this repository. </p>

<h2> Project description </h2>
<p> The focus of this project is to create a user interface for the Acousto-Optics and Radiometry Laboratory of the Interdisciplinary Institute of Sciences, which is part of the University of Quindío (Colombia). Therefore, although the main README is in English, all documents in this repository, as well as the entries, text and labels of the interface, are in Spanish. It is not ruled out to add other languages ​​for better accessibility at a global level, however, users who clone this repository are invited to adapt it to their native language! :D. </p>

<h2> Characteristics </h2>
<p> Although the Openflexure microscope was used as a reference, this microscope works in a completely different way. The most significant changes are listed below: </p>

<ul>
  <li> Automatic image measurement. </li>
  <li> Creation of 2D and 3D images. </li>
  <li> Uses a laser as a point source of illumination. </li>
  <li> Uses reflection mode for imaging. </li>
  <li> The microscope structure has been completely inverted. </li>
  <li> An additional lens and two pinholes have been added to the assembly. </li>
  <li> It is controlled from a different interface, developed in Python. </li>
</ul>

<h2> Used technology </h2>
<p> The project code is mainly built in Python and a small part in C language for the control of the components connected to the Arduino. The Python libraries and their corresponding version used are described below: </p>

<ul>
  <li> Numpy 1.23.2 </li>
  <li> Tkinter 1.3.3 </li>
  <li> OpenCV 4.6.0.66 </li>
  <li> Pyserial 3.5 </li>
</ul>

<h2> Functionalities </h2>
<p> This section explains in detail the features of the user interface and image processing. Considering the current state of the project, this section will be updated as features are added, modified or removed. </p>

<h3> Interface window </h3>
<p> The user interface consists of two windows: the welcome window, in which the user enters his basic data; the control window, whose function is to control the laser status, the position of the motors and the measurement of the microscope to produce images. Therefore, in this subsection each window will be shown together with several marks where its function will be explained. </p>

<h4> Welcome window </h4>
<h4> Control window </h4>
<p> More detailed description when code optimization is done. </p>