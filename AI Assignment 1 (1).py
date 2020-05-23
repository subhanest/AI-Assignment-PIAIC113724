#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
path=r'C:\Users\DELL\Desktop\All Folders\PIAIC AI\Q1\Ass1 AI\StudentsPerformance.csv'
df  =pd.read_csv(path);
df


# # Converting the dataframe in more simpler Table

# In[2]:


a=df['gender'];
b=df['math score'];
c=df['reading score'];
d=df['writing score'];
e=df['parental level of education'];
from pandas import DataFrame 
Dates = {'Gender': a, 'Math S': b, 'Reading S': c,'Writing S':d, 'Parent Education':e} 
df = DataFrame(Dates, columns= ['Gender', 'Math S','Reading S','Writing S','Parent Education'])
print (df)


# In[3]:


female = df['Gender'][0] 
male   = df['Gender'][3]


# # Calculating the scores

# In[4]:


def malevsfemaleoverall():
    femalescore=0;
    malescore=0;
    i = 0;
    for i in range (0,999):
        if df['Gender'][i] == 'female':
            femalescore = femalescore + ((df['Math S'][i])+(df['Reading S'][i])+(df['Writing S'][i]))
            i = i + 1;  
    for i in range (0,999):
        if df['Gender'][i] == 'male':
            malescore = malescore + ((df['Math S'][i])+(df['Reading S'][i])+(df['Writing S'][i]))
            i = i + 1;      
    femalescore_maths=0;
    malescore_maths=0;
    i = 0;
    for i in range (0,999):
        if df['Gender'][i] == 'female':
            femalescore_maths = femalescore_maths + (df['Math S'][i])
            i = i + 1;   
    for i in range (0,999):
        if df['Gender'][i] == 'male':
            malescore_maths = malescore_maths + (df['Math S'][i])
            i = i + 1; 
    femalescore_reading=0;
    malescore_reading=0;
    i = 0;
    for i in range (0,999):
        if df['Gender'][i] == 'female':
            femalescore_reading = femalescore_reading + (df['Reading S'][i])
            i = i + 1;   
    for i in range (0,999):
        if df['Gender'][i] == 'male':
            malescore_reading = malescore_reading + (df['Reading S'][i])
            i = i + 1;
    femalescore_writing=0;
    malescore_writing=0;
    i = 0;
    for i in range (0,999):
        if df['Gender'][i] == 'female':
            femalescore_writing = femalescore_writing + (df['Writing S'][i])
            i = i + 1;   
    for i in range (0,999):
        if df['Gender'][i] == 'male':
            malescore_writing = malescore_writing + (df['Writing S'][i])
            i = i + 1;   
    p=df['Gender'].value_counts()
    avg_femalescore = (femalescore/p[0])
    avg_malescore = (malescore/p[1])
    avg_femalescore_maths = (femalescore_maths/p[0])
    avg_malescore_maths = (malescore_maths/p[1])
    avg_femalescore_reading = (femalescore_reading/p[0])
    avg_malescore_reading = (malescore_reading/p[1])
    avg_femalescore_writing = (femalescore_writing/p[0])
    avg_malescore_writing = (malescore_writing/p[1])
    if avg_femalescore > avg_malescore:
        print("");
        print("");
        print("Females overall performance is better than Males")
        print("");
        print("");
    elif avg_femalesscore < avg_malesscore:
        print("");
        print("");
        print("Males overall performance is better than Females")
        print("");
        print("");
    else:
        print("");
        print("");
        print("Same overall level of performance")
        print("");
        print("");
    if avg_femalescore_maths > avg_malescore_maths:
        print("");
        print("");
        print("Females performance is better than Males in maths")
        print("");
        print("");
    elif avg_femalescore_maths < avg_malescore_maths:
        print("");
        print("");
        print("Males performance is better than Females in maths")
        print("");
        print("");
    else:
        print("");
        print("");
        print("Same level of performance in maths")
        print("");
        print("");
    if avg_femalescore_reading > avg_malescore_reading:
        print("");
        print("");
        print("Females performance is better than Males in reading")
        print("");
        print("");
    elif avg_femalesscore_reading < avg_malesscore_reading:
        print("");
        print("");
        print("Males performance is better than Females in reading")
        print("");
        print("");
    else:
        print("");
        print("");
        print("Same level of performance in reading")
        print("");
        print("");
    if avg_femalescore_writing > avg_malescore_writing:
        print("");
        print("");
        print("Females performance is better than Males in writing")
        print("");
        print("");
    elif avg_femalesscore_writing < avg_malesscore_writing:
        print("");
        print("");
        print("Males performance is better than Females in writing")
        print("");
        print("");
    else:
        print("");
        print("");
        print("Same level of performance in writing")
        print("");
        print("");


# # Question 1 :
# Is there any difference in student score if parents have master-level education in a specified score (we will take user input for choosing the score column) ?

# In[8]:


df['Parent Education'].value_counts()


# In[9]:


bachelors_degree = df['Parent Education'][0] 
some_college     = df['Parent Education'][1]
mastes_degree    = df['Parent Education'][2]
associate_degree = df['Parent Education'][3] 
high_school      = df['Parent Education'][997]
some_high_school = 'some high school'


# In[10]:


score_maths=0;
i = 0;
for i in range (0,999):
  if df['Parent Education'][i] == mastes_degree:
      score_maths = score_maths + (df['Math S'][i])
      i = i + 1;  
score_reading=0;
i = 0;
for i in range (0,999):
  if df['Parent Education'][i] == mastes_degree:
      score_reading = score_reading + (df['Reading S'][i])
      i = i + 1;   
score_writing=0;
i = 0;
for i in range (0,999):
  if df['Parent Education'][i] == mastes_degree:
      score_writing = score_writing + (df['Writing S'][i])
      i = i + 1;


# In[11]:


Total_maths   = df['Math S'].sum()
Total_reading = df['Reading S'].sum()
Total_writing = df['Writing S'].sum()


# In[12]:


def scorerwithmasterparent(cours):
    def abcde(course):
        score=0;
        i = 0;
        if course == 'Math S':  
            score_maths=0;
            i = 0;
            for i in range (0,999):
                if df['Parent Education'][i] == mastes_degree:
                    score_maths = score_maths + (df['Math S'][i])
                    i = i + 1;  
            avg_score_math_mastes_degree = (score_maths/59);
            avg_score_math_others        = ((Total_maths-score_maths)/(226+222+196+179+118));
            if avg_score_math_mastes_degree > avg_score_math_others:
                print("");
                print("");
                print("Student with parental master degree are better performers in maths");
            elif avg_score_math_mastes_degree < avg_score_math_others:
                print("");
                print("");
                print("Student with parental master degree are inferior performers in maths");
            else:
                print("");
                print("");
                print("Same performance in maths");
        elif course == 'Reading S':
            score_reading=0;
            i = 0;
            for i in range (0,999):
                if df['Parent Education'][i] == mastes_degree:
                    score_reading = score_reading + (df['Reading S'][i])
                    i = i + 1; 
            avg_score_reading_mastes_degree = (score_reading/59);
            avg_score_reading_others        = ((Total_reading-score_reading)/(226+222+196+179+118));
            if avg_score_reading_mastes_degree > avg_score_reading_others:
                print("");
                print("");
                print("Student with parental master degree are better performers in reading");
            elif avg_score_reading_mastes_degree < avg_score_reading_others:
                print("");
                print("");
                print("Student with parental master degree are inferior performers in reading");
            else:
                print("");
                print("");
                print("Same performance in reading");
        elif course == 'Writing S':
            score_writing=0;
            i = 0;
            for i in range (0,999):
                if df['Parent Education'][i] == mastes_degree:
                    score_writing = score_writing + (df['Writing S'][i])
                    i = i + 1;
            avg_score_writing_mastes_degree = (score_writing/59);
            avg_score_writing_others        = ((Total_writing-score_writing)/(226+222+196+179+118));
            if avg_score_writing_mastes_degree > avg_score_writing_others:
                print("");
                print("");
                print("Student with parental master degree are better performers in writing");
            elif avg_score_writing_mastes_degree < avg_score_writing_others:
                print("");
                print("");
                print("Student with parental master degree are inferior performers in writing");
            else:
                print("");
                print("");
                print("Same performance in writing");
        else:
            print("");
            print("");
            print("Enter the correct course");
    if cours == "Math S":
        abcde("Math S")
    elif cours == "Reading S":
        abcde("Reading S")
    elif cours == "Writing S":
        abcde("Writing S")
    else:
        print("Looks like you entered the wrong course try any option mentioned below;");
        print("Math S , Reading S , Writing S");
        course = input ("Enter any course mentioned in the list:");
        score = 0;
        abcde(course)


# # Question 2 :
# Is there any difference in student score if parents have Bachler level education in a specified score (we will take user input for choosing the score column) ?

# In[13]:


