import pandas as pd
import matplotlib.pyplot as plt

#REQUIREMENT 2
#Roller coasters are thrilling amusement park rides designed to make you squeal and scream!
#They take you up high, drop you to the ground quickly, and sometimes even spin you upside down before returning to a stop.
#Today you will be taking control back from the roller coasters and visualizing data covering international roller coaster rankings and roller coaster statistics.
#Roller coasters are often split into two main categories based on their construction material: wood or steel.
#Rankings for the best wood and steel roller coasters from the 2013 to 2018 Golden Ticket Awards are provided in 'Golden_Ticket_Award_Winners_Wood.csv' and 'Golden_Ticket_Award_Winners_Steel.csv', respectively.
#Load each csv into a DataFrame and inspect it to gain familiarity with the data.

df_wood = pd.read_csv('Golden_Ticket_Award_Winners_Wood.csv')
df_steel = pd.read_csv('Golden_Ticket_Award_Winners_Steel.csv')

#Inspecting Wood
#print(df_wood.head())
#print(df_wood.columns)
#print(len(df_wood))

#Inspecting Steel
#print(df_steel.head())
#print(df_steel.columns)
#print(len(df_steel))

#Combining datatables

df_steel["Type"] = "Steel"
df_wood["Type"] = "Wood"

df_list = [df_steel,df_wood]
coasters = pd.concat(df_list)

#print(coasters.head())
#print(coasters.Type.value_counts())
#print(coasters["Year of Rank"].value_counts())

# MY FUNCTIONS
# My functions that power the required functions go here

#This function creates a list of consecutive years given a first year and a last year.

def year_list(min_year,max_year):
  years = [min_year]
  while years[-1] != max_year:
    years.append(years[-1] +1)
  return years

def year_adder(year_list, df):
  name = df.Name.iloc[0]
  park = df.Park.iloc[0]
  for year in year_list:
    if year in df["Year of Rank"].unique():
        pass
    else:
      df = df.append({"Name" : name, "Park" : park, "Year of Rank" : year} , ignore_index=True)
  df.sort_values(by =["Year of Rank"], inplace = True)
  return df


# REQUIREMENT 3
# Write a function that will plot the ranking of a given roller coaster over time as a line.
#Your function should take a roller coaster’s name and a ranking DataFrame as arguments.
#Make sure to include informative labels that describe your visualization.
# Call your function with "El Toro" as the roller coaster name and the wood ranking DataFrame.
#What issue do you notice? Update your function with an additional argument to alleviate the problem, and retest your function.

def ranking_over_time(name,park, df = coasters):
  #Generating the Rankings
  sub_df = df[(df.Name == name) & (df.Park == park)].reset_index(drop = True)
  #print(sub_df.head(10))
  #Charting Rankings
  ax = plt.subplot()
  ax.invert_yaxis()
  plt.plot(sub_df["Year of Rank"],sub_df["Rank"], marker='o', linestyle = "--")
  #Labels
  plt.title(name+" at "+park+", Ranking Over Time")
  plt.xlabel("Year")
  plt.ylabel("Ranking")
  #Showing & Closing Plot
  plt.show()
  plt.close("all")
  plt.clf()

#ranking_over_time("El Toro","Six Flags Great Adventure")

#REQUIREMENT 4
#Write a function that will plot the ranking of two given roller coasters over time as lines.
#Your function should take both roller coasters’ names and a ranking DataFrame as arguments.
#Make sure to include informative labels that describe your visualization.
#Call your function with "El Toro" as one roller coaster name, “Boulder Dash“ as the other roller coaster name, and the wood ranking DataFrame.
#What issue do you notice? Update your function with two additional arguments to alleviate the problem, and retest your function.

