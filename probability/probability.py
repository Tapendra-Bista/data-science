
#* #* Defination
#* Probability is the likelihood of an event occuring.
#* This event can be any things

#* #* formula
#* p(x) = preferred outcomes/ sample space
#* * preferred outcomes--> it is an outcomes we are interested 
#* * sample space--> all possible out comes that can be occur 
 

#* #* Probability of two independent events
#* p(X) = product of event 1 . event 2 i.e multiplication p of event 1 and p of event 2


#* #* Trial--> Observing an event occur and recording the outcomes
#* Example flipping a coin and recording the outcome.

#* #* Experimental Probability--> The Probability of an event which is based on Experimental we conduct
#* Example flipping a coin 20 times and recording the 20 individual outcomes

#* #* Expected value--> The specific outcome we Expect to occur when we run an Experiment
#* it can be numerical ,boolean , categorial or other 
#* #* formula

#* Expected value for categorial variables
#* E(X)= n.p
#* Where
#* n (Number of Trials)
#* p (Probability of Success)

#* Expected value of numeric variables
#* E(X) = Σ Xi  . pi 
#* where i=1 and n


#* #*---------Complements-----------------

#* denote with apostrope
#* A' = Not a

#* Characteristics 

#* A + A' = Sample space
#* p(A) + p(A') = 1
#* (A')' = A 

#* Example 
#* P(A) = 0.25
#* Then p(A') = 1- 0.25 = 0.75


#* #*------------------- Permutations---------------------
#* #* Permutations represent the number  of different possible ways  we can arrange a number of elements.
#* P(n) = factorial of n 

#* #* Characteristics
#* Arranging all elements within the sample space.
#* No repetion

#* Example :
#* if we need to arrange 5 people , we would have p(5)
#* = 5! = 5*4*3*2*1


#* #*-------------------- Variations----------------------
#* Variations represent the number of different possible ways we can pick and arrange a number of elements .


#* #* Variations with repetion
#* #* repetion allowed 
#* #* we need Permutations too
#* #* and total different elements too

#* V(n,p) =  n ko power P

#* #* Variations without repetion 
#* V(n,p) = n! / (n-p)!

#* #* Combinations represent the number of different possible ways we can pick a number elements
#* C(n,p) = n!/ (n-p)!p!

#* #* ------------Combinations with separate sample spaces----------------
#* C = n1 * n2 * np


#* Example 
#* Winning the Lottery
#* To win the lottery, you need to satisfy two distinct independent events:
#* • Correctly guess the “Powerball” number. (From 1 to 26)
#* • Correctly guess the 5 regular numbers. (From 1 to 69)
#* 𝐶 =
#* 69!
#* 64! 5!
#* × 26
#* Total number of
#* Combinations
#* Intuition behind the formula:
#* • We consider the two distinct events as a combination of two elements with different sample sizes.
#* • One event has a sample size of 26, the other has a sample size of 𝐶5
#* 69
#* .
#* • Using the “favoured over all” formula, we find the probability of any single ticket winning equals 1/(
#* 69!
#* 64!5!
#* × 26).
#* 𝐶5 𝑛𝑢𝑚𝑏𝑒𝑟𝑠
#* 𝐶𝑃𝑜𝑤𝑒𝑟𝑏𝑎𝑙𝑙 𝑛𝑢𝑚𝑏𝑒�


#* #*------------------- Combinations with repetition--------------------

#* C(n,p) = (n+p-1)! / (n-1)! p!



#* #* Question related it 

#* 1. Imagine you are working at an office and have 5 tasks labelled as “Critical” in Jira to complete by the
#* end of the day. In how many ways can you complete said tasks before the day ends?
#* ** “Jira” is a Project Management software which allows you to create tasks and label them
#* depending on their importance. “Critical” is the highest level of importance and no task with a
#* lower-level can be started once such a task is initiated


