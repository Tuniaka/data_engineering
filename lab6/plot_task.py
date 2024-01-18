import os
from optimization import *
import pandas as pd
from plots import *

def task_ex(name, number, colums):
    print(f"Execution {number}")
    filename = name
    filesize = os.path.getsize(filename)
    print(f'Size on disk = {filesize // (1024 ** 2)} MB')

    dataset = pd.read_csv(filename)
    os.makedirs(f'lab6/result/task{number}', exist_ok=True)
    get_memory_stat(dataset, f'lab6/result/task{number}/stat.json')
    optimized_dataset = optimize_dataset(dataset)
    get_memory_stat(optimize_dataset(dataset), f'lab6/result/task{number}/stat_optimized.json')

    column_types = {}
    use_columns = colums
                
    for key in use_columns:
        column_types[key] = optimized_dataset.dtypes[key]

    with open(f'lab6/result/task{number}/dtypes.json', 'w', encoding='utf-8') as file:
        file.write(json.dumps(column_types,  default=str))

    df = pd.DataFrame()
    for chunck in pd.read_csv(filename,
                            usecols=colums,
                            dtype=column_types,
                            chunksize=1000000,
                            index_col=False, 
                            low_memory=False):
        df = pd.concat([df, chunck], ignore_index=True)
        chunck.to_csv(f'lab6/result/task{number}/dataframe.csv', mode='a', header=True)
        return df