def two_rankings(name1,park1,name2,park2, df = coasters):
  #Generating Rankings
  sub_df1 = df[(df.Name == name1) & (df.Park == park1)].reset_index(drop = True)
  sub_df2 = df[(df.Name == name2) & (df.Park == park2)].reset_index(drop = True)
  #Are years in each list identical? If so, we can skip to visualization.
  if sub_df1["Year of Rank"].equals(sub_df2["Year of Rank"]):
    pass
  #If not, we need new tables for all the years
  else:
    #To start, we need to create a list of all the years which should be in both tables.
    #We ultimately want to capture all the years already in either table and any years in between.
    min_year = min(min(sub_df1["Year of Rank"].unique()), min(sub_df2["Year of Rank"].unique()))
    max_year = max(min(sub_df1["Year of Rank"].unique()), max(sub_df2["Year of Rank"].unique()))
    #print(min_year)
    #print(max_year)
    years = year_list(min_year, max_year)
    #We need to add these years to both tables:
    #Simplifying the tables because I am sick of scrolling. Comment this out later.
    #sub_df1.drop(columns = ["Location","Supplier", "Year Built","Points","Type"], inplace = True)
    #sub_df2.drop(columns = ["Location","Supplier", "Year Built","Points","Type"], inplace = True)
    #Later, write a function to avoid repeating code.
    sub_df1 = year_adder(years, sub_df1)
    sub_df2 = year_adder(years, sub_df2)
  #Line Chart Visulatization
  plt.figure()
  ax = plt.subplot()
  ax.invert_yaxis()
  plt.plot(sub_df1["Year of Rank"],sub_df1["Rank"], label = name1+ " at "+park1, marker='o', linestyle = "--")
  plt.plot(sub_df2["Year of Rank"],sub_df2["Rank"], label = name2+ " at "+park2, marker='o', linestyle = "--")
  plt.legend()
  #Labels
  plt.legend()
  plt.title("Rankings Over Time")
  plt.xlabel("Years")
  plt.ylabel("Ranking")
  #Showing & Closing Chart
  plt.show()
  plt.close("all")
  plt.clf()

#Test when roller coasters have the same years
#two_rankings("El Toro","Six Flags Great Adventure","Boulder Dash","Lake Compounce")

#Test when roller coasters have different years
#two_rankings("El Toro","Six Flags Great Adventure","Steel Vengeance", "Cedar Point")

#REQUIREMENT 5
#Write a function that will plot the ranking of the top n ranked roller coasters over time as lines.
#Your function should take a number n and a ranking DataFrame as arguments.
#Make sure to include informative labels that describe your visualization.
#For example, if n == 5, your function should plot a line for each roller coaster that has a rank of 5 or lower.
#Call your function with a value for n and either the wood ranking or steel ranking DataFrame.

def top_n(n, df):
  #Simplifying the tables because I am sick of scrolling. Comment this out later.
  #Identifying the top n coasters
  #Here is a df of the top n coasters this year
  df.drop(columns = ["Location","Supplier", "Year Built","Points","Type"], inplace = True)
  latest_year_df = df[(df.Rank <= n) & (df["Year of Rank"] == max(df["Year of Rank"].unique()))].reset_index(drop = True)
  #We're going to create a new column that combines name and park, so that we can filter by the combination
  latest_year_df["NamePark"] = latest_year_df.Name + latest_year_df.Park
  namepark_list = latest_year_df.NamePark.unique()
  df["NamePark"] = df.Name + df.Park
  #Now we can filter down to just the data that we actually want and identify the years for which we need data
  sub_df = df[df.NamePark.isin(namepark_list)].reset_index(drop = True)
  #print(sub_df)
  min_year = min(sub_df["Year of Rank"])
  max_year = max(sub_df["Year of Rank"])
  years = year_list(min_year,max_year)
  #Starting the visualization
  plt.figure()
  ax = plt.subplot()
  ax.invert_yaxis()
  #Adding each coaster to the visualization, using NamePark as the unique identifier
  for i in sub_df.NamePark.unique():
    sub_df_i = sub_df[sub_df.NamePark == i].reset_index(drop = True)
    sub_df_i = year_adder(years, sub_df_i)
    plt.plot(sub_df_i["Year of Rank"],sub_df_i["Rank"], label = sub_df_i.Name.iloc[0]+ " at "+sub_df_i.Park.iloc[0], marker='o', linestyle = "--")
  #Labels
  plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.15))
  plt.tight_layout()
  plt.title("Top "+str(n)+ " Roller Coasters, Rankings Over Time")
  plt.xlabel("Years")
  plt.ylabel("Rankings")
  #Showing & Closing Visualization
  plt.show()
  plt.close("all")
  plt.clf()

#top_n(5,df_wood)

#REQUIREMENT 6
#Now that you’ve visualized rankings over time, let’s dive into the actual statistics of roller coasters themselves.
#Captain Coaster is a popular site for recording roller coaster information.
#Data on all roller coasters documented on Captain Coaster has been accessed through its API and stored in roller_coasters.csv.
#Load the data from the csv into a DataFrame and inspect it to gain familiarity with the data.

df_facts = pd.read_csv("roller_coasters.csv")

#print(df_facts.head(10))
#print(df_facts.columns)
#print(len(df_facts))

#print(df_facts.material_type.unique())
#print(df_facts.seating_type.unique())

#REQUIREMENT 7
#Write a function that plots a histogram of any numeric column of the roller coaster DataFrame.
#Your function should take a DataFrame and a column name for which a histogram should be constructed as arguments.
#Make sure to include informative labels that describe your visualization.
#Call your function with the roller coaster DataFrame and one of the column names.

#print(df_facts.dtypes)

