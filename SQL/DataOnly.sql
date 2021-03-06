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
-- Dumping data for table `addanalyst`
--

LOCK TABLES `addanalyst` WRITE;
/*!40000 ALTER TABLE `addanalyst` DISABLE KEYS */;
INSERT INTO `addanalyst` VALUES (5,'Random  blood sugar',2,'حقل كتابة','Biochemistry','2021-05-11 18:39:48','mg / dl','( 80 - 140 )','',NULL,1),(6,'Blood Urea',3,'حقل كتابة','Biochemistry','2021-02-22 23:11:50',' mg / dl','( 20 - 45 )',NULL,NULL,2),(7,'S. Creatinin',3,'حقل كتابة','Biochemistry','2021-02-22 23:13:53','mg / dl','( 0.7 - 1.4 )',NULL,NULL,3),(8,'S. Uric acid',3,'حقل كتابة','Biochemistry','2021-06-06 00:07:15','mg/dl','( 3-7 )','',NULL,4),(9,'S. Cholesterol',3,'حقل كتابة','Biochemistry','2021-02-22 23:15:47','mg / dl','( 150 - 250 )',NULL,NULL,5),(10,'S. Triglycerid',3,'حقل كتابة','Biochemistry','2021-02-22 23:16:20','mg / dl','( 65 - 180 )',NULL,NULL,6),(11,'Total serum Bilirubin',3,'حقل كتابة','Biochemistry','2021-02-22 23:17:26','mg / dl','( 0.3 - 1.0 )',NULL,6,7),(12,'S.Calcium',3,'حقل كتابة','Biochemistry','2021-02-22 23:18:14','mg / dl','( 8.8 - 10.2 )',NULL,NULL,8),(13,'Vitamin D',15,'حقل كتابة','Biochemistry','2021-02-22 23:18:58','ng / dl','( 30 - 70 )',NULL,NULL,9),(14,'Color ',3,'خيارات','General Stool Examination','2021-06-12 10:59:48',' ',' ','\'milky\', \'yallow\', \'brown\', \'green\', \'\'',NULL,1),(15,'Consistency',0,'خيارات','General Stool Examination','2021-06-08 22:19:45','','','\'Solid\', \'Liquid\', \'Semi solid\', \'Semi liquid\', \'Mucoid\', \'  \'',NULL,2),(16,'R.B.Cs',0,'خيارات','General Stool Examination','2021-06-10 17:25:44','/ H.P.F','','\'Nil\', \'0-1\', \'0-2\', \'1-2\', \'1-3\', \'2-4\', \'3-5\', \'4-6\', \'6-8\', \'Few\', \'+\', \'++\', \'+++\', \'++++\', \'\'',NULL,3),(18,'E.Histolytica',0,'خيارات','General Stool Examination','2021-06-10 22:38:57','','','\'Nil\', \'Cyst\', \'Trophozoite\', \'\'',NULL,5),(19,'G.Lamblia',0,'خيارات','General Stool Examination','2021-06-10 22:40:16','','','\'Nil\', \'Cyst\', \'Trophozoite\', \'\'',NULL,6),(22,'Appearance',3,'خيارات','General Urine Examination','2021-02-22 23:26:16','','','\'Turbid\', \'Clear\', \' \'',NULL,1),(23,'Reaction.',0,'خيارات','General Urine Examination','2021-06-12 17:05:55','','','\'Acidic\', \' Alkaline\', \'\'',NULL,2),(24,'Albumin',0,'خيارات','General Urine Examination','2021-02-22 23:26:57','','','\'Nil\', \'+\', \'++\', \'+++\', \'Trace\', \' \'',NULL,3),(25,'Pus cells..',0,'خيارات','General Urine Examination','2021-06-10 17:52:18','/ H.P.F','','\'Nil\', \'0-1\', \'0-2\', \'1-2\', \'2-3\', \'3-5\', \'4-6\', \'6-8\', \'+\', \'++\', \'+++\', \'++++\', \'\', \'\'',NULL,7),(26,'RBCs',0,'خيارات','General Urine Examination','2021-06-10 17:27:28','/ H.P.F','','\'Nil\', \'0-1\', \'0-2\', \'1-2\', \'1-3\', \'2-3\', \'2-4\', \'3-5\', \'4-6\', \'6-8\', \'Few\', \'+\', \'++\', \'+++\', \'++++\', \'\'',NULL,6),(27,'Pus cells,',0,'خيارات','General Stool Examination','2021-06-10 17:23:42','/ H.P.F','','\'Nil\', \'0-1\', \'0-2\', \'1-2\', \'2-3\', \'3-5\', \'4-6\', \'5-7\', \'6-8\', \'+\', \'++\', \'+++\', \'++++\', \'\'',NULL,4),(28,'Epith .cells',0,'خيارات','General Urine Examination','2021-06-10 17:17:20','/ H.P.F','','\'Nil\', \'Few\', \'+\', \'++\', \'+++\', \'++++\', \'\'',NULL,8),(29,'Crystals',0,'خيارات','General Urine Examination','2021-06-12 16:47:15','','','\'Nil\', \'Am.Urate few\', \'Am.Urate +\', \'Am.Urate ++\', \'Am.Urate +++\', \'Am.Urate ++++\', \' Ca.Oxalate few\', \' Ca.Oxalate +\', \' Ca.Oxalate ++\', \' Ca.Oxalate +++\', \' Ca.Oxalate ++++\', \' Uric Acid few\', \' Uric Acid +\', \' Uric Acid ++\', \' Uric Acid +++\', \' Uric Acid ++++\', \' Am.Phosphatase +\', \' Am.Phosphatase ++\', \' Am.Phosphatase +++\', \' Am.Phosphatase ++++\', \' Am.Phosphatase few\', \'\'',NULL,9),(30,'Casts',0,'خيارات','General Urine Examination','2021-06-10 17:15:26','','','\'Nil\', \'Granular cast +\', \'Granular cast ++\', \'Granular cast +++\', \'\'',NULL,10),(32,'Hb',3,'حقل كتابة',' Hematology and Serology','2021-02-22 23:31:12','gm/dl','','4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, \' \'',NULL,7),(33,'PCV',0,'حقل كتابة',' Hematology and Serology','2021-07-04 18:43:20','%','','',NULL,8),(34,'WBCs',3,'حقل كتابة',' Hematology and Serology','2021-07-04 18:51:14','cells/cumm','','',NULL,8),(35,'E.S.R',3,'حقل كتابة',' Hematology and Serology','2021-02-22 23:32:33','mm/1 hr','','',NULL,10),(36,'Blood Group',3,'خيارات',' Hematology and Serology','2021-06-12 10:13:41',' ',' ','\'\', \'A (+ve)\', \'B (+ve)\', \'AB (+ve)\', \'O (+ve)\', \'O (-ve)\', \'A (-ve)\', \'B (-ve)\', \'AB (-ve)\', \'\'',NULL,1),(37,'Rh',0,'خيارات',' Hematology and Serology','2021-06-08 22:59:07','','','\' \', \'Positive (+ve)\', \'Negative (-ve)\', \'\'',NULL,2),(38,'Pregnancy test  in urine',3,'خيارات',' Hematology and Serology','2021-06-11 21:02:36','','','\'\', \'Positive (+ve)\', \'Negative (-ve)\', \'Weak Positive\', \'\'',NULL,11),(39,'Pregnancy test  in serum',3,'خيارات',' Hematology and Serology','2021-07-05 17:32:51','','','\'\', \'Positive (+ve)\', \'Negative (-ve)\', \'Weak Positive\', \'\'',NULL,1),(40,'R.B.Sugar',2,'حقل كتابة',' Hematology and Serology','2021-02-22 23:35:07','mg/dl','',NULL,NULL,3),(41,'Bl. Urea',3,'حقل كتابة',' Hematology and Serology','2021-02-22 23:35:28','mg/dl','',NULL,NULL,22),(42,'Salmonella typhi  IgG',4,'خيارات',' Hematology and Serology','2021-06-12 10:15:04','','','\'\', \'Positive (+ve)\', \'Negative (-ve)\', \'\'',NULL,13),(43,'Salmonella typhi  IgM',0,'خيارات',' Hematology and Serology','2021-06-12 10:15:38','','','\'\', \'Positive (+ve)\', \'Negative (-ve)\', \'\'',NULL,14),(44,'Rose-Bengal test',3,'خيارات',' Hematology and Serology','2021-06-12 10:16:21','','','\'\', \'Positive (+ve)\', \'Negative (-ve)\', \'\'',NULL,15),(45,'T3',7,'حقل كتابة','Hormones and Viruses','2021-02-23 23:10:14','ng / ml','( 0.6 - 1.85 )',NULL,NULL,13),(46,'T4',7,'حقل كتابة','Hormones and Viruses','2021-02-23 23:11:06','g / dl','Females (4.8 - 12.0 )  males (4.4 - 10.8 )',NULL,NULL,14),(47,'TSH',7,'حقل كتابة','Hormones and Viruses','2021-02-23 23:11:36','IU /ml','(0.4 - 7.0 )',NULL,NULL,15),(48,'LH',10,'حقل كتابة','Hormones and Viruses','2021-02-23 23:12:03','m Iu/ml','',NULL,NULL,16),(49,'FSH',10,'حقل كتابة','Hormones and Viruses','2021-02-23 23:12:41','m IU/ml','',NULL,NULL,17),(50,'Prolactin',15,'حقل كتابة','Hormones and Viruses','2021-02-23 23:13:23','ng / ml','women-non gestation 4.5-25 men ( 3.7 - 17.5 )',NULL,NULL,18),(51,'Testosterone',10,'حقل كتابة','Hormones and Viruses','2021-06-08 23:31:03','ng/ml','','',NULL,19),(52,'Toxoplasma IgG',25,'خيارات','Hormones and Viruses','2021-06-12 09:38:40','','','\'\', \'Negative (-ve)\', \'Positive (+ve)\', \'0.5 Negative\', \'0.6 Negative\', \'0.7 Negative\', \'0.8 Negative\', \'1.1 Positive\', \'1.1 Positive\', \'1.2 Positive\', \'1.3 Positive\', \'1.4 Positive\', \'1.5 Positive\', \'\'',NULL,1),(53,'Toxoplasma IgM',0,'خيارات','Hormones and Viruses','2021-06-12 09:44:10','','','\'\', \'Negative (-ve)\', \'Positive (+ve)\', \'0.5 Negative\', \'0.6 Negative\', \'0.7 Negative\', \'0.8 Negative\', \'1.1 Positive\', \'1.1 Positive\', \'1.2 Positive\', \'1.3 Positive\', \'1.4 Positive\', \'1.5 Positive\', \'\'',NULL,2),(54,'Cytomegalo Virus IgG',0,'خيارات','Hormones and Viruses','2021-06-12 09:47:23','','','\'\', \'Negative (-ve)\', \'Positive (+ve)\', \'0.5 Negative\', \'0.6 Negative\', \'0.7 Negative\', \'0.8 Negative\', \'1.1 Positive\', \'1.1 Positive\', \'1.2 Positive\', \'1.3 Positive\', \'1.4 Positive\', \'1.5 Positive\', \'\'',NULL,3),(55,'Cytomegalo Virus IgM',0,'خيارات','Hormones and Viruses','2021-06-12 09:50:06','','','\'\', \'Negative (-ve)\', \'Positive (+ve)\', \'0.5 Negative\', \'0.6 Negative\', \'0.7 Negative\', \'0.8 Negative\', \'1.1 Positive\', \'1.1 Positive\', \'1.2 Positive\', \'1.3 Positive\', \'1.4 Positive\', \'1.5 Positive\', \'\'',NULL,4),(56,'Rubella IgG',0,'خيارات','Hormones and Viruses','2021-06-12 09:54:39','','','\'\', \'Negative (-ve)\', \'Positive (+ve)\', \'0.5 Negative\', \'0.6 Negative\', \'0.7 Negative\', \'0.8 Negative\', \'1.1 Positive\', \'1.1 Positive\', \'1.2 Positive\', \'1.3 Positive\', \'1.4 Positive\', \'1.5 Positive\', \'\'',NULL,5),(57,'Rubella IgM',0,'خيارات','Hormones and Viruses','2021-06-12 09:57:15','','','\'\', \'Negative (-ve)\', \'Positive (+ve)\', \'0.5 Negative\', \'0.6 Negative\', \'0.7 Negative\', \'0.8 Negative\', \'1.1 Positive\', \'1.1 Positive\', \'1.2 Positive\', \'1.3 Positive\', \'1.4 Positive\', \'1.5 Positive\', \'\'',NULL,6),(58,'Anti - Phspholipin IgG',35,'خيارات','Hormones and Viruses','2021-02-23 23:41:17','','','\'0.5 Negative\', \'0.6 Negative\', \'0.7 Negative\', \'0.8 Negative\', \'1.1 Positive\', \'1.1 Positive\',\'1.2 Positive\', \'1.3 Positive\', \'1.4 Positive\', \'1.5 Positive\', \' \'',NULL,9),(59,'Anti - Phspholipin  IgM',0,'خيارات','Hormones and Viruses','2021-02-23 23:41:44',' ',' ','\'0.5 Negative\', \'0.6 Negative\', \'0.7 Negative\', \'0.8 Negative\', \'1.1 Positive\', \'1.1 Positive\',\'1.2 Positive\', \'1.3 Positive\', \'1.4 Positive\', \'1.5 Positive\', \' \'',NULL,10),(60,'Anti - Cardiolipin  IgG',0,'خيارات','Hormones and Viruses','2021-02-23 23:41:58','','','\'0.5 Negative\', \'0.6 Negative\', \'0.7 Negative\', \'0.8 Negative\', \'1.1 Positive\', \'1.1 Positive\',\'1.2 Positive\', \'1.3 Positive\', \'1.4 Positive\', \'1.5 Positive\', \' \'',NULL,11),(61,'Anti - Cardiolipin  IgM',0,'خيارات','Hormones and Viruses','2021-02-23 23:42:14',' ',' ','\'0.5 Negative\', \'0.6 Negative\', \'0.7 Negative\', \'0.8 Negative\', \'1.1 Positive\', \'1.1 Positive\',\'1.2 Positive\', \'1.3 Positive\', \'1.4 Positive\', \'1.5 Positive\', \' \'',NULL,12),(62,'Herps   IgG',0,'خيارات','Hormones and Viruses','2021-06-12 09:59:58','','','\'\', \'Negative (-ve)\', \'Positive (+ve)\', \'0.5 Negative\', \'0.6 Negative\', \'0.7 Negative\', \'0.8 Negative\', \'1.1 Positive\', \'1.1 Positive\', \'1.2 Positive\', \'1.3 Positive\', \'1.4 Positive\', \'1.5 Positive\', \'\'',NULL,7),(63,'Herpes  IgM',0,'خيارات','Hormones and Viruses','2021-06-12 10:02:40','','','\'\', \'Negative (-ve)\', \'Positive (+ve)\', \'0.5 Negative\', \'0.6 Negative\', \'0.7 Negative\', \'0.8 Negative\', \'1.1 Positive\', \'1.1 Positive\', \'1.2 Positive\', \'1.3 Positive\', \'1.4 Positive\', \'1.5 Positive\', \'\'',NULL,8),(65,'Volume',3,'خيارات','Seminal Fluid Analysis','2021-06-12 10:48:06','ml','','\' \', \'1\', \'2\', \'3\', \'4\', \'5\', \'0.2\', \'0.3\', \'0.3\', \'0.4\', \'0.5\', \'0.6\', \'0.7\', \'0.8\', \'0.9\', \'\'',NULL,1),(66,'Reaction',0,'خيارات','Seminal Fluid Analysis','2021-06-08 23:22:40','','','\'Acidic\', \' Alkaline\', \' \'',NULL,2),(68,'Liquefaction',0,'خيارات','Seminal Fluid Analysis','2021-06-12 10:51:41','min.','','\'30\', \'5\', \'10\', \'15\', \'20\', \'25\', \'35\', \'40\', \'45\', \' \'',NULL,1),(69,'Count',0,'حقل كتابة','Seminal Fluid Analysis',NULL,'million/ml','',NULL,NULL,5),(70,'Motility:Active',0,'خيارات','Seminal Fluid Analysis','2021-05-21 18:41:52','%','','\'  10\', \'  15\', \'  20\', \'  25\', \'  30\', \'  35\', \'  40\', \'  45\', \'  50\', \'  55\', \'  60\', \'  65\', \'  70\', \'  75\', \'  80\', \' \', \' 5\', \' \'',NULL,6),(71,'Motility:Sluggish',0,'خيارات','Seminal Fluid Analysis','2021-05-21 18:41:12','%','','\' 5\', \'10\', \'15\', \'20\', \'25\', \'30\', \'35\', \'40\', \'45\', \'50\', \'55\', \'60\', \'65\', \'70\', \'75\', \'80\', \' \'',NULL,7),(72,'Motility:Dead',0,'خيارات','Seminal Fluid Analysis','2021-05-21 18:41:27','%','','\' 5\', \'10\', \'15\', \'20\', \'25\', \'30\', \'35\', \'40\', \'45\', \'50\', \'55\', \'60\', \'65\', \'70\', \'75\', \'80\', \' \'',NULL,8),(73,'Morphology:Normal',0,'خيارات','Seminal Fluid Analysis',NULL,'%','','\' 5\', \'10\', \'15\', \'20\', \'25\', \'30\', \'35\', \'40\', \'45\', \'50\', \'55\', \'60\', \'65\', \'70\', \'75\', \'80\', \' \'',NULL,9),(74,'Morphology:Abnormal',0,'خيارات','Seminal Fluid Analysis',NULL,'%','','\' 5\', \'10\', \'15\', \'20\', \'25\', \'30\', \'35\', \'40\', \'45\', \'50\', \'55\', \'60\', \'65\', \'70\', \'75\', \'80\', \' \'',NULL,10),(75,' Pus cells:',0,'خيارات','Seminal Fluid Analysis','2021-06-08 22:44:48','/ H.P.F','','\'1-2\', \'1-3\', \'2-3\', \'2-4\', \'4-6\', \'3-5\', \'5-7\', \'6-8\', \'4-5\', \'+\', \'++\', \'+++\', \'++++\', \' \', \' \', \' \'',NULL,11),(77,'HBS Ag',5,'خيارات',' Hematology and Serology','2021-06-08 23:06:00','','','\' \', \'Positive (+ve)\', \'Negative (-ve)\', \'\'',NULL,4),(78,'HCV Ab',5,'خيارات',' Hematology and Serology','2021-06-08 23:08:03','','','\' \', \'Positive (+ve)\', \'Negative (-ve)\', \'\'',NULL,5),(79,'HIV',5,'خيارات',' Hematology and Serology','2021-06-08 23:08:58','','','\' \', \'Positive (+ve)\', \'Negative (-ve)\', \'\'',NULL,6),(80,'Bacteria',0,'خيارات','General Stool Examination','2021-06-10 17:07:57','','','\'Nil\', \'Few\', \'+\', \'++\', \'+++\', \'++++\', \'\'',NULL,8),(81,'Monillia.',0,'خيارات','General Stool Examination','2021-06-10 22:29:16','','','\'Nil\', \'Few\', \'+\', \'++\', \'+++\', \'++++\', \'\'',NULL,9),(82,'Fatty drop',0,'خيارات','General Stool Examination','2021-06-10 22:36:03','','','\'Nil\', \'Few\', \'+\', \'++\', \'+++\', \'++++\', \'\'',NULL,10),(83,'Bacteria. ',0,'خيارات','General Urine Examination','2021-06-10 17:08:57','','','\'Nil\', \'Few\', \'+\', \'++\', \'+++\', \'++++\', \'\'',NULL,11),(84,'Monillia',0,'خيارات','General Urine Examination','2021-06-10 22:30:08','','','\'Nil\', \'Few\', \'+\', \'++\', \'+++\', \'++++\', \'\'',NULL,12),(85,'sugar',0,'خيارات','General Urine Examination','2021-06-10 17:10:09','','','\'Nil\', \'Few\', \'+\', \'++\', \'+++\', \'++++\', \'\'',NULL,4),(98,'HbA1C',15,'حقل كتابة','Biochemistry','2021-06-06 00:06:40','%','( 4.2 - 6.2 )','',NULL,10),(99,'B - HCG titer',15,'حقل كتابة',' Hematology and Serology','2021-06-06 01:18:37','mIU/ml','( Less than 10 )','',NULL,21),(100,'lha',0,'حقل كتابة','Hormones and Viruses','2021-06-06 01:25:46','','','',NULL,20),(101,'H.Pylori in Serum',10,'خيارات',' Hematology and Serology','2021-06-10 09:30:50','','','\'\', \'Positive (+ve)\', \'Negative (-ve)\'',NULL,19),(102,'H.Pylori in Stool',10,'خيارات',' Hematology and Serology','2021-06-10 09:31:46','','','\'\', \'Positive (+ve)\', \'Negative (-ve)\'',NULL,20),(103,'Reumatoid Facter',3,'خيارات',' Hematology and Serology','2021-06-10 09:50:51','','','\'\', \'Positive (+ve)\', \'Negative (-ve)\'',NULL,16),(104,'A.S.O titer',3,'خيارات',' Hematology and Serology','2021-06-10 09:55:23','','','\'\', \'Negative (-ve)\', \'Positive (+ve) 1/200\', \'Positive (+ve) 1/400\', \'Positive (+ve) 1/600\', \'Positive (+ve) 1/800\', \'Positive (+ve) 1/1000\', \'Positive (+ve) 1/1200\', \'Positive (+ve) 1/1400\', \'Positive (+ve) 1/1600\', \'Positive (+ve) 1/1800\', \'\'',NULL,17),(105,'C.Reactive Protein',3,'خيارات',' Hematology and Serology','2021-06-10 09:58:29','','','\'\', \'Positive (+ve)\', \'Negative (-ve)\', \'\'',NULL,18),(106,'HAV',5,'خيارات',' Hematology and Serology','2021-06-10 10:01:04','','','\'\', \'Positive (+ve)\', \'Negative (-ve)\', \'\'',NULL,23),(108,'Mucus',0,'خيارات','General Urine Examination','2021-06-10 17:56:26','','','\'Nil\', \'Few\', \'+\', \'++\', \'+++\', \'++++\', \'\'',NULL,13),(114,'F.Blood Sugar:',0,'حقل كتابة','Oral Glucose Tolerance Test (O.G.T.T)','2021-06-19 19:32:03','mg/dl','','',NULL,1),(115,'Blood sugar:',0,'حقل كتابة','Oral Glucose Tolerance Test (O.G.T.T)','2021-06-19 19:33:18','mg/dl','after 1/2 hr.','',NULL,2),(116,'Blood Sugar:-',0,'حقل كتابة','Oral Glucose Tolerance Test (O.G.T.T)','2021-06-19 19:34:18','mg/dl','after 1  hr.','',NULL,3),(117,'Blood Sugar,,',0,'حقل كتابة','Oral Glucose Tolerance Test (O.G.T.T)','2021-06-19 19:35:32','mg/dl','after 1 hr. and 30 min.','',NULL,4),(118,'Blood Sugar;',12,'حقل كتابة','Oral Glucose Tolerance Test (O.G.T.T)','2021-06-19 19:36:38','mg/dl','after  2 hr.','',NULL,5);
/*!40000 ALTER TABLE `addanalyst` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `addbuys`
--

LOCK TABLES `addbuys` WRITE;
/*!40000 ALTER TABLE `addbuys` DISABLE KEYS */;
/*!40000 ALTER TABLE `addbuys` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `addclient`
--

LOCK TABLES `addclient` WRITE;
/*!40000 ALTER TABLE `addclient` DISABLE KEYS */;
/*!40000 ALTER TABLE `addclient` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `addnewitem`
--

LOCK TABLES `addnewitem` WRITE;
/*!40000 ALTER TABLE `addnewitem` DISABLE KEYS */;
/*!40000 ALTER TABLE `addnewitem` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `adduser`
--

LOCK TABLES `adduser` WRITE;
/*!40000 ALTER TABLE `adduser` DISABLE KEYS */;
INSERT INTO `adduser` VALUES (12,'1','n','n','2021-05-30 17:56:37');
/*!40000 ALTER TABLE `adduser` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `category`
--

LOCK TABLES `category` WRITE;
/*!40000 ALTER TABLE `category` DISABLE KEYS */;
INSERT INTO `category` VALUES (12,' Hematology and Serology'),(13,'Biochemistry'),(14,'General Stool Examination'),(15,'General Urine Examination'),(16,'Hormones and Viruses'),(17,'Oral Glucose Tolerance Test (O.G.T.T)'),(18,'Seminal Fluid Analysis');
/*!40000 ALTER TABLE `category` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `doctor`
--

LOCK TABLES `doctor` WRITE;
/*!40000 ALTER TABLE `doctor` DISABLE KEYS */;
INSERT INTO `doctor` VALUES (10,'  ','male');
/*!40000 ALTER TABLE `doctor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `his`
--

LOCK TABLES `his` WRITE;
/*!40000 ALTER TABLE `his` DISABLE KEYS */;
/*!40000 ALTER TABLE `his` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `paths`
--

LOCK TABLES `paths` WRITE;
/*!40000 ALTER TABLE `paths` DISABLE KEYS */;
INSERT INTO `paths` VALUES (1,'C:\\Users\\halla\\Desktop\\MyExeApp-main\\a tahlel project 2\\word for dad','C:\\Users\\halla\\Desktop\\MyExeApp-main\\a tahlel project 2\\word for dad');
/*!40000 ALTER TABLE `paths` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `report`
--

LOCK TABLES `report` WRITE;
/*!40000 ALTER TABLE `report` DISABLE KEYS */;
/*!40000 ALTER TABLE `report` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `userper`
--

LOCK TABLES `userper` WRITE;
/*!40000 ALTER TABLE `userper` DISABLE KEYS */;
INSERT INTO `userper` VALUES (13,'1',1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1);
/*!40000 ALTER TABLE `userper` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `word`
--

LOCK TABLES `word` WRITE;
/*!40000 ALTER TABLE `word` DISABLE KEYS */;
INSERT INTO `word` VALUES (1,'مختبر بغداد','07812385684','','','','','','بلد - شارع بنت الحسن','أسـم المريض :','المحترم','حضرة الدكتور :','المحترم','اسم المريضة :','المحترمة','حضرة الدكتورة :','المحترمة');
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

-- Dump completed on 2021-07-12 18:27:35
