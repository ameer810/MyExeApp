-- MySQL dump 10.13  Distrib 8.0.23, for Win64 (x86_64)
--
-- Host: localhost    Database: tahlel2
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
  `price` int DEFAULT NULL,
  `category` varchar(45) DEFAULT NULL,
  `sub_category` varchar(45) DEFAULT NULL,
  `date` datetime DEFAULT NULL,
  `unit` text,
  `defult` text,
  `results` varchar(455) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=92 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `addanalyst`
--

LOCK TABLES `addanalyst` WRITE;
/*!40000 ALTER TABLE `addanalyst` DISABLE KEYS */;
INSERT INTO `addanalyst` VALUES (5,'Random  blood sugar',2,'عدد','bio','2021-04-20 04:55:06','mg/dl','random def',''),(6,'Blood Urea',3,'عدد','bio','2021-02-22 23:11:50','mg2/dl','def2,g',NULL),(7,'S. Creatinin',3,'عدد','bio','2021-02-22 23:13:53','please','def please',NULL),(8,'S. Uric acid',3,'عدد','bio','2021-02-22 23:14:50',NULL,NULL,NULL),(9,'S. Cholesterol',3,'عدد','bio','2021-02-22 23:15:47',NULL,NULL,NULL),(10,'S. Triglycerid',3,'عدد','bio','2021-02-22 23:16:20',NULL,NULL,NULL),(11,'Total serum Bilirubin',3,'عدد','bio','2021-02-22 23:17:26',NULL,NULL,NULL),(12,'S.Calcium',3,'عدد','bio','2021-02-22 23:18:14',NULL,NULL,NULL),(13,'Vitamin D',10,'عدد','bio','2021-02-22 23:18:58',NULL,NULL,NULL),(14,'Color:GSE',0,'خيارات','Full GSE','2021-02-22 23:20:34','please','please def','\'yallow\', \'brown\', \'green\', \'milk\''),(15,'Consistency',0,'خيارات','Full GSE','2021-02-22 23:22:08',NULL,NULL,'\'Solid\', \'Liquid\', \'Semi solid\', \'Semi liquid\', \'Mucoid\''),(16,'R.B.Cs:GSE',0,'خيارات','Full GSE','2021-02-22 23:22:58','pldold',NULL,'\'1 - 2\', \'1 - 3\', \'2 - 3\', \'2 - 4\', \'0 - 1\', \'0 - 2\', \'3 - 5\', \'4 - 6\', \'5 - 6\','),(17,'Pus cells:GSE',0,'خيارات','Full GSE','2021-02-22 23:23:17',NULL,NULL,'\'1 - 2\', \'1 - 3\', \'2 - 3\', \'2 - 4\', \'0 - 1\', \'0 - 2\', \'3 - 5\', \'4 - 6\', \'5 - 6\','),(18,'E. Histolytica',0,'خيارات','Full GSE','2021-02-22 23:23:41',NULL,NULL,'\'Cyst\', \'Trophozoite\''),(19,'G. Lembilia',0,'خيارات','Full GSE','2021-02-22 23:24:19',NULL,NULL,'\'Cyst\', \'Trophozoite\''),(20,'Ova',0,'خيارات','Full GSE','2021-02-22 23:24:56',NULL,NULL,'\'Nill\''),(21,'Other:GSE',0,'خيارات','Full GSE','2021-02-22 23:25:22',NULL,NULL,NULL),(22,'Appearance',0,'خيارات','Full GUE','2021-02-22 23:26:16',NULL,NULL,'\'Turbid\', \'Clear\''),(23,'Reaction:GUE',0,'خيارات','Full GUE','2021-02-22 23:26:37',NULL,NULL,'\'Acidic\', \'Alkaline\''),(24,'Albumin',0,'خيارات','Full GUE','2021-02-22 23:26:57',NULL,NULL,'\'Nil\', \'+\', \'++\', \'+++\', \'Trace\''),(25,'Sugar',0,'خيارات','Full GUE','2021-02-22 23:27:30',NULL,NULL,'\'Nil\', \'+\', \'++\', \'+++\', \'Trace\''),(26,'RBCs:GUE',0,'خيارات','Full GUE','2021-02-22 23:28:04',NULL,NULL,'\'1 - 2\', \'1 - 3\', \'2 - 3\', \'2 - 4\', \'0 - 1\', \'0 - 2\', \'3 - 5\', \'4 - 6\', \'5 - 6\','),(27,'Pus cells:GUE',0,'خيارات','Full GUE','2021-02-22 23:28:29',NULL,NULL,'\'1 - 2\', \'1 - 3\', \'2 - 3\', \'2 - 4\', \'0 - 1\', \'0 - 2\', \'3 - 5\', \'4 - 6\', \'5 - 6\','),(28,'Epith .cells',0,'خيارات','Full GUE','2021-02-22 23:28:59',NULL,NULL,'\'Few\', \'+\', \'++\', \'+++\', \'++++\''),(29,'Crystals',0,'خيارات','Full GUE','2021-02-22 23:29:30',NULL,NULL,'\'Am.Urate\', \'Am.Phosphatase\', \'Uric Acid\', \'Ca.Oxalate\''),(30,'Casts',0,'خيارات','Full GUE','2021-02-22 23:30:06',NULL,NULL,'\'Granular cast +\', \'Granular cast ++\', \'Granular cast +++\''),(31,'Other:GUE',0,'خيارات','Full GUE','2021-02-22 23:30:39',NULL,NULL,NULL),(32,'Hb',3,'خيارات مع تعديل','hematology','2021-02-22 23:31:12',NULL,NULL,'4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18'),(33,'PCV',3,'عدد','hematology','2021-02-22 23:31:42',NULL,NULL,NULL),(34,'WBCs',3,'عدد','hematology','2021-02-22 23:32:10',NULL,NULL,NULL),(35,'E.S.R',3,'عدد','hematology','2021-02-22 23:32:33',NULL,NULL,'\'A (+ve)\', \'B (+ve)\', \'AB (+ve)\', \'O (+ve)\', \'O (-ve)\', \'A (-ve)\', \'B (-ve)\', \'AB (-ve)\''),(36,'Blood Group',3,'خيارات','hematology','2021-02-22 23:33:03','no','yes','\'yellow\',\'green\',\'red\''),(37,'Rh',3,'خيارات','hematology','2021-02-22 23:33:30',NULL,NULL,NULL),(38,'Pregnancy test  in urine',3,'خيارات','hematology','2021-02-22 23:34:12',NULL,NULL,'\'Positive (+ve)\', \'Negative (-ve)\', \'Weak Positive\''),(39,'Pregnancy test  in serum',3,'خيارات','hematology','2021-02-22 23:34:40',NULL,NULL,'\'Positive (+ve)\', \'Negative (-ve)\''),(40,'R.B.Sugar',2,'عدد','hematology','2021-02-22 23:35:07',NULL,NULL,NULL),(41,'Bl. Urea',3,'عدد','hematology','2021-02-22 23:35:28',NULL,NULL,NULL),(42,'Salmonella typhi  IgG',4,'خيارات','hematology','2021-02-22 23:35:50',NULL,NULL,'\'Positive (+ve)\', \'Negative (-ve)\''),(43,'Salmonella typhi  IgM',4,'خيارات','hematology','2021-02-22 23:36:16',NULL,NULL,'\'Positive (+ve)\', \'Negative (-ve)\''),(44,'Rose-Bengal test',3,'خيارات','hematology','2021-02-22 23:36:34',NULL,NULL,'\'Positive (+ve)\', \'Negative (-ve)\''),(45,'T3',7,'عدد','هرمونات مشترك','2021-02-23 23:10:14',NULL,NULL,NULL),(46,'T4',7,'عدد','هرمونات مشترك','2021-02-23 23:11:06',NULL,NULL,NULL),(47,'TSH',7,'عدد','هرمونات مشترك','2021-02-23 23:11:36',NULL,NULL,NULL),(48,'LH',10,'عدد','هرمونات مشترك','2021-02-23 23:12:03',NULL,NULL,NULL),(49,'FSH',10,'عدد','هرمونات مشترك','2021-02-23 23:12:41',NULL,NULL,NULL),(50,'Prolactin',10,'عدد','هرمونات مشترك','2021-02-23 23:13:23','lkeo;k','iwiuw',NULL),(51,'Testosterone',10,'عدد','هرمونات مشترك','2021-02-23 23:13:55',NULL,NULL,'\'0.5 Negative\', \'0.6 Negative\', \'0.7 Negative\', \'0.8 Negative\', \'1.1 Positive\', \'1.1 Positive\','),(52,'Toxoplasma IgG',10,'خيارات','هرمونات مشترك','2021-02-23 23:38:11',NULL,NULL,'\'0.5 Negative\', \'0.6 Negative\', \'0.7 Negative\', \'0.8 Negative\', \'1.1 Positive\', \'1.1 Positive\','),(53,'Toxoplasma IgM',10,'خيارات','هرمونات مشترك','2021-02-23 23:38:29',NULL,NULL,'\'0.5 Negative\', \'0.6 Negative\', \'0.7 Negative\', \'0.8 Negative\', \'1.1 Positive\', \'1.1 Positive\','),(54,'Cytomegalo Virus IgG',10,'خيارات','هرمونات مشترك','2021-02-23 23:40:00',NULL,NULL,'\'0.5 Negative\', \'0.6 Negative\', \'0.7 Negative\', \'0.8 Negative\', \'1.1 Positive\', \'1.1 Positive\','),(55,'Cytomegalo Virus IgM',10,'خيارات','هرمونات مشترك','2021-02-23 23:40:25',NULL,NULL,'\'0.5 Negative\', \'0.6 Negative\', \'0.7 Negative\', \'0.8 Negative\', \'1.1 Positive\', \'1.1 Positive\','),(56,'Rubella IgG',10,'خيارات','هرمونات مشترك','2021-02-23 23:40:45',NULL,NULL,'\'0.5 Negative\', \'0.6 Negative\', \'0.7 Negative\', \'0.8 Negative\', \'1.1 Positive\', \'1.1 Positive\','),(57,'Rubella IgM',10,'خيارات','هرمونات مشترك','2021-02-23 23:36:56',NULL,NULL,'\'0.5 Negative\', \'0.6 Negative\', \'0.7 Negative\', \'0.8 Negative\', \'1.1 Positive\', \'1.1 Positive\','),(58,'Anti - Phspholipin IgG',10,'خيارات','هرمونات مشترك','2021-02-23 23:41:17',NULL,NULL,'\'0.5 Negative\', \'0.6 Negative\', \'0.7 Negative\', \'0.8 Negative\', \'1.1 Positive\', \'1.1 Positive\','),(59,'Anti - Phspholipin  IgM',10,'خيارات','هرمونات مشترك','2021-02-23 23:41:44','klskks','jxdn','\'0.5 Negative\', \'0.6 Negative\', \'0.7 Negative\', \'0.8 Negative\', \'1.1 Positive\', \'1.1 Positive\','),(60,'Anti - Cardiolipin  IgG',10,'خيارات','هرمونات مشترك','2021-02-23 23:41:58',NULL,NULL,'\'0.5 Negative\', \'0.6 Negative\', \'0.7 Negative\', \'0.8 Negative\', \'1.1 Positive\', \'1.1 Positive\','),(61,'Anti - Cardiolipin  IgM',10,'خيارات','هرمونات مشترك','2021-02-23 23:42:14','oeoke','oiejj','\'0.5 Negative\', \'0.6 Negative\', \'0.7 Negative\', \'0.8 Negative\', \'1.1 Positive\', \'1.1 Positive\','),(62,'Herps   IgG',10,'خيارات','هرمونات مشترك','2021-02-23 23:42:34',NULL,NULL,'\'0.5 Negative\', \'0.6 Negative\', \'0.7 Negative\', \'0.8 Negative\', \'1.1 Positive\', \'1.1 Positive\','),(63,'Herpes  IgM',10,'خيارات','هرمونات مشترك','2021-02-23 23:42:50',NULL,NULL,'\'0.5 Negative\', \'0.6 Negative\', \'0.7 Negative\', \'0.8 Negative\', \'1.1 Positive\', \'1.1 Positive\','),(65,'Volume',0,'خيارات','Full SFA',NULL,NULL,NULL,'\'0.5\', \'0.6\', \'0.7\''),(66,'Reaction:SFA',0,'خيارات','Full SFA',NULL,NULL,NULL,'\'Acidic\', \'Alkaline\''),(67,'Colour:SFA',0,'خيارات','Full SFA',NULL,NULL,NULL,'\'yallow\', \'brown\', \'green\', \'milk\''),(68,'Liquefaction',0,'خيارات','Full SFA',NULL,NULL,NULL,'\'5\', \'10\', \'15\', \'20\', \'25\', \'30\', \'35\', \'40\', \'45\''),(69,'Count',0,'عدد','Full SFA',NULL,NULL,NULL,NULL),(70,'Motility:Active',0,'خيارات','Full SFA',NULL,NULL,NULL,'\'5\', \'10\', \'15\', \'20\', \'25\', \'30\', \'35\', \'40\', \'45\', \'50\', \'55\', \'60\', \'65\', \'70\', \'75\', \'80\','),(71,'Motility:Sluggish',0,'خيارات','Full SFA',NULL,NULL,NULL,'\'5\', \'10\', \'15\', \'20\', \'25\', \'30\', \'35\', \'40\', \'45\', \'50\', \'55\', \'60\', \'65\', \'70\', \'75\', \'80\','),(72,'Motility:Dead',0,'خيارات','Full SFA',NULL,NULL,NULL,'\'5\', \'10\', \'15\', \'20\', \'25\', \'30\', \'35\', \'40\', \'45\', \'50\', \'55\', \'60\', \'65\', \'70\', \'75\', \'80\','),(73,'Morphology:Normal',0,'خيارات','Full SFA',NULL,NULL,NULL,'\'5\', \'10\', \'15\', \'20\', \'25\', \'30\', \'35\', \'40\', \'45\', \'50\', \'55\', \'60\', \'65\', \'70\', \'75\', \'80\','),(74,'Morphology:Abnormal',0,'خيارات','Full SFA',NULL,NULL,NULL,'\'5\', \'10\', \'15\', \'20\', \'25\', \'30\', \'35\', \'40\', \'45\', \'50\', \'55\', \'60\', \'65\', \'70\', \'75\', \'80\','),(75,'Morphology:Pus cells',0,'خيارات','Full SFA',NULL,NULL,NULL,'\'5\', \'10\', \'15\', \'20\', \'25\', \'30\', \'35\', \'40\', \'45\', \'50\', \'55\', \'60\', \'65\', \'70\', \'75\', \'80\','),(76,'Other:SFA',0,'خيارات','Full SFA',NULL,NULL,NULL,NULL),(77,'HBS Ag',5,'خيارات','hematology',NULL,NULL,NULL,NULL),(78,'HCV Ab',5,'خيارات','hematology',NULL,NULL,NULL,NULL),(79,'HIV',5,'خيارات','hematology',NULL,NULL,NULL,NULL),(80,'Bacteria:GSE',0,'خيارات','Full GSE',NULL,NULL,NULL,'\'Few\', \'+\', \'++\', \'+++\', \'++++\''),(81,'Monillia:GSE',0,'خيارات','Full GSE',NULL,NULL,NULL,'\'Few\', \'+\', \'++\', \'+++\', \'++++\''),(82,'Fatty drop:GSE',0,'خيارات','Full GSE',NULL,NULL,NULL,'\'Few\', \'+\', \'++\', \'+++\', \'++++\''),(83,'Bacteria:GUE',0,'خيارات','Full GUE',NULL,NULL,NULL,'\'Few\', \'+\', \'++\', \'+++\', \'++++\''),(84,'Monillia:GUE',0,'خيارات','Full GUE',NULL,NULL,NULL,'\'Few\', \'+\', \'++\', \'+++\', \'++++\''),(85,'Mucuse:GUE',0,'خيارات','Full GUE',NULL,NULL,NULL,'\'Few\', \'+\', \'++\', \'+++\', \'++++\''),(87,'new2',6,'خيارات','bio','2021-04-27 18:18:29','none','no','\'gg\', \'   hello\', \'   hi\', \' yah my boy\''),(88,'',2,'Full GUE','new sub_category','2021-04-21 02:18:29','kk','mm',''),(89,'rnfvikjwhnerivn',2,'عدد','new sub_category','2021-04-21 02:31:59','sergwr','  knlajncfl',''),(90,'please',2,'عدد','bio','2021-04-21 02:36:40','nn','mm',''),(91,'tr3trh4th',2,'حقل كتابة','Full GSE','2021-04-21 02:41:07','vv','v','');
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
  `date` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `addbuys`
