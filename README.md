# Temporal Mechanics

When things go awry with someone's car, they call their mechanic.  
When things go awry with the timeline, they call you!

---

## Acts
Each game's story is subdivided into three acts:
   1. __Setup:__
      The first act is set in the future.
      In this act the characters relive a catastrophic past event and prepare a warning about that event to send back to their former selves.
      The players first play through a [flashback scene](#flashback-scene) in which they describe what happened in the game's original timeline and how their characters were affected.
      The players then build a [story tree](#story-tree) describing the events that led up to the climax and that, if changed, could make it easier to alter the timeline for the better.
   2. __Confrontation:__
      The second act is set in the present.
      In this act, the characters receive the warning sent by their future selves and try to prevent the prophesied catastrophe.
      The players play through the [story scenes](#story-scenes) described in the story tree that they created in the previous act. Each story scene culminates with a [check](#checks) to determine its outcome.
   3. __Resolution:__
      The third act is again set in the future.
      In this act, the characters learn the consequences of their meddling with the timeline.
      The players play through a [flashforward scene](#flashforward-scene) in which they learn about how their actions will change the future.

---

## Story Scenes
During story scenes the characters revisit the events that, in the original timeline, led to the catastrophe described in the [flashback scene](#flashback-scene).
Each story scene is subdivided into three phases:
   1. __Investigate:__
      In this phase, the characters explore the scene.
      The players identify/assign [aspects](#aspects) to the people/places/things that their characters encounter during this phase.
   2. __Influence:__
      In this phase, the characters attempt to alter the timeline.
      The players make a [check](#checks) to determine the outcome of the scene.
   3. __Interpret:__
      In this phase, the characters find out what happened as a result of their actions.
      The players describe the narrative consequences of the outcome of the check made to determine the outcome of the scene.

To create a story scene, the players describe what their characters hope to accomplish during that scene.
This should be a proactive goal.
That is, it should describe something that the characters want to do rather than something that they hope to prevent from occurring.
This is particularly important when creating the climactic scene.
While it is easy to describe the characters' goal in the climactic scene to be to prevent the catastrophe described in the [flashback scene](#flashback-scene), it is better for the players to describe how the characters intend to do so.

## Flashback Scene
During the flashback scene the characters relive a catastrophic past event.
The players establish important details about the game's story including:
   - __The Antagonist:__
     The main foil for the player characters.
     At least three [aspects](#aspects) should be attached to the antagonist during the flashback scene.
     These aspects should be similar to [traits](#traits) in that they describe who the antagonist is, what they can do, and how they are connected to the events of the game's story.
   - __The Setting__:
     A description of the time(s) and place(s) in which the game's story will be set.
   - __The Catastrophe:__
     The fateful event that the characters will want to prevent when they try to alter the timeline.
     This is the event around which the rest of the game's story will revolve.
     The players should create a situation that their characters will be able to affect, but doing so will be both difficult and dangerous.

## Flashforward Scene
During the flashforward scene, the characters learn the consequences of their meddling with the timeline.
If the players succeeded at the check to determine the outcome of the climactic scene, then this should be a triumphant celebration of their success.
If they failed, however, then this is should be a somber reflection on the consequences of their failure.

---

## Story Tree
The players describe a sequence of significant events by creating a _story tree_.
A story tree is a collection of [story scenes](#story-scenes) that are arranged in a tree-like structure.
Every story tree has a special scene called the _climactic scene_.
All of the other scenes in the story tree are _upstream_ of the climactic scene.
That is, they occur earlier in the timeline of the game's story than does the climactic scene.

To create a story tree, the players should:
   1.  __Create the climactic scene:__
      This scene should be defined by the actions that the characters will take to try avert the catastrophe described in the [flashback scene](#flashback-scene).
      The difficulty rating of the climactic scene is always _d = 4_.
   2. __Create additional scenes__:
      To create additional scenes, the players should repeatedly:
      <ol type="a">
        <li>
           <b>Choose an existing story scene:</b>
           The existing scene can be any story scene with difficulty <i>d > 1</i>.
        </li>
        <li>
           <b>Create a new story scene:</b>
           The new scene will be <i>immediately upstream</i> of the existing scene.
           The difficulty rating of the new scene will be one less than that of the existing scene.
         </li>
      </ol>

<!-- #### Example
```mermaid
graph BT;
  n0("Destroy the Death Star (4)");
  n0 ---- n1("Engage the enemy fighters (3)");
  n0 ----- n2("Find a critical weakness (3)");
           n2 --- n4("Rescue Princess Leia (2)");
           n2 ---- n5("Deliver the schematics to the rebels (2)");
                   n5 ---- n7("Find Obi-Wan Kenobi (1)");
  n0 --- n3("Use The Force (3)");
         n3 ------- n6("Train to become a Jedi (2)");
``` -->

---

## Time Limits
Most groups should be able to play a complete game in no more than three hours.
The game's story should be tightly focused on the climactic scene and the scenes that led to that fateful event.
To encourage this kind of storytelling, the players should adhere to the following guiding principles:
 - __Short Scenes:__
   Each scene should be played out in no more than ten minutes of real time.
 - __Simple Structures:__
   Each [story tree](#story-tree) should consist of no more than eight [story scenes](#story-scenes) (including the climactic scene).

---

## Aspects
An _aspect_ is a word or short phrase that describes something noteworthy about a person, place, or thing in the game's story.
Aspects can be thought of as adjectives while the objects that they describe can be thought of as nouns.
Each aspect is _attached_ to a single object.
There are two kinds of aspects:
   1. __Character Aspects:__
      These are aspects that are attached to a player character.
      Five special character aspects are attached to each player character when they are created.
      These aspects are called [traits](#traits).
      Other character aspects are generally discovered/created during the investigate phase of [story scenes](#story-scenes).
   2. __Environment Aspects:__
      These are aspects that are attached to anything that is not a player character.
      Environment aspects are generally discovered/created during the investigate phase of [story scenes](#story-scenes).

### Matching Aspects
A pair of _matching aspects_ is a set of two [aspects](#aspects), one character aspect and one environment aspect, that together allow the characters manipulate a scene to their advantage.
Pairs of matching aspects are used to determine the size of the dice pool when making a [check](#checks).

#### Example
Suppose an NPC who needs to be prevented from catching a flight has the aspect "Argumentative".
In this case, "Argumentative" itself might be the best match that could appear in the characters' aspect list.
The NPC could be drawn into an argument with the PCs or even provoked into doing something that would get them kicked off of the flight.

If instead the NPC had the the aspect "Meek", then character aspects like "Aggressive", "Demanding", or even simply "Angry" might be appropriate matches.
The NPC could be simply intimidated by the PCs and coerced into doing what the PCs want them to do.

## Traits
Characters are described by a set of _traits_.
A trait is simply an [aspect](#aspects) that is assigned to a character.
Five traits are assigned to each character during character creation.
Each character should be assigned one trait from each of the following categories:
   - __Occupation:__
     An aspect that describes a character's profession, hobbies, or other interests.
     This aspect should be the character's answer to the question "What do you do?"
   - __Physical or Mental Characteristic:__
     An aspect that describes a character's body and/or mind.
     Are they a genius?
     Are they clumsy?
     Are they particularly strong?
     This aspect is a chance to capture that kind of detail.
   - __Psychological Characteristic:__
     An aspect that describes a character's personality.
     These characteristics could be beneficial or detrimental; the best are a little bit of both.
     This aspect should reveal something about how the character thinks about the world around them.
   - __Relationship:__
     An aspect that describes a character's connection with another character.
     The game's story should test the relationship between the two characters.
     This aspect speaks volumes about the character's personal history.
   - __Affiliation:__
     An aspect that describes a character's connection with an organisation.
     Such an organisation should be a prominent feature of the game's story.
     Affiliations tend to be much more transactional than relationships.
     This aspect implies both a set of benefits that the character enjoys and a set obligations that the character incurs as a result of their affiliation.

---

## Checks
A _check_ is used to determine the outcome of a scene.
To make a check, the players will:
   1. __Assemble a dice pool:__
      A dice pool is made up of one or more six-sided dice (d6s).
      One die is added to the dice pool for each pair of [matching aspects](#matching-aspects) that the players discover during the investigation phase of the scene.
      In addition, one _reward die_ is added to the dice pool for each scene immediately upstream of the current scene that was resolved successfully.
   2. __Roll the dice:__
      The dice in the dice pool are _exploding dice_.
      That is, for every die that yields a value of `6` one additional die is added to the dice pool and rolled.
      The values of all the rolls contribute to the result of the check.
   3. __Determine the result of the roll:__
      Any die that yields a value of `1`, `2`, or `3` is a _miss_.
      Any die that yields a value of `4`, `5`, or `6` is a _hit_.
      The result of a roll is the total number of hits.
   4. __Compare the result of the roll to the check's difficulty rating:__
      If the result of the players' roll exceeds or meets the check's difficulty, then they _succeed_ at the check and their characters accomplish their goal.
      Otherwise, the players _fail_ at the check and their characters do not accomplish their goal.

#### Example
   The players are making a check to determine the outcome of a scene that has a difficulty rating of _d = 3_.
   The players discovered three pairs of matching aspects during the investigate phase of scene and earned two reward dice in the scenes immediately upstream of the current scene.
   Therefore, the dice pool consists of five dice.
   When rolled, these dice yield the values {`3`, `6`, `5`, `1`, `6`}.
   Because two of the dice yielded a value of `6`, two additional dice are added to the pool.
   When rolled, these dice yield the values {`2`,`6`}.
   Because one of the dice yielded a value of `6`, one additional die is added to the pool.
   When rolled, this die yields the value {`4`}.
   In total, this roll yields the values {`3`, `6`, `5`, `1`, `6`, `2`, `6`, `4`}.
   The result of this roll would be five hits.
   The number of hits exceeds the difficulty rating so the players would succeed at the check.   

---

## Technobabble
Any good work of science fiction needs a modicum of technobabble to grease the narrative wheels a bit and facilitate the suspension of disbelief required by the genre.
   1. __Tachyonic Antitelephone:__
      Characters send messages from the future back to their past selves using a _Tachyonic Antitelephone_.
      A tachyonic antitelephone can only be used to send messages to a past version of itself.
      As such, no messages can be sent to a time before the first tachyonic antitelephone was created.
      These devices are rare, expensive, and incredibly energy hungry.
      Therefore, any messages sent by an tachyonic antitelephone are necessarily short.

   2. __Temporal Inertia:__
      The timeline is robust.
      Altering the course of history is difficult and fraught with peril.
      The more significant an event is the more difficult it is to affect and the more serious the consequences for failure.
      This property is known as _temporal inertia_.  

---

## Acknowledgements
Thanks to everyone who helped refine the design of Temporal Mechanics.
   - Dannielle Harden
   - Jo Stephenson
   - Scott Joblin
   - Sarah Hewat
   - Brett Witty
   - Farzana Choudhury
   - Keydan Bruce
   - Michael Cromer
   - Luke Purcell
   - Kira Purcell
