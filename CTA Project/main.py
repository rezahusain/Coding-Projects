# Hi, my name is Reza Husain. This is a project where I 
# coded a CTA database through Python and SQL. The commands retrieve 
# stats of the CTA train system by querying using SQL. The value this
# program brings to our current society is the access to quick information
# for anyone needing data related to the CTA in a very short amount of time.
import sqlite3
import matplotlib.pyplot as plt
import matplotlib as mpl
#mpl.use('Agg')
import datetime


##################################################################  
#
# print_stats
#
# Given a connection to the CTA database, executes various
# SQL queries to retrieve and output basic stats.
#
def print_stats(dbConn):
    dbCursor = dbConn.cursor()
    
    print("General stats:")
    #SQL query to find amount of stations, prints count
    dbCursor.execute("Select count(*) From Stations;")
    row = dbCursor.fetchone();
    print("  # of stations:", f"{row[0]:,}")
    #SQL query to find amount of stops, prints count
    dbCursor.execute("Select count(*) From Stops;")
    row = dbCursor.fetchone();
    print("  # of stops:", f"{row[0]:,}")
    #SQL query to find amount of ride entries, prints count
    dbCursor.execute("Select count(*) From Ridership;")
    row = dbCursor.fetchone();
    print("  # of ride entries:", f"{row[0]:,}")
    #SQL query to find oldest and newest date
    dbCursor.execute("Select date(Ride_Date) From Ridership;")
    row1 = dbCursor.fetchone();
    dbCursor.execute("Select date(Ride_Date) From Ridership ORDER BY date(Ride_Date) DESC LIMIT 1;")
    row2 = dbCursor.fetchone();
    #Concatenates both sql results, creates the date range, and prints
    date_range = row1[0] + " - " + row2[0]
    print("  date range:", f"{date_range:}")
    dbCursor.execute("Select sum(Num_Riders) From Ridership;")
    row = dbCursor.fetchone();
    print("  Total ridership:", f"{row[0]:,}")
    total = row[0]
    weekday = 0
    saturday = 0
    sunday = 0
    dbCursor.execute("Select Type_Of_Day, Num_Riders From Ridership;")
    result = dbCursor.fetchall();  
    for row in result:
      if row[0] == 'W':
        weekday+=row[1]
      elif row[0] == 'A':
        saturday+=row[1]
      else:
        sunday+=row[1]
    print("  Weekday ridership:", f"{weekday:,}", f"({str(round((weekday/total)*100, 2)) + str('%')})")
    print("  Saturday ridership:", f"{saturday:,}",f"({str(round((saturday/total)*100, 2)) + str('%')})")
    print("  Sunday/holiday ridership:", f"{sunday:,}", f"({str(round((sunday/total)*100, 2)) + str('%')})")
  
#
# pre_menu
#
# Nice helper function which stores the menu which the user 
# will loop through throughout the duration of the program
#
def pre_menu():
  print("\r")
  command = str(input("Please enter a command (1-9, x to exit):"))
  if command.isdigit() and int(command) >= 1 and int(command) <= 9:
    return command
  elif command == "x":
    quit()
  else:
    print(" **Error, unknown command, try again...")
#
# choice_1
#
# Stores the functionality of command 1, takes a partial station name
# which the user inputs and queries SQL for rows which have similar 
# station names. Prints them all if they're found
def choice_1():
  dbCursor = dbConn.cursor()
  print("\r")
  user_input = input("Enter partial station name (wildcards _ and %): ")
  #SQL Query which finds a station id and station name similar to the user inputted phrase
  dbCursor.execute("SELECT Station_ID, Station_Name FROM Stations WHERE Station_Name LIKE :phrase ORDER BY Station_Name ASC", {'phrase':user_input})
  result = dbCursor.fetchall()
  # Checks if there was no data retrieved
  if result == []:
    print(" **No stations found...")
    return
  for rows in result:
    print(f"{rows[0]:}", ":", f"{rows[1]}")
