FROM tomcat:9-jdk17

ENV SRC /src/
ADD ${SRC}/sample.war /usr/local/tomcat/webapps/

EXPOSE 8080
