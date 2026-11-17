import random
import Monday
import Tuesday
import Wednesday
import Thursday
import Friday

score = 0
hours = 7
hours_Tuesday = 4
hours_Wednesday = 1.5
hours_Thursday = 6
hours_Friday = 4.5

def early_morning_options():
    """
    This function runs given the player wakes up before 6am and asks what they will do with their "extra" time in the morning.

    Input:
        yes/no: user input in response to two questions, str. 
    Output:
        print statements: Depending on the inputs, case-specific sentences are output to the player, str. 
        score: a certain number of points are added to the score given what tasks the player did, int. 
    """
    global score
    gym = input("Do you want to go to the gym? (yes/no)").lower()
    chore = input("Do you want to do any chores this morning? (yes/no)").lower()

    if gym == "yes":
            score += 2
            print(f"You said {gym} to going to the gym. That's a great way to start your day! Bonus points.")
    if chore == "yes":
            score += 1
            print(f"You said {chore} to doing a chore! You earned a point.")
    elif gym == "no" and chore == "no":
        print("You earned no points.")

def wakeup():
      """
      This function helps the player pick their wakeup time, which is the first points scoring opportunity of the game.
      The function also includes input validation where an exception is raised for ValueErrors that adds one
      to a counter that tracks invalid input. Numbers outside of the specified range also add one to that counter.
      The player has three chances to enter valid input and if that does not happen, a time is randomly assigned. 
       
      Inputs:
      wakeup_time: a user input time, float. 
       
      Output:
      score : int. 
      wakeup_time : see above, float. 

      Side Effect: modifies the global variable, score
      """
      global score
      invalid_wakeup_count = 0 
      try: 
            wakeup_time = float(input("Pick a wakeup time between 5-7 am (use decimals to represent minutes):"))
      except ValueError:
            print("Input is an invalid type!")
            invalid_wakeup_count += 1

      if wakeup_time <= 6 and wakeup_time >= 5:
            score += 1
            print("The early bird gets the worm! You earned a point.")
      elif wakeup_time <=7 and wakeup_time >= 6:
            print("Get ready for your day!")
      else:
            print("Not a valid time!")
            invalid_wakeup_count += 1
      while 1 <= invalid_wakeup_count < 3:
            try: 
                  wakeup_time = float(input("Pick a wakeup time between 5-7 am:"))
                  if 5 <= wakeup_time and wakeup_time <= 7:
                        if wakeup_time <= 6 and wakeup_time >= 5:
                              score += 1
                              print("The early bird gets the worm! You earned a point.")
                              break
                        elif wakeup_time <=7 and wakeup_time >= 6:
                              print("Get ready for your day!")
                              break 
                  else: 
                        print("Not a valid wakeup time!")
                        invalid_wakeup_count += 1
            except ValueError:
                  print("Input is an invalid type!")
                  invalid_wakeup_count += 1

      if invalid_wakeup_count == 3: 
            random_wakeup_time = [5, 5.25, 5.5, 5.75, 6, 6.25, 6.5, 6.75, 7]
            pick_random_wakeup_time = random.choice(random_wakeup_time)
            print(f"The time selected for you is: {pick_random_wakeup_time} ")
            if random_wakeup_time <= 6:
                 score += 1
      return wakeup_time, score

def Mon_lunch():
      """
      This function is to determine how long a player wants to spend eating lunch on Mondays 
      and calculate how much time is left after. There is also user validation in the form of both
      try/except blocks and conditionals. If invalid input is entered, a random time is assigned for
      the player. 

      Inputs:
        lunch_mins: how long a player spends eating lunch in minutes, int. 

      Output:
        hours = how many hours are left until the next activity (Moot), float. 

      Side Effect: modifies the global variable, hours. 
      """
      global hours
      try:
        lunch_mins = int(input("How long will you spend eating lunch in minutes?"))
      except ValueError:
           print("Input is invalid!")
           lunch_mins = random.randint(5, 60)
      if 0<= lunch_mins <= 5:
           score -= 1
           print("You lost a point because your lunch was too short!")
      elif lunch_mins < 0 or lunch_mins > 100:
           print("That's not a valid time! You will be randomly assigned an amount of time.")
           random_time = random.randint(6,60)
           lunch_mins = random_time
           print(f"Your lunch was {random_time} minutes long.")
      lunch_min_to_hrs = lunch_mins / 60
      hours -= lunch_min_to_hrs