#
# choice_2
#
# Stores the functionality of command 2, queries SQL and prints out
# every station name and the amount of riders which they've accumulated through
# out time in ascending order
def choice_2():
  print(" ** ridership all stations **")
  dbCursor = dbConn.cursor()
  #SQL Query which finds the ridership of all stations along with their names
  dbCursor.execute("SELECT Stations.Station_Name, sum(Ridership.Num_Riders) FROM Stations INNER JOIN Ridership ON Stations.Station_ID = Ridership.Station_ID GROUP BY Stations.Station_Name ORDER BY Stations.Station_Name ASC")
  result = dbCursor.fetchall()
  for rows in result:
    #Ratio finds the ratio of ridership for the specific station out of the total ridership
    ratio = (rows[1]/3377404512) * 100
    print(rows[0], ":", f"{rows[1]:,}", f"({ratio:.2f}%)")
#
# choice_3
#
# Stores the functionality of command 3, queries SQL and prints out
# the top 10 stations in relation to the amounts of their riderships
def choice_3():
  print(" ** top-10 stations **")
  dbCursor = dbConn.cursor()
  #SQL Query which finds the top 10 stations based off of their ridership
  dbCursor.execute("SELECT Stations.Station_Name, SUM(Ridership.Num_Riders) FROM Stations INNER JOIN Ridership ON Stations.Station_ID = Ridership.Station_ID GROUP BY Station_Name ORDER BY SUM(Ridership.Num_Riders) DESC LIMIT 10")
  result = dbCursor.fetchall()
  for rows in result:
    #Ratio finds the ratio of ridership for the specific station out of the total ridership
    ratio = (rows[1]/3377404512) * 100
    print(rows[0], ":", f"{rows[1]:,}", f"({ratio:.2f}%)")
#
# choice_4
#    
# Stores the functionality of command 4, queries SQL and prints out
# the least 10 stations in relation to the amounts of their riderships
def choice_4():
  print(" ** least-10 stations **")
  dbCursor = dbConn.cursor()
  #SQL Query which finds the least 10 stations based off of their ridership
  dbCursor.execute("SELECT Stations.Station_Name, SUM(Ridership.Num_Riders) FROM Stations INNER JOIN Ridership ON Stations.Station_ID = Ridership.Station_ID GROUP BY Station_Name ORDER BY SUM(Ridership.Num_Riders) ASC LIMIT 10")
  result = dbCursor.fetchall()
  for rows in result:
    #Ratio finds the ratio of ridership for the specific station out of the total ridership
    ratio = (rows[1]/3377404512) * 100
    print(rows[0], ":", f"{rows[1]:,}", f"({ratio:.2f}%)")
#
# choice_5
#
# Stores the functionality of command 5, queries SQL and prints out
# the all the stop names, directions, and accesibility based off of the
# inputted line color.
def choice_5():
  print("\r")
  user_input = input("Enter a line color (e.g. Red or Yellow): ")
  user_input = user_input.title()
  dbCursor = dbConn.cursor()
  sql = "SELECT Stops.Stop_Name, Stops.Direction, Stops.ADA FROM Stops INNER JOIN StopDetails ON Stops.Stop_ID = StopDetails.Stop_ID INNER JOIN Lines ON Lines.Line_ID = StopDetails.Line_ID WHERE Lines.Color = ? ORDER BY Stops.Stop_NAME ASC"
  dbCursor.execute(sql, [user_input])
  result = dbCursor.fetchall()
  if result == []:
    print("**No such line...")
    return
  handicap = "yes"
  for rows in result:
    if rows[2] == 1:
      handicap = "yes"
    else:
      handicap = "no"
    print(rows[0], ":", "direction = " + rows[1], f"(accessible? {handicap})")

# Prints the plot based off of the information provided in either
# command 6 or command 7
def plot_choice6and7(result, date_type):
  x = []
  y = []
  for row in result:
    new_pop = row[1] / 10**8
    x.append(row[0])
    y.append(new_pop)
  plt.xlabel(date_type)
  plt.ylabel("number of riders (x * 10^8)")
  plt.title(date_type + "ly ridership")
  plt.plot(x, y)
  plt.show()
  #plt.savefig('graph.png')
#
# choice_6
#
# Stores the functionality of command 6, queries SQL and prints out
# the ride date and number of riders per month in ascending order
# Also gives the user the option to print out a plot
def choice_6():
  date_type = "month"
  print(" ** ridership by month **")
  dbCursor = dbConn.cursor()
  dbCursor.execute("SELECT strftime('%m', date(Ride_Date)) as Month, SUM(Num_Riders) FROM Ridership GROUP BY Month ORDER BY Month ASC")
  result = dbCursor.fetchall()
  for rows in result:
    print(rows[0], ":", f"{rows[1]:,}")
  print("\n")
  plot_input = input("Plot? (y/n)")
  if plot_input == "y":
    plot_choice6and7(result, date_type)
  else:
    return
