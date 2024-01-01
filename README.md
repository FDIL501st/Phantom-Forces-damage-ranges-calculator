# Phantom-Forces-damage-ranges-calculator
Python GUI that calculates hits to kill for Phantom Forces (Roblox) guns. Have to give information about damage and damage ranges into the system, can't just search the gun up.  

Our latest release is v1.3.0. 

When you provide incorrect input for damage information, the app will tell you what is expected of the values.
You can save the results in a .txt file wherever you want. It is good idea to make a folder to save all the results in.

## PF Jan.1, 2024 Update
The New Years Update in the game introduced a new mechanic of some guns having multi point damage ranges. 
What this mechanic is a gun can have multiple damage drop slopes at different ranges. <br>
This app does is not support that feature. The closest thing one can do is run the calculator assuming one one damage drop slope between a range, then ignore any hits to kill outsite that range.

## How to run
### Run PF_DamageRangesCalculator.py

Make sure you have all the python modules as in requirements.txt in the environment you are running, else the app won't run and instantly close.
Can run in terminal:

```pip install -r requirements.txt```

Just run PF_DamageRangesCalculator.py. In terminal, run:

```py PF_DamageRangesCalculator.py```


### Run PF_DamageRangesCalculator executable

You can find the executable within dist/PF_DamageRangesCalculator

