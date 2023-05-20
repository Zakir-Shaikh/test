from dataclasses import dataclass

import numpy as np
import matplotlib.pyplot as plt

calories_goal_limit = 3000
protein_goal_limit=180
fat_goal_limit=80
carbs_goal_limit=300

today = []


class food:
    name:str
    calories:int
    protein:int
    fat:int
    carbs:int

done = False

while not done:
    print("""
    (1) add a new food
    (2) visualize progress
    (q) Quit
    """ )

    choice=input("choose an option:")

    if choice =="1":
        print("adding a new food")
        name=input("name: ")
        calories=int(input("calories:"))
        protein = int(input("proteins:"))
        fat = int(input("fats:"))
        carbs = int(input("carbs:"))
        food=food(name ,calories ,protein ,fat ,carbs)
        print("successfully added!")
    elif choice=="2":
        calories_sum=sum(food.calories for food in today)
        protein_sum = sum(food.protein for food in today)
        fat_sum = sum(food.fat for food in today)
        carbs_sum = sum(food.carbs for food in today)

        fig,axs = plt.subplots(2,2)
        axs[0,0].pie([protein_sum,fat_sum,carbs_sum],labels=["proteins","fats","carbs"],autopct="%1.1f%%")
        axs[0,0].set_title("macronutrients distribution")
        axs[0,1].bar([0,1,2],[protein_sum,fat_sum,carbs_sum],width=0.4)
        axs[0, 1].bar([0.5, 1.5, 2.5], [protein_goal_limit, fat_goal_limit, carbs_goal_limit], width=0.4)
        axs[0,1].set_title("macronutrients progress")
        axs[1,0].pie([calories_sum,calories_goal_limit-calories_sum],labels=["calories","Remaining"],autopct="%1.1f%%")
        axs[1,0].set_title("calories goal progress")
        axs[1,1].plot(list(range(len(today))), np.cumsum([food.calories for food in today]),labels="calories eaten")
        axs[1,1].plot(list(range(len(today))),[calories_goal_limit]*len(today),labels="calrories goal")
        axs[1,1].legend()
        axs[1,1].set_title("calories goal over time")
        fig.tight_layour()
        plt.show()
    elif choice=="q":
        done=True
    else:
        print("invalid choice!")


