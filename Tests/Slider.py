import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button

x = list(range(0, 11))
y = [10] * 11

fig, ax = plt.subplots()
plt.subplots_adjust(left=0.1, bottom=0.35)
p, = plt.plot(x, y, linewidth=2, color='blue')
plt.axis([0, 10, 0, 100])

axSlider1 = plt.axes([0.1, 0.2, 0.8, 0.05])
slder1 = Slider(axSlider1, 'Slider 1', valmin=0, valmax=100)

axSlider2 = plt.axes([0.1, 0.1, 0.8, 0.05])
slder2 = Slider(	ax=axSlider2,
					label='Slider 2',
					valmin=0,
					valmax=100,
					valinit=30,
					valfmt='%1.2f',
					valstep=10,
					# slidermin=slder1,
					closedmax=True,
					color='green')

def val_update(val):
	yval = slder2.val
	p.set_ydata(yval)
	plt.draw()

cid2 = slder2.on_changed(val_update)
# slder2.disconnect(cid2)

axButton1 = plt.axes([0.1, 0.9, 0.1, 0.1])
btn1 = Button(axButton1, 'Reset')

axButton2 = plt.axes([0.25, 0.9, 0.2, 0.1])
btn2 = Button(axButton2, 'Set Val')

def resetSLiders(event):
	slder1.reset()
	slder2.reset()
btn1.on_clicked(resetSLiders)

def setValue(val):
	slder2.set_val(50)
btn2.on_clicked(setValue)

plt.show()