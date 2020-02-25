# Extensions

This folder contains the extensions made.

### How to use it?

These are the explanations and examples for each different class.

* **Text**

The text class can be used to place text inside a scene with ease. 

For the initialisation of the text class it'll need three arguments: `tColor`, `fontSize` &
`properties`. For the `tColor` you'll need to set an color from the `Color` class or a tuple with
RGB values, for the `fontSize` it'll need an int & for the 'properties' it'll need a list with the
width and height.

***Example***

> `self.UIText = text((0, 0, 0), 24, [100, 30])`

Once this is initialised, you'll need to set the position of the text. This is done like this.

> `self.UIText.position = [100, 100]`

The text class has template text, to change the string you'll need to adjust the text variable.

> `self.UIText.text = 'Start'`

There's also the option to change the font. This can be done by the `setFont` method. It'll need
only one argument: `path`. The `path` is a string that contains the path where the font is located.

> `self.UIText.setFont('scenes/assets/fonts/KulimPark-Regular.ttf')`

Once these steps are all initialised run the method `draw`. The `draw` method needs one argument:
`win`. The `win` argument will need an pygame window.

> `self.UIText.draw(window)`

* **Slider**

The slider class can be used to adjust a value via a slider. 

For the initialisation of the slider class it'll need two arguments: `colors` & `properties`. For
the `colors` you'll need a list of two RGB tuples (one for the indicator & one for the slider), for
the `properties` it'll need a list with the width and the height.

***Example***

> `self.UISlider = slider([(0, 0, 0), (200, 200, 200)], [150, 10])`

Once this is initialised, you'll need to set the position of the slider. This is done like this.

***Example***

> `self.UISlider.position = [200, 150]`

There are some optional method for slider usage. The `getPercentage` & the `setPercentage`. The
`getPercentage` returns the sliders current value & the `setPercentage` sets the value & position of
the indicator. it'll just need an integer of the new percentage.

> `self.UISlider.getPercentage()`
> `self.UISlider.setPercentage(newPercentage)`

* **Button**

The button class can be used to create a button is a simple way.

For the initialisation of the button class it'll need two arguments: `colors` & `properties`. For
the `colors` you'll need a list of two RGB tuples (one for the button & one for the text) & for the
`properties` it'll need a list with the width and height.

***Example***

> `self.UIButton = button([(0, 0, 0), (255, 255, 255)], [150, 50])`

Once this is initialised, you'll need to set the position of the button. This is done like this.

***Example***

> `self.UIButton.position = [50, 50]`

After this you'll want to set the string inside the button. This is done like this.

***Example***

> `self.UIButton.text = 'Start'`

For checking the state of button, you'll need to use the `getClick()` method. You'll want to use
this inside the draw method.

***Example***

> `self.UIButton.getClick()`

After the initialisation of the steps above, you'll need to run the `draw` method. This method needs
one argument: `win`. The win argument needs a pygame window as value.

***Example***

> `self.UIButton.draw(window)`

* **Image**

The image class is used to load an image. The image class is necessary for the `Actor` class. 

For the initialisation of the image class it'll need two arguments: `fileName` & `properties`.
For the `fileName` you'll need to set the name of the sprite. The fixed path is located in
`scenes/assets/sprites`. So all it needs to have is the file name & for the `properties` it'll need
a list with the width and the height.

***Example***

> `self.UIImage = image('nameOfSprite.png', [64, 64])`

Once this is initialised there's the option to set the position, angle & the scale. The reason they
are optional is mainly because the same functionalities are located in the `Actor` class. 

> `self.UIImage.setAngle(90)` & `self.UIImage.getAngle()`
> `self.UIImage.setScale2X()` & `self.UIImage.setScale(3)`

Once this is done you'll need to run the `draw` method. This will only be necessary if it'll not be
used as an actor.

> `self.UIImage.draw(window)`

Next to all of this there's the option to request the width and the height.

> `self.UIImage.getWidth()`
> `self.UIImage.getHeight()`

* **Actor**

The actor class is used to create a sprite or animation. This class is best used with an inherited
class.

For the initialisation of the actor class it'll need two arguments: `image` & `hasAnim`. The `image`
argument ca be used with two different types. Type 1: an instance of the image class, Type 2: a
string with the path to the folder with frames (There's a fixed path: 'scenes/assets/animations/') & for the `hasAnim` argument its a boolean with
`True` sets animation on true & `False` will set the animation to true.

***Example***

> `self.player = actor('Pac-Man', True)`

Once the `actor` class is initialised you'll want to set the position. This is done like this.

***Example***

> `self.player.setPosition([150, 400])`

Now if the actor is initialised as an animation, you'll need to initialise the animation. This
method takes one argument: `dependency`. The `dependency` argument has two types: `'time'` &
`'frame'`, these two arguments set the animation type. This is done like this:

***Example***

> `self.player.setAnimation('time')`

Once this is all done, you can move the actor around with the setVelocity method. The method takes a
list as argument with the `x` & `y` values.

***Example***

> `self.player.setVelocity([1, 0])`

There's also the option to set and get the angle. This is done like this.

***Example***

> `self.player.setAngle(90)`
> `self.player.getAngle()`

There's also the option to request the position of the actor.

***Example***

> `self.player.getPosition()`

After all these steps (or some of them), you'll need to run the `_draw` method.

***Example***

> `self.player._draw(window)`

* **scenes**

The scenes class is used to switch between scenes. 

For the initialisation of the scenes class, it'll two arguments: `scene` & `win`. For the `scene`
argument it'll need an instance of the class, you'll want to draw & for the `win` argument it'll
need the pygame window.

***Example***

self.scene = scenes(scene(), window)

Once this is initialised you'll need to update the scene when the scene needs to be switched. The
`update` method is used with two arguments: `clock`, this arguments needs a pygame time clock &
`fps` is an int in which frames per second the games is gonna run. This is done like this.

***Example***

> `self.scene.update(clock, fps)`

* **Color**

This class contains pre initialised colors.

For the initialisation there's no argument involved.

> `self.color = color()`

There's also the option to create a custom color using hexcodes. This is done like this.

> `self.color.custom('#738291')`

Here's a list of pre initialised colors:

* black
* white
* red
* green
* blue
* yellow
* violet
* orange
* pink
* brown
* cyan
* gray

* **Collision** 

The collision class contains simple ways to set collision, square collision and circle collision
inside an actor inherited class. 

For the initialisation of the collision class it'll need two arguments: `actor` & `colType`. For the
`actor` you'll need to set the current actor and for the `colType` it needs to be string type with
`'square'` or `'circle'` as type. If this is not the case it'll raise an error.

***Example***

> `self.collision = collision(self, 'circle')`

Once this is initialised, you'll need to set the collision. The reason behind this method is fairly
simple, this way the collision could be turned off & on on command.

***Example***

> `self.collision.setCollision(True)`

When the collision is set to `True`, the way to check for the collision state is done by one method,
no matter which type.

***Example***

> `self.collision.checkState()`

***Disclaimer:** This method returns `True` or `False`. This means when there's a detection nothing will happen.
This 100% up to the developer.*

There's also the option to request the active positions of each collision. It'll only need one
argument: `colType`. This argument is exactly the same as with the constructor.

> `self.collision.getActiveCols('circle')`