#* without reputattion 
#* Answer --->  We have to find  Permutations  and we know that formula Permutations is 
#* factorial total number here n = 5
#* Answer be 125


#* Imagine your company is trying to gain customers by running an online ad campaign. The idea is to
#* focus on a certain demographic which frequently uses social media. Your campaign will run ads on
#* Facebook, Messenger, Instagram, Twitter and Reddit. Your graphical designers have created 8
#* different versions of the banner you can use. Based on this information:

#* a) Calculate how many different options you have for the entire campaign, assuming you want
#* to use a different one for each platform.
#* ==== Answer -----------> Variation nikaldai when repetation not allowed 
#* Given 
#* Number of total banner = 8
#* Number of total platform = 5  (Permutations)
#* different options =  n! / (n-p)! = 8! / 3!




#* b) Calculate how many different options you have for the entire campaign, assuming you can
#* use the same banner for some or all the platforms.
#* ==== Answer ----------->Variation nikaldai when repetation  allowed 
#* Given 
#* Number of total banner = 8
#* Number of total platform = 5  (Permutations)
#* different options =  8 pow 5 


#* c) Calculate how many ways we can pick which of the 8 banners to use,
#*  assuming we use
#* different ones for each platform.
#* ==== Answer -----------> 


#* d) Calculate how many ways we can pick which of the 8 banners to use,
#*  assuming we can use
#* each one multiple times.
#* ==== Answer -----------> 








#* #*----------------------- Distributions------------------
#* #* Notation
#* Y -> The actual outcome of an event
#* y -> One of the possible outcomes
#* P(Y=y) or p(Y)

#* #* Example
#* Y -> The number of red marbles we draw out of a bag
#* y -> may be 3

#* P(y) is a probability function

#* #* Characteristics
#* mean -> average value  -> µ
#* variance -> how spread out the data is -> σ^2

#* #* Population vs Sample

#* Population data      vs    Sample  data
  
#* "all" the data             just a part of it 

#*                            Entire department
#* Population of the department               Sample of the whole company

#* #* different Notation
#* sample mean --> x̄
#* sample  variance --> S^2

#* #* Standard deviation -> square root of variance  

#* #* mean and variance
#* a constant  relationship between mean and variance is  
#*  sample variance       (σ^2) = E ((Y - µ)^2) = E (Y^2 ) - µ^2
#*  E -> Expected value 



#* #* Types of Distributions 


#* #*   New topics 

#* A Distribution shows the poossible values a random variabl can take and how frequently they occur .


#* #* importance Notation for Distribution
#* Y is an actual outcome
#* y is one of the possible outcomes

#* P(Y == Y) is equivalent to p (y).

#* we call a function that assigns a probability to each distinct
#* outcome in the sample space, a probability
#* function
#* ---------------------------------------|--------------| 
#*                       | Population    | Sample  
#* -----------------------|-------------- |--------------|
#* Mean                   |    miu        | x̄            |
#* Variance               |   sigma square| S square    |
#* Standard Deviation     |   sigma       | s            |
#*                        |               |              |
#* -------------------------------------------------------
         

#* Characteristtis of discrete  distrubtion probability 
#* Peculiarity 
#* p(Y   is less and equal to y) = P[Y < (y+1)]
#* For example 
#* P(❤️_<_ 3) = P(❤️< 4)
#* 
#* 
#* Uniform Distribution 
#*  Notation is U
#* U(a,b)
#* X ~   U(3,7) 
#* Here every case have equal probability of outcomes like in rolling dice every 6 case have equal probability of outcomes
#* p(a) = p(b)
#* 
#* Another Example 
#* Suppose, we have three chocolate and
#* X =>  Choosing a specific chocolate 
#*  X ~ U(3)  #*         

#*
#*             Discrete                           
#* . Have a finite number of outcomes 
#* . Expected Values might be unattainable 
#* 
#* 
#* 
#*               Continuous 
#* Have infinitely many consecutive possible values 
#* Can be expressed with a graph or a continous funnction
#* Graph consists of a smooth curve
#*                                            #*


