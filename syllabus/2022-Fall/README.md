# Fall 2022 Course Information

----------------

## [Santa Clara University](http://scu.edu/)

## [MSIS 2627: Big Data Modeling and Analytics](https://www.scu.edu/business/ms-information-systems/curriculum/msis-courses/)

-----------------

## Course Description & Objectives

* Understand the fundamentals of big data 
* Understand the fundamentals of MapReduce Paradigm
* Use PySpark (Python API to Spark) to solve big data problems
* Use SQL for NoSQL data (DataFrames in Spark and Amazon Athena)
* Understand Amazon Athena: Access Big Data by SQL

-----------------

## Course Objectives

At the completion of this course, students will be able to understand:

* What is MapReduce? Examples of MapReduce
* Elements of Big Data: Persistence, Queries, Analytics
* Distributed File System and Fault Tolerance
* Introduction to classic MapReduce Algorithms
* Understand Spark and Hadoop frameworks
* MapReduce algorithms and some design patterns
* NoSQL Databases
* Fundamentals of Spark and PySpark
* Running simple programs in PySpark
* Scale-out vs. Scale-up
* SQL for NoSQL data & Relational Algebra
* Amazon Athena and SQL

----------------
## Required books (all resources are online):

* [1. Data Algorithms with Spark by Mahmoud Parsian](https://www.oreilly.com/library/view/data-algorithms-with/9781492082378/)
* [2. Data-Intensive Text Processing with MapReduce by Jimmy Lin and Chris Dyer](http://lintool.github.io/MapReduceAlgorithms/ed1n/MapReduce-algorithms.pdf)

## Extra books (all resources are online):

* [1. PySpark Algorithms by Mahmoud Parsian](https://www.amazon.com/PySpark-Algorithms-Version-Mahmoud-Parsian-ebook/dp/B07X4B2218)
* [2. Mining of Massive Datasets by Jure Leskovec, Anand Rajaraman, Jeffrey D. Ullman](http://infolab.stanford.edu/~ullman/mmds/book0n.pdf)

------------------

## Required Software, API, and Documentation

* [Apache Spark (main site)](http://spark.apache.org)
* [PySpark API and documentation](https://spark.apache.org/docs/latest/api/python/index.html)
* [RDD Programming Guide](https://spark.apache.org/docs/latest/rdd-programming-guide.html)
* [DataFrame Programming Guide](https://spark.apache.org/docs/latest/api/python/getting_started/quickstart_df.html)

-------------------

## Tentative Course Outline

The weekly coverage might change as it depends 
on the progress of the class. However, you must 
keep up with the reading and programming assignments.

### Main Subjects

* Classic MapReduce (Jimmy Lin's Book)
	* Solve Big Data problems using `map()`, `combine()`, and `reduce()` functions
	* up to 25%

* PySpark and Spark (Mahmoud Parsian's book: Data Algorithms with Spark)
	* up to 65%

* Data Partitioning and Amazon Athena and Google BigQuery
	* up to 10%

----------------

### Session-1:  Tuesday, September 20, 2022

* [Introduction to Big Data](https://lagesoft.files.wordpress.com/2018/11/bd-introduction-to-big-data.pdf)
* [Chapter 1 of Data-Intensive Text Processing with MapReduce](http://lintool.github.io/MapReduceAlgorithms/ed1n/MapReduce-algorithms.pdf) 
* [A Very Brief Introduction to MapReduce](http://hci.stanford.edu/courses/cs448g/a2/files/map_reduce_tutorial.pdf) 
* [Introduction to MapReduce](http://lsd.ls.fi.upm.es/lsd/nuevas-tendencias-en-sistemas-distribuidos/IntroToMapReduce_2.pdf) 
* [MapReduce: Simplified Data Processing on Large Clusters by Jeffrey Dean and Sanjay Ghemawat](https://static.googleusercontent.com/media/research.google.com/en//archive/mapreduce-osdi04.pdf)

----------------

### Session-2: Thursday, September 22, 2022
	
* Introduction to Big Data 
* [MapReduce wikipedia](https://en.wikipedia.org/wiki/MapReduce)
* [A Comprehensive Study on MapReduce Applications](https://github.com/mahmoudparsian/big-data-mapreduce-course/blob/master/slides/mapreduce/A_Comprehensive_Study_on_MapReduce_Applications.pdf)
* [MapReduce Tutorial Slides by Jimmy Lin](https://cs.uwaterloo.ca/~jimmylin/publications/WWW2013-MapReduce-tutorial-slides.pdf)
* [Chapter 2 of Data-Intensive Text Processing with MapReduce](http://lintool.github.io/MapReduceAlgorithms/ed1n/MapReduce-algorithms.pdf) 
* [Introduction to MapReduce by Mahmoud Parsian](http://mapreduce4hackers.com/docs/Introduction-to-MapReduce.pdf) 
* [Introduction to MapReduce and Hadoop by Matei Zaharia](https://github.com/mahmoudparsian/big-data-mapreduce-course/blob/master/slides/mapreduce/MapReduce_by_Matei_Zaharia.pdf) 
* [MapReduce: Simplified Data Processing on Large Clusters by Jeffrey Dean and Sanjay Ghemawat](https://static.googleusercontent.com/media/research.google.com/en//archive/mapreduce-osdi04.pdf)

----------------

### Session-3: Tuesday, September 27, 2022

* [Introduction to MapReduce: Watch a Video](https://www.youtube.com/watch?v=ht3dNvdNDzI&t=250s) 
* [The Future of Big Data by Matei Zaharia -- Video](https://www.youtube.com/watch?v=oSj2vYw5RLs)   
* [1st half of Chapter 3 of Data-Intensive Text Processing with MapReduce](http://lintool.github.io/MapReduceAlgorithms/ed1n/MapReduce-algorithms.pdf)   
* [Introduction to MapReduce and Hadoop by Matei Zaharia](https://github.com/mahmoudparsian/big-data-mapreduce-course/blob/master/slides/mapreduce/MapReduce_by_Matei_Zaharia.pdf)  

----------------

### Session-4: Thursday, September 29, 2022

* Introduction to MapReduce: Watch a Video    
* [Simplifying Big Data Applications with Apache Spark 2.0 by Matei Zaharia](https://www.youtube.com/watch?v=Zb9YW8XjxnE)  
* [2nd half of Chapter 3 of Data-Intensive Text Processing with MapReduce](http://lintool.github.io/MapReduceAlgorithms/ed1n/MapReduce-algorithms.pdf) 
* [Introduction to MapReduce and Hadoop by Matei Zaharia](https://github.com/mahmoudparsian/big-data-mapreduce-course/blob/master/slides/mapreduce/MapReduce_by_Matei_Zaharia.pdf)   
* [NEW: Introduction to MapReduce](https://courses.cs.ut.ee/MTAT.08.011/2013_spring/uploads/Main/L3_MapReduce.pdf)
* [NEW: MapReduce Algorithms](https://courses.cs.ut.ee/MTAT.08.027/2018_spring/uploads/Main/L5_MapReduceAlgorithms2018.pdf)
* Classic Join in MapReduce

----------------

### Session-5: Tuesday, October 4, 2022

* Introduction to MapReduce/Spark 
* [Chapters 1, 2 of PySpark Algorithms Book by Mahmoud Parsian](https://github.com/mahmoudparsian/pyspark-algorithms) 
* [Chapter 4 of Data-Intensive Text Processing with MapReduce](http://lintool.github.io/MapReduceAlgorithms/ed1n/MapReduce-algorithms.pdf)  
* [Introduction to MapReduce and Hadoop by Matei Zaharia](https://github.com/mahmoudparsian/big-data-mapreduce-course/blob/master/slides/mapreduce/MapReduce_by_Matei_Zaharia.pdf) 

----------------

### Session-6: Thursday, October 6, 2022

* Practice MapReduce/Spark/...
* [Chapters 1, 2, 3 of PySpark Algorithms Book by Mahmoud Parsian](https://github.com/mahmoudparsian/pyspark-algorithms) 
* [Introduction to Spark](http://www.slideshare.net/jeykottalam/spark-sqlamp-camp2014)  
* [Introduction to Spark by Shannon Quinn](http://cobweb.cs.uga.edu/~squinn/mmd_s15/lectures/lecture13_mar3.pdf)  

----------------

### Session-7: Tuesday, October 11, 2022

* Spark's Nuts and Bolts    
* [Chapters 4, 5 of PySpark Algorithms Book by Mahmoud Parsian](https://github.com/mahmoudparsian/pyspark-algorithms)
* [Making Big Data Simple: by Matei Zaharia](https://www.youtube.com/watch?v=Nev1s6fHwMI) 
* [Introduction to Spark](http://www.slideshare.net/jeykottalam/spark-sqlamp-camp2014)  
* [Parallel-Programming-With-Spark-Matei-Zaharia](http://ampcamp.berkeley.edu/wp-content/uploads/2013/02/Parallel-Programming-With-Spark-Matei-Zaharia-Strata-2013.pptx) 

----------------

### Session-8: Thursday, October 13, 2022

* MapReduce Design Patterns
* MinMax  
* Top-10  
* [Chapters 4, 5, 6 of PySpark Algorithms Book by Mahmoud Parsian](https://github.com/mahmoudparsian/pyspark-algorithms) 
* [Chapter 3, 4 of Data-Intensive Text Processing with MapReduce](http://lintool.github.io/MapReduceAlgorithms/ed1n/MapReduce-algorithms.pdf)  

----------------

### Session-9: Tuesday, October 18, 2022

* MapReduce Design Patterns: InMapper Combiner, mapPartitions
* Top-10 Algorithm   
* MinMax Algorithm  
* [Chapters 4, 6, 7, 12 of PySpark Algorithms Book by Mahmoud Parsian](https://github.com/mahmoudparsian/pyspark-algorithms)

----------------

### Session-10: Thursday, October 20, 2022

* Spark's RDD Partitioning
* Spark's `mapPartitions()` Transformation
* Review reducers: `groupByKey()` and `reduceByKey()`
* Review `mapPartitions()` Transformation
----------------

### Session-11: Tuesday, October 25, 2022
	
* Review Midterm Exam, 
* Q/A session 
	
----------------
### Session-12: Tuesday, October 27, 2022
	
* Midterm Exam: closed book/notes/friend/internet/software

----------------
### Session-13: Tuesday, November 1, 2022
	
* Midterm Exam Discussion and Review

----------------

### Session-14: Thursday, November 3, 2022
	
* Spark's DataFrames (1)
* [Chapters 4, 6, 7, 12 of PySpark Algorithms Book by Mahmoud Parsian](https://github.com/mahmoudparsian/pyspark-algorithms)
* [Video: Structuring Spark: SQL, DataFrames, Datasets And Streaming - 28 mins](https://www.youtube.com/watch?v=1a4pgYzeFwE)

----------------
### Session-15: Thursday, November 8, 2022
	
* Spark's DataFrames (2)
* [Chapters 4, 6, 7, 12 of PySpark Algorithms Book by Mahmoud Parsian](https://github.com/mahmoudparsian/pyspark-algorithms)
* [Video: Structuring Spark: SQL, DataFrames, Datasets And Streaming - 28 mins](https://www.youtube.com/watch?v=1a4pgYzeFwE)

----------------
### Session-16: Tuesday, November 10, 2022
	
* MapReduce Design Pattern: Graph Algorithms 
* [Chapters 11 of PySpark Algorithms Book by Mahmoud Parsian](https://github.com/mahmoudparsian/pyspark-algorithms)
 
----------------
### Session-17: Tuesday, November 15, 2022
	
* MapReduce Design Pattern: Graph Algorithms 
* [Chapters 11 of PySpark Algorithms Book by Mahmoud Parsian](https://github.com/mahmoudparsian/pyspark-algorithms)
 
----------------

### Session-18: Thursday, November 17, 2022
	
* Introduction to Serverless Analytics  
* SQL Access: Amazon Athena 
* SQL Access: Google BigQuery 	

----------------

### Session-19: Thursday, November 29, 2022
	
* Introduction to Serverless Analytics  
* SQL Access: Amazon Athena 
* SQL Access: Google BigQuery 	
* Relational Algebra and Big Data  
* SQL Access to Big Data  


----------------

### Session-20: Thursday, December 1, 2022
	
* Review for Final Exam 
* Q/A session 

----------------

### Session-21: Final Exam 
	
* Date: TBDL, 2022

----------------
