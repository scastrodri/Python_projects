# There are many tools to graph data, but let's 'code' our own graphs from scratch using the turtle
# module.

import turtle
import random
import time

country_name = ['Philippines', 'Costa Rica', 'Ghana', 'Vietnam', 'Honduras', 'Kenya', 'Guatemala', 
    'Togo', 'Peru', 'Lebanon', 'Bolivia', 'Kenya', 'Philippines', 'Kyrgyzstan', 'Vietnam', 'Colombia', 
    'Peru', 'Guatemala', 'El Salvador', 'Tanzania', 'Cambodia', 'Cambodia', 'Ghana', 'Philippines', 
    'Philippines', 'Colombia', 'Sierra Leone', 'Nicaragua', 'Lebanon', 'Kenya', 'Tajikistan', 'Kenya', 
    'Bolivia', 'Kenya', 'Uganda', 'Benin', 'Ghana', 'Cambodia', 'Peru', 'Palestine', 'Vietnam', 
    'Ecuador', 'Kyrgyzstan', 'Philippines', 'Samoa', 'Philippines', 'Philippines', 'Philippines', 
    'Honduras', 'Philippines', 'Philippines', 'Philippines', 'Philippines', 'Nigeria', 'India', 
    'Philippines', 'Philippines', 'Guatemala', 'Zimbabwe', 'Jordan', 'Togo', 'Bolivia', 'Cambodia', 
    'Philippines', 'Colombia', 'Philippines', 'Kosovo', 'Philippines', 'India', 'Bolivia', 'Vietnam', 
    'Peru', 'Paraguay', 'Ghana', 'Sierra Leone', 'Ecuador', 'Kenya', 'Nicaragua', 'Nigeria', 'Kenya', 
    'Philippines', 'Cambodia', 'Mongolia', 'Kenya', 'Paraguay', 'Kenya', 'Vietnam', 'Sierra Leone', 
    'Kenya', 'Peru', 'Nigeria', 'Philippines', 'Palestine', 'Nicaragua', 'Togo', 'Ecuador', 
    'Philippines', 'El Salvador', 'Togo', 'Cambodia']

loan_amount = [175.0, 4075.0, 250.0, 725.0, 875.0, 475.0, 800.0, 1050.0, 350.0, 1200.0, 700.0, 1500.0, 
    300.0, 1300.0, 725.0, 1325.0, 1050.0, 2650.0, 1500.0, 525.0, 100.0, 800.0, 300.0, 475.0, 250.0, 
    1050.0, 175.0, 275.0, 500.0, 125.0, 900.0, 250.0, 725.0, 950.0, 325.0, 375.0, 475.0, 1200.0, 550.0, 
    2500.0, 475.0, 350.0, 1575.0, 625.0, 1100.0, 275.0, 450.0, 275.0, 500.0, 500.0, 225.0, 425.0, 375.0, 
    100.0, 375.0, 225.0, 225.0, 400.0, 300.0, 500.0, 1150.0, 1500.0, 1300.0, 1125.0, 125.0, 475.0, 
    1775.0, 75.0, 400.0, 4200.0, 475.0, 175.0, 3600.0, 300.0, 200.0, 600.0, 325.0, 2500.0, 175.0, 
    1125.0, 225.0, 700.0, 1625.0, 250.0, 225.0, 225.0, 625.0, 175.0, 400.0, 375.0, 475.0, 600.0, 650.0, 
    575.0, 300.0, 650.0, 325.0, 950.0, 675.0, 175.0]

status = ['funded', 'funded', 'funded', 'funded', 'funded', 'funded', 'funded', 'funded', 'funded', 
    'expired', 'funded', 'funded', 'funded', 'funded', 'funded', 'funded', 'funded', 'funded', 
    'expired', 'funded', 'funded', 'funded', 'funded', 'funded', 'funded', 'funded', 'funded', 'funded', 
    'funded', 'funded', 'funded', 'funded', 'funded', 'funded', 'funded', 'funded', 'funded', 'funded', 
    'funded', 'funded', 'funded', 'funded', 'funded', 'funded', 'funded', 'funded', 'funded', 'funded', 
    'funded', 'funded', 'funded', 'funded', 'funded', 'funded', 'funded', 'funded', 'funded', 'funded', 
    'funded', 'funded', 'funded', 'funded', 'funded', 'funded', 'funded', 'funded', 'expired', 'funded', 
    'funded', 'funded', 'refunded', 'funded', 'funded', 'funded', 'funded', 'funded', 'funded', 
    'funded', 'funded', 'expired', 'funded', 'funded', 'funded', 'funded', 'funded', 'funded', 'funded', 
    'funded', 'funded', 'funded', 'funded', 'funded', 'funded', 'funded', 'funded', 'funded', 'funded', 
    'expired', 'funded', 'funded']