def numeric_hist(column, df = df_facts):
  #Validate Column Entry
  try:
    #Plot Histogram
    plt.hist(df[column], bins = 20)
    #Labels
    plt.title("Histogram of "+column)
    plt.ylabel("Frequency")
    plt.xlabel(column)
    #Showing & Closing Visualization
    plt.show()
    plt.close("all")
    plt.clf()
  except KeyError:
    print("Please enter a valid numerical column")

#numeric_hist("speed")

#REQUIREMENT 8
#Write a function that creates a bar chart showing the number of inversions for each roller coaster at an amusement park.
#Your function should take the roller coaster DataFrame and an amusement park name as arguments.
#Make sure to include informative labels that describe your visualization.
#Call your function with the roller coaster DataFrame and an amusement park name.

def inversions_bar(park_val, df = df_facts):
  sub_df = df[df.park == park_val].reset_index(drop = True)
  sub_df.sort_values(by =["num_inversions"], ascending=False, inplace = True)
  #Simplifying the tables because I am sick of scrolling. Comment this out later.
  #sub_df.drop(columns = ["material_type", "status", "seating_type", "height", "length", "manufacturer", "speed", "park"], inplace = True)
  #print(sub_df)
  #Visualizing Bar
  ax = plt.subplot()
  plt.bar(range(len(sub_df.name.values)), sub_df.num_inversions)
  #Labels
  ax.set_xticks(range(len(sub_df.name.values)))
  ax.set_xticklabels(sub_df.name.values)
  plt.xticks(rotation=90)
  plt.title("Inversions Per Rollercoaster at "+park_val)
  plt.ylabel("Inversions")
  ##Showing & Closing Visualization
  plt.tight_layout()
  plt.show()
  plt.close("all")
  plt.clf()

#inversions_bar("Six Flags Great Adventure")

#REQUIREMENT 9
#Write a function that creates a pie chart that compares the number of operating roller coasters ('status.operating') to the number of closed roller coasters ('status.closed.definitely').
#Your function should take the roller coaster DataFrame as an argument.
#Make sure to include informative labels that describe your visualization.

#print(df_facts.status.unique())

def status_pie(park_val, df = df_facts):
    #Filtering to just the roller coasters that we're interested in
    sub_df = df[(df.park == park_val) & ((df.status == "status.operating") | (df.status == "status.closed.definitely"))].reset_index(drop = True)
    #Simplifying the tables because I am sick of scrolling. Comment this out later.
    #sub_df.drop(columns = ["material_type", "num_inversions", "seating_type", "height", "length", "manufacturer", "speed", "park"], inplace = True)
    #print(sub_df)
    #Creating Table by status & renaming labels
    status_df = sub_df.groupby(["status"]).name.count().reset_index()
    status_df.status = status_df.status.apply(lambda x : "Operating" if x == "status.operating" else x)
    status_df.status = status_df.status.apply(lambda x : "Closed" if x == "status.closed.definitely" else x)
    print(status_df)
    #Visualizing pie
    plt.pie(status_df.name.tolist(), autopct ='%0.1f%%' )
    plt.axis('equal')
    #Labels
    plt.title("Closed & Operating Roller Coasters at "+park_val)
    plt.legend(status_df.status.tolist())
    ##Showing & Closing Visualization
    plt.tight_layout()
    plt.show()
    plt.close("all")
    plt.clf()

#status_pie("Six Flags Great Adventure")

# REQUIREMENT 10
#.scatter() is another useful function in matplotlib that you might not have seen before.
#.scatter() produces a scatter plot, which is similar to .plot() in that it plots points on a figure.
#.scatter(), however, does not connect the points with a line.
#This allows you to analyze the relationship between to variables.
#Find .scatter()‘s documentation here.
# Write a function that creates a scatter plot of two numeric columns of the roller coaster DataFrame.
#Your function should take the roller coaster DataFrame and two-column names as arguments.
#Make sure to include informative labels that describe your visualization.
# Call your function with the roller coaster DataFrame and two-column names.

def numeric_scatter(col1,col2, df = df_facts):
    #Validate Column Entries
    try:
        #Visualizing Scatter
        plt.scatter(df[col1],df[col2])
        #labels
        plt.title("Roller Coaster "+col1+" versus "+col2)
        plt.xlabel(col1)
        plt.ylabel(col2)
        #Showing & Closing Visualization
        plt.tight_layout()
        plt.show()
        plt.close("all")
        plt.clf()
    except KeyError:
        print("Please enter valid numerical columns")

#numeric_scatter("speed","height")

# REQUIREMENT 11
#Part of the fun of data analysis and visualization is digging into the data you have and answering questions that come to your mind.

#Size of Tallest Coaster by Park?

#print(df_facts.columns)
#print(df_facts.manufacturer.nunique())
