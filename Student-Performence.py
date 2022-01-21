import pandas as pd 
import statistics
import csv

df = pd.read_csv("StudentsPerformence.csv")
student_list = df["Education"].to_list()


#Finding the mean 
student_mean = statistics.mean(student_list)

#Finding the median
student_median = statistics.median(studentt_list)

#Finding the mode 
student_mode = statistics.mode(student_list)

print("Mean, Median and Mode of student  is {}, {} and {} respectively".format(height_mean,student_median,student_mode))


#Finding the Std
height_std_deviation = statistics.stdev(student_list)


# For Performence 
height_first_std_deviation_start,student_first_std_deviation_end = mean -height_std_deviation, mean+height_std_deviation
height_second_std_deviation_start,student_second_std_deviation_end = mean - (2*height_std_deviation), mean + (2*height_std_deviation)
height_third_std_deviation_start,height_third_std_deviation_end = mean -(3*height_std_deviation),mean +(3*height_std_deviation)



#Printing the findings
height_list_of_data_within_1_std_deviation = [result for result in dice_result if result >student_first_std_deviation_start and result <student_first_std_deviation_end]
height_list_of_data_within_2_std_deviation = [result for result in dice_result if result >student_second_std_deviation_start and result <student_second_std_deviation_end]
height_list_of_data_within_3_std_deviation = [result for result in dice_result if result >student_third_std_deviation_start and result <student_third_std_deviation_end]



print("{}% of data for student lies within 1 standard deviation".format(len(height_list_of_data_within_1_std_deviation)*100.0/len(height_list)))
print("{}% of data for student lies within 2 standard deviations".format(len(height_list_of_data_within_2_std_deviation)*100.0/len(height_list)))
print("{}% of data for student lies within 3 standard deviations".format(len(height_list_of_data_within_3_std_deviation)*100.0/len(height_list)))


