#! /usr/local/bin/python

import tweepy, time, sys, subprocess, pandas as pd, numpy as np
import random
 
CONSUMER_KEY = 'M6czSJa9ZHpQfZieLx7ZADzon'#keep the quotes, replace this with your consumer key
CONSUMER_SECRET = 'OxsgRd8TK9ey3jzXztPk478xKOQjI8KTsoac0xVeKT3lycjUDx'#keep the quotes, replace this with your consumer secret key
ACCESS_KEY = '972236811043880961-Krd17Uom7jxjStqdg1AtL6fhzHFoX3d7'#keep the quotes, replace this with your access token
ACCESS_SECRET = 'gsubSl1lFoQ3Tkp1AeLmHDECsGsGYU9dzNlRQch1Y2jOb'#keep the quotes, replace this with your access token secret
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)


# insert salad stuff here
greens = ["Romaine", "Kale", "Arugula", "Mixed Greens", "Baby Spinach"]
toppings = ["alfalfa sprouts", "bean sprouts", "beets", "black beans", "black olives", "broccoli", "carrots", "celery", "crispy onions",
            "crispy wontons", "corn", "cucumbers", "edamame", "garbanzo beans", "granny smith apples", "grape tomatoes", "hard boiled egg",
            "house croutons", "house pita chip", "jalapenos", "jicama", "kidney beans", "mandarin orange", "peanuts", "pepperoncinis", "purple cabbage",
          "rainbow rotelli pasta", "raisins", "red bell peppers", "red onions", "sauteed mushrooms", "sunflower seeds", "tortilla strips"]


meats = ["bbq chicken", "crispy bacon", "buffalo chicken", "curry chicken", "grilled chicken", "grilled steak", "pesto chicken", "roasted turkey breast"]

premium_toppings = ["artichoke hearts", "asparagus", "avocado", "baked tofu",
"candied walnuts", "dried cherries", "dried cranberries", "hummus", "quinoa",
"roasted almonds", "snow peas"]


cheeses = ["cheddar cheese", "crumbled feta", "mozzarella", "shredded parmesan", "crumbled blue cheese", "goat cheese", "pepper jack cheese"]

dressing = ["balsamic vinaigrette", "blue cheese", "honey mustard", "ranch",
"BBQ ranch", "caesar", "italian", "cilantro lime vinaigrette", "horseradish",
"sweet waldorf", "wasabi", "far east", "pesto vinaigrette", "tahini", "whole grain dijon",
"honey chipotle vinaigrette", "spicy chipotle", "thai peanut", 
"balsamic vinegar", "buffalo sauce", "honey curry", "pomegranate vinaigrette",
"BBQ sauce", "creamy dill", "lemon juice", "red wine vinegar", "olive oil",
"sriracha", "tapatio"]


toppings_out = random.sample(toppings, 7)
premium_toppings_out = random.sample(premium_toppings,2)

mns_salad = ["Base of ", random.sample(greens,1)[0]," with ", random.sample(meats,1)[0], ", ",toppings_out[0],", ", 
               toppings_out[1],", ", toppings_out[2],", ",
         toppings_out[3],", ", toppings_out[4],", ", random.sample(cheeses,1)[0],", and ", random.sample(dressing,1)[0], " dressing"]

veggie_salad = ["Base of ",random.sample(greens,1)[0]," with ", premium_toppings_out[0],", ", premium_toppings_out[1],", ", toppings_out[0],", ", toppings_out[1],", ", toppings_out[2],", ",
         toppings_out[3],", ", toppings_out[4], ", ", toppings_out[5], ", ", random.sample(cheeses,1)[0], 
         ", and ", random.sample(dressing,1)[0], " dressing"]


mns_salad_no_cheese = ["Base of ", random.sample(greens,1)[0]," with ", random.sample(meats,1)[0], ", ",toppings_out[0],", ", 
               toppings_out[1],", ", toppings_out[2],", ",
         toppings_out[3],", ", toppings_out[4], ", and ", random.sample(dressing,1)[0], " dressing"]


veggie_salad_no_cheese = ["Base of ",random.sample(greens,1)[0]," with ", premium_toppings_out[0],", ", premium_toppings_out[1],", ", toppings_out[0],", ", toppings_out[1],", ", toppings_out[2],", ",
         toppings_out[3],", ", toppings_out[4], ", ", toppings_out[5],
         ", and ", random.sample(dressing,1)[0], " dressing"]

def salad():
    number = random.randint(1,4)
    if number == 1:
        salad = mns_salad
    elif number ==2:
        salad = veggie_salad
    elif number ==3:
        salad = mns_salad_no_cheese
    elif number ==4:
        salad = veggie_salad_no_cheese
    return("".join(salad) + ' #SimplySalad #RandomSalad')

api.update_status(salad())
