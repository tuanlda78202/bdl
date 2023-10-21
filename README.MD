# Docker HDFS cluster 

## 0. Materials
1. Clone BDL repository 
```bash
git clone https://github.com/tuanlda78202/bdl.git
cd bdl
```

2. Install Docker 
```bash
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```


3. Install Hadoop & JDK into `assets`
```bash
cd assets 

# hadoop-3.3.6.tar.gz
wget https://dlcdn.apache.org/hadoop/common/hadoop-3.3.6/hadoop-3.3.6.tar.gz 

# jdk-8u202-linux-x64.tar.gz
gdown --id 1rLl42HqyTda69ARzKgy-OExoa175Ty0n
```

## 1. Build images 
```bash
sudo docker build . -t hadoop_base:latest
```

## 2. Start containers
```bash 
sudo docker network create dock_net
sudo docker run -itd --net dock_net --hostname namenode-master --name namenode --mount type=bind,src="$(pwd)/data",target="/root/data" -p 9870:9870 -p 8088:8088 hadoop_base:latest
sudo docker run -itd --net dock_net --hostname datanode1 --name datanode1 hadoop_base:latest
sudo docker run -itd --net dock_net --hostname datanode2 --name datanode2 hadoop_base:latest
sudo docker run -itd --net dock_net --hostname datanode3 --name datanode3 hadoop_base:latest

sudo docker exec namenode sh -c "hdfs namenode -format"

sudo docker exec -it namenode bash
root@namenode-master:/opt start-all.sh
```

## 3. Stop containers
```bash 
sudo docker exec namenode sh -c "stop-all.sh"
sudo docker stop namenode
sudo docker stop datanode1
sudo docker stop datanode2
sudo docker stop datanode3
```

## 4. Restart
```bash 
# Automatical stats one namenode and 3 datanodes in a docker network
sudo docker start namenode
sudo docker start datanode1
sudo docker start datanode2
sudo docker start datanode3

sudo docker exec -it namenode bash
root@namenode-master:/opt start-all.sh
```

## 5. Clean 
```bash 
sudo docker stop $(sudo docker ps -a -q)
sudo docker rm $(sudo docker ps -a -q) 
sudo docker network rm -f dock_net
```

## 6. Monitor HDFS

1. On `namenode`, running
```bash
hdfs dfsadmin -report
```

2. Web UI
```bash
# HDFS settings
namenode:9870 

# Resouce Manager
namenode:8088
```