#
# choice_7
#
# Stores the functionality of command 7, queries SQL and prints out
# the ride date and number of riders per year in ascending order
# Also gives the user the option to print out a plot
def choice_7():
  date_type = "year"
  print(" ** ridership by year **")
  dbCursor = dbConn.cursor()
  dbCursor.execute("SELECT strftime('%Y', date(Ride_Date)) as Year, SUM(Num_Riders) FROM Ridership GROUP BY Year ORDER BY Year ASC")
  result = dbCursor.fetchall()
  for rows in result:
    print(rows[0], ":", f"{rows[1]:,}")
  print("\n")
  plot_input = input("Plot? (y/n)")
  if plot_input == "y":
    plot_choice6and7(result, date_type)
  else:
    return
    
def print_choice8(result1, result2):
  print("Station 1:", result1[0][0], result1[0][1])
  for rows in result1:
    print(rows[2], f"{rows[3]}")
  print("Station 2:", result2[0][0], result2[0][1])
  for rows in result2:
    print(rows[2], f"{rows[3]}")
#
# choice_8
#
# Stores the functionality of command 8, queries SQL and prints out
# the information regarding two stations which the user inputted.
# Also gives the user the option to plot
def plot_choice8(year, station_1, station_2):
  dbCursor = dbConn.cursor()
  #Grabs the rows in the sql database
  sql = "SELECT Stations.Station_ID, Stations.Station_Name, date(Ridership.Ride_Date), Ridership.Num_Riders FROM Stations INNER JOIN Ridership ON Stations.Station_ID = Ridership.Station_ID WHERE Stations.Station_Name LIKE ? AND strftime('%Y', date(Ridership.Ride_Date)) == ? GROUP BY Ridership.Ride_Date ORDER BY date(Ridership.Ride_Date) ASC"
  dbCursor.execute(sql, [station_1, year])
  result1 = dbCursor.fetchall()
  dbCursor.execute(sql, [station_2, year])
  result2 = dbCursor.fetchall()
  x1 = []
  x2 = []
  y1 = []
  y2 = []
  for row in result1:
    #Converts the date into a datetime object in order to find day of the year
    dt = datetime.datetime.strptime(row[2], '%Y-%m-%d')
    day_of_year = dt.timetuple().tm_yday
    x1.append(day_of_year)
    y1.append(row[3])
  for row in result2:
    dt = datetime.datetime.strptime(row[2], '%Y-%m-%d')
    day_of_year = dt.timetuple().tm_yday
    x2.append(day_of_year)
    y2.append(row[3])
  plt.xlabel("day")
  plt.ylabel("number of riders")
  plt.title("riders each day of 2020")
  plt.plot(x1, y1, label = result1[0][1])
  plt.plot(x2, y2, label = result2[0][1])
  plt.show()
  
#Compares two stations and prints a plot out if the user desires
def choice_8(year, station):
  dbCursor = dbConn.cursor()
  #Grabs the first 5 rows in the sql database
  sql = "SELECT Stations.Station_ID, Stations.Station_Name, date(Ridership.Ride_Date), Ridership.Num_Riders FROM Stations INNER JOIN Ridership ON Stations.Station_ID = Ridership.Station_ID WHERE Stations.Station_Name LIKE ? AND strftime('%Y', date(Ridership.Ride_Date)) == ? GROUP BY Ridership.Ride_Date ORDER BY date(Ridership.Ride_Date) ASC LIMIT 5"
  #Grabs the last 5 rows in the sql data base
  sql2 = "SELECT Stations.Station_ID, Stations.Station_Name, date(Ridership.Ride_Date), Ridership.Num_Riders FROM Stations INNER JOIN Ridership ON Stations.Station_ID = Ridership.Station_ID WHERE Stations.Station_Name LIKE ? AND strftime('%Y', date(Ridership.Ride_Date)) == ? GROUP BY Ridership.Ride_Date ORDER BY date(Ridership.Ride_Date) DESC LIMIT 5"
  dbCursor.execute(sql, [station, year])
  result = dbCursor.fetchall()
  dbCursor.execute(sql2, [station, year])
  result2 = dbCursor.fetchall()
  #Rearranges the second result so that its ascending throughout the last 5 rows
  new_res2 = result2[::-1]
  total = result + new_res2
  return total

