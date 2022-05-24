# Summary and observsations

I spent a bit of time writing down and organizing some design thoughts, and an hour or so creating a flow chart. Normally I never use flowcharts - I find them of very limited use and generally a waste of time. They're OK for simple presentations, but require a lot of work to make them even vaguely usable for coding. However,I wanted to experiment with <a href="https://mermaid-js.github.io/mermaid/#/">Mermaid markdown</a>. Did you know that this little feature is integrated into PyCharm? I didn't! See <b>Settings -> Editor -> Gutter Icons</b> and <b>Settings -> Languages & Frameworks -> Markdown</b>.

My coding starting point was to create the Bricks class. I quickly had a simple display of 5 rows of 10 bricks correctly positioned on the screen. I generalized the screen variables and positioning so that it could be easily resized should that become necessary (or desirable) in the future.

Next I created a simple Ball class, and quickly had that running, bouncing from the edges of the screen.

Then came the Paddle class. I had the idea of changing the ball angle, depending upon which part of the paddle it hit. The obvious solution was to create 5 square turtles and give each an identification that could be used later to modify the angle.

Having got all of those working, I could integrate them onto one screen. Success! A couple of `onkeypress()` bindings got the paddle moving.

I was going to use a numpy array, but since it can't store brick objects, I opted for a list (inside a dictionary) for the brick layout. Using the dictionary allowed me to easily create multiple levels. I had already decided that "special" bricks could be defined using integer values, and I soon had a simple test to display the bricks on screen. My first crude attempt at flashing bricks worked, but wasn't very satisfying, so I spent some time messing around with that to achieve a satisfactory result. The overall colour scheme will need quite some work, I think.

I created some code to generate a gradient background by changing the colour of a turtle as it traversed down the screen from top to bottom. It looked really nice, but because of the way the canvas updates turtle traces, it slowed the game to a crawl, so I eventually had to abort making live backgrounds. However, I could use the code to generate the backgrounds and save them as GIF files. This approach does not affect the game speed at all 😀 

I also removed the sleep timer. I find that it makes the game inherently slow. Now the game was super fast! The ball was just a series of dots as it raced around the screen. I introduced a simple `for` loop doing nothing so that I could tweak the overall game performance to my liking.

Next, I got the collision detection and bouncing angles right for the ball hitting the paddle. Then the collision detection for the bricks, and basic destruction of the bricks when hit.

At this stage the game was becoming "playable". But the Turtle `onkeypress()` is sadly lacking (well, it's the operating system really). There is a huge delay when holding down a key before it starts to repeat, and the paddle animation is far too slow because of the poor repeat rate. This makes the paddle almost unusable. After a bit of a search on the net, I came across a nice solution which I was able to modify to get the fast key repeat working in my Paddle class. The paddle now moved smoothly across the screen with no delay. It was starting to look and feel like a real game! 😁

Brick collision detection wasn't great. I decided to create a 3 segment brick so that the ball doesn't pass through any part of the brick. Although the previous implementation using only bounce in the Y direction looked passable in practice, having a left and right section also allows me to bounce in both the X and Y directions making it look more realistic.

Now I needed to get the scoring and messages working. An initial instruction page was easy, and I also implemented a Pause feature that works really well with a countdown when you unpause.

I was still unhappy with the way the ball bounced when two bricks side by side were hit simultaneously. Sorting this out was tricky and took me some hours of careful observation and debugging, but eventually I got there. Both bricks are removed and the score incremented. The ball will bounce in the Y direction instead of causing two separate X bounces.

The final major task was to get the special bricks to drop bonuses and penalties when destroyed! What fun! I extensively tested the code with 8 different brick types, and I am very happy with the way the code is working. There is still a lot of refactoring to do, as it's quite messy - but it's functional!!

The ball travelled noticeably faster towards the end of each level as there are fewer and fewer bricks remaining. The only really variable execution time was the turtle `screen.update()`. This varied from about 15ms with 80 odd bricks, down to about 5ms with only one brick to render. After quite some time measuring different parts of the game loop, and experimenting with different approaches, I eventually opted for simply adjusting the `for` loop delay depending purely on the number of bricks visible. This worked very well, and the game loop runs at a constant 15ms to 17ms on each level. Obviously it would be possible to reduce this time to make the game more difficult at higher levels.

In the end, I decided not to use the gradient backgrounds. I opted for a Space theme instead, so I downloaded a few free pictures from <a href="https://pixabay.com/">Pixabay</a> and edited them to fit the screen.

With all the testing done at each stage, I have sat here for literally hours, just watching the test screen play itself, as well as playing the game myself. It's quite hypnotic just watching, and to some extent frustrating to play! This has turned into a real playable game. It has worked out much better than I expected from a game written in pure Turtle Graphics, and I am really impressed by how responsive it is. I've surprised myself with how well it has all come together.

Do try it out and enjoy yourself... I think you will be as surprised as I am. All comments welcome.