--

LOCK TABLES `addbuys` WRITE;
/*!40000 ALTER TABLE `addbuys` DISABLE KEYS */;
INSERT INTO `addbuys` VALUES (1,'ali',21,100,'--------------',16,'2000-01-01'),(3,'item_name',10,100,'item_type',18,'2021-02-12'),(4,'منتج',10,50,NULL,5,'2021-04-25');
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
) ENGINE=InnoDB AUTO_INCREMENT=1738 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `addclient`
--

LOCK TABLES `addclient` WRITE;
/*!40000 ALTER TABLE `addclient` DISABLE KEYS */;
INSERT INTO `addclient` VALUES (1732,'علي محمود قاسم عليوي فاضل',20,'ذكر','عدوية شمس سعيد','2021-04-30 02:54:02'),(1733,'علي محمود قاسم عليوي فاضل',20,'ذكر','عدوية شمس سعيد','2021-04-30 02:55:37'),(1734,'jjekekd',20,'انثى','عدوية شمس سعيد','2021-04-30 04:21:44'),(1735,'jjekekd',20,'انثى','عدوية شمس سعيد','2021-04-30 04:21:47'),(1736,'jjekekd',20,'انثى','عدوية شمس سعيد','2021-04-30 04:21:59'),(1737,'jjekekd',20,'انثى','عدوية شمس سعيد','2021-04-30 04:26:19');
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
  `sub_category` varchar(455) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1700 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `addnewitem`
