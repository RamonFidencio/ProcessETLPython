# ProcessETLPython

1 - We have three PostgreSQL database instances, I will name them instance A, instance B and instance C.
![image](https://user-images.githubusercontent.com/87341232/157033959-7ce66174-4d5d-4ea7-b37e-fba68ef735b3.png)


2 - In instance A we have the sales table and in instance B we have the tables employee and category.
![image](https://user-images.githubusercontent.com/87341232/157034082-d1935158-6b9a-472d-868d-f35aeb9b993f.png)



3 - The goal of this challenge is to create one or more tables in instance C, in the structure you find best, where these tables contain all the information of sales, employees and categories.
![image](https://user-images.githubusercontent.com/87341232/157034174-9fcb435e-7bb9-47e7-a672-6f614bdfc425.png)


4 - A requirement of this challenge is that this movement of data from instance A and B to instance C must be done on a daily basis, because you have been informed that the tables receive new data periodically and therefore the data in instance C will not be up to date.

# Version 1.0 - Ruining Local.
I chose Python and its libraries to solve this challenge, because of the low cost and processing speed for small lines.
Using the lib psycopg2 to connect on Postgres databases
For example:
## Connecting on instace_A
![image](https://user-images.githubusercontent.com/87341232/157035319-146fae12-337f-49d1-a35c-bd4cd69994f2.png)
## Connecting on instace_B
![image](https://user-images.githubusercontent.com/87341232/157035463-69e6032e-e349-411c-9206-63588724a039.png)
### PANDAS helps me to make the task more visual and process the tables more efficiently 
![image](https://user-images.githubusercontent.com/87341232/157035671-207cb185-7fd1-4fe3-8b05-9df8d146aef9.png)
## Connecting on instace_C and creating the new table
![image](https://user-images.githubusercontent.com/87341232/157036876-a5927174-aea2-4f8e-80c7-b515c7cef2fd.png)
### Inserting the data in the new table on instance_C
![image](https://user-images.githubusercontent.com/87341232/157037106-f02430ed-74a4-43a1-ae68-e00027aa8d85.png)

### At this point the above code is no longer necessary because the historical data has been entered. The next step is to keep them up to date
### I use the code: https://github.com/RamonFidencio/ProcessETLPython/blob/main/teste.py
The steps:
1- Connect on istance_C and research the biggest id entered
2- Connect on instance_B and bring the tables employees and category
3- Connect on instance_A using the largest ID from instance_C I look for the largest ones in instance_A
4- I prepare the data to be inserted in the instance_C
5- Insert on instance_C

## Used the Windows Task Scheduler to run my code every day
![image](https://user-images.githubusercontent.com/87341232/157045217-77543b2f-5a32-4194-9751-14ce7ef0a765.png)



# Version 2.0 - Runing this solution on Cloud - GCP
In version 2.0 I use Google Cloud Platarform, to run my code in a VM previously configured and scheduled to run every day for 10 minutes.
![image](https://user-images.githubusercontent.com/87341232/155524610-dc8a59d1-f6cc-42ed-83e9-7525547ab03d.png)

