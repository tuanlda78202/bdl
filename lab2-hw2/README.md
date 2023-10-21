# Lab 02 - Homework 2

## Setup

1. Pull data and code from main repository
```bash
docker cp lab2-hw2/data-l2hw2.txt namenode:/opt
docker cp lab2-hw2/ namenode:/root
```

2. Put data HDFS 
```bash
root@namenode-master:/opt hdfs dfs -mkdir -p /user/root/l2hw2-r1/input
root@namenode-master:/opt hdfs dfs -put data-l2hw2.txt -p /user/root/l2hw2-r1/input
root@namenode-master:/opt dfs dfs -ls -h /user/root/l2hw2-r1/input
```

3. Export path Hadoop Streaming
```bash
root@namenode-master:~ export HADOOP_STREAMING_JAR=/opt/hadoop-3.3.6/share/hadoop/tools/lib/hadoop-streaming-3.3.6.jar
```

## Round 1 

1. Map & Reduce 
```bash
root@namenode-master:~ yarn jar $HADOOP_STREAMING_JAR -input /user/root/l2hw2-r1/input -output /user/root/l2hw2-r1/output \
                    -file /root/lab2-hw2/mapper.py -mapper /root/lab2-hw2/mapper.py \
                    -file /root/lab2-hw2/reducer.py -reducer /root/lab2-hw2/reducer.py
```

2. Get output
```bash
root@namenode-master:/opt mkdir l2hw2-r1-output
root@namenode-master:/opt hdfs dfs -get /user/root/l2hw2-r1/output/part-00000 l2hw2-r1-output/
root@namenode-master:/opt sort -nr -k 2 l2hw2-r1-output/part-00000 | head -n 10
```

## Round 2 
1. Put result from Round 1 to HDFS
```bash
root@namenode-master:/opt hdfs dfs -mkdir -p /user/root/l2hw2-r2/input
root@namenode-master:/opt hdfs dfs -put l2hw2-r1-output/part-00000 -p /user/root/l2hw2-r2/input
root@namenode-master:/opt dfs dfs -ls -h /user/root/l2hw2-r2/input
``````

2. Reduce 
```bash
root@namenode-master:~ yarn jar $HADOOP_STREAMING_JAR -input /user/root/l2hw2-r2/input -output /user/root/l2hw2-r2/output \
                    -file /root/lab2-hw2/r2-reducer.py -reducer /root/lab2-hw2/r2-reducer.py \
                    -mapper cat
```

3. Get output
```bash
root@namenode-master:/opt mkdir l2hw2-r2-output
root@namenode-master:/opt hdfs dfs -get /user/root/l2hw2-r2/output/part-00000 l2hw2-r2-output/
root@namenode-master:/opt sort -nr -k 2 l2hw2-r2-output/part-00000 | head -n 10
```