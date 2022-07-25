def add_time(start, duration, dotw = False):

  days_of_the_week_dict = {"monday": 0, "tuesday": 1, "wednesday": 2, "thursday": 3, "friday": 4, "saturday": 5, "sunday": 6}
  days_of_the_week_list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"] 

  start_tuple = start.partition(":")
  start_hours = int(start_tuple[0])
  start_minutes_tuple = start_tuple[2].partition(" ")
  start_minutes = int(start_minutes_tuple[0])
  am_or_pm = start_minutes_tuple[2]
  am_and_pm_flip = {"AM": "PM", "PM": "AM"} # Purely for switching am/pm using key values
  duration_tuple = duration.partition(":")
  duration_hours = int(duration_tuple[0])
  duration_minutes = int(duration_tuple[2])
  amount_of_days = int(duration_hours / 24)
  end_minutes = start_minutes + duration_minutes
  
  if (end_minutes >= 60):
    start_hours += 1 
    end_minutes = end_minutes % 60
    
  am_and_pm_flipcount = int((start_hours + duration_hours) / 12)

  end_hours = (start_hours + duration_hours) % 12  
  
  end_minutes = end_minutes if end_minutes > 9 else "0" + str(end_minutes)
  
  end_hours = end_hours = 12 if end_hours == 0 else end_hours
  
  if (am_or_pm == "PM" and start_hours + (duration_hours % 12) >= 12):
    amount_of_days += 1
    
  am_or_pm = am_and_pm_flip[am_or_pm] if am_and_pm_flipcount % 2 == 1 else am_or_pm # Dict to output next am/pm if flips = 1
  
  end = str(end_hours) + ":" + str(end_minutes) + " " + am_or_pm

  if (dotw): 
    dotw = dotw.lower()
    index = int((days_of_the_week_dict[dotw]) + amount_of_days) % 7
    new_day = days_of_the_week_list[index]
    end += ", " + new_day
    
  if (amount_of_days == 1):
    return end + " " + "(next day)"
  elif (amount_of_days > 1):
    return end + " (" + str(amount_of_days) + " days later)"
    
  return end

# Lists start with 0
# Learnt an important lesson on how sequence matters in python