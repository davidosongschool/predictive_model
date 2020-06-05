import os
import json 
from statistics import stdev
import numpy
import matplotlib.pyplot as plt



""" Get learning data from json file """
def learn_data(): 
    with open("/Users/David/Desktop/predict/data.json", "r") as json_data:
        data = json.load(json_data)
    return data

learnData = learn_data() 
""" Get test data """ 
def test_data():
    with open("/Users/David/Desktop/predict/test.json", "r") as json_data:
        data = json.load(json_data)
        return data 

testData = test_data() 
zscores= []

# Experiment results to compare model to 
zscoresexp = [1.661149652, -0.029969195, -1.389286242, -1.442802661, -0.265441439, 1.532710245, -0.244034871, 0.661462941, -0.372474278, -0.233331588, 0.248316185, 0.398162159, 0.087766927, 1.703962787, -0.99326474]




for items in testData:
# Lets just work with one test item and then we can wrap it in a for loop """ 
        testData = items
        # We need to break down our learned data to make it more manageable - lets break down each category into its own list 
        categoryA = []
        categoryB = []
        categoryC = []

        for x in learnData: 
            if x["4"] == "category A":
                categoryA.append(x)
            elif x["4"] == "category B":
                categoryB.append(x)
            elif x["4"] == "category C":
                categoryC.append(x)

        # number of items in each category 
        sizeA = len(categoryA)
        sizeB = len(categoryB)
        sizeC = len(categoryC)



        def categoryDom(category,size):
            """ This function will return category dominance - It takes two arguments - The category and the size of the category"""
            d1= 0
            d2= 0
            d3= 0
            # Get dominance factor for Category A
            # For each dim you need to loop through the learned data and count how many times it occurs  
                # Dim One
            for y in category:
                if y["1"] == testData["1"]:
                    d1 += 1
                if y["2"] == testData["2"]:
                    d2 += 1
                if y["3"] == testData["3"]:
                    d3 += 1


            # At this point we have counts for each occurence in Category A accross all three dims
            domFact = [d1, d2, d3]

            return domFact

        def exclusiveFactor():
            """ Returns how many times each test case occurs overall """
            d1 = 0
            d2 = 0
            d3 = 0

            for y in learnData:
                if y["1"] == testData["1"]:
                    d1 += 1
                if y["2"] == testData["2"]:
                    d2 += 1
                if y["3"] == testData["3"]:
                    d3 += 1
            # At this point we have counts for each occurence in Category A accross all three dims
            exFactor = [d1, d2, d3]

            return exFactor



        # Get each category dom for text case
        domA = categoryDom(categoryA, sizeA)
        domB = categoryDom(categoryB, sizeB)
        domC = categoryDom(categoryC, sizeC)

        ex = exclusiveFactor() #Total occurence of each factor

        # Compare dominance in Category vs Dominance Overall = if they are equal them it's exclusive to that catrgory and we can double it's dominance
        count = 0
        while count < (sizeA -1):
            #CATEGORY A
            if domA[count] == ex[count]:
                domA[count] = domA[count] * 4
            #CATEGORY B
            if domB[count] == ex[count]:
                domB[count] = domB[count] * 4
            #CATEGORY C
            if domC[count] == ex[count]:
                domC[count] = domC[count] * 4
            count += 1 

        count = 0 
        while count < (sizeA - 1):
            domA[count] = domA[count] / sizeA
            domB[count] = domB[count] / sizeB
            domC[count] = domC[count] / sizeC
            count += 1

        # Average Dominance factor for each category 
        averageA = sum(domA) / len(domA)
        averageB = sum(domB) / len(domB)
        averageC = sum(domC) / len(domC)

        #Overall Average for all three categories  
        totalAverage = (averageA + averageB + averageC) / 3 

        averages = [averageA, averageB, averageC]
        #Standard deviation
        standarddev = stdev(averages)

        #Z-Scores for Category A, B, C 
        # Average A minus overall average / standard dev * 10 

        zScoreCatA = (averageA - totalAverage) / standarddev * 10
        zScoreCatB = (averageB - totalAverage) / standarddev * 10
        zScoreCatC = (averageC - totalAverage) / standarddev * 10

        answerA = ""
        answerB = ""
        answerC = ""

       
        zscores.append(zScoreCatA)
        zscores.append(zScoreCatB)
        zscores.append(zScoreCatC)

        if zScoreCatA >= 0:
            answerA = "Yes"
        else:
            answerA = "No"   

        if zScoreCatB >= 0:
            answerB = "Yes"
        else:
            answerB = "No" 

        if zScoreCatC >= 0:
            answerC = "Yes"
        else:
            answerC = "No"  


        print (f"The results for {items} are: Category A - {answerA} ... Category B - {answerB} ... Category C - {answerC}")
        

#Scatter plot 
plt.scatter(zscores, zscoresexp)
plt.show()

