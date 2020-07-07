# #1- A Prisoners Escape (Part 1)

Given the potential increase in time between challenges, I've decided to up the difficulty (& hopefully interest) factor(s) even further.

This single challenge will consist of two sub-challenges:

 1. Implementing the original "Nearly Impossible Chessboard" puzzle solution
 2. Using this implementation to solve a steganography challenge.

Part one is an exceptionally interesting puzzle on it's own & will take a decent amount of time to solve. I promise that it is worth that eureka moment at the end.

While extremely rewarding to solve by hand, this puzzle is very hard. A brute-force method could be implemented (which would be awesome to see) but in the event that this first step proves prohibitively difficult, I will provide hints & then links to some Youtube videos explaining the solution & the steps taken to get there (on request via discord).

The "Nearly Impossible Chessboard" (NIC) puzzle goes as follows:
```
 You and another prisoner are to be executed, however a warden offers you a chance at freedom.

 You must enter a room with a chessboard, on each of the squares of which lays a coin and under each, a hidden compartment.

 The warden will place the key to your freedom in one of these hidden compartments, beneath a coin of his choosing in full view of yourself.

 You are then told to flip ONE coin, of your choosing & leave.

 The second prisoner enters, and based only on the state of the coins on the chessboard, they must correctly identify the correct compartment to win both your freedom.
```
Some rules:
 - You are allowed to discuss strategy beforehand, however the warden will listen & set up the initial state to minimize your chance of success
 - You MUST flip one and only one coin.
 - There's no hidden meta-game here, eg none of:
   - leaving the correct coin slightly to the side
   - leaving a hidden message
   - anything other than flipping a coin.
- You accomplice gets ONE chance and will follow your instructions perfectly, failure will result in the immediate execution of both of you.

TL;DR: You must perfectly encode the position of the key in the state of the chessboard with ONE coin flip from ANY initial state.

I would advise you start with a simpler case but be warned, this only works for certain sizes of board. 

The obvious simplest cases (1x1, 1x2 and 2x2) all work.

<details>
    <summary> This works for: </summary>
    Any board where the total number of spaces is a power of two. (This works for an 8x8 chessboard since 64 is the 6th power of two).
</details>

Extra challenge: prove the above "this works for: " statement. (doesn't have to be a formal proof)

This describes part 1 of this challenge, see [Part 2](https://github.com/NCEES-discord/Weekly-Challenges/blob/master/%231%20-%20A%20Prisoners%20Escape/Part2.md) for the steganography section
