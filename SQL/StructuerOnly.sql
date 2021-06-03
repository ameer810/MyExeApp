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
  `quantity` int DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=99 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

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
  `item_quantity` int DEFAULT NULL,
  `to_analysts` varchar(455) DEFAULT NULL,
  `still_price` int DEFAULT NULL,
  `pushed_price` int DEFAULT NULL,
  `notification_date` date DEFAULT NULL,
  `mandob` varchar(455) DEFAULT NULL,
  `category` varchar(455) DEFAULT NULL,
  `date` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

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
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

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
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

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
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_name_UNIQUE` (`user_name`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `category`
--

DROP TABLE IF EXISTS `category`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `category` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(455) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name_UNIQUE` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `doctor`
--

DROP TABLE IF EXISTS `doctor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `doctor` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `genus` varchar(45) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name_UNIQUE` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

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
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

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
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

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
  `add_doctor` int NOT NULL,
  `edit_doctor` int NOT NULL,
  `delete_doctor` int NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

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
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-06-03 16:03:51
