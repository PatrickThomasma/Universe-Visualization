# An Analysis of Dark Matter clouds using VisIt Toolkit

This is a README for my CIS410 final project in where I used the VisIT toolkit to visualize a dataset representing dark matter clouds and particle density change in the universe.

[Details](#Details)

[Installation](#Installation)

[Making a movie](#Making-a-movie)

[Velocity Particle fly through](#Velocity-Particle-fly-through)

[Vector Zoom in](#Vector-Zoom-in)

[Volume Rendering](Volume-Rendering)

[Acceleration](#FullTimeScale-of-acceleration)

[Final Thoughts](#Final-Thoughts)

[Sources](#Sources)

[Authors](#Authors)

The final video can be viewed here [Movie](https://www.youtube.com/watch?v=1PQ-9w8j_hk)

# Details
This is my visualization based off of data tracking local particle density that is used to help identify where dark matter halos are located. Initially I had wanted to do a project on visualizing data from a Supernova, after failing to find any data that I could reliably use with VisIt I was recommended to use one of the datasets provided in class but I had really wanted to do something related to Space and I found a dataset that was close to what I wanted. The IEEE SciVis 2015 contest was about Dark matter clouds and I thought that would be perfect for me, all the data however was in this file format called SDF which visIt couldn't recognize but with help from Hank Childs I was able to extrapolate the data from the SDF files and build them into VTK object files to use with VisIt. I have provided the scripts I used to extrapolate the data points from those files and also provided a script that would create 300 additional data files based on the initial 100. This README also includes images that I couldn't make it into the final movie and also work in progress images, also included is a link to the movie. In the repo I included scripts that I used to create the animation of my datapoints, I also included a few of my notes that I did on notepad which was helpful when I had to animate and had to figure out how to interpolate between camera values. I also included links showing where I got this data from and any outside material I used to help me create this movie.

## Installation

I installed the VisIt toolkit from the visit-dav.github and used version 3.1.2 for my visualization project, I know some people had problems working with visit on windows but I think that if anyone has an Linux WSL on their windows then they will be able to run scripts through visit using that.

## Making a movie

After I had the toolkit installed and converted the SDF files into VTK I was ready to make a movie, before making the movie I had a vision in my head of what I wanted to achieve. Things I noticed about past students projects was that albeit impressive I had found them a bit dry since they had only expressed scientific data. I've always had a bit of an artist itch so for my project I wanted to add music to it and try to frame some shots as if I were trying to make a movie that would've come out in theaters. Trying to balance my desire for an exciting movie and also trying to accurately represent the data best I could was tough at times since at several points I had to give up one or the other since in the end it would be a better movie showcasing my skills as a computer scientist. I am still really happy with the final movie and I believe that I blended the two different sides of me making this movie very well.

In order to  make the movie I had to animate every frame that I wanted to use in the final product, some clips such as the Velocity Particle fly through produced 4900 tiff images that I compiled into a minute clip at 60fps, I used tiff since it's lossless and I aimed for the highest quality possible for my movie. After I compiled the four clips I wanted to use I used lightworks pro to edit the clips together and I used the editor to include music fade in/out and titles to the clips that I had made. The movie ended up being 3 minutes and I would say it took around 6-7 hours 
### Velocity Particle fly through
Making this clip was probably my favorite part of the movie making experience. For this clip I had the goal of wanting to show the beauty of space and I thought ending the movie here would leave a lasting impression for the people watching it. In order to create it I used a pseudocolor plot over the velocity_magnitude of the data and spent around maybe 4-5 hours trying to pick the perfect size/shape for the particles and then after I wanted to pick the best most aesthetically pleasing color to show off. I used the last time slice of my data point since that was the most expanded piece and I feel like I was able to show off more about the expensiveness of the universe in that way. After I found the perfect aesthetic I wanted for the image I scripted about 8 different camera points that I wanted to fly through/show off and I each camera position to about 4200 tif image files. The reason I picked tif was because its nearly lossless in compression and the professor Hank Childs had mentioned that he didn't want project that were too artifacted so I wanted to make sure that the images I was saving were the highest quality I could possibly make them. This part definitely had the most images saved and the single clip that these images saved into were around 6 gb

### Vector Zoom in 
The zooming in to the vector was an area of the project that I wish I could've done more but I am happy with how it ended up, the current product I believe accurately represents the gravitational velocity that is pulling particles into dark matter clouds, what I would like to have improved on in this section given the time is to remove a lot of the background vectors so highlight the cosmic web that is built from these particles being pulled in together and to smooth out a lot of the vector lines so they look more connected then all being apart. In the data I had gathered there were halo catalogs and after doing some research I believe they had the data I needed to create the image I wanted but after some time spent trying to also extrapolate the data from those I decided that there were too many outdated libraries and a lack of explanation of how to get that data compared to my other one that I decided I should move on with the rest of the project and just be happy with what I had managed to make!

 
 

### Volume Rendering
In this clip I thought it would be really nice to take a certain slice of the time slices and rotate around the model showing the changes in volume that is happening over time. I am actually really happy with what I did in this clip and I spent a lot of time messing with the bins and colors in this model to try and make it look aesthetically pleasing while still giving a visualization of the density of these dark matter clouds. I built the model using a the volume databinning 3D mesh plot and using a dual mesh operator to really make the image come together. One thing I wish I could've added to this part was raycasting, my professor had tried to make it work with my visualization but for some reason the computing engine would stall at 0% while eating up a insane amount of my memory. After playing with some settings on visit I did eventually get a image that was raycasted to show up and I left a picture of it under above this section, this image is screencapped because trying to export it as a image would fail everytime let alone make a movie with 1800 frames each of them being raycaster at different positions. I was tempted to use the talapas supercomputer at UO, but in the interest of time I decided against it. If in the future I were given the tools and a deeper understanding of how to enable visit to allocate more computing power I would love to update this clip and make it even more beautiful but as it is now I am happy with it.



### FullTimeScale of acceleration
This clip probably took me the most time to make and by far the hardest one to achieve. Going into it I had thought that it wouldn't be too difficult and my first version that I made it actually wasn't that difficult, the idea was to get a good camera position of the model in an early time slice then a good position at the last time slice and interpolate the camera in between so it would look like the model was taking up the full screen and trick the audience into thinking that my model wasn't just a square with particles inside but that it was an expansive model with unlimited particles. My first version was competent but since I only was working with 100 data points making a 10 second video in was only possible with 10 frames per second which looked a bit too choppy to me and 30 frames would be 3.5 seconds and 60 frames would be 1.5 seconds which were both too short for me to include it in my final film. To remedy this I decided to make 300 mock datasets based on the initial 100 datasets by doing temporal interpolation between the 10 datapoints in each dataset. Doing this I now had 400 datasets that would hopefully make a smoother video at 30fps for 13 seconds or at 60fps for 6 seconds. I had thought about doing 800 datasets so I could make a smooth 60 fps video that was 13 seconds long but the amount of stoage that would've used was too much and when I made started to make the images, 400 was almost too much as visit had to use alot of memory to make a movie on all 400 timeslices and it was 50/50 whether my animation script would crash because visit had used up all of my 32 gigs of memory. Whlie I was succesful in making the 400 datapoints a huge roadblock that I had hit for two days was that the camera would outpace the expansion of the image and the movie would look awkward as the model would go from taking up the whole video to suddenly becoming a very small block to quickly becoming too big. To fix this I decided instead of only having two camera points I would instead have 20 camera points and each camera point was what I thought to be the perfect spot every 20 timesslices and I would interpolate in between each camera point since some points were further than others (the zoom for timeslice 18 was at 40 while timeslice 38 was at 18) and much closer (the zoom 378 and 398 only had a .4 difference). Doing this I was successful in keeping the camera to be in pace with the model but the other major roadblock was that the camera was extremely bumpy and even using editing tools like lightworks,videopad, and Adobe premier pro couldn't stabilize the movie. 

Repeatedly I had to go back to my temporal interpolation and my scripts and try and see what I possibly missed, add a fix that I thought would work then run my script again then copy over the VTK data into visit's data folder then play my camera animation then compile the images into a movie. This whole process would take about an hour and I would say I probably had to do it 10 times or more since I would watch the movie and see that it wasn't right and the only way to fix it was to do the whole process again. Unfortunately despite trying so hard to make it work I eventually hit one final roadblock that made me consider that maybe what I was doing wasn't possible. The image I included here was the final result of me interloping the datasets and as you can see the model here looks very different than what I included in the final movie. I looked really hard into figuring out why these models had seemed to be split into several different boxes but after a few hours of looking for help and seeing if there was anything wrong with my conversion I realized that my conversion wasn't the problem. This is a large dataset and the data that I've chosen to represent from is not the full representation of the data, There were also halo catalogs and merger trees. The merger trees I soon discovered were key for doing what I wanted to do. Unfortunately I realized that temporal interpolation wasn't going to fulfill what I wanted to do because this data is complex and in order to create more data I would've had to learn about Data prediction. Unfortunately I only realized this the day before my presentation but after some light research data prediction seems to be a very detailed topic in computer science and I don't believe it would've been doable to achieve in only two weeks. At the end I ended up going back to my first version, my video did benefit from this back and forth though and for my final product I implemented 20 camera spaces that interpolated with the model and it does look like there is no bound when the clip plays.


## Final Thoughts 

 This was definitely one of my favorite projects to work on since I got to use my creativity in making a good movie and since I was the only one doing this dataset and as far as I know maybe the only student who took this course that did this dataset it really felt like I was doing an independent project and taught me a lot of what it would be like doing a project for a job would feel like since it was something I was building entirely on my own and it forced me to use a lot of the knowledge I've gained from taking computer science and applying it here. Trying to make a more cinematic visualization was also pretty nerve wrecking since all the sources I found online about data visualization was very similar in that they were purely a visualization movie and I felt nervous about doing something different than that as I wasn't sure if it was some industry standard to make movies like that, thankfully my professor Hank Childs gave me the go ahead in trying to make a more cinematic movie so I pushed forward in making that and im really glad that I did.

I am overall very happy with what I made and I hope that whoever watches it will be inspired to maybe make a more cinematic visualization of their own, I put a lot of work into this project and despite some shortcomings in the movie such as the lack of raycasting on the volume data, lack of a clearer picture for vectors, and the shakiness of the time-lapse clip I feel like I never wasted time and every second that I worked on this movie I was really happy that I was building something that I thought would be visually beautiful and have a lot of energy coming out from it. My hope is that maybe one day all visualization movies will have more of a dramatic flair to it and I am hoping this inclusion will get more people interested in the field seeing that they don't have to restrict their artistic vision purely because they are more focused on visualizing accurate data.

## Sources

[Data set used](https://darksky.slac.stanford.edu/scivis2015/data/)

[Inspiration for this project](https://www.youtube.com/watch?v=1p8ADoTqggY)

## Authors

Creator and editor: Patrick Thomasma
Contributors: Hank Childs, Tammas Hicks (Helped a ton with smoothing out my timelapse clip) and Melissa Milbrandt (Helped me with some of the more monotonous tasks such as the conversion script and gave me moral support through the whole project)