time_to_raise = [29536.0, 855800.0, 525437.0, 446139.0, 318259.0, 233510.0, 959437.0, 180379.0, 
    149253.0, 'NaN', 24078.0, 2109764.0, 399465.0, 3093264.0, 480324.0, 2967345.0, 1440097.0, 520440.0, 
    'NaN', 695592.0, 1589143.0, 912703.0, 106892.0, 897403.0, 303536.0, 2796346.0, 464517.0, 3200624.0, 
    359739.0, 2694864.0, 1477409.0, 1160378.0, 154704.0, 2751213.0, 561688.0, 464193.0, 110779.0, 
    139249.0, 59124.0, 1228481.0, 570862.0, 562786.0, 391749.0, 956970.0, 215575.0, 1732692.0, 387149.0, 
    238235.0, 60656.0, 1034437.0, 200404.0, 2638660.0, 441376.0, 193005.0, 1579789.0, 1751202.0, 
    209067.0, 358058.0, 534379.0, 152210.0, 1114154.0, 2301012.0, 1796158.0, 2192826.0, 274454.0, 
    2580368.0, 'NaN', 29783.0, 214339.0, 1637260.0, 236306.0, 47364.0, 347076.0, 177559.0, 358278.0, 
    1762084.0, 239353.0, 722627.0, 1666895.0, 'NaN', 387850.0, 2891946.0, 2496478.0, 3581819.0, 
    1022886.0, 598047.0, 53170.0, 246086.0, 821339.0, 416969.0, 127372.0, 481125.0, 1182454.0, 365786.0, 
    196809.0, 498223.0, 511130.0, 'NaN', 1911732.0, 345751.0]

num_lenders_total = [1, 144, 10, 23, 22, 16, 22, 35, 11, 32, 28, 53, 8, 39, 19, 49, 30, 85, 9, 16, 4, 
    31, 12, 6, 9, 21, 6, 10, 11, 7, 34, 8, 23, 38, 11, 15, 12, 46, 14, 50, 16, 12, 62, 18, 35, 7, 18, 
    10, 19, 12, 9, 10, 13, 3, 13, 8, 9, 9, 11, 18, 14, 52, 48, 40, 2, 11, 42, 1, 9, 106, 17, 6, 18, 11, 
    5, 21, 10, 88, 6, 9, 7, 23, 61, 6, 9, 9, 14, 6, 7, 15, 15, 1, 22, 20, 12, 7, 10, 6, 20, 2]

# Creating a dictionary of dictionaries with the total info
def new_dict(list1,list2):
    a_dict = {}
    for i in range(len(list1)):
        a_dict[list1[i]] = a_dict.get(list1[i],[]) + [list2[i]]
    return a_dict

d_amount = new_dict(country_name,loan_amount)
d_status = new_dict(country_name,status)
d_ttr = new_dict(country_name,time_to_raise)
d_lenders = new_dict(country_name,num_lenders_total)

big_d = {}
for country in d_amount.keys():
    big_d[country] = {'loan_amount': d_amount[country], 'status': d_status[country], 
                        'time_to_raise': d_ttr[country], 'num_lenders_total': d_lenders[country]}

# Creating the turtle to make the graphics
tes = turtle.Turtle()
tes.speed(0)
wn = turtle.Screen()

# Creating the 'x', 'y' coordinates
def drawCoordinates(turtle,xmin=-500,ymin=-700,xmax=500,ymax=700):
    ''' Set up the turtle's screen according to the graphic'''
    wn.setworldcoordinates(xmin,ymin,xmax,ymax)
    wn.colormode(255)
    turtle.up()
    turtle.goto(xmin,ymin)
    turtle.down()
    turtle.forward(xmax)
    turtle.stamp()
    turtle.left(180)
    turtle.forward(xmax)
    turtle.right(90)
    turtle.forward(ymax)
    turtle.stamp()
    turtle.right(180)
    turtle.forward(ymax)
    turtle.left(90)

# Creates the barchar graphic
def drawBar(turtle,label,size,y):
    ''' Create a vertical bar chart plot. '''
    R, G, B = random.randint(0,255), random.randint(0,255), random.randint(0,255)
    turtle.fillcolor(R,G,B)
    turtle.begin_fill()
    turtle.left(90)
    turtle.forward(y)
    turtle.write(str(label), font=('Arial',6,'normal'))
    turtle.right(90)
    turtle.forward(size)
    turtle.right(90)
    turtle.forward(y)
    turtle.left(90)
    turtle.end_fill()

# A scatter plot graphic
def drawScatter(turtle,x_pos,y_pos):
    ''' Create a scatter plot '''
    R, G, B = random.randint(0,255), random.randint(0,255), random.randint(0,255)
    turtle.up()
    turtle.goto(x_pos,y_pos)
    turtle.dot(10,(R,G,B))

# The loan amount by country
while True:
    size = 100
    minx = 0
    miny = 0
    maxx = len(big_d)*size*1.1
    maxy = sum(big_d['Philippines']['loan_amount'])*1.1
    drawCoordinates(tes,minx,miny,maxx,maxy)
    for country in big_d:
        drawBar(tes,country,size,sum(big_d[country]['loan_amount']))
    time.sleep(5)
    break

wn.clearscreen()

while True:
    minx = 0
    miny = 0
    maxx = max(num_lenders_total)*.9
    maxy = max(loan_amount)*1.1
    drawCoordinates(tes,minx,miny,maxx,maxy)
    for i in range(len(num_lenders_total)):
        drawScatter(tes,num_lenders_total[i],loan_amount[i])
    time.sleep(5)
    break

wn.clearscreen()

# Creates a histogram using the bar chart graphic
while True:
    bucketList = [x for x in range(0,int(max(loan_amount))+int(max(loan_amount)/10),
                int(max(loan_amount)/10))]
    bucket = {}
    for i in range(len(bucketList)-1):
        for value in loan_amount:
            if value >= bucketList[i] and value < bucketList[i+1]:
                bucket[f'bucket{i}'] = bucket.get(f'bucket{i}', 0) + 1
    size = 1
    minx = 0
    miny = 0
    maxx = len(bucket)*1.1
    maxy = bucket[sorted(bucket,key=lambda x: bucket[x],reverse=True)[0]]*1.1
    drawCoordinates(tes,minx,miny,maxx,maxy)
    for k,v in bucket.items():
        drawBar(tes,k,size,v)
    time.sleep(5)
    break