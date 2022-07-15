import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import time
def babylonian_sqrroot():
    global seta, setb, setguess, guess, sqr, a, b
    sqr = float(input("What would you like to find the square root of?:   "))
    guess = sqr/10 #First guess for the sqr root. Im not using the math module because that's no fun and defeats the whole purpose of the babylonian method
    seta = []
    setb = []
    setguess = []
    while True:
        a = sqr/guess
        b = (a+guess)/2
        seta.append(a)
        setb.append(b)
        setguess.append(guess)
        if round(guess, 5) == round(a, 5):
            return "The square root of {} is: {}!".format(str(round(sqr, 5)), str(round(guess, 5)))
        guess = b

print(babylonian_sqrroot())
print(setguess)
print(seta)
print(setb)

# set up the figure
fig = plt.figure("Illustration of Babylonian Square Root Algorithm")
ax = fig.add_subplot(111)
ax.set_xlim(0,10)
ax.set_ylim(0,10)




# draw lines
xmin = 0
xmax = 10
y = 5
height = 1

plt.hlines(y, xmin, xmax)
plt.vlines(xmin, y - height / 2., y + height / 2.)
plt.vlines(xmax, y - height / 2., y + height / 2.)

plt.text(xmin - 0.1, y, '0', horizontalalignment='right')
plt.text(xmax + 0.1, y, str(max(setguess)), horizontalalignment='left')
plt.pause(.01)
red_patch = mpatches.Patch(color='red', label='Average between guess and radicand÷guess')
yellow_patch = mpatches.Patch(color='yellow', label='New Guess')
blue_patch = mpatches.Patch(color='blue', label='Radicand÷Guess')
green_patch = mpatches.Patch(color='green', label='Correct Answer')
plt.legend(handles=[yellow_patch, blue_patch, red_patch, green_patch], loc='upper center')
plt.plot(5,y+2, 'ro', ms = 10, mfc = 'r') #Where all of the arrows stem from
plt.axis('off')
plt.ion()
fig.canvas.draw()
fig.canvas.flush_events()
ax = 0
time.sleep(7)
for ax in range(0, len(setguess)-1):
    plt.plot((setguess[ax]/max(setguess))*10,y, 'ro', ms = 5, mfc = 'r')
    plt.annotate('', ((setguess[ax]/max(setguess))*10,y), xytext = (5, y + 2), 
            arrowprops=dict(facecolor='yellow', shrink=0.01), 
            horizontalalignment='center')
    time.sleep(.5)
    fig.canvas.draw()
    fig.canvas.flush_events()
    plt.plot((seta[ax]/max(setguess))*10,y, 'ro', ms = 5, mfc = 'r')
    plt.annotate('', ((seta[ax]/max(setguess))*10,y), xytext = (5, y + 2), 
            arrowprops=dict(facecolor='blue', shrink=0.01), 
            horizontalalignment='center')
    time.sleep(.5)
    fig.canvas.draw()
    fig.canvas.flush_events()
    plt.plot((setb[ax]/max(setguess))*10,y, 'ro', ms = 5, mfc = 'r')
    plt.annotate('', ((setb[ax]/max(setguess))*10,y), xytext = (5, y + 2), 
            arrowprops=dict(facecolor='red', shrink=0.01), 
            horizontalalignment='center')
    time.sleep(.5)
    fig.canvas.draw()
    fig.canvas.flush_events()
    ax+=1
ax=len(setguess)-1
time.sleep(2)
plt.plot((setb[ax]/max(setguess))*10,y, 'ro', ms = 5, mfc = 'r')
plt.annotate('', ((setb[ax]/max(setguess))*10,y), xytext = (5, y + 2), 
            arrowprops=dict(facecolor='green', shrink=0.01), 
            horizontalalignment='center')
plt.text(5, 10, "The square root of {} is: {}!".format(str(round(sqr, 5)), str(round(guess, 5))), horizontalalignment='center')

fig.canvas.draw()
fig.canvas.flush_events()
plt.show()
time.sleep(8)

# add numbers