def afternoon_activity(eat_lunch):
    """
    This function presents the player with options for Monday afternoon. The options are stored in
    a dictionary in a separate Python file that is called within the function. 

    Input: 
    decision: the player selects what they would like to do, str. 
    Output: 
    score: how many points the player has, int. 

    Side Effect: modifies global variables, score, hours. 
    """
    global score
    global hours
    if eat_lunch == True:
           Mon_lunch()
   

    options = Monday.Mon_afternoon_activity
    print("You will now get to pick your activities for the afternoon. "
       "Be careful as some gain you more points than others and all will eat up time!")
    
    for key, choice in options.items():
        print(f"{key}: {choice["activity"]}")
        
    decision = input("Which activity do you want to do? (please enter corresponding number)")
    choice = options[decision]
    hours -= choice["hours"]
    score += choice["score"]

    
    if hours >= 3:
        print("You have enough time to do something else!")
        afternoon_activity(False) #recursive use of a function
    elif hours >= 1:
        print("Start winding down for the day!")
        score += choice["score"]
    elif hours < 1:
          print("You ran out of time! Head to Moot practice.")
          score -= 1

def play_Monday():
    """
    This function plays through all the functions that make up a day and outputs a print message based on the score. 

    Side Effect: prints out an f-string that includes the scoer.
    """
    wakeup()
    early_morning_options()
    afternoon_activity(True)
    if score >= 7:
        print(f"Congratulations! You won. Your score was {score}.")
    else:
          print(f"You lost! Your score was {score}.")

def Tuesday_morning_activity():
    """
    The player gets to pick one activity to do on Tuesday mornings which can change their score. 
    The options are stored in a dictionary in a separate Python file that is called within the function. 
    
    Inputs:
    decision: choice of activity, str. 
    Output: 
    score: points earned or lost, int. 
    
    Side Effect: modifies the global variable score. 
    """
    global score
    options = Tuesday.Tue_morning_activity
    print("You will get one choice for what else you can do this morning!" \
    "Choose carefully as some options can gain points, some have no points, and some may make you lose points.")
    for key, choice in options.items():
          print(f"{key}: {choice["activity"]}")
    decision = input("Which activity do you want to do? (Please enter the corresponding number)")
    score += choice["score"]
      
def Tue_lunch():
      """
      This function is to determine how long a player wants to spend eating lunch on Tuesdays. 
      and calculate how much time is left after. There is also user validation in the form of both
      try/except blocks and conditionals. If invalid input is entered, a random time is assigned for
      the player. 

      Inputs:
        lunch_mins: how long a player spends eating lunch in minutes, int. 

      Output:
        hours_Tuesday : how many hours are left until the next activity (exercise class), float. 

      Side Effect: modifies global variable hours_Tuesday
      """
      global hours_Tuesday
      try:
       lunch_mins = int(input("How long will you spend eating lunch in minutes?"))
      except ValueError:
                 print("Input is invalid!")
                 lunch_mins = random.randint(5, 60)
      if 0<= lunch_mins <= 5:
                 score -= 1
                 print("You lost a point because your lunch was too short!")
      elif lunch_mins < 0 or lunch_mins > 100:
                 print("That's not a valid time! You will be randomly assigned an amount of time.")
                 random_time = random.randint(6,60)
                 lunch_mins = random_time
                 print(f"Your lunch was {random_time} minutes long.")
      lunch_min_to_hrs = lunch_mins / 60
      hours_Tuesday -= lunch_min_to_hrs