def plot_choice9(user_input, rows):
  color = user_input
  #
  # populate x and y lists with (x, y) coordinates --- note that longitude
  # are the X values and latitude are the Y values
  #
  x = []
  y = []

  for row in rows:
    x.append(row[2])
    y.append(row[1])

  image = plt.imread("chicago.png")
  xydims = [-87.9277, -87.5569, 41.7012, 42.0868] # area covered by the map:
  plt.imshow(image, extent=xydims)

  plt.title(color + " line")
  #
  # color is the value input by user, we can use that to plot the
  # figure *except* we need to map Purple-Express to Purple:
  #
  if (color.lower() == "purple-express"):
   color="Purple" # color="#800080"

  plt.plot(x, y, "o", c=color)
  #
  # annotate each (x, y) coordinate with its station name:
  #
  for row in rows:
   plt.annotate(row[0], (row[2], row[1]))

  plt.xlim([-87.9277, -87.5569])
  plt.ylim([41.7012, 42.0868])
  plt.show()
  
def choice_9():
  print("\r")
  user_input = input("Enter a line color (e.g. Red or Yellow): ")
  user_input = user_input.title()
  dbCursor = dbConn.cursor()
  sql = "SELECT DISTINCT Stations.Station_Name, Stops.Latitude, Stops.Longitude FROM Stations INNER JOIN Stops ON Stations.Station_ID = Stops.Station_ID INNER JOIN StopDetails ON Stops.Stop_ID = StopDetails.Stop_ID INNER JOIN Lines ON StopDetails.Line_ID = Lines.Line_ID WHERE Lines.Color = ? ORDER BY Stations.Station_Name ASC"
  dbCursor.execute(sql, [user_input])
  result = dbCursor.fetchall()
  if result == []:
    print("**No such line...")
    return

  for rows in result:
    print(rows[0], ":", (rows[1], rows[2]))
  print("\r")
  plot_input = input("Plot? (y/n)")
  if plot_input == "y":
    plot_choice9(user_input, result)
  else:
    return
def check(year, station):
  dbCursor = dbConn.cursor()
  count = 0
  check = "SELECT DISTINCT Stations.Station_Name FROM Stations INNER JOIN Ridership ON Stations.Station_ID = Ridership.Station_ID WHERE Stations.Station_Name LIKE ? AND strftime('%Y', date(Ridership.Ride_Date)) == ?"
  dbCursor.execute(check, [station, year])
  result = dbCursor.fetchall()
  for row in result:
    count+=1
  return count
##################################################################  
#
# main
#
print('** Welcome to CTA L analysis app **')
print()

dbConn = sqlite3.connect('CTA2_L_daily_ridership.db')
print_stats(dbConn)

while(1):
  choice = pre_menu()
  if choice == "1":
    choice_1()
  elif choice == "2":
    choice_2()
  elif choice == "3":
    choice_3()
  elif choice == "4":
    choice_4()
  elif choice == "5":
    choice_5()
  elif choice == "6":
    choice_6()
  elif choice == "7":
    choice_7()
  elif choice == "8":
    print("\n")
    year = input("Year to compare against?")
    print("\r")
    station_1 = input("Enter station 1 (wildcards _ and %):")
    count = check(year, station_1)
    if int(count) > 1:
      print(" **Multiple stations found...")
      continue
    elif int(count) < 1:
      print(" **No station found...")
      continue
    result_1 = choice_8(year, station_1)
    print("\r")
    station_2 = input("Enter station 2 (wildcards _ and %): ")
    count = check(year, station_2)
    if int(count) > 1:
      print(" **Multiple stations found...")
      continue
    elif int(count) < 1:
      print(" **No station found...")
      continue
    result_2 = choice_8(year, station_2)
    print_choice8(result_1, result_2)
    plot_input = input("Plot? (y/n)")
    if plot_input == "y":
      plot_choice8(year, station_1, station_2)
    else:
      continue
  elif choice == "9":
    choice_9()
#
# done
#