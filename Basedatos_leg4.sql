-- --------------------------------------------------------
-- Host:                         localhost
-- Versión del servidor:         10.5.8-MariaDB - mariadb.org binary distribution
-- SO del servidor:              Win64
-- HeidiSQL Versión:             11.0.0.5919
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;


-- Volcando estructura de base de datos para flask_mvc
CREATE DATABASE IF NOT EXISTS `flask_mvc` /*!40100 DEFAULT CHARACTER SET latin1 */;
USE `flask_mvc`;

-- Volcando estructura para tabla flask_mvc.productos
CREATE TABLE IF NOT EXISTS `productos` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(255) NOT NULL,
  `descripcion` varchar(150) NOT NULL,
  `precio_venta` decimal(6,2) DEFAULT NULL,
  `precio_compra` decimal(6,2) DEFAULT NULL,
  `estado` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

-- Volcando datos para la tabla flask_mvc.productos: ~6 rows (aproximadamente)
/*!40000 ALTER TABLE `productos` DISABLE KEYS */;
INSERT INTO `productos` (`id`, `nombre`, `descripcion`, `precio_venta`, `precio_compra`, `estado`) VALUES
	(1, 'Gaseosa', '', NULL, NULL, NULL),
	(2, 'firulais', '5000 CABALLOS DE FUERZA', 1500.00, 1200.00, 0),
	(3, 'ACER NITRO 5', 'portatil gamer', 200.00, 1200.00, 1),
	(4, 'firulais', 'portatil gamer', 200.00, 100.00, 1),
	(5, 'Mecato', 'portatil gamer', 1500.00, 100.00, 0),
	(6, 'Margarita', 'Papitas', 1200.00, 1000.00, 0);
/*!40000 ALTER TABLE `productos` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