def Tuesday_afternoon_activity(eat_lunch):
    """
    This function presents the player with options for Tuesday afternoon. It has 2 global variables: 
    score and hours_Tuesday. The options are stored in a dictionary in a separate Python file that is 
    called within the function. 

    Input:
    decision: the player gets to pick what activity they'll do in the afternoon, str. 
    Output:
    score: the player's decision can add or subtract points to their score (or do nothing), int. 

    Side Effects: modifies global variable score, hours_Tuesday.
    """
    global score
    global hours_Tuesday
    if eat_lunch == True:
           Tue_lunch()
    options = Tuesday.Tue_afternoon_activity
    print("You will now get to pick your activities for the afternoon. "
       "Be careful as some gain you more points than others and all will eat up time!")
    
    for key, choice in options.items():
        print(f"{key}: {choice["activity"]}")
        
    decision = input("Which activity do you want to do? (please enter corresponding number)")
    choice = options[decision]
    hours_Tuesday -= choice["hours"]
    score += choice["score"]

    
    if hours_Tuesday >= 3:
        print("You have enough time to do something else!")
        Tuesday_afternoon_activity(False) #recursive use of a function
    elif hours_Tuesday >= 1:
        print("You can have a break!")
        score += choice["score"]
    elif hours_Tuesday < 1:
          print("You ran out of time! Head to your workout class.")
          score -= 1

def play_Tuesday():
    """
    This function plays through all the functions that make up a day and outputs a print message based on the score. 

    Side Effect: prints an f-string that includes the score.
    """
    wakeup()
    early_morning_options()
    Tuesday_morning_activity()
    Tuesday_afternoon_activity(True)
    if score >= 7:
        print(f"Congratulations! You won. Your score was {score}.")
    else:
        print(f"You lost! Your score was {score}.")

def Wed_lunch():
    """
    This function determines how long a player wants to spend eating lunch on Wednesdays
    and calculates how much time is left after. There is also user validation in the form of both
      try/except blocks and conditionals. If invalid input is entered, a random time is assigned for
      the player. 
    Inputs:
        lunch_mins: how long a player spends eating lunch in minutes, int. 
    Output:
        hours_Wednesday: how many hours are left until the next activity (class- Museum Studies), float.

    Side Effects: modifies the global variable hours_Wednesday
    """
    global hours_Wednesday
    try:
        lunch_mins = int(input("How long will you spend eating lunch in minutes?"))
    except ValueError:
        print("Input is invalid!")
        lunch_mins = random.randint(5, 60)
    if 0<= lunch_mins <= 5:
        score -= 1
        print("You lost a point because your lunch was too short!")
    elif lunch_mins < 0 or lunch_mins > 100:
               print("That's not a valid time! You will be randomly assigned an amount of time.")
               random_time = random.randint(6,60)
               lunch_mins = random_time
               print(f"Your lunch was {random_time} minutes long.")
    lunch_min_to_hrs = lunch_mins / 60
    hours_Wednesday -= lunch_min_to_hrs

def Wednesday_afternoon_activity(eat_lunch):
    """
    This function presents the player with options for Wednesday afternoon. It has 2 global variables: 
    score and hours_Tuesday. The options are stored in a dictionary in a separate Python file that is 
    called within the function. 
     
    Input:
         decision: the player gets to pick what activity they'll do in the afternoon, str. 
    Output:
         score: the player's decision can add or subtract points to their score (or do nothing), int.

    Side Effects: modifies global variables score, hours_Wednesday. 
    """
    global score
    global hours_Wednesday
    if eat_lunch == True:
        Wed_lunch()
    options = Wednesday.Wed_afternoon_activity
    print("You will now get to pick your activities for the afternoon. "
            "Be careful as some gain you more points than others and all will eat up time!")
         
    for key, choice in options.items():
        print(f"{key}: {choice["activity"]}")
             
    decision = input("Which activity do you want to do? (please enter corresponding number)")
    choice = options[decision]
    hours_Wednesday -= choice["hours"]
    score += choice["score"]
     
         
    if hours_Wednesday >= 1:
             print("You have enough time to do something else!")
             Wednesday_afternoon_activity(False) #recursive use of a function
    elif hours_Wednesday >= .25:
             print("You can have a break before class!")
             score += choice["score"]
    elif hours_Wednesday < 0.25:
               print("You ran out of time! Head to your workout class.")
               score -= 1