--

LOCK TABLES `addnewitem` WRITE;
/*!40000 ALTER TABLE `addnewitem` DISABLE KEYS */;
INSERT INTO `addnewitem` VALUES (1696,'jjekekd',1734,20,'انثى','عدوية شمس سعيد','','Random  blood sugar','12',2,'2','2021-04-30 04:21:44','bio'),(1697,'jjekekd',1734,20,'انثى','عدوية شمس سعيد','','Random  blood sugar','12',2,'2','2021-04-30 04:21:48','bio'),(1698,'jjekekd',1734,20,'انثى','عدوية شمس سعيد','','Blood Urea','1',3,'3','2021-04-30 04:21:59','bio'),(1699,'jjekekd',1734,20,'انثى','عدوية شمس سعيد','','Color:GSE','yallow',3,'0','2021-04-29 04:26:19','Full GSE');
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
  `user_email` varchar(255) NOT NULL,
  `date` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `adduser`
--

LOCK TABLES `adduser` WRITE;
/*!40000 ALTER TABLE `adduser` DISABLE KEYS */;
INSERT INTO `adduser` VALUES (3,'ameer','5','a','2021-04-30 03:34:43'),(4,'ali','5','a','2021-04-30 03:34:43'),(5,'ah','55','a','2021-04-30 03:34:43'),(6,'new','1','newemail','2021-04-30 07:07:35'),(7,'test','5','newemailtest','2021-04-30 07:26:39');
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
  `name` varchar(255) DEFAULT NULL,
  `genus` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `doctor`
