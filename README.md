# Temporal Mechanics

When things go awry with someone's car, they call their mechanic.  
When things go awry with the timeline, they call you!

## Structure
Each adventure takes place in two phases.

The first phase is set in the future.
In this phase the characters are preparing a message to send back to their former selves.
This message describes a series of events that occured during a job that they did many years ago.

The second phase is set in the present.
In this phase, the characters receive the message sent by their future selves.
Their job is to ensure that the events described in the message occur.

## Technobabble
Characters send messages from the future back to their past selves using a _Tachyonic Antitelephone_.
These devices are rare, expensive, and incredibly energy hungry.
A tachyonic antitelephone can only be used to send messages to a past version of itself.
As such, no messages can be sent to a time before the first tachyonic antitelephone was created.
Furthermore, any such messages are necessarily short.
Most systems limit messages to no more than 256 characters.

# Players
Temporal Mechanics is a game for three or more players.
All of the players have equal roles; there is no game master.

## Characters
There are two kinds of characters.
_Player Characters_ (PCs) are the heroes of the story.
Each PC is controlled by a single player throughout the game.
_Non-Player Characers_ (NPCs) are everybody else.
The NPCs can be controlled by any of the players as the need arises during the game.

## Game Play
There are two phases to each session.
The first phase is set in the future whilst the second phase is set in the present.
During the first phase the players will describe a sequence of events.
During the second phase, the players will guide their characters through that sequence of events.

#### Story Tree
The players describe a sequence of significant events by creating a _story tree_.

   - Story trees have a maximum depth of three.
   - Each encounter can have at most three child encounters.

#### Time Limits
Each encounter is played out in ten minutes of real time.

## Checks
A _check_ is used to determine the outcome of an encounter.
To make a check, the players will:
   1. Compute the check's difficulty rating.
   2. Assemble a dice pool.
   3. Roll the dice.
   4. Determine the result of their roll.
   5. Compare the result of their roll to the check's difficulty rating.

If the result of the players' roll exceeds or meets the check's difficulty, then they succeed at the check and their characters accomplish their goal.
Otherwise, the players fail at the check and their characters do not accomplish their goal.

#### Compute the Check's Difficulty Rating
Each check has an associated _difficulty rating_.
The difficulty rating of a check depends on the _challenge rating_ of the encounter and on the outcomes of earlier encounters.
In general, the challenge rating of an encounter with depth $d$ is $10 - 3d$.
That is:
   - Encounters with depth zero (i.e. the climactic encounter) have a challenge rating of 10.
   - Encounters with depth one have a challenge rating of 7.
   - Encounters with depth two have a challenge rating of 4.
   - Encounters with depth three have a challenge rating of 1.

The difficulty rating for a check also depends on the outcomes of earlier encounters.
In general, the difficulty rating for a check made to resolve an encounter with depth $d$ is decreased by $(3-d)$ for every child encounter that was resolved successfully.

##### Example
The climactic encounter always has depth zero.
Therefore, the difficulty of a check made to resolve the climactic encounter is reduced by three for each child encounter that was resolved successfully.
Suppose that two such child encounters were resolved successfully.
The difficulty rating will be decreased by three for each such child encounter.
Then the difficulty rating for the climactic encounter would be $10 - 2*3 = 4$.

##### Example
Consider an encounter with depth one.
Suppose that one of that encounters child encounters had been resolved successfully.
The difficulty rating for that encounter would be $7 - 2$ = 5.

#### Assemble a Dice Pool
A dice pool is made up of one or more ten-sided dice (d10s).
The number of dice in the dice pool depends on both the characters involved, those characters' actions, and the environment.

#### Aspect matching
Characters and environments both have aspects.
Character aspects are generally created before the encounter begins and describe who the characters are and what they can do.
Environment aspects are generally created during the encounter and describe the people, places, and things that the characters can interact with during that encounter.

At the end of the scene, make two lists.
One list consists of all of the character aspects.
The other list consists of the environment aspects.
Add one die to the dice pool for each aspect in the environment list that _matches_ an aspect in the character list.
Two aspects are considered a match if the characters could use the interplay between them to manipulate the encounter to their advantage.

##### Example
Suppose an NPC who needs to be prevented from catching a flight has the aspect "Argumentative".
In this case, "Argumentative" itself might be the best match that could appear in the characters' aspect list. The NPC could be drawn into an argument with the PCs or even provoked into doing something that would get them kicked off of the flight.

If instead the NPC had the the aspect "Meek", then character aspects like "Aggressive", "Demanding", or even "Angry" might be appropriate matches. The NPC could be simply intimidated by the PCs and coerced into doing what the PCs want them to do.

For a more lighthearted variant on this idea, consider the character aspects "Fumbling Fool" or "Smarter than They Look".
Either of these could be a match for an NPC's "Meek" aspect if the PCs could arrange for the foolish character to be one step ahead of the NPC as they try to make their way through the airport.
At every step, the foolish PC slows things down to the point that the NPC will miss their flight if they don't take some kind of assertive action.
Of course, the "Meek" NPC will be reluctant to do so.  

##### Commitment scheme (Taboo):
Each player secretly writes down an event that the characters controlled by other players could take that would affect the outcome of an encounter.
At the end of the encounter, these secret events are revealed.
One die is added to the dice pool for each secret event that occurred during the encounter.
Players are not allowed to explicitly say what events they wrote down. Instead these secret events should be implicit in the actions that they characters take during the encounter.

#### Roll the Dice
Not much to say here.  Roll dem bones!

#### Determine the Result of the Roll
The result of a roll is the largest value shown on the rolled dice.
Note that a standard d10 has faces numbered $0,1,\ldots,9$.
As such, the result of a roll is always less than 10.


#### Compare the Result to the Check's Difficulty Rating