def play_Wednesday():
    """
    This function plays through all the functions that make up a day and outputs a print message based on the score. 

    Side Effects: prints an f-strong that includes the score.
    """
    wakeup()
    early_morning_options()
    Wednesday_afternoon_activity(True)
    if score >= 7:
        print(f"Congratulations! You won. Your score was {score}.")
    else:
          print(f"You lost! Your score was {score}.")

def Thursday_morning_activity():
    """
    The player gets to pick one activity to do on Thursday mornings which can change their score. 
    The options are stored in a dictionary in a separate Python file that is called within the function. 
    
    Inputs:
    decision: choice of activity, str. 
    Output: 
    score: points earned or lost, int. 

    Side Effects: modifies the global variable score. 
    """
    global score
    options = Thursday.Thu_morning_activity
    print("You will get one choice for what else you can do this morning!" \
    "Choose carefully as some options can gain points, some have no points, and some may make you lose points.")
    for key, choice in options.items():
          print(f"{key}: {choice["activity"]}")
    decision = input("Which activity do you want to do? (Please enter the corresponding number)")
    score += choice["score"]

def Thu_lunch():
      """
      This function is to determine how long a player wants to spend eating lunch on Thursdays. 
      and calculate how much time is left after. There is also user validation in the form of both
      try/except blocks and conditionals. If invalid input is entered, a random time is assigned for
      the player. 

      Inputs:
        lunch_mins: how long a player spends eating lunch in minutes, int. 

      Output:
        hours_Tuesday : how many hours are left until the next activity (exercise class), float.

      Side Effects: modifies the global variable hours_Thursday. 
      """
      global hours_Thursday
      try:
        lunch_mins = int(input("How long will you spend eating lunch in minutes?"))
      except ValueError:
            print("Input is invalid!")
            lunch_mins = random.randint(5, 60)
      if 0<= lunch_mins <= 5:
            score -= 1
            print("You lost a point because your lunch was too short!")
      elif lunch_mins < 0 or lunch_mins > 100:
            print("That's not a valid time! You will be randomly assigned an amount of time.")
            random_time = random.randint(6,60)
            lunch_mins = random_time
            print(f"Your lunch was {random_time} minutes long.")
      lunch_min_to_hrs = lunch_mins / 60
      hours_Thursday -= lunch_min_to_hrs

def Thursday_afternoon_activity(eat_lunch):
    """
    This function presents the player with options for Thursday afternoon. It has 2 global variables: 
    score and hours_Thursday. The options are stored in a dictionary in a separate Python file that 
    is called within the function. 

    Input:
    decision: the player gets to pick what activity they'll do in the afternoon, str. 
    Output:
    score: the player's decision can add or subtract points to their score (or do nothing), int.

    Side Effects: modifies the global variables score, hours_Thursday.  
    """
    global score
    global hours_Thursday
    if eat_lunch == True:
           Tue_lunch()
    options = Thursday.Thu_afternoon_activity
    print("You will now get to pick your activities for the afternoon. "
       "Be careful as some gain you more points than others and all will eat up time!")
    
    for key, choice in options.items():
        print(f"{key}: {choice["activity"]}")
        
    decision = input("Which activity do you want to do? (please enter corresponding number)")
    choice = options[decision]
    hours_Thursday -= choice["hours"]
    score += choice["score"]


    
    if hours_Thursday >= 3:
        print("You have enough time to do something else!")
        Thursday_afternoon_activity(False) #recursive use of a function
    elif hours_Tuesday >= 1:
        print("You can have a break before Moot!")
        score += choice["score"]
    elif hours_Thursday < 1:
          print("You ran out of time! Head to Moot.")
          score -= 1

def play_Thursday():
    """
    This function plays through all the functions that make up a day and outputs a print message based on the score. 

    Side Effects: prints at f-string that includes the score.
    """
    wakeup()
    early_morning_options()
    Thursday_morning_activity()
    Thursday_afternoon_activity(True)
    if score >= 7:
        print(f"Congratulations! You won. Your score was {score}.")
    else:
        print(f"You lost! Your score was {score}.")