#*
#* Discrete Distributions
#* 
#* Discrete Distributions have finitely many different possible outcomes.
#* They posses several key  characteristics which separate them from continuous ones.
#* 
#* Key Characteristics of discrete distribution 
#* . Have a finite number of outcomes 
#* . Use formulas we already talked about 
#* . Can be expressed with a table, graph or a piece-wise function 
#* . Expected  Values might be untainable 
#* . Graph consists of bars lined up one after the other 
#*  P(Y _<_ y)= P(Y _<_ Y+1)
#*  fOR example of it 
#*  p(Y_<_ 3) = p(Y  <  4)
#*  




#* Eaxmple  of Discrete Distributions
#* 1. Discrete Uniform Distribution 
#* 2. Bernoulli Distribution
#* 3. Binomial Distribution
#* 4. Poisson Distribution#*

#*
#*      Uniform Distribution 
#* 
#* A distribution where  all the outcomes are equally likely  is called a Uniform Distribution
#* 
#* Notation: 
#*  Y ~ U(a,b)
#* * alternatively, if the values are categorical, we simply indicate the number of categories, like so: Y~U(a) 
#* 
#* 
#* 
#* Key Characteristics 
#* 1. All outcomes are equally  likely. 
#* 2. All the bars on the  graph are equally tall.
#* 3. The expected value and  variance have no  predictive power.
#* 
#* 
#* Example and users:
#* Outcomes of rolling a single die.
#* Often used in shuffling algorithms due to its fairness
#* 
#* 
#* Bernoulli Distribution 
#* 
#*
#*A distribution consisting of a single trial and only two possible oucomes -success or failure is called a Bernoulli Distribution
#* 
#*Notation:
#* Y~  Bern(p)
#* 
#* 
#*Key characteristics 
#* 1. One trial
#* 2. Two possible outcomes
#* 3. E(Y) = p
#* 4. Var (Y) = p X (1-p)   
#* 
#* 
#* Example and uses: 
#* Guessing a single True/False question.
#* Often used in when trying to determine what we expect to get out a single trial of an experiment.
#* 
#* 
#* Binomial Distribution 
#* A sequence of identical Bernoulli events is called Binomial and follows a  Binomial Distribution 
#* 
#* 
#*TODO Notation 
#* Y~ B(n,p) 
#* 
#* 
#* Key characteristics 
#* 1. Measures the frequency of occurence of one  of the possible outcomes over the n trials 
#* 2. P(Y=y) = C(y,n) X p pow y X (1-p) pow (n-y)
#* 3. E(Y) = nXp
#* 4. Var(Y) = n X p X (1-p)
#* 
#*
#*! Example and uses:
#* Determine how many  times we expect  to get a heads if we flip a coin 10 times.
#* * Often used when trying to predict how likely an event is to occur over a series of trials  
#* 
#* 
#**Poisson Distribution 
#* 
#*? When we want ton know the likelihood of a certain event occuring over a given interval of time or distance , we use a poisson Distribution 
#* 
#* 
#*? Notation 
#*?  Y~ Po(alpha)
#* 
#*? Key Characteristics 
#*? 1. Measures the frequency over an an interval of time or distance 
#*? 2. P(Y=y) = alpha*y* e ko power -alpha divide y!
#*? 3. E(Y) = alpha 
#*? 4. Var (Y) = alpha  #*

#*? Example and uses:
#*Used to determine how  likely  a specific outcome is,
#*Knowing how often the event usually occurs. 
#*Often incorporated in marketing analysis to determine whether above average visits are out of 
#* the ordinary out.


#! Continous Distributions
#* If the possible values a random variable can take are a sequence of infinitely many consecutive values, we are dealing with a continuous distribution


