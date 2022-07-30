from psycopg2.extensions import AsIs
from statistics import mode, mean, median, variance
from unittest import result
import psycopg2
import math


dress_color = {
    'MONDAY': ['GREEN', 'YELLOW', 'GREEN', 'BROWN', 'BLUE', 'PINK', 'BLUE', 'YELLOW', 'ORANGE', 'CREAM', 'ORANGE', 'RED', 'WHITE', 'BLUE', 'WHITE', 'BLUE', 'BLUE', 'BLUE', 'GREEN'],
    'TUESDAY': ['ARSH', 'BROWN', 'GREEN', 'BROWN', 'BLUE', 'BLUE', 'BLEW', 'PINK', 'PINK', 'ORANGE', 'ORANGE', 'RED', 'WHITE', 'BLUE', 'WHITE', 'WHITE', 'BLUE', 'BLUE', 'BLUE'],
    'WEDNESDAY': ['GREEN', 'YELLOW', 'GREEN', 'BROWN', 'BLUE', 'PINK', 'RED', 'YELLOW', 'ORANGE', 'RED', 'ORANGE', 'RED', 'BLUE', 'BLUE', 'WHITE', 'BLUE', 'BLUE', 'WHITE', 'WHITE'],
    'THURSDAY': ['BLUE', 'BLUE', 'GREEN', 'WHITE', 'BLUE', 'BROWN', 'PINK', 'YELLOW', 'ORANGE', 'CREAM', 'ORANGE', 'RED', 'WHITE', 'BLUE', 'WHITE', 'BLUE', 'BLUE', 'BLUE', 'GREEN'],
    'FRIDAY': ['GREEN', 'WHITE', 'GREEN', 'BROWN', 'BLUE', 'BLUE', 'BLACK', 'WHITE', 'ORANGE', 'RED', 'RED', 'RED', 'WHITE', 'BLUE', 'WHITE', 'BLUE', 'BLUE', 'BLUE', 'WHITE']
}

color_combined = []
for color in dress_color:
    color_combined += (dress_color[color])

num_color = []
for i in color_combined:
    if i not in num_color:
        num_color.append(i)

####################----- 1. MEAN COLOR-----########################

num_GREEN = 0
num_YELLOW = 0
num_BROWN = 0
num_BLUE = 0
num_PINK = 0
num_ORANGE = 0
num_CREAM = 0
num_RED = 0
num_WHITE = 0
num_ARSH = 0
num_BLEW = 0
num_BLACK = 0

color_to_num  = []
for i in color_combined:
    if i == 'GREEN':
        i = 1
    if i == 'YELLOW':
        i = 2
    if i == 'BROWN':
        i = 3
    if i == 'BLUE':
        i = 4
    if i == 'PINK':
        i = 5
    if i == 'ORANGE':
        i = 6
    if i == 'CREAM':
        i = 7
    if i == 'RED':
        i = 8
    if i == 'WHITE':
        i = 9
    if i == 'ARSH':
        i = 10
    if i == 'BLEW':
        i = 11
    if i == 'BLACK':
        i = 12
    color_to_num.append(i)

mean = math.floor(sum(color_to_num)/len(color_to_num))

color_stac = mean

if color_stac == 1:
    color_stac = 'GREEN'
if color_stac == 2:
    color_stac = 'YElLOW'
if color_stac == 3:
    color_stac = 'BLUE'
if color_stac == 4:
    color_stac = 'PINK'
if color_stac == 5:
    color_stac = 'ORANGE'
if color_stac == 6:
    color_stac = 'CREAM'
if color_stac == 7:
    color_stac = 'RED'
if color_stac == 8:
    color_stac = 'GREEN'
if color_stac == 9:
    color_stac = 'WHITE'
if color_stac == 10:
    color_stac = 'ARSH'
if color_stac == 11:
    color_stac = 'BLEW'
if color_stac == 12:
    color_stac = 'BLACK'
print('The average color is ', color_stac)

####################-----MEAN COLOR-----########################




####################-----2. VARIANT COLOR-----########################
variance = math.floor(variance(color_to_num))

color_stac = variance
if color_stac == 1:
    color_stac = 'GREEN'
if color_stac == 2:
    color_stac = 'YElLOW'
if color_stac == 3:
    color_stac = 'BLUE'
if color_stac == 4:
    color_stac = 'PINK'
if color_stac == 5:
    color_stac = 'ORANGE'
if color_stac == 6:
    color_stac = 'CREAM'
if color_stac == 7:
    color_stac = 'RED'
if color_stac == 8:
    color_stac = 'GREEN'
if color_stac == 9:
    color_stac = 'WHITE'
if color_stac == 10:
    color_stac = 'ARSH'
if color_stac == 11:
    color_stac = 'BLEW'
if color_stac == 12:
    color_stac = 'BLACK'
print('the variant color is ', color_stac)
####################-----VARIANT COLOR-----########################




####################-----3. MODE COLOR-----########################
most_worn = mode(color_combined)
print('the most worn color is ', most_worn)



####################-----4. MEDIAN COLOR-----########################
median = median(color_combined)
print('the most median color is ', median)



####################-----5. COLOR AND COOLOR FREQUENCY STORED IN POSTGRESQL DATABASE-----########################
data = {x:color_combined.count(x) for x in color_combined}
print(data)


connection = psycopg2.connect('dbname=bincom_test')


cursor = connection.cursor()

cursor.execute('''DROP TABLE IF EXISTS dress_color CASCADE''')

cursor.execute('''
CREATE TABLE dress_color (
  color VARCHAR,
  frequency INT
);
''')
connection.commit()
color_value = data.keys()
frequency = data.values()
f_value = [data[column] for column in data]

for i in data:
    d = data[i]
    print(i, ":", d)
    cursor.execute('INSERT INTO dress_color ( color, frequency ) VALUES ( '+ "'" + str(i) + "'" + ', ' + "'" + str(d) + "'" + ' );')

cursor.execute('SELECT * FROM dress_color;')

result = cursor.fetchall()
print(result)
connection.commit()
connection.close()
cursor.close()
####################-----COLOR AND COOLOR FREQUENCY STORED IN POSTGRESQL DATABASE-----########################