def Fri_lunch():
      """
      This function is to determine how long a player wants to spend eating lunch on Fridays. 
      and calculate how much time is left after. There is also user validation in the form of both
      try/except blocks and conditionals. If invalid input is entered, a random time is assigned for
      the player. 

      Inputs:
        lunch_mins: how long a player spends eating lunch in minutes, int. 

      Output:
        hours_Friday = how many hours are left until the next activity (Moot), float.

      Side Effects: modifies the global variable hours_Fridat. 
      """
      global hours_Friday
      try:
        lunch_mins = int(input("How long will you spend eating lunch in minutes?"))
      except ValueError:
            print("Input is invalid!")
            lunch_mins = random.randint(5, 60)
      if 0<= lunch_mins <= 5:
            score -= 1
            print("You lost a point because your lunch was too short!")
      elif lunch_mins < 0 or lunch_mins > 100:
            print("That's not a valid time! You will be randomly assigned an amount of time.")
            random_time = random.randint(6,60)
            lunch_mins = random_time
            print(f"Your lunch was {random_time} minutes long.")
      lunch_min_to_hrs = lunch_mins / 60
      hours_Friday -= lunch_min_to_hrs

def Friday_afternoon_activity(eat_lunch):
    """
    This function presents the player with options for Friday afternoon. The options are stored in
    a dictionary in a separate Python file that is called within the function. 

    Input: 
    decision: the player selects what they would like to do, str. 
    Output: 
    score: how many points the player has, int. 

    Side Effects: modifies the global variables score, hours_Friday. 
    """
    global score
    global hours_Friday
    if eat_lunch == True:
           Fri_lunch()
   

    options = Friday.Fri_afternoon_activity
    print("You will now get to pick your activities for the afternoon. "
       "Be careful as some gain you more points than others and all will eat up time!")
    
    for key, choice in options.items():
        print(f"{key}: {choice["activity"]}")
        
    decision = input("Which activity do you want to do? (please enter corresponding number)")
    choice = options[decision]
    hours_Friday -= choice["hours"]
    score += choice["score"]

   
    
    if hours_Friday >= 2:
        print("You have enough time to do something else!")
        Friday_afternoon_activity(False) #recursive use of a function
    elif hours_Friday >= 1:
        print("Start your weekend!")
        score += choice["score"]

def play_Friday():
    """
    This function plays through all the functions that make up a day and outputs a print message based on the score. 

    Side Effects: prints an f-string that includes the score. 
    """
    wakeup()
    early_morning_options()
    Friday_afternoon_activity(True)
    if score >= 7:
          print(f"Congratulations! You won. Your score was {score}.")
    else:
          print(f"You lost! Your score was {score}.")

def game():
    """
    This function picks a random day that determines which schedule the player will play. 

    Side Effects: this function includes various print statements. 
    """
    days = ["Monday", "Tuesday", "Wednesday", "Thursday"]

    day_picked = random.choice(days)

    print(f"You will be playing {day_picked}!")
    print("To win you need to score 7 points by picking what to do with your limited free time.")

    if day_picked == "Monday":
        print("Today's schedule includes Python at 9 am, Quantitative Macroeconomics"
                          "at 10 am, Fed Challenge at 11 am, and Moot Court at 7 pm.")
        play_Monday()
    if day_picked == "Tuesday":
        print("Today's schedule includes a work meeting at 9:30 am, a workout class at 3 pm, a book club meeting" \
            "at 4 pm, and a work meeting at 5:15 pm.")
        play_Tuesday()
    if day_picked == "Wednesday":
        print("Today's schedule includes Python at 9 am, Quantitative Macroeconomics at 10 am, Fed Challenge at 11 am", 
                      "Museum Studies at 1:30pm, and TA Office Hours at 5:30pm")
        play_Wednesday()
    if day_picked == "Thursday":
        print("Today's schedule includes SPUD at 8:15 am and Moot Court at 6pm.") 
        play_Thursday()
    if day_picked == "Friday":
        print("Today's schedule includes Python at 9 am, Quantitative Macroeconomics at 10 am, and Fed Challenge at 11 am.")
        play_Friday()
 


if __name__ == "__main__":

    game()
