# Summary and observsations

I spent a bit of time writing down some design thoughts, and an hour or so creating a flow chart (mainly because I wanted to experiment with mermaid markdown).

My starting point was to create the Bricks class. I quickly had a simple display of 5 rows of 10 bricks correctly positioned on the screen.

Next I created a simple Ball class, and quickly had that running, bouncing from the edges of the screen.

Then came the Paddle class. I had the idea of changing the ball angle, depending upon which part of the paddle it hit. The obvious solution was to create 5 square turtles and give each an identification that could be used later.

Having got all of those working, I could integrate them onto one screen. Success!

I was going to use a numpy array, but since it can't store brick objects, I opted for a list (inside a dictionary) for the brick layout. Using the dictionary allowed me to easily create multiple levels. I had already decided that "special" bricks could be defined using integer values, and I soon had a simple test to display the bricks on screen. My first crude attempt at flashing bricks worked, but wasn't very satisfying, so I spent some time messing around with that to achieve a satisfactory result. The overall colour scheme will need quite some work.

I created some code to give a gradient background by changing the colour of a turtle as it traversed down the screen from top to bottom. It looked really nice, but because of the way the canvas updates, it slowed the game to a crawl, so I eventually had to abort this approach. 

I also removed the sleep timer. I find that it makes the game inherently slow. Now the game was super fast! I introduced a simple for loop so that I can tweak the overall game performance to my liking.

Next, I got the collision detection and bouncing angles right for the ball hitting the paddle. Then the collision detection for the bricks, and basic destruction of the bricks when hit.

At this stage the game was becoming playable. But the Turtle onkeypress() is sadly lacking (well, it's the operating system really). There is a huge delay when holding down a key before it starts to repeat, and the animation is far too slow. This makes the paddle almost unusable. After a bit of a search on the net, I came across a nice solution which I was able to modify to get the fast key repeat working in my Paddle class. The paddle now moves smoothly across the screen with no delay. It's starting to look like a real game! 😁

Brick collision detection isn't great. I think I'll end up creating a 3 segment brick so that I don't pass through any part of the brick. Although the current implementation looks passable in practice, having a left and right section will also allow me to bounce in both the x and y directions.

Now I need to get the scoring and messages working. An initial instructions page would be good.

The final(?) major task is to get the special bricks to drop bonuses and bombs when destroyed! What fun!
