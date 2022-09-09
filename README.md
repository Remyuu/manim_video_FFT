# manim_video_FFT
# Introduction
Sounds have frequencies.
Here are two notes playing together, 
```
1. Show a sound icon, broadcast the sound.
```
or if we try to draw down the vibration of the air, 
```
2. Show f.
```
a periodic function. That's what mathematicians call it. We can see it from the graph, it is repeated, or periodic.

I can tell you that it is formed by 2 sine or cosine function, just as they come from two pure notes.
```
sin()+sin()
```
But what exactly?
```
?sin(?x)+?sin(?x)
```
A musician may recognize imidiately. But not always. And just looking at the graph, it doesn't seem obvious.
How are we going to solve it? Fortunately, there's a method in mathematics called the **Fourier Transform**.
```
背景虚化，show 'Fourier Transform'
```
But before we look at how mathematicians deal with it, let's try to play with the wave ourself. 
```
clear the screen
```
We try to build the sound ourselves. We add 2 known sine or cosine functions, say, these two.
```
1. In C_coordinate, show sin(x) first, 
then add 2sin(4x). Show also the formulas, one by one.
```
![](video_script/2022-08-04-18-33-32.png)

Or maybe these two.
```
sin(x)+0.5sin(8x)
```
<!-- sin5x + sin8x -->
![](video_script/2022-08-04-18-33-32.png)

Paterms can be seen as the intensity of the second wave is smaller, that adding periodic functions together looks like a *wave in a wave*.
```
Plot the first component inside the final sum-up graph.
```
An advantage of this paterms may be that, after mixing up together, the frequency property are preserved somehow, and being combined. And the two components can be seen as interference of each other, but not that destructive.

What I would like to say is that the idea of Fourier transform may have used this paterm.
```
clear screen
```

# Fourier Transform
Now we come to the mathematics.
```
Show text 'Fourier Transform'
```
Here is the core formula for the **Fourier Transform**.
```
Show the formula
```
We first focus on the two terms inside.
```
Leaves only f(t)e^.., move to RIGHT.
Meanwhile, show the two coordinate system.
```
The f(t) is just our sound to be handled, where t is time. For a simpler explanation, we look at one note first, i.e. a single sine or cosine wave. ==↓==
```
circumscribe f(t)
f(t)->wave on cartessian coordinate
```
But also note that we would like to shift our function up a little bit, just a minor detail to make things simpler.
```
f(t) shift up by 1.
```
And then for the exponential terms,
```
circumscribe e^..
```
all we have to know is that it is a mathematical abbreviation of spinning vector w.r.t time.
```
Show the progress bar (t from 0 to 1)
Show a unit vector on the polar plane, with the tip [e^..t].
Change t, vector change accordingly,t in the e^..t change
```
Together with 2pi and k, it means that the vector swept 2 pi k radius within the give time. Here k is 0.4. So in 1 second, the vector swept accross 0.4 of a whole circle.
```
Show 2pi*0.4 with arc arround the polar plane.
```
Finally, multiplying f(t) with this just mean stretching and compressing this spining vector according to the magnitude of f at that time t.
```
Add the new trace.
Change t again, the vector show new trace.
```
Or it can also be interpreted as if we wound up the f(t) around on the plane as the trace of the vector, with the wounding frequency k = 0.4 of the whole circle.
```
wound up animation
```
==↑==
Now coming back to our Fourier formula.
```
Add the integral sign on f(t)e^.. to complete the formula.
```
This simply meams finding some *Center of Mass* of the wound-up graph.
```
circumscribe the whole formula, meanwhile, show the CoM.
```
So as we change our winding frequency, i.e. for different k, we may get different CoM.
```
Change k animation, slowly
```
We may record and draw the distance of CoM from the y axis.
```
Show, draw frequency domain graph.
```
Note here that we may say the different frequency of winding, corresponds to stretching the sound f(t). This can be seen both from our eyes or from the formula.
```
stretching f(t), add to channel
```

It looks like the CoM is always at the origin as the graph behind has some kind of symmetry.
But the important thing is that, when we wound the graph in a frequency that is just the true frequency of the original wave, the CoM will be far away from y axis.
```
k have moved to the peak value now.
```

The reason behind might be that at this winding frequency, every period of f are just wound in one full circle, so we can gather all the peaks of f(t) on the right of the graph. Therefore by tracing the positon of CoM, we get feedback on whether the current k is similar to the true frequency of f. We are able to reveal the unknown frequencies of f(t) by looking at the position of CoM, with this mathematical wounding machine.

What about a more complex f(t), like what we look at earier, the sum of two waves mixing together?
```
When the mass are all on the right(k=5 unchanged)，
the graph change to the case that we add the other sine wave.
polar graph and cartesian graph should both change
```

Here we stopped and keep the winding frequency at k=5, and we changed the f to sin(5x)+0.5sin(8x). And we have continued exactly the same process earlier.

```
replay the changing process
```

We see that the machine still work somehow. The position of the CoM is far away from the origin, still indicating the existence of frequency 5 in the sound.


The reason might be what we've discussed earlier. The second wave can be seen as an interference on the first wave. 
```
replay the changing process
```
It is also seen on the wound-up graph, the new graph is not completely different. It looks like some adjustment base on the old graph.
```
replay the changing process
```
So the frequency property are not destroyed when mixing the two waves. Our machine is still working.

Finally, let's change the winding frequency for the new graph and complete our new frequency domain.
```
do not remove the last freq_domain
draw new frequency domain to show comparison
k change from 5 to 0
k change from 0 to 10
```

# Let's see what we did on a true music!
```
Show the true application result animation
```

