# CDC_immunization
This project explores the relationships in between different vaccines and the sex, age and other basic features in the data.

Note: This project was a part of the Coursera course, "Introduction to Data Science in Python" offered by University of Michigan.

The code has 4 parts corresponding to 4 questions as seen below:

Question 1

Return the proportion of children in the dataset who had a mother with the education levels equal to less than high school (<12), high school (12), more than high school but not a college graduate (>12) and college degree.

Observation: The proportion is highest from the children of the mothers having a college degree.

Question 2

Let's explore the relationship between being fed breastmilk as a child and getting a seasonal influenza vaccine from a healthcare provider. Return a tuple of the average number of influenza vaccines for those children we know received breastmilk as a child and those who know did not.

Observation: the code returns (1.9,1.6), meaning breastfed children receive approximately 2 vaccines. However, those who were not breastfed received less number of influenza vaccine in comparison to the ones who were breastfed.

Question 3

Let's see if there is any evidence of a link between vaccine effectiveness and sex of the child. Calculate the ratio of the number of children who contracted chickenpox but were vaccinated against it (at least one varicella dose) versus those who were vaccinated but did not contract chicken pox by sex.  

Observation: The code should return (0.01,0.008). The ratio of male kids getting chickenpox even after being vaccinated is higher than for females.


Question 4

Calculate correlation between the use of the vaccine and whether it results in prevention of the infection or disease. Here, we calculate the correlation between having had the chicken pox and the number of chickenpox vaccine doses given (varicella).

Observation: The code returned 0.07 which means the correlation is very low, but however positive.

