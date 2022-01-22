-- MySQL dump 10.13  Distrib 8.0.21, for Win64 (x86_64)
--
-- Host: localhost    Database: newfeedbackschema
-- ------------------------------------------------------
-- Server version	8.0.21
CREATE DATABASE newfeedbackschema;
/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `courseteacher`
--

DROP TABLE IF EXISTS `courseteacher`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `courseteacher` (
  `sno` int NOT NULL AUTO_INCREMENT,
  `coursename` varchar(255) DEFAULT NULL,
  `tearchername` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`sno`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `courseteacher`
--

LOCK TABLES `courseteacher` WRITE;
/*!40000 ALTER TABLE `courseteacher` DISABLE KEYS */;
INSERT INTO `courseteacher` VALUES (1,'Software Engineering','Saurabh'),(2,'Artificial Intelligence','Aloke'),(3,'Introduction to Data Science','Poulami'),(4,'Computer Security','Mohit'),(5,'KRR','Ravi'),(6,'Web Security','Shweta'),(7,'Integrated Software Development lab','Mukesh');
/*!40000 ALTER TABLE `courseteacher` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `feedback_table`
--

DROP TABLE IF EXISTS `feedback_table`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `feedback_table` (
  `sno` int NOT NULL AUTO_INCREMENT,
  `username` varchar(255) DEFAULT NULL,
  `coursename` varchar(255) DEFAULT NULL,
  `teachername` varchar(255) DEFAULT NULL,
  `q1` float DEFAULT NULL,
  `q2` float DEFAULT NULL,
  `q3` float DEFAULT NULL,
  `comment` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`sno`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `feedback_table`
--

LOCK TABLES `feedback_table` WRITE;
/*!40000 ALTER TABLE `feedback_table` DISABLE KEYS */;
/*!40000 ALTER TABLE `feedback_table` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `login`
--

DROP TABLE IF EXISTS `login`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `login` (
  `sno` int NOT NULL AUTO_INCREMENT,
  `username` varchar(255) DEFAULT NULL,
  `userpasswd` varchar(255) DEFAULT NULL,
  `usertype` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`sno`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `login`
--

LOCK TABLES `login` WRITE;
/*!40000 ALTER TABLE `login` DISABLE KEYS */;
INSERT INTO `login` VALUES (1,'Sameer','Sameer@123','Student'),(2,'Manthan','Manthan@123','Student'),(3,'Devang','Devang@123','Student'),(4,'Pranjal','Pranjal@123','Student'),(5,'Priyansh','Priyansh@123','Student'),(6,'Anshuman','Anshuman@123','Student'),(7,'Shivam','Shivam@123','Student'),(8,'Mukesh','Mukesh@123','Teacher'),(9,'Saurabh','Saurabh@123','Teacher'),(10,'Poulami','Poulami@123','Teacher'),(11,'Aloke','Aloke@123','Teacher'),(12,'Mohit','Mohit@123','Teacher'),(13,'Shweta','Shweta@123','Teacher'),(14,'Ravi','Ravi@123','Teacher');
/*!40000 ALTER TABLE `login` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-01-09 20:38:26