--

LOCK TABLES `doctor` WRITE;
/*!40000 ALTER TABLE `doctor` DISABLE KEYS */;
INSERT INTO `doctor` VALUES (1,'عدوية شمس سعيد','female'),(2,'داود سلمان','male');
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
  `uid` varchar(255) DEFAULT NULL,
  `action` int DEFAULT NULL,
  `tabled` int DEFAULT NULL,
  `dates` datetime DEFAULT NULL,
  `def` int NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2539 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `his`
--

LOCK TABLES `his` WRITE;
/*!40000 ALTER TABLE `his` DISABLE KEYS */;
INSERT INTO `his` VALUES (2527,'ali',1,5,'2021-04-30 06:40:59',1),(2528,'ali',1,5,'2021-04-30 06:45:52',1),(2529,'ali',1,5,'2021-04-30 06:54:29',1),(2530,'ali',1,5,'2021-04-30 06:58:13',1),(2531,'ali',1,5,'2021-04-30 06:59:05',1),(2532,'ali',1,5,'2021-04-30 07:06:43',1),(2533,'new',1,5,'2021-04-30 07:06:58',1),(2534,'ali',1,5,'2021-04-30 07:07:20',1),(2535,'ali',1,5,'2021-04-30 07:10:50',1),(2536,'ali',1,5,'2021-04-30 07:14:32',1),(2537,'ali',1,5,'2021-04-30 07:15:58',1),(2538,'ali',1,5,'2021-04-30 07:26:20',1);
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
INSERT INTO `paths` VALUES (1,'F:\\a tahlel project 2','F:\\a tahlel project 2');
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
  `employee_name` varchar(255) NOT NULL,
  `add_sale_item_page` int NOT NULL,
  `sales_page` int NOT NULL,
  `analyst_page` int NOT NULL,
  `statics` int NOT NULL,
  `clients_page` int NOT NULL,
  `history_page` int NOT NULL,
  `settings_page` int NOT NULL,
  `add_analyst` int NOT NULL,
  `edit_analyst` int NOT NULL,
  `delete_analyst` int NOT NULL,
  `change_theme` int NOT NULL,
  `add_buys` int NOT NULL,
  `edit_report` int NOT NULL,
  `change_path` int NOT NULL,
  `delet_history` int NOT NULL,
  `add_user` int NOT NULL,
  `edit_user` int NOT NULL,
  `delete_user` int NOT NULL,
  `search_by_date_in_sales_page` int NOT NULL,
  `show_clients` int NOT NULL,
  `search_client` int NOT NULL,
  `search_client_info` int NOT NULL,
  `prev_report` int NOT NULL,
  `print_report` int NOT NULL,
  `search_in_all_sales` int NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `userper`
