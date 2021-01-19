import statistics
import pandas as pd

df = pd.read_csv("StudentsPerformance.csv")

maths_list = df["math score"].to_list()
reading_list = df["reading score"].to_list()
writing_list = df["writing score"].to_list()

maths_mean = statistics.mean(maths_list)
maths_median = statistics.median(maths_list)
maths_mode = statistics.mode(maths_list)
maths_std_deviation = statistics.stdev(maths_list)

reading_mean = statistics.mean(reading_list)
reading_median = statistics.median(reading_list)
reading_mode = statistics.mode(reading_list)
reading_std_deviation = statistics.stdev(reading_list)

writing_mean = statistics.mean(writing_list)
writing_median = statistics.median(writing_list)
writing_mode = statistics.mode(writing_list)
writing_std_deviation = statistics.stdev(writing_list)

print("Mean, Median, Mode and Standard Deviation of the maths_score_list is {}, {}, {} and {} respectively".format(maths_mean, maths_median, maths_mode, maths_std_deviation))
print("Mean, Median, Mode and Standard Deviation of the reading_score_list is {}, {}, {} and {} respectively".format(reading_mean, reading_median, reading_mode, reading_std_deviation))
print("Mean, Median, Mode and Standard Deviation of the writing_score_list is {}, {}, {} and {} respectively".format(writing_mean, writing_median, writing_mode, writing_std_deviation))

maths_data_first_std_deviation_start, maths_data_first_std_deviation_end = maths_mean - maths_std_deviation, maths_mean + maths_std_deviation
maths_data_second_std_deviation_start, maths_data_second_std_deviation_end = maths_mean - (2*maths_std_deviation), maths_mean + (2*maths_std_deviation)
maths_data_third_std_deviation_start, maths_data_third_std_deviation_end = maths_mean - (3*maths_std_deviation), maths_mean + (3*maths_std_deviation)

list_of_maths_data_within_first_std_deviation = [result for result in maths_list if result > maths_data_first_std_deviation_start and result < maths_data_first_std_deviation_end]
print("\n{}% of data of maths_list lies within the first standard deviation".format(len(list_of_maths_data_within_first_std_deviation)*100.0 / len(maths_list)))

list_of_maths_data_within_second_std_deviation = [result for result in maths_list if result > maths_data_second_std_deviation_start and result < maths_data_second_std_deviation_end]
print("{}% of data of maths_list lies within the second standard deviation".format(len(list_of_maths_data_within_second_std_deviation)*100.0 / len(maths_list)))

list_of_maths_data_within_third_std_deviation = [result for result in maths_list if result > maths_data_third_std_deviation_start and result < maths_data_third_std_deviation_end]
print("{}% of data of maths_list lies within the third standard deviation".format(len(list_of_maths_data_within_third_std_deviation)*100.0 / len(maths_list)))




reading_data_first_std_deviation_start, reading_data_first_std_deviation_end = reading_mean - reading_std_deviation, reading_mean + reading_std_deviation
reading_data_second_std_deviation_start, reading_data_second_std_deviation_end = reading_mean - (2*reading_std_deviation), reading_mean + (2*reading_std_deviation)
reading_data_third_std_deviation_start, reading_data_third_std_deviation_end = reading_mean - (3*reading_std_deviation), reading_mean + (3*reading_std_deviation)

list_of_reading_data_within_first_std_deviation = [result for result in reading_list if result > reading_data_first_std_deviation_start and result < reading_data_first_std_deviation_end]
print("\n{}% of data of reading_list lies within the first standard deviation".format(len(list_of_reading_data_within_first_std_deviation)*100.0 / len(reading_list)))

list_of_reading_data_within_second_std_deviation = [result for result in reading_list if result > reading_data_second_std_deviation_start and result < reading_data_second_std_deviation_end]
print("{}% of data of reading_list lies within the second standard deviation".format(len(list_of_reading_data_within_second_std_deviation)*100.0 / len(reading_list)))

list_of_reading_data_within_third_std_deviation = [result for result in reading_list if result > reading_data_third_std_deviation_start and result < reading_data_third_std_deviation_end]
print("{}% of data of reading_list lies within the third standard deviation".format(len(list_of_reading_data_within_third_std_deviation)*100.0 / len(reading_list)))





writing_data_first_std_deviation_start, writing_data_first_std_deviation_end = writing_mean - writing_std_deviation, writing_mean + writing_std_deviation
writing_data_second_std_deviation_start, writing_data_second_std_deviation_end = writing_mean - (2*writing_std_deviation), writing_mean + (2*writing_std_deviation)
writing_data_third_std_deviation_start, writing_data_third_std_deviation_end = writing_mean - (3*writing_std_deviation), writing_mean + (3*writing_std_deviation)

list_of_writing_data_within_first_std_deviation = [result for result in writing_list if result > writing_data_first_std_deviation_start and result < writing_data_first_std_deviation_end]
print("\n{}% of data of writing_list lies within the first standard deviation".format(len(list_of_writing_data_within_first_std_deviation)*100.0 / len(writing_list)))

list_of_writing_data_within_second_std_deviation = [result for result in writing_list if result > writing_data_second_std_deviation_start and result < writing_data_second_std_deviation_end]
print("{}% of data of writing_list lies within the second standard deviation".format(len(list_of_writing_data_within_second_std_deviation)*100.0 / len(writing_list)))

list_of_writing_data_within_third_std_deviation = [result for result in writing_list if result > writing_data_third_std_deviation_start and result < writing_data_third_std_deviation_end]
print("{}% of data of writing_list lies within the third standard deviation".format(len(list_of_writing_data_within_third_std_deviation)*100.0 / len(writing_list)))