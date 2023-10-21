FROM ubuntu:latest

MAINTAINER tuanlda78202

# Environment variables for changing JDK, HADOOP versions and directories
ENV JDK_TAR_NAME=jdk-8u202-linux-x64.tar.gz
ENV HADOOP_TAR_NAME=hadoop-3.3.6.tar.gz

# Install basic utils and python
RUN apt update
RUN apt install -y python3 arp-scan openssh-server

# SSH without key
RUN ssh-keygen -t rsa -f ~/.ssh/id_rsa -P '' &&
    cat ~/.ssh/id_rsa.pub >>~/.ssh/authorized_keys

### Setup JDK
WORKDIR /opt
ADD ./assets/${JDK_TAR_NAME} .

# Add path variables for JDK
ENV JAVA_HOME=/opt/jdk1.8.0_202
ENV PATH=$PATH:$JAVA_HOME:$JAVA_HOME/bin

# Make datafolder
RUN mkdir -p /opt/hdfs_data/datanode
RUN mkdir -p /opt/hdfs_data/namenode

### Setup Hadoop
ADD ./assets/${HADOOP_TAR_NAME} .

# Adding path variables and environment variables for Hadoop
ENV HADOOP_HOME=/opt/hadoop-3.3.6
ENV HADOOP_STREAMING_JAR=$HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-3.3.6.jar
ENV PATH=$PATH:$HADOOP_HOME:$HADOOP_HOME/bin:$HADOOP_HOME/sbin

# Configuration
# Adding hadoop configuration files
ADD ./config-files/hadoop-env.sh $HADOOP_HOME/etc/hadoop/
ADD ./config-files/core-site.xml $HADOOP_HOME/etc/hadoop/
ADD ./config-files/mapred-site.xml $HADOOP_HOME/etc/hadoop/
ADD ./config-files/hdfs-site.xml $HADOOP_HOME/etc/hadoop/
ADD ./config-files/yarn-site.xml $HADOOP_HOME/etc/hadoop/
ADD ./config-files/workers $HADOOP_HOME/etc/hadoop/

# Start ssh service when start a docker
CMD [ "sh", "-c", "service ssh start; /bin/bash"]