--

LOCK TABLES `userper` WRITE;
/*!40000 ALTER TABLE `userper` DISABLE KEYS */;
INSERT INTO `userper` VALUES (4,'ameer',0,0,0,1,0,1,1,1,0,1,0,1,0,1,1,0,1,0,0,0,1,1,1,0,0),(5,'ameer',0,0,0,1,0,1,1,1,0,1,0,1,0,1,1,0,1,0,0,0,1,1,1,0,0),(6,'ah',1,0,0,1,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0),(7,'new',1,1,1,1,1,1,1,0,1,0,1,1,1,1,0,1,1,1,1,1,0,1,1,0,1),(8,'test',1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1);
/*!40000 ALTER TABLE `userper` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `word`
--

DROP TABLE IF EXISTS `word`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `word` (
  `id` int NOT NULL AUTO_INCREMENT,
  `shop_name` varchar(45) DEFAULT NULL,
  `phone1` varchar(45) DEFAULT NULL,
  `phone2` varchar(45) DEFAULT NULL,
  `employee_name1` varchar(45) DEFAULT NULL,
  `employee_name2` varchar(45) DEFAULT NULL,
  `employee1_shahada` varchar(45) DEFAULT NULL,
  `employee2_shahada` varchar(45) DEFAULT NULL,
  `gps` varchar(455) DEFAULT NULL,
  `client_name` varchar(45) DEFAULT NULL,
  `client_lqb` varchar(45) DEFAULT NULL,
  `doctor_name` varchar(45) DEFAULT NULL,
  `doctor_lqb` varchar(45) DEFAULT NULL,
  `client_name2` varchar(45) DEFAULT NULL,
  `client_lqb2` varchar(45) DEFAULT NULL,
  `doctor_name2` varchar(45) DEFAULT NULL,
  `doctor_lqb2` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `word`
--

LOCK TABLES `word` WRITE;
/*!40000 ALTER TABLE `word` DISABLE KEYS */;
INSERT INTO `word` VALUES (1,'مختبر O3','07803353441','07733336462','لارا عواد مظهر','عمر رحيم عبد الله','بكالوريوس تحليلات مرضية','دبلوم تحليلات مرضية','الضلوعية_مركز القضاء_مجمع الحياة_مجاور مستشفى الحارث الاهلي','أسـم المريض','المحترم','حضرة الدكتور','المحترم','اسم المريضة','المحترمة','حضرة الدكتورة','المحترمة');
/*!40000 ALTER TABLE `word` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-04-30  7:41:57
