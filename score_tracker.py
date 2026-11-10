# ================================
#  INTRODUCTION TO MATPLOTLIB
# ================================

# ================================================
#  ACTIVITY - MY SCORE TRACKER
#  File: DSCM8L3-Jr-activity-complete.py
# ================================================

# PART 1 - IMPORT MATPLOTLIB
# Before drawing any chart you need to import the matplotlib library.
# matplotlib.pyplot is the drawing tool -- "plt" is its short nickname.
import matplotlib.pyplot as plt

# PART 2 - YOUR DATA
# days holds the x-axis labels -- the days of your school week.
# scores holds the y-axis values -- your quiz score for each day.
# Every score pairs up with the day in the same position.
days   = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']
scores = [70, 85, 60, 90, 75]

# PART 3 - PLOT YOUR FIRST LINE GRAPH
# plt.plot(x, y) draws a line through all your data points.
# plt.show() opens the chart window -- call it at the end of every chart.
plt.plot(days, scores)
plt.show()

# PART 4 - ADD LABELS AND A TITLE
# plt.title()      -- adds a heading at the top of the chart.
# plt.xlabel()     -- labels the x-axis (across the bottom).
# plt.ylabel()     -- labels the y-axis (up the side).
# plt.grid(True)   -- adds faint gridlines so values are easier to read.
# plt.ylim(0, 100) -- locks the y-axis from 0 to 100 so scores fit neatly.
plt.plot(days, scores)
plt.title('My Quiz Score Tracker')
plt.xlabel('Day of the Week')
plt.ylabel('Score')
plt.grid(True)
plt.ylim(0, 100)
plt.show()

# PART 5 - STYLE YOUR LINE CHART
# color='blue'        -- changes the line colour.
# marker='o'          -- puts a filled dot on every data point.
# linestyle='dashed'  -- draws the line as dashes instead of solid.
# linewidth=2         -- makes the line thicker so it stands out.
# All four style options go inside the same plt.plot() call.
plt.plot(days, scores, color='blue', marker='o', linestyle='dashed', linewidth=2)
plt.title('My Quiz Score Tracker')
plt.xlabel('Day of the Week')
plt.ylabel('Score')
plt.grid(True)
plt.ylim(0, 100)
plt.show()

# PART 6 - DRAW A BAR CHART
# plt.bar(x, y) draws a bar chart -- one bar per day rising to its score.
# Bar charts are great for comparing values side by side.
# color='orange' fills every bar with orange.
# The same title, labels, and ylim commands work exactly the same way.
plt.bar(days, scores, color='orange')
plt.title('My Quiz Score Bar Chart')
plt.xlabel('Day of the Week')
plt.ylabel('Score')
plt.ylim(0, 100)
plt.show()
