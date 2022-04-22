import tkinter
from tkinter import ttk

import CountriesService
import StatsService

import matplotlib.pyplot as plt
import numpy as np

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

form = tkinter.Tk()

form.title("Covid Stats")
form.geometry("1000x600")



lblinfo = tkinter.Label(form, text="Covid info from RestApi", font=("Ariel Black", 20), fg="blue")

lblinfo.grid(row=0,column=0,sticky="we")

left_frame = tkinter.Frame(form, bg="green", highlightbackground="black", highlightthickness=2)
left_frame.grid(row=1,column=0)

right_frame = tkinter.Frame(form, bg="gray", highlightbackground="black", highlightthickness=2)
right_frame.grid(row=1,column=1)

plot_frame = tkinter.Frame(form, bg="yellow", highlightbackground="black", highlightthickness=2)
plot_frame.grid(row=2,column=1)

countries = CountriesService.CountriesService.get_countries()

countriesList=[]


def SelectedIndexChanged(event):
    global selectedCountry
    selectedCountry=str(event.widget.get())
    stats=StatsService.StatsService.get_stats(selectedCountry)
    if(stats != False):
        text.set(stats.country + "\n Confirmed:" + str(stats.mystats['confirmed']) +
        "\n deaths:" + str(stats.mystats['deaths']) +
        "\n date:" + str(stats.mystats['date']) +
        "\n active:" + str(stats.mystats['active'])
        )
    else:
        text.set("no data")

combi = ttk.Combobox(left_frame, values=countries)
combi.grid(row=0,column=0)
combi.bind("<<ComboboxSelected>>", SelectedIndexChanged)


text = tkinter.StringVar()
text.set("result")

lblResult = tkinter.Label(right_frame, textvariable=text)
lblResult.grid(row=0,column=0,padx=20,pady=20)

def btnAddCountry():
    countriesList.append(selectedCountry)
    str=""
    for c in countriesList:
        str = str+c+"\n"
    textCountries.set(str)
        

btn = tkinter.Button(right_frame, width=30, height=2,text="Add country", command=btnAddCountry)
btn.grid(row=1,column=0)


textCountries = tkinter.StringVar()
textCountries.set("countries")

lblCountries = tkinter.Label(right_frame, textvariable=textCountries)
lblCountries.grid(row=0,column=1,padx=20,pady=20)

def btnShowPlot():
    drawPlot()

btnShow = tkinter.Button(right_frame, width=30, height=2,text="Show plot", command=btnShowPlot)
btnShow.grid(row=1,column=1)

def drawPlot():
    data = print(StatsService.StatsService.get_deaths_for_all_countries(countriesList))

    fig = Figure(figsize=(5,5), dpi=100)

    plot1 = fig.add_subplot(111)

    width=.5
    plot1.bar(countriesList, data, width)

    canvas = FigureCanvasTkAgg(fig, master=plot_frame)
    canvas.draw()

    canvas.get_tk_widget().grid(row=0,column=0)





tkinter.mainloop()