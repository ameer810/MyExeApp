-- MySQL dump 10.13  Distrib 8.0.23, for Win64 (x86_64)
--
-- Host: localhost    Database: tahlel
-- ------------------------------------------------------
-- Server version	8.0.23

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
-- Table structure for table `addanalyst`
--

DROP TABLE IF EXISTS `addanalyst`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `addanalyst` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `default_result1` float DEFAULT NULL,
  `default_result2` float DEFAULT NULL,
  `price` decimal(10,5) DEFAULT NULL,
  `category` varchar(45) DEFAULT NULL,
  `sub_category` varchar(45) DEFAULT NULL,
  `date` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=77 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `addanalyst`
--

LOCK TABLES `addanalyst` WRITE;
/*!40000 ALTER TABLE `addanalyst` DISABLE KEYS */;
INSERT INTO `addanalyst` VALUES (5,'Random  blood sugar',80,140,0.00000,'عدد','bio','2021-02-22 23:07:23'),(6,'Blood Urea',20,45,0.00000,'عدد','bio','2021-02-22 23:11:50'),(7,'S. Creatinin',0.7,1.4,0.00000,'عدد','bio','2021-02-22 23:13:53'),(8,'S. Uric acid',3,7,0.00000,'عدد','bio','2021-02-22 23:14:50'),(9,'S. Cholesterol',150,250,0.00000,'عدد','bio','2021-02-22 23:15:47'),(10,'S. Triglycerid',65,80,0.00000,'عدد','bio','2021-02-22 23:16:20'),(11,'Total serum Bilirubin',0.3,1,0.00000,'عدد','bio','2021-02-22 23:17:26'),(12,'S.Calcium',8.8,10.2,0.00000,'عدد','bio','2021-02-22 23:18:14'),(13,'Vitamin D',0,0,0.00000,'عدد','bio','2021-02-22 23:18:58'),(14,'Color:GSE',0,0,0.00000,'خيارات','GSE','2021-02-22 23:20:34'),(15,'Consistency',0,0,0.00000,'خيارات','GSE','2021-02-22 23:22:08'),(16,'R.B.Cs',0,0,0.00000,'خيارات مع تعديل','GSE','2021-02-22 23:22:58'),(17,'Pus cells',0,0,0.00000,'خيارات مع تعديل','GSE','2021-02-22 23:23:17'),(18,'E. Histolytica',0,0,0.00000,'خيارات مع تعديل','GSE','2021-02-22 23:23:41'),(19,'G. Lembilia',0,0,0.00000,'خيارات مع تعديل','GSE','2021-02-22 23:24:19'),(20,'Ova',0,0,0.00000,'خيارات مع تعديل','GSE','2021-02-22 23:24:56'),(21,'Other:GSE',0,0,0.00000,'خيارات مع تعديل','GSE','2021-02-22 23:25:22'),(22,'Appearance',0,0,0.00000,'خيارات مع تعديل','GUE','2021-02-22 23:26:16'),(23,'Reaction',0,0,0.00000,'خيارات مع تعديل','GUE','2021-02-22 23:26:37'),(24,'Albumin',0,0,0.00000,'خيارات مع تعديل','GUE','2021-02-22 23:26:57'),(25,'Sugar',0,0,0.00000,'خيارات مع تعديل','GUE','2021-02-22 23:27:30'),(26,'RBCs',0,0,0.00000,'خيارات مع تعديل','GUE','2021-02-22 23:28:04'),(27,'Pus cells',0,0,0.00000,'خيارات مع تعديل','GUE','2021-02-22 23:28:29'),(28,'Epith .cells',0,0,0.00000,'خيارات مع تعديل','GUE','2021-02-22 23:28:59'),(29,'Crystals',0,0,0.00000,'خيارات مع تعديل','GUE','2021-02-22 23:29:30'),(30,'Casts',0,0,0.00000,'خيارات مع تعديل','GUE','2021-02-22 23:30:06'),(31,'Other:GUE',0,0,0.00000,'خيارات مع تعديل','GUE','2021-02-22 23:30:39'),(32,'Hb',0,0,0.00000,'خيارات مع تعديل','hematology','2021-02-22 23:31:12'),(33,'PCV',0,0,0.00000,'عدد','hematology','2021-02-22 23:31:42'),(34,'WBCs',0,0,0.00000,'خيارات مع تعديل','hematology','2021-02-22 23:32:10'),(35,'E.S.R',0,0,0.00000,'خيارات مع تعديل','hematology','2021-02-22 23:32:33'),(36,'Blood Group',0,0,0.00000,'خيارات','hematology','2021-02-22 23:33:03'),(37,'Rh',0,0,0.00000,'خيارات مع تعديل','hematology','2021-02-22 23:33:30'),(38,'Pregnancy test  in urine',0,0,0.00000,'خيارات مع تعديل','hematology','2021-02-22 23:34:12'),(39,'Pregnancy test  in serum',0,0,0.00000,'خيارات مع تعديل','hematology','2021-02-22 23:34:40'),(40,'R.B.Sugar',0,0,0.00000,'خيارات مع تعديل','hematology','2021-02-22 23:35:07'),(41,'Bl. Urea',0,0,0.00000,'خيارات مع تعديل','hematology','2021-02-22 23:35:28'),(42,'Salmonella typhi  IgG',0,0,0.00000,'خيارات مع تعديل','hematology','2021-02-22 23:35:50'),(43,'Salmonella typhi  IgM',0,0,0.00000,'خيارات مع تعديل','hematology','2021-02-22 23:36:16'),(44,'Rose-Bengal test',0,0,0.00000,'خيارات مع تعديل','hematology','2021-02-22 23:36:34'),(45,'T3',0,0,0.00000,'خيارات مع تعديل','هرمونات مشترك','2021-02-23 23:10:14'),(46,'T4',0,0,0.00000,'خيارات مع تعديل','هرمونات مشترك','2021-02-23 23:11:06'),(47,'TSH',0,0,0.00000,'خيارات مع تعديل','هرمونات مشترك','2021-02-23 23:11:36'),(48,'LH',0,0,0.00000,'خيارات مع تعديل','هرمونات مشترك','2021-02-23 23:12:03'),(49,'FSH',0,0,0.00000,'خيارات مع تعديل','هرمونات مشترك','2021-02-23 23:12:41'),(50,'Prolactin',0,0,0.00000,'خيارات مع تعديل','هرمونات مشترك','2021-02-23 23:13:23'),(51,'Testosterone',0,0,0.00000,'خيارات مع تعديل','هرمونات مشترك','2021-02-23 23:13:55'),(52,'Toxoplasma IgG',0,0,0.00000,'عدد','هرمونات مشترك','2021-02-23 23:38:11'),(53,'Toxoplasma IgM',0,0,0.00000,'عدد','هرمونات مشترك','2021-02-23 23:38:29'),(54,'Cytomegalo Virus IgG',0,0,0.00000,'عدد','هرمونات مشترك','2021-02-23 23:40:00'),(55,'Cytomegalo Virus IgM',0,0,0.00000,'عدد','هرمونات مشترك','2021-02-23 23:40:25'),(56,'Rubella IgG',0,0,0.00000,'عدد','هرمونات مشترك','2021-02-23 23:40:45'),(57,'Rubella IgM',0,0,0.00000,'عدد','هرمونات مشترك','2021-02-23 23:36:56'),(58,'Anti - Phspholipin IgG',0,0,0.00000,'عدد','هرمونات مشترك','2021-02-23 23:41:17'),(59,'Anti - Phspholipin  IgM',0,0,0.00000,'عدد','هرمونات مشترك','2021-02-23 23:41:44'),(60,'Anti - Cardiolipin  IgG',0,0,0.00000,'عدد','هرمونات مشترك','2021-02-23 23:41:58'),(61,'Anti - Cardiolipin  IgM',0,0,0.00000,'عدد','هرمونات مشترك','2021-02-23 23:42:14'),(62,'Herps   IgG',0,0,0.00000,'عدد','هرمونات مشترك','2021-02-23 23:42:34'),(63,'Herpes  IgM',0,0,0.00000,'عدد','هرمونات مشترك','2021-02-23 23:42:50'),(65,'Volume',0,0,0.00000,'خيارات مع تعديل','SFA',NULL),(66,'Reaction',0,0,0.00000,'خيارات مع تعديل','SFA',NULL),(67,'Colour:SFA',0,0,0.00000,'خيارات مع تعديل','SFA',NULL),(68,'Liquefaction',0,0,0.00000,'خيارات مع تعديل','SFA',NULL),(69,'Count',0,0,0.00000,'عدد','SFA',NULL),(70,'Motility:Active',0,0,0.00000,'عدد','SFA',NULL),(71,'Motility:Sluggish',0,0,0.00000,'عدد','SFA',NULL),(72,'Motility:Dead',0,0,0.00000,'عدد','SFA',NULL),(73,'Morphology:Normal',0,0,0.00000,'عدد','SFA',NULL),(74,'Morphology:Abnormal',0,0,0.00000,'عدد','SFA',NULL),(75,'Morphology:Pus cells',0,0,0.00000,'خيارات مع تعديل','SFA',NULL),(76,'Other:SFA',0,0,0.00000,'خيارات مع تعدبل','SFA',NULL);
/*!40000 ALTER TABLE `addanalyst` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `addbuys`
--

DROP TABLE IF EXISTS `addbuys`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `addbuys` (
  `id` int NOT NULL AUTO_INCREMENT,
  `item_name` varchar(255) DEFAULT NULL,
  `signal_item_price` int DEFAULT NULL,
  `total_price` int DEFAULT NULL,
  `buys_type` varchar(255) DEFAULT NULL,
  `quantity` int DEFAULT NULL,
  `date` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `addbuys`
--

LOCK TABLES `addbuys` WRITE;
/*!40000 ALTER TABLE `addbuys` DISABLE KEYS */;
INSERT INTO `addbuys` VALUES (1,'ali',21,100,'--------------',16,'2000-01-01 00:00:00'),(3,'item_name',10,100,'item_type',18,'2021-02-12 18:12:14');
/*!40000 ALTER TABLE `addbuys` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `addclient`
--

DROP TABLE IF EXISTS `addclient`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `addclient` (
  `id` int NOT NULL AUTO_INCREMENT,
  `client_name` varchar(255) DEFAULT NULL,
  `client_age` int DEFAULT NULL,
  `client_genus` varchar(255) DEFAULT NULL,
  `client_doctor` varchar(255) DEFAULT NULL,
  `date` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=159 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `addclient`
--

LOCK TABLES `addclient` WRITE;
/*!40000 ALTER TABLE `addclient` DISABLE KEYS */;
INSERT INTO `addclient` VALUES (118,'alia',12,'ذكر','hj','2021-02-23 22:32:45'),(119,'alih',19,'انثى','h','2021-02-24 01:56:48'),(120,'alia',12,'ذكر','----------------------','2021-02-24 01:57:47'),(121,'alia',12,'ذكر','----------------------','2021-02-24 01:57:55'),(122,'alih',19,'انثى','----------------------','2021-02-26 20:29:47'),(123,'alihji',90,'انثى','----------------------','2021-02-26 20:43:55'),(124,'alihji',90,'انثى','----------------------','2021-02-26 20:44:08'),(125,'alih',119,'ذكر','h','2021-02-26 22:28:48'),(130,'علاوي عبيس حميد',19,'انثى','عدوية شمس سعيد','2021-02-27 23:55:22'),(131,'حميد',20,'انثى','عدوية شمس سعيد','2021-02-27 23:57:02'),(132,'حمييد',29,'انثى','عدوية شمس سعيد','2021-02-27 23:59:33'),(133,'حميييد',98,'انثى','عدوية شمس سعيد','2021-02-28 00:01:03'),(134,'حميييييييييد',35,'انثى','عدوية شمس سعيد','2021-02-28 00:04:29'),(135,'حمووووووووود',99,'انثى','عدوية شمس سعيد','2021-02-28 00:08:07'),(136,'حمود',45,'انثى','عدوية شمس سعيد','2021-02-28 00:09:58'),(137,'اموري الورد',92,'انثى','عدوية شمس سعيد','2021-02-28 00:15:50'),(138,'امير عبد عبد',56,'انثى','عدوية شمس سعيد','2021-02-28 00:25:44'),(139,'اتنسنص',15,'انثى','تت','2021-02-28 00:30:59'),(140,'اتنسنص',139,'انثى','تت','2021-02-28 00:33:11'),(141,'alih',119,'ذكر','h','2021-02-28 00:38:04'),(142,'alih',119,'ذكر','h','2021-02-28 00:38:20'),(143,'alih',119,'ذكر','h','2021-02-28 00:38:31'),(144,'alih',119,'ذكر','h','2021-02-28 20:01:07'),(145,'new h',19,'انثى','h','2021-02-28 20:15:00'),(146,'new hg',19,'انثى','h','2021-02-28 20:15:15'),(147,'new hg',19,'انثى','h','2021-02-28 20:15:29'),(148,'امير سعد عبد',18,'انثى','hj','2021-02-28 20:28:12'),(149,'امير سعد عبد',18,'انثى','hj','2021-02-28 20:32:35'),(150,'امير سعد عبد',18,'انثى','hj','2021-02-28 20:33:17'),(151,'امير سعد عبد',18,'انثى','hj','2021-02-28 20:33:51'),(152,'امير سعد عبد',18,'انثى','hj','2021-02-28 20:34:23'),(153,'امير سعد عبد',18,'انثى','hj','2021-02-28 20:35:08'),(154,'عباس',19,'انثى','عدوية شمس سعيد','2021-02-28 21:22:33'),(155,'عباس علي',19,'انثى','عدوية شمس سعيد','2021-02-28 21:23:23'),(156,'عباس علي',19,'انثى','عدوية شمس سعيد','2021-02-28 21:23:38'),(158,'',0,'ذكر','--------------','2021-03-01 21:01:22');
/*!40000 ALTER TABLE `addclient` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `addnewitem`
--

DROP TABLE IF EXISTS `addnewitem`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `addnewitem` (
  `id` int NOT NULL AUTO_INCREMENT,
  `client_name` varchar(255) NOT NULL,
  `client_id` int DEFAULT NULL,
  `client_age` int DEFAULT NULL,
  `genus` varchar(255) NOT NULL,
  `doctor_name` varchar(255) NOT NULL,
  `notes` text,
  `analyst_name` varchar(255) NOT NULL,
  `analyst_result` varchar(255) DEFAULT NULL,
  `price` int DEFAULT NULL,
  `total_price` varchar(45) DEFAULT NULL,
  `date` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=128 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `addnewitem`
--

LOCK TABLES `addnewitem` WRITE;
/*!40000 ALTER TABLE `addnewitem` DISABLE KEYS */;
INSERT INTO `addnewitem` VALUES (87,'alia',118,12,'ذكر','hj','jh','Random  blood sugar ','13',0,'0','2021-02-23 22:32:45'),(88,'alih',119,19,'انثى','h','j','Blood Urea','17',0,'0','2021-02-24 01:56:49'),(89,'alia',118,12,'ذكر','----------------------','jh','S. Uric acid','18',0,'0','2021-02-24 01:57:47'),(90,'alia',118,12,'ذكر','----------------------','jh','Total serum Bilirubin','90',0,'0','2021-02-24 01:57:55'),(91,'alih',119,19,'انثى','----------------------','j','Random  blood sugar','12',0,'0','2021-02-26 20:29:47'),(92,'alihji',123,90,'انثى','----------------------','jj','Hb','67',0,'0','2021-02-26 20:43:56'),(93,'alihji',123,90,'انثى','----------------------','jj','PCV','0',0,'0','2021-02-26 20:44:08'),(94,'alih',119,119,'انثى','h','انثى','PCV','19',0,'0','2021-02-26 22:28:48'),(99,'علاوي عبيس حميد',130,19,'انثى','عدوية شمس سعيد','','Toxoplasma IgG','1',0,'0','2021-02-27 23:55:22'),(100,'حميد',131,20,'انثى','عدوية شمس سعيد','','Toxoplasma IgG','1',0,'0','2021-02-27 23:57:02'),(101,'حمييد',132,29,'انثى','عدوية شمس سعيد','','Toxoplasma IgG','1',0,'0','2021-02-27 23:59:33'),(102,'حميييد',133,98,'انثى','عدوية شمس سعيد','','Toxoplasma IgM','1',0,'0','2021-02-28 00:01:03'),(103,'حميييييييييد',134,35,'انثى','عدوية شمس سعيد','','Toxoplasma IgM','1',0,'0','2021-02-28 00:04:29'),(104,'حمووووووووود',135,99,'انثى','عدوية شمس سعيد','','Toxoplasma IgM','1',0,'0','2021-02-28 00:08:07'),(105,'حمود',136,45,'انثى','عدوية شمس سعيد','','Toxoplasma IgM','1',0,'0','2021-02-28 00:09:58'),(106,'اموري الورد',137,92,'انثى','عدوية شمس سعيد','','Toxoplasma IgM','0',0,'0','2021-02-28 00:15:50'),(107,'امير عبد عبد',138,56,'انثى','عدوية شمس سعيد','','Toxoplasma IgM','1',0,'0','2021-02-28 00:25:45'),(108,'اتنسنص',139,15,'انثى','تت','','Toxoplasma IgG','0',0,'0','2021-02-28 00:31:01'),(109,'اتنسنص',139,139,'انثى','تت','انثى','Cytomegalo Virus IgG','2',0,'0','2021-02-28 00:33:12'),(110,'alih',119,119,'ذكر','h','انثى','Other:GUE','k',0,'0','2021-02-28 00:38:04'),(111,'alih',119,119,'ذكر','h','انثى','Salmonella typhi  IgM','kh',0,'0','2021-02-28 00:38:20'),(112,'alih',119,119,'ذكر','h','انثى','Toxoplasma IgG','2',0,'0','2021-02-28 00:38:31'),(113,'alih',119,119,'ذكر','h','انثى','Count','10',0,'0','2021-02-28 20:01:07'),(114,'new h',145,19,'انثى','h','Salmonella typhi  IgM','Salmonella typhi  IgM','please',0,'0','2021-02-28 20:15:00'),(115,'new hg',146,19,'انثى','h','Salmonella typhi  IgM','Random  blood sugar','10',0,'0','2021-02-28 20:15:15'),(116,'new hg',146,19,'انثى','h','Salmonella typhi  IgM','Salmonella typhi  IgM','please',0,'0','2021-02-28 20:15:29'),(117,'امير سعد عبد',148,18,'انثى','hj','تتت','Random  blood sugar','10',0,'0','2021-02-28 20:28:12'),(118,'امير سعد عبد',148,18,'انثى','hj','تتت','R.B.Cs','هة اثقث',0,'0','2021-02-28 20:32:35'),(119,'امير سعد عبد',148,18,'انثى','hj','تتت','Appearance','hello',0,'0','2021-02-28 20:33:17'),(120,'امير سعد عبد',148,18,'انثى','hj','تتت','PCV','12',0,'0','2021-02-28 20:33:51'),(121,'امير سعد عبد',148,18,'انثى','hj','تتت','T4','45',0,'0','2021-02-28 20:34:23'),(122,'امير سعد عبد',148,18,'انثى','hj','تتت','Volume','80',0,'0','2021-02-28 20:35:09'),(123,'عباس',154,19,'انثى','عدوية شمس سعيد','تة','PCV','100898',0,'0','2021-02-28 21:22:33'),(124,'عباس علي',155,19,'انثى','عدوية شمس سعيد','تة','Random  blood sugar','112345',0,'0','2021-02-28 21:23:23'),(125,'عباس علي',155,19,'انثى','عدوية شمس سعيد','تة','PCV','1748387389373',0,'0','2021-02-28 21:23:38'),(127,'',158,0,'ذكر','--------------','','----------------','1',0,'0','2021-03-01 21:01:22');
/*!40000 ALTER TABLE `addnewitem` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `adduser`
--

DROP TABLE IF EXISTS `adduser`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `adduser` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_name` varchar(255) NOT NULL,
  `user_password` varchar(255) NOT NULL,
  `user_mail` varchar(255) NOT NULL,
  `date` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `adduser`
--

LOCK TABLES `adduser` WRITE;
/*!40000 ALTER TABLE `adduser` DISABLE KEYS */;
INSERT INTO `adduser` VALUES (3,'ali','5','a',NULL),(4,'ameer','5','a',NULL);
/*!40000 ALTER TABLE `adduser` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `doctor`
--

DROP TABLE IF EXISTS `doctor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `doctor` (
  `id` int NOT NULL AUTO_INCREMENT,
  `uid` varchar(255) DEFAULT NULL,
  `action` varchar(45) DEFAULT NULL,
  `table` varchar(45) DEFAULT NULL,
  `date` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `doctor`
--

LOCK TABLES `doctor` WRITE;
/*!40000 ALTER TABLE `doctor` DISABLE KEYS */;
INSERT INTO `doctor` VALUES (1,'1','1','1','datetime.datetime.now()');
/*!40000 ALTER TABLE `doctor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `his`
--

DROP TABLE IF EXISTS `his`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `his` (
  `id` int NOT NULL AUTO_INCREMENT,
  `uid` int DEFAULT NULL,
  `action` int DEFAULT NULL,
  `tabled` int DEFAULT NULL,
  `dates` datetime DEFAULT NULL,
  `def` int NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=593 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `his`
--

LOCK TABLES `his` WRITE;
/*!40000 ALTER TABLE `his` DISABLE KEYS */;
INSERT INTO `his` VALUES (477,4,6,2,'2021-02-26 03:30:12',1),(478,3,1,5,'2021-02-26 03:30:19',1),(479,4,6,2,'2021-02-26 03:31:17',1),(480,3,1,5,'2021-02-26 03:31:25',1),(481,4,6,2,'2021-02-26 03:31:58',1),(482,3,1,5,'2021-02-26 03:32:05',1),(483,4,6,2,'2021-02-26 03:32:35',1),(484,4,6,2,'2021-02-26 03:32:51',1),(485,4,6,2,'2021-02-26 03:35:06',1),(486,3,1,5,'2021-02-26 03:35:15',1),(487,4,6,2,'2021-02-26 03:35:41',1),(488,3,1,5,'2021-02-26 03:35:48',1),(489,4,6,2,'2021-02-26 03:36:39',1),(490,3,1,5,'2021-02-26 03:36:48',1),(491,4,6,2,'2021-02-26 03:37:10',1),(492,4,6,2,'2021-02-26 03:37:51',1),(493,4,6,2,'2021-02-26 03:38:26',1),(494,3,1,5,'2021-02-26 03:38:34',1),(495,4,6,2,'2021-02-26 03:39:54',1),(496,4,1,5,'2021-02-26 03:40:00',1),(497,4,6,2,'2021-02-26 03:40:23',1),(498,4,6,2,'2021-02-26 03:41:11',1),(499,3,1,5,'2021-02-26 03:41:26',1),(500,4,6,2,'2021-02-26 03:42:24',1),(501,3,1,5,'2021-02-26 03:42:32',1),(502,4,6,2,'2021-02-26 03:43:10',1),(503,3,1,5,'2021-02-26 03:43:16',1),(504,4,6,2,'2021-02-26 03:43:35',1),(505,3,1,5,'2021-02-26 03:43:49',1),(506,4,6,2,'2021-02-26 03:44:09',1),(507,3,1,5,'2021-02-26 03:44:16',1),(508,4,6,2,'2021-02-26 03:44:47',1),(509,3,1,5,'2021-02-26 03:44:53',1),(510,4,6,2,'2021-02-26 03:45:48',1),(511,3,1,5,'2021-02-26 03:45:57',1),(512,4,6,2,'2021-02-26 03:46:13',1),(513,3,1,5,'2021-02-26 03:46:21',1),(514,4,6,2,'2021-02-26 03:47:10',1),(515,3,1,5,'2021-02-26 03:47:17',1),(516,4,6,2,'2021-02-26 03:47:50',1),(517,3,1,5,'2021-02-26 03:47:58',1),(518,4,6,2,'2021-02-26 03:48:56',1),(519,4,6,2,'2021-02-26 14:55:34',1),(520,4,6,2,'2021-02-26 14:56:43',1),(521,4,6,2,'2021-02-26 14:56:54',1),(522,4,6,2,'2021-02-26 14:58:05',1),(523,3,1,5,'2021-02-26 14:58:13',1),(524,4,6,2,'2021-02-26 14:58:55',1),(525,4,6,2,'2021-02-26 14:59:53',1),(526,4,6,2,'2021-02-26 15:01:48',1),(527,4,6,2,'2021-02-26 15:02:50',1),(528,4,6,2,'2021-02-26 15:03:42',1),(529,4,6,2,'2021-02-26 15:04:12',1),(530,3,1,5,'2021-02-26 15:04:20',1),(531,4,6,2,'2021-02-26 15:05:04',1),(532,3,1,5,'2021-02-26 15:05:13',1),(533,4,6,2,'2021-02-26 15:08:57',1),(534,4,6,2,'2021-02-26 15:09:18',1),(535,4,6,2,'2021-02-26 15:09:42',1),(536,4,6,2,'2021-02-26 15:10:50',1),(537,3,1,5,'2021-02-26 15:11:00',1),(538,4,6,2,'2021-02-26 15:11:43',1),(539,3,1,5,'2021-02-26 15:11:51',1),(540,4,6,2,'2021-02-26 15:12:34',1),(541,3,1,5,'2021-02-26 15:12:40',1),(542,4,6,2,'2021-02-26 15:13:28',1),(543,4,6,2,'2021-02-26 15:16:31',1),(544,4,6,2,'2021-02-26 15:17:31',1),(545,4,6,2,'2021-02-26 15:22:24',1),(546,3,1,5,'2021-02-26 15:22:40',1),(547,4,6,2,'2021-02-26 15:26:23',1),(548,3,1,5,'2021-02-26 15:26:29',1),(549,4,6,2,'2021-02-26 15:28:55',1),(550,4,6,2,'2021-02-26 15:29:27',1),(551,3,1,5,'2021-02-26 15:29:33',1),(552,4,6,2,'2021-02-26 15:29:58',1),(553,3,1,5,'2021-02-26 15:30:05',1),(554,4,6,2,'2021-02-26 15:30:35',1),(555,3,1,5,'2021-02-26 15:30:43',1),(556,4,6,2,'2021-02-26 15:31:03',1),(557,3,1,5,'2021-02-26 15:31:09',1),(558,4,6,2,'2021-02-26 15:32:20',1),(559,3,1,5,'2021-02-26 15:32:28',1),(560,4,6,2,'2021-02-26 15:32:53',1),(561,3,1,5,'2021-02-26 15:33:02',1),(562,4,6,2,'2021-02-26 15:33:43',1),(563,4,6,2,'2021-02-26 15:34:26',1),(564,4,6,2,'2021-02-26 15:36:41',1),(565,3,1,5,'2021-02-26 15:36:50',1),(566,4,6,2,'2021-02-26 15:37:58',1),(567,3,1,5,'2021-02-26 15:38:06',1),(568,4,6,2,'2021-02-26 15:39:14',1),(569,4,6,2,'2021-02-26 15:41:10',1),(570,4,6,2,'2021-02-26 15:43:11',1),(571,4,6,2,'2021-02-26 15:49:51',1),(572,4,6,2,'2021-02-26 15:50:44',1),(573,4,6,2,'2021-02-26 15:51:52',1),(574,4,6,2,'2021-02-26 15:53:07',1),(575,4,6,2,'2021-02-26 15:55:56',1),(576,4,6,2,'2021-02-26 15:57:11',1),(577,4,6,2,'2021-02-26 15:57:33',1),(578,4,6,2,'2021-02-26 15:57:52',1),(579,4,6,2,'2021-02-26 15:58:35',1),(580,4,6,2,'2021-02-26 15:58:47',1),(581,4,6,2,'2021-02-26 15:59:04',1),(582,3,1,5,'2021-02-26 15:59:11',1),(583,4,6,2,'2021-02-26 16:00:24',1),(584,4,6,2,'2021-02-26 16:01:09',1),(585,4,6,2,'2021-02-26 16:08:41',1),(586,4,6,2,'2021-02-26 16:08:53',1),(587,3,1,5,'2021-02-26 16:09:01',1),(588,4,6,2,'2021-02-26 16:09:47',1),(589,3,1,5,'2021-02-26 16:09:58',1),(590,4,6,2,'2021-02-26 16:16:16',1),(591,3,1,5,'2021-02-26 16:16:24',1),(592,3,6,5,'2021-02-26 16:16:58',1);
/*!40000 ALTER TABLE `his` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `paths`
--

DROP TABLE IF EXISTS `paths`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `paths` (
  `id` int NOT NULL AUTO_INCREMENT,
  `file_path` varchar(255) DEFAULT NULL,
  `save_file_path` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `paths`
--

LOCK TABLES `paths` WRITE;
/*!40000 ALTER TABLE `paths` DISABLE KEYS */;
INSERT INTO `paths` VALUES (1,'F:\\برنامج التحليلات\\word','F:\\برنامج التحليلات');
/*!40000 ALTER TABLE `paths` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `report`
--

DROP TABLE IF EXISTS `report`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `report` (
  `id` int NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `time` time NOT NULL,
  `report_type` int NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `report`
--

LOCK TABLES `report` WRITE;
/*!40000 ALTER TABLE `report` DISABLE KEYS */;
/*!40000 ALTER TABLE `report` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `userper`
--

DROP TABLE IF EXISTS `userper`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `userper` (
  `id` int NOT NULL AUTO_INCREMENT,
  `add_sale_item_page` int NOT NULL,
  `analyst_page` int NOT NULL,
  `clients_page` int NOT NULL,
  `history_page` int NOT NULL,
  `settings_page` int NOT NULL,
  `show_analyst` int NOT NULL,
  `add_analyst` int NOT NULL,
  `edit_analyst` int NOT NULL,
  `delete_analyst` int NOT NULL,
  `change_theme` int NOT NULL,
  `add_buys` int NOT NULL,
  `report` int NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `userper`
--

LOCK TABLES `userper` WRITE;
/*!40000 ALTER TABLE `userper` DISABLE KEYS */;
/*!40000 ALTER TABLE `userper` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-03-01 21:05:41
