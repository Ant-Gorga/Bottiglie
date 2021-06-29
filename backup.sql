-- MariaDB dump 10.17  Distrib 10.4.13-MariaDB, for Linux (x86_64)
--
-- Host: localhost    Database: test_bottiglie
-- ------------------------------------------------------
-- Server version	10.4.13-MariaDB-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `bottiglie`
--

DROP TABLE IF EXISTS `bottiglie`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `bottiglie` (
  `Cod_Bottiglia` varchar(15) NOT NULL,
  `Nome` varchar(45) NOT NULL,
  `Quantita` tinyint(4) DEFAULT NULL,
  `P_Acquisto` float NOT NULL,
  `P_Vendita` float NOT NULL,
  `Data_Acqusito` datetime DEFAULT NULL,
  `Id_Fornitore` int(11) NOT NULL,
  `Id_tipo` int(11) NOT NULL,
  PRIMARY KEY (`Cod_Bottiglia`),
  KEY `Partita_IVA_idx` (`Id_Fornitore`),
  KEY `Id_tipo_idx` (`Id_tipo`),
  CONSTRAINT `Id_Forntore` FOREIGN KEY (`Id_Fornitore`) REFERENCES `foritori` (`Partita_IVA`),
  CONSTRAINT `Id_tipo` FOREIGN KEY (`Id_tipo`) REFERENCES `tipi` (`Id_tipo`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bottiglie`
--

LOCK TABLES `bottiglie` WRITE;
/*!40000 ALTER TABLE `bottiglie` DISABLE KEYS */;
INSERT INTO `bottiglie` VALUES ('8003905042351','Astoria Valdobiadene Preosecco Superiore',4,10,20,'2020-05-09 00:00:00',157890092,3),('8003905044140','Astoria 9.5 COLD WINE black',5,7.5,15,'2020-05-10 00:00:00',157890092,3),('80220718','Strega',0,9.5,17,'2020-01-30 00:00:00',157890092,1);
/*!40000 ALTER TABLE `bottiglie` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `foritori`
--

DROP TABLE IF EXISTS `foritori`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `foritori` (
  `Partita_IVA` int(11) NOT NULL AUTO_INCREMENT,
  `Nome` varchar(45) NOT NULL,
  `Email` varchar(40) NOT NULL DEFAULT '*@*.*',
  `Telefono` varchar(45) NOT NULL,
  `Indirizzo` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`Partita_IVA`)
) ENGINE=InnoDB AUTO_INCREMENT=157890093 DEFAULT CHARSET=utf8mb4 COMMENT='Tabella dei fornitori delle Bottiglie';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `foritori`
--

LOCK TABLES `foritori` WRITE;
/*!40000 ALTER TABLE `foritori` DISABLE KEYS */;
INSERT INTO `foritori` VALUES (157890092,'Pinco Pallino SPA','antonio','08289866','VIa tal dei tali');
/*!40000 ALTER TABLE `foritori` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tipi`
--

DROP TABLE IF EXISTS `tipi`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tipi` (
  `Id_tipo` int(11) NOT NULL AUTO_INCREMENT,
  `Nome` varchar(45) NOT NULL,
  PRIMARY KEY (`Id_tipo`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tipi`
--

LOCK TABLES `tipi` WRITE;
/*!40000 ALTER TABLE `tipi` DISABLE KEYS */;
INSERT INTO `tipi` VALUES (1,'Liquore'),(2,'Grappa'),(3,'Spumante'),(4,'Vino');
/*!40000 ALTER TABLE `tipi` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `vendite`
--

DROP TABLE IF EXISTS `vendite`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `vendite` (
  `Id_Vendita` int(11) NOT NULL AUTO_INCREMENT,
  `Data_Vendita` datetime DEFAULT NULL,
  `Quantita` int(11) NOT NULL DEFAULT 1,
  `Id_Bottiglia` varchar(15) NOT NULL,
  PRIMARY KEY (`Id_Vendita`),
  KEY `Cod_Barre_idx` (`Id_Bottiglia`),
  CONSTRAINT `ID_Bottiglia` FOREIGN KEY (`Id_Bottiglia`) REFERENCES `bottiglie` (`Cod_Bottiglia`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `vendite`
--

LOCK TABLES `vendite` WRITE;
/*!40000 ALTER TABLE `vendite` DISABLE KEYS */;
INSERT INTO `vendite` VALUES (1,'0000-00-00 00:00:00',3,'80220718'),(4,'0000-00-00 00:00:00',3,'80220718'),(5,'2020-06-01 00:00:00',2,'8003905042351'),(6,'2020-06-03 00:00:00',5,'8003905044140'),(7,'2020-06-23 00:00:00',1,'8003905042351');
/*!40000 ALTER TABLE `vendite` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-07-02 22:21:11
