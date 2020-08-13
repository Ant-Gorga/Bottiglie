-- MariaDB dump 10.17  Distrib 10.4.14-MariaDB, for Linux (x86_64)
--
-- Host: localhost    Database: test_bottiglie
-- ------------------------------------------------------
-- Server version	10.4.14-MariaDB

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
  `Data_Acquisto` datetime DEFAULT NULL,
  `Id_Fornitore` int(11) NOT NULL,
  `Id_tipo` int(11) NOT NULL,
  PRIMARY KEY (`Cod_Bottiglia`),
  KEY `Partita_IVA_idx` (`Id_Fornitore`),
  KEY `Id_tipo_idx` (`Id_tipo`),
  CONSTRAINT `Id_Fornitore` FOREIGN KEY (`Id_Fornitore`) REFERENCES `fornitori` (`Partita_IVA`),
  CONSTRAINT `Id_tipo` FOREIGN KEY (`Id_tipo`) REFERENCES `tipi` (`Id_tipo`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;




--
-- Table structure for table `fornitori`
--

DROP TABLE IF EXISTS `fornitori`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `fornitori` (
  `Partita_IVA` int(11) NOT NULL AUTO_INCREMENT,
  `Nome` varchar(45) NOT NULL,
  `Email` varchar(40) NOT NULL DEFAULT '*@*.*',
  `Telefono` varchar(45) NOT NULL,
  `Indirizzo` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`Partita_IVA`)
) ENGINE=InnoDB AUTO_INCREMENT=157890093 DEFAULT CHARSET=utf8mb4 COMMENT='Tabella dei fornitori delle Bottiglie';
/*!40101 SET character_set_client = @saved_cs_client */;


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


/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-08-13 18:01:54