def scorerwithbachelorparent(cours):
    def abcd(course):
        score=0;
        i = 0;
        if course == 'Math S':  
            score_maths=0;
            i = 0;
            for i in range (0,999):
                if df['Parent Education'][i] == bachelors_degree:
                    score_maths = score_maths + (df['Math S'][i])
                    i = i + 1;  
            avg_score_math_bachelors_degree = (score_maths/118);
            avg_score_math_others        = ((Total_maths-score_maths)/(226+222+196+179+59));
            if avg_score_math_bachelors_degree > avg_score_math_others:
                print("");
                print("");
                print("Student with parental bachelors degree are better performers in maths");
            elif avg_score_math_bachelors_degree < avg_score_math_others:
                print("");
                print("");
                print("Student with parental bachelors degree are inferior performers in maths");
            else:
                print("");
                print("");
                print("Same performance in maths");
        elif course == 'Reading S':
            score_reading=0;
            i = 0;
            for i in range (0,999):
                if df['Parent Education'][i] == bachelors_degree:
                    score_reading = score_reading + (df['Reading S'][i])
                    i = i + 1;   
            avg_score_reading_bachelors_degree = (score_reading/118);
            avg_score_reading_others        = ((Total_reading-score_reading)/(226+222+196+179+59));
            if avg_score_reading_bachelors_degree > avg_score_reading_others:
                print("");
                print("");
                print("Student with parental bachelors degree are better performers in reading");
            elif avg_score_reading_bachelors_degree < avg_score_reading_others:
                print("");
                print("");
                print("Student with parental bachelors degree are inferior performers in reading");
            else:
                print("");
                print("");
                print("Same performance in reading");
        elif course == 'Writing S':
            score_writing=0;
            i = 0;
            for i in range (0,999):
                if df['Parent Education'][i] == bachelors_degree:
                    score_writing = score_writing + (df['Writing S'][i])
                    i = i + 1;
            avg_score_writing_bachelors_degree = (score_writing/118);
            avg_score_writing_others = ((Total_writing-score_writing)/(226+222+196+179+59));
            if avg_score_writing_bachelors_degree > avg_score_writing_others:
                print("");
                print("");
                print("Student with parental bachelors degree are better performers in writing");
            elif avg_score_writing_bachelors_degree < avg_score_writing_others:
                print("");
                print("");
                print("Student with parental bachelors degree are inferior performers in writing");
            else:
                print("");
                print("");
                print("Same performance in writing");
        else:
            print("");
            print("");
            print("Enter the correct course");
    if cours == "Math S":
        abcd("Math S")
    elif cours == "Reading S":
        abcd("Reading S")
    elif cours == "Writing S":
        abcd("Writing S")
    else:
        print("Looks like you entered the wrong course try any option mentioned below;");
        print("Math S , Reading S , Writing S");
        course = input ("Enter any course mentioned in the list:");
        score = 0;
        abcd(course)


# # Question 3 :
# How many parents have bachelors education, master education, or some college degrees level education ?

# In[14]:


def bacmascolparentnumber():
    i1 = 0;
    i2 = 0;
    i3 = 0;
    i4 = 0;
    i  = 0;
    l  = 0;
    for i in range (0,999):
        if df['Parent Education'][i] == mastes_degree:
            i1 = i1 + 1;
        else:
            l
    for i in range (0,999):
        if df['Parent Education'][i] == bachelors_degree:
            i2 = i2 + 1;
        else:
            l
    for i in range (0,999):
        if df['Parent Education'][i] == some_college:
            i3 = i3 + 1;
        else:
            l
    i4 = i3 +i2 + i1 ;
    print("");
    print("");
    print("The parents with bachelors education, master education, or some college degrees level education are",i4);
    print("");
    print("");

# # Question 4 :
# In a user given score, is the top scorer a female or male?

# In[15]:


female = df['Gender'][0] 
male   = df['Gender'][3]


# In[16]:


def topscorer(cours):
    def abc(course):    
        a = df['Math S'].max()
        b = df['Reading S'].max()
        c = df['Writing S'].max()
        i1 = 0;
        if course == 'Math S':
            for i in range (0,999):
                if df['Math S'][i] == a:
                    i1 = i1 + 1;
                    d = df['Gender'][i1]
                    print("");
                    print("");
                    print("The top scorer in Maths is ",d); 
        elif course == 'Reading S':
            for i in range (0,999):
                if df['Reading S'][i] == b:
                    i1 = i1 + 1;
                    d = df['Gender'][i1]
                    print("");
                    print("");
                    print("The top scorer in reading is ",d);  
        elif course == 'Writing S':
            for i in range (0,999):
                if df['Writing S'][i] == c:
                    i1 = i1 + 1;
                    d = df['Gender'][i1]
                    print("");
                    print("");
                    print("The top scorer in writing is ",d); 
        else:
            print("");
            print("");
            print("Enter the correct course");
            print("");
            print("");
    if cours == "Math S":
        abc("Math S")
    elif cours == "Reading S":
        abc("Reading S")
    elif cours == "Reading S":
        abc("writing S")
    else:
        print("Looks like you entered the wrong course try any option mentioned below;");
        print("Math S , Reading S , Writing S");
        course = input ("Enter any course mentioned in the list:");
        score = 0;
        abc(course)


# # Question 5 :
# How many students have good in reading (> 75) but not good in writing( < 70) ?

# In[17]:


def studentgoodatreadingbadatwriting():  
    s = 0;
    i = 0;
    l = 0;
    for i in range (0,999):
        if df['Reading S'][i] > 75:
            if df['Writing S'][i] < 70:
                s = s + 1;
            else:
                l
        else:
            l
    print("");
    print("");
    print("Students good in reading (> 75) but not good in writing( < 70) are",s,".");
    print("");
    print("");


# In[ ]:


# All the functions are


# Foroverall: malevsfemaleoverall() 

# Question1: scorerwithmasterparent("course")

# Question2: scorerwithbachelorparent("course")

# Question3: bacmascolparentnumber()

# Question4: topscorer("course")

# Question5: studentgoodatreadingbadatwriting()

# Note : Course should be entered in string form (""). 

















