# Life Expectancy Predictor

There have been many studies undertaken in the past which detail factors that affect life expectancy using demographic variables, income composition and mortality rates; it was found that what was lacking is the effect of immunization and HDI, these aspects were not taken into account. Past research conducted on multiple linear regression was based on a dataset of only one year for all countries. This was not as conclusive or intricate as this analysis calls for, instead, I formulated a multiple linear regression model to encompass all components, including immunization, mortality, economic, social and other health related factors, from a period of 2000-2015, in all countries. This will help countries predict areas of improvement to ameliorate the life expectancy of its population.

The dataset was obtained from kaggle.com, found on the World Health Organisation’s (WHO) repository website, its corresponding economic data was collected from the United Nations website. After considering all factors in the dataset, the following multiple linear regression equation was produced:

Life_Expectancy = -1.6*status + -0.02*adult_mortality + 0.16*infant_deaths + 0.085*alcohol + 0.00057*%_expenditure + -0.017*hepatitis_B + -0.000023*measles + 0.044*BMI + -0.13*under_five_deaths + 0.029*polio + -0.0026*total_expenditure + 0.048*diphtheria + -0.72*HIV + -0.000033*GDP + 0.000000014*population + -0.026*thinness_1-19 + -0.072*thinness_5-9 + 4.6*income_composition + 0.52*Schooling + 59.20

We can observe from the value of the coefficients that the HDI in terms of income composition of resources has the most significant impact on the life expectancy, followed by whether a country is developed/developing and HIV/AIDS deaths per 1000 live births. I disregarded population, GDP, measles and Expenditure on health as a percentage of GDP per capita, their impact was insignificant compared to the other factors.

In-terms of accuracy I was able to achieve a very reliable Root-Mean-Square Error (RMSE) value of : 4.04