#*  Key characteristics
#* Have infinitely  many  consecutive possible values.
#* Cannot add up the individual values that make up an interval because there are infinitely many of them.
#* Can be expressed with a graph or a continuous function. Cannot use a table,be
#* Graph consists of a smooth curve.
#* To Calculate the likelihood of an interval, we need integrals.
#* They have important CDFs.
#* p(Y=y) =0 for any individual value y.
#* p(Y<y) = p(Y_<_ y)


#! Normal  Distribution 

#* Notation 
#* . Y~ N(µ,sigma square)

#* Key characteristics 
# Its graph is bell-shaped  curve, symmetric and has thin tails.
# E(Y) = µ 
# Var (Y) = sigma square
# 68% of all its value should fall in the interval:
                # .(µ-sigma, µ+sigma)



#* Example and uses:
# Often observed in the size of animals in the wilderness.
# Could be standardized to use the Z-table.                


#! Standardizing a Normal Distribution
# To standardize any normal distribution we need to transform it so that the mean is 0 and variance and standard deviation are 1.
# Using a transformation to create a new random vaibale z.
# Ensures mean is 0.
# Ensures standard deviation is 1.

#    z =  (y-µ)/sigma 

#* Importance of the Standard Normal Distribution.
# The new variable z, represents how many  standard  deviations away from the mean, each corresponding value is.
# We can transform any Normal Distribution into a Standard Normal Distribution using the transformation shown above.
# Convenient to use because of a table of known values for its CDF, called the Z-score table, or sinply the Z-table.



#! Students'  T Distribution 
# A Normal Distribution represents a small size approximation of a Normal Distribution.

#* Notation 
# Y~ t(K)


#* Key characteristics
# 1. A small sample  size  approximation of a Normal Distribution.
# 2. Its graph is bell-shaped curve, symmetric, but has fat tails.
# 3. Accounts for extreme values better than a Normal Distribution.
# 4. If k>2: E(Y)= µ and Var(Y) = s^2 X k/(k-2)


#* Example and uses:
# Often used  in analysis when examining small sample of data that usually follows a Normal Distribution.


#! Chi-Squared Distribution 
# A Chi-Squared distribution  is often used in hypothesis testing and constructing confidence intervals.


#* Notation:
# Y~ Chi-squared (k) or Y~ X^2 (k)


#* Key Characteristics:
# Its graph is asymmetric and skewed to the right.
# E(Y) = K
# Var (Y) = 2k
# The Chi-Squared distribution is the square of then t-distribution

#* Example and uses:
# Often used to test goodness of fit.
# Contains a table of known values for its CDF, called the Chi-Squared table.The only difference is the table shows what part of the table is to the right of a given value, not to the left as in the Z-table.
# Often used in hypothesis testing and constructing confidence intervals.



#! Exponential Distribution
# The Exponential Distribution is usually observed in events which significantly chnage early on.

#* Notation:
# Y~ Exp(lambda)

#* Key Characteristics:
# Both the PDF and CDF are  plateau after a certain point.
# E(Y) = 1/lambda
# Var(Y) = 1/lambda square
# WE often use natural logarithms to transform the values of such  distributions 
# since of such distributions  since we do not have a table  of known values like the Normal or Chi-Squared

#* Example and uses:
# Often used with dynamically changing varibles, like stock prices, online website traffic, and etc.



#! Logistic Distribution
# The Continuous Logistic Distribution is observed when  trying to determine how continuous variable inputs can affect the probability of a binary outcome.

#* Notation:
# Y~ Logistic(µ,s)

#* Key Characteristics:
# E(Y) = µ
# Var(Y) = s square X pi square / 3
# The CDF picks up when we reach values near the mean.
# The smaller the scale parameter, the quicker it reaches values close to 1.

#* Example and uses:
# Often used in sports to anticipate how a player's  or team's performance can affect the probability of winning a game.
# Often used in machine learning classification problems.   