if __name__ == "__main__":
    f_names = ["lab6/data/[1]game_logs.csv","lab6/data/CIS_Automotive_Kaggle_Sample.csv","lab6/data/[3]flights.csv",
           "lab6/data/vacancies_2020.csv","lab6/data/dataset.csv"]
    f_colums = [["v_game_number","h_score", "v_score","v_line_score","h_line_score",
                "v_at_bats","v_hits","v_homeruns","v_rbi","v_walks"],
                ["firstSeen", "lastSeen","stockNum", "msrp", "askPrice", "dealerID", "mileage", 
                "isNew","vf_FuelTypePrimary", "vf_FuelTypeSecondary"],
                ["YEAR","MONTH","DAY","DAY_OF_WEEK","AIRLINE","FLIGHT_NUMBER","DEPARTURE_TIME",
                "WHEELS_ON", "TAXI_IN", "WEATHER_DELAY"],
                ["id", "key_skills", "schedule_name", "experience_id", "experience_name",
                'employer_id', 'salary_from', 'salary_to', 'type_name', 'accept_incomplete_resumes'],
                ["spkid", "name", "class", "diameter", "albedo","e","a","q","i","om"]]
    
    # for i in range(0,len(f_names)):
    #     task_ex(f_names[i],i+1,f_colums[i])

    # task1
    # df1 = task_ex(f_names[0],0+1,f_colums[0])
    # linear_plot(df1, 'v_score', 'h_score', 'plot1', 'lab6/result/task1/1.png')
    # bar_plot(df1, 'v_game_number', 'h_score', 'plot2', 'lab6/result/task1/2.png')
    # plot_step(df1,'v_homeruns', 'v_game_number', 'plot3', 'lab6/result/task1/3.png')
    # scatter_plot(df1,"v_rbi","v_walks", 'plot4', 'lab6/result/task1/4.png')
    # plot_histogram(df1,"v_hits","v_at_bats",'plot5','lab6/result/task1/5.png')

    # task2
    # df2 = task_ex(f_names[1],1+1,f_colums[1])
    # linear_plot(df2, "dealerID", "mileage", 'plot1', 'lab6/result/task2/1.png')
    # bar_plot(df2, "vf_FuelTypeSecondary", "askPrice", 'plot2', 'lab6/result/task2/2.png')
    # plot_step(df2, "vf_FuelTypePrimary", "askPrice", 'plot3', 'lab6/result/task2/3.png')

    # scatter_plot(df2, "firstSeen", "lastSeen", 'plot1', 'lab6/result/task4/1_1.png')
    # scatter_plot(df2, "lastSeen","stockNum", 'plot1', 'lab6/result/task4/1_2.png')
    # scatter_plot(df2, "stockNum", "msrp", 'plot1', 'lab6/result/task4/1_3.png')
    # scatter_plot(df2, "msrp", "askPrice", 'plot1', 'lab6/result/task4/1_4.png')
    # scatter_plot(df2, "askPrice", "dealerID", 'plot1', 'lab6/result/task4/1_5.png')
    # scatter_plot(df2, "dealerID", "mileage", 'plot1', 'lab6/result/task4/1_6.png')
    # scatter_plot(df2, "mileage", "isNew", 'plot1', 'lab6/result/task4/1_7.png')
    # scatter_plot(df2, "isNew","vf_FuelTypePrimary", 'plot1', 'lab6/result/task4/1_8.png')
    # scatter_plot(df2, "vf_FuelTypePrimary", "vf_FuelTypeSecondary", 'plot1', 'lab6/result/task4/1_9.png')
    # scatter_plot(df2, "lastSeen","firstSeen", 'plot1', 'lab6/result/task4/1_10.png')
    # scatter_plot(df2, "lastSeen","msrp", 'plot1', 'lab6/result/task4/1_11.png')
    # scatter_plot(df2, "lastSeen","askPrice", 'plot1', 'lab6/result/task4/1_12.png')
    # scatter_plot(df2, "lastSeen","mileage", 'plot1', 'lab6/result/task4/1_13.png')
    # scatter_plot(df2, "lastSeen","vf_FuelTypePrimary", 'plot1', 'lab6/result/task4/1_14.png')

    # plot_histogram(df2, "firstSeen", "lastSeen", 'plot1', 'lab6/result/task5/1_1.png')
    # plot_histogram(df2, "lastSeen","stockNum", 'plot1', 'lab6/result/task5/1_2.png')
    # plot_histogram(df2, "stockNum", "msrp", 'plot1', 'lab6/result/task5/1_3.png')
    # plot_histogram(df2, "msrp", "askPrice", 'plot1', 'lab6/result/task5/1_4.png')
    # plot_histogram(df2, "askPrice", "dealerID", 'plot1', 'lab6/result/task5/1_5.png')
    # plot_histogram(df2, "dealerID", "mileage", 'plot1', 'lab6/result/task5/1_6.png')
    # plot_histogram(df2, "mileage", "isNew", 'plot1', 'lab6/result/task5/1_7.png')
    # plot_histogram(df2, "isNew","vf_FuelTypePrimary", 'plot1', 'lab6/result/task5/1_8.png')
    # plot_histogram(df2, "vf_FuelTypePrimary", "vf_FuelTypeSecondary", 'plot1', 'lab6/result/task5/1_9.png')
    # plot_histogram(df2, "lastSeen","firstSeen", 'plot1', 'lab6/result/task5/1_10.png')
    # plot_histogram(df2, "lastSeen","msrp", 'plot1', 'lab6/result/task5/1_11.png')
    # plot_histogram(df2, "lastSeen","askPrice", 'plot1', 'lab6/result/task5/1_12.png')
    # plot_histogram(df2, "lastSeen","mileage", 'plot1', 'lab6/result/task5/1_13.png')
    # plot_histogram(df2, "lastSeen","vf_FuelTypePrimary", 'plot1', 'lab6/result/task5/1_14.png')

    #  task3
    # df3 = task_ex(f_names[2],2+1,f_colums[2])
    # linear_plot(df3, "AIRLINE", "FLIGHT_NUMBER", 'plot1', 'lab6/result/task3/1.png')
    # bar_plot(df3, "MONTH","DAY", 'plot2', 'lab6/result/task3/2.png')
    # plot_step(df3, "DEPARTURE_TIME", "WHEELS_ON", 'plot3', 'lab6/result/task3/3.png')
    # scatter_plot(df3, "TAXI_IN","WEATHER_DELAY", 'plot4', 'lab6/result/task3/4.png')
    # plot_histogram(df3, "DEPARTURE_TIME","FLIGHT_NUMBER", 'plot5', 'lab6/result/task3/5.png')

    # task4
    df4 = task_ex(f_names[3],3+1,f_colums[3])
    # linear_plot(df4, "id", "salary_from", 'plot1', 'lab6/result/task4/1.png')
    # linear_plot(df4, "id", "salary_to", 'plot2', 'lab6/result/task4/2.png')
    # plot_step(df4, "experience_id", "accept_incomplete_resumes", 'plot3', 'lab6/result/task4/3.png')
    # scatter_plot(df4, "salary_from","salary_to", 'plot4', 'lab6/result/task4/4.png')
    # plot_histogram(df4, "id", "employer_id", 'plot5', 'lab6/result/task4/5.png')
    
    
    # task5
    # df5 = task_ex(f_names[4],4+1,f_colums[4])
    # linear_plot(df5, "diameter", "albedo", 'plot1', 'lab6/result/task5/1.png')
    # bar_plot(df5, "class", "albedo", 'plot2', 'lab6/result/task5/2.png')
    # plot_step(df5, "spkid", "class", 'plot3', 'lab6/result/task5/3.png')
    # scatter_plot(df5, "diameter","om", 'plot4', 'lab6/result/task5/4.png')
    # plot_histogram(df5, "spkid", "diameter", 'plot5', 'lab6/result/task5/5.png')

