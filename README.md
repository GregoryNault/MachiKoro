Disclaimer: This is my text based version of the board game Machi Koro. I am new to coding and to python (started learning in September 2021).  This is my first attempt at creating something outside of YouTube tutorials.
I own no rights to this game, the sole purpose in creating it was for me to develop my programming skills with python.

# Machi Koro
You are the newly elected Mayor of the city Machi Koro. Develop your city by creating city developments, public works and collecting income from different cities. Grow your city and be the first one to complete all of your city's landmarks

Each mayor starts off their city with two development cards, a wheat field and a bakery, and one landmark card, town hall. The mayor uses the income collected from these developments to grow their city by adding new developments or to building city landmarks.



# Cards

Development cards are only activated by the players dice roll. Certain cards are activated on the players turn only, on anyone's turn, or on another player's turn.

|Roll   |Card Type    |Card Name          |Cost   |Activation                                                                       |
|:-----:|:-----------:|:------------------|:-----:|:--------------------------------------------------------------------------------|
|1      |Wheat        |Wheat Field        |1      |Get 1 coin from the bank, on anyone's turn.                                      |
|2      |Cattle       |Ranch              |1      |Get 1 coin from the bank, on anyone's turn.                                      |
|2-3    |Bread        |Bakery             |1      |Get 1 coin from the bank (your turn only).                                       |
|3      |Cup          |Cafe               |2      |Get 1 coin from the player who rolled the dice.                                  |
|4      |Bread        |Convenience Store  |2      |Get 3 coins from the bank (your turn only).                                      |
|5      |Industry     |Forest             |3      |Get 1 coin from the bank, on anyone's turn.                                      |
|6      |Establishment|Stadium            |6      |Get 2 coins from all players, your turn only.                                    |
|6      |Establishment|TV Station         |7      |Get 5 coins from any one player, on your turn only.                              |
|6      |Establishment|Business Center    |8      |Trade one non-establishment card with another player.                            |
|7      |Production   |Cheese Factory     |5      |Get 3 coins from the bank for each Cattle type card you own (your turn only).    |
|8      |Production   |Furniture Factory  |3      |Get 3 coins from the bank for each industry type card you own (your turn only).  |
|9      |Industry     |Mine               |6      |Get 5 coins from the bank on anyone's turn                                       |
|9-10   |Cup          |Family Restaurant  |3      |Get 2 coins from the player who rolled the dice.                                 |
|10     |Wheat        |Apple Orchard      |3      |Get 3 coins from the bank, on anyone's turn.                                     |
|11-12  |Market       |Farmer's Market    |2      |Get 2 coins from the bank for each Wheat type card you own (your turn only).     |



There are also five Landmark cards that are available for each city. These represent major attractions that each city would invest in as they grow. Each city begins the the Town Hall lanmark card already activated, the rest of the Landmark cards are activated when the Mayor pays the activation fee. Once activated the bonuses are always applied to that city on the players turn.


|Card Name        |Cost |Activation                                                                   |
|:----------------|:---:|:----------------------------------------------------------------------------|
|Town Hall        |0    |At the beginning of turn if player has 0 coins, collect 1 coin from the bank.|
|Train Station    |4    |You may roll 2 dice.                                                         |
|Shopping Mall    |10   |Your Cup and Bread type cards earn +1 coin when activated.                   |
|Amusement Park   |16   |If you roll doubles, take another turn after this one.                       |
|Radio Tower      |22   |Once per turn, you may reroll the dice                                       |



# Game Play

The player begins their turn by rolling one dice, or two dice if the train station is activated. Any cards with a matching activation number are activated and players collect income from the bank or from other players. If payment is owed to another player that payment is paid first, and then the collection of coins will happen. 

For example:

Another player owns a cafe and the current player rolls a 3: First the current player pays the other player 1 coin for the cafe, then the current player collects 1 coin from the bank for their bakery. If after all the activations are completed the current player still has no coins they can collect one coin from the bank from their town hall activation.

Now the current player is given several options through a numbered list:

1) Show Coins - this will display your coin total, your turn continues.
2) Show Cards - this will display all the cards in your deck, your turn continues.
3) Buy Development - you will be able to buy one of the cards that have been dealt out. 
4) Buy Landmark - you will be able to activate one of your city landmarks by paying its activation cost.
5) Show current deck - this will display the current dealt cards, your turn continues.
6) Pass - pass your turn.

# Winning the Game

Play end immediately when one of the players completes all of their city's five landmarks.


