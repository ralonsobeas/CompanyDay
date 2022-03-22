-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 07-03-2022 a las 16:52:46
-- Versión del servidor: 10.4.11-MariaDB
-- Versión de PHP: 7.4.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `companyday`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `empresas`
--

CREATE TABLE `empresas` (
  `validado` tinyint(1) NOT NULL DEFAULT 0,
  `id` int(11) NOT NULL,
  `nombre` varchar(120) DEFAULT NULL,
  `password` varchar(120) NOT NULL,
  `personaContacto` varchar(120) DEFAULT NULL,
  `email` varchar(120) DEFAULT NULL,
  `telefono` varchar(15) DEFAULT NULL,
  `direccion` varchar(120) DEFAULT NULL,
  `poblacion` varchar(120) DEFAULT NULL,
  `provincia` varchar(120) DEFAULT NULL,
  `codigoPostal` varchar(15) DEFAULT NULL,
  `pais` varchar(120) DEFAULT NULL,
  `urlWeb` varchar(120) DEFAULT NULL,
  `logo` varchar(120) DEFAULT NULL,
  `consentimientoNombre` tinyint(1) DEFAULT NULL,
  `buscaCandidatos` tinyint(1) DEFAULT NULL,
  `admin` tinyint(1) NOT NULL DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `empresas`
--

INSERT INTO `empresas` (`validado`, `id`, `nombre`, `password`, `personaContacto`, `email`, `telefono`, `direccion`, `poblacion`, `provincia`, `codigoPostal`, `pais`, `urlWeb`, `logo`, `consentimientoNombre`, `buscaCandidatos`, `admin`) VALUES
(1, 1, 'BMW', '6b86b273ff34fce19d6b804eff5a3f5747ada4eaa22f1d49c01e52ddb7875b4b', 'Fernando Alonso', 'falonso@bmw.com', '665656565', 'Calle', 'Las Rozas', 'Madrid', '28230', 'España', 'https://www.bmw.es/es/index.html', 'bmwlogo.png', 1, 1, 0),
(1, 2, 'Telefonica', '', 'Sandra López', 'slopez@telefonica.com', '676666666', 'Avenida', 'Miranda de Ebro', 'Burgos', '09200', 'España', 'https://www.telefonica.es/es/', 'telefonicalogo.png', 1, 1, 0),
(1, 3, 'CaixaBank', '', 'Carlos Martínez', 'cmartinez@caixabank.com', '687878787', 'Calle', 'Barcelona', 'Barcelona', '87655', 'España', 'https://www.caixabank.es/index_es.html', 'caixabanklogo.png', 1, 1, 0),
(1, 4, 'Santander', '', 'Mónica Soria', 'msoria@santander.com', '656767676', 'Alameda', 'Santander', 'Santander', '78655', 'España', 'https://www.bancosantander.es/particulares', 'santanderlogo.png', 1, 1, 0),
(1, 5, 'U-Tad', 'sha256$JIG2gyT35SsJFNz7$ae4f2d66ad9d1335e5e8bee653c5d43401aff0b341617d18f55dc4a4287b2741', 'Marta Izquierdo', 'mizquiedo@u-tad.com', '673434343', 'direccion', 'Las Rozas', 'Madrid', '28230', 'España', 'https://u-tad.com/en/', 'utadlogo.jpg', 1, 1, 0),
(0, 6, 'admin', 'sha256$gu1vTdLYzQbhi9Yq$b16e4f324b1acccc612b271a7450d7f3b14fef31dea10a06f5773f98896b4b7e', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `eventocharlas`
--

CREATE TABLE `eventocharlas` (
  `id` int(11) NOT NULL,
  `tema` varchar(4096) DEFAULT NULL,
  `presencialidad` tinyint(1) DEFAULT NULL,
  `titulo` varchar(120) DEFAULT NULL,
  `fecha` date DEFAULT NULL,
  `idempresa` int(11) DEFAULT NULL,
  `aprobada` tinyint(1) DEFAULT NULL,
  `empresa_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `eventoferiaempresas`
--

CREATE TABLE `eventoferiaempresas` (
  `id` int(11) NOT NULL,
  `fecha` date DEFAULT NULL,
  `presencial` tinyint(1) DEFAULT NULL,
  `empresa_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `eventoferiaempresas`
--

INSERT INTO `eventoferiaempresas` (`id`, `fecha`, `presencial`, `empresa_id`) VALUES
(2, '2022-03-25', 1, 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `eventospeedmeeting`
--

CREATE TABLE `eventospeedmeeting` (
  `id` int(11) NOT NULL,
  `presencialidad` tinyint(1) DEFAULT NULL,
  `fecha` date DEFAULT NULL,
  `duracion` int(11) DEFAULT NULL,
  `perfiles` varchar(4096) DEFAULT NULL,
  `pregunta` varchar(4096) DEFAULT NULL,
  `idempresa` int(11) DEFAULT NULL,
  `aprobada` tinyint(1) DEFAULT NULL,
  `empresa_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `presentacionproyectos`
--

CREATE TABLE `presentacionproyectos` (
  `id` int(11) NOT NULL,
  `presencial` tinyint(1) DEFAULT NULL,
  `videojuegos` tinyint(1) DEFAULT NULL,
  `disenoDigital` tinyint(1) DEFAULT NULL,
  `cortosAnimacion` tinyint(1) DEFAULT NULL,
  `ingenieria` tinyint(1) DEFAULT NULL,
  `empresa_id` int(11) DEFAULT NULL,
  `validado` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `presentacionproyectos`
--

INSERT INTO `presentacionproyectos` (`id`, `presencial`, `videojuegos`, `disenoDigital`, `cortosAnimacion`, `ingenieria`, `empresa_id`, `validado`) VALUES
(1, 1, 1, 0, 1, 0, 1, 1);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `empresas`
--
ALTER TABLE `empresas`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `eventocharlas`
--
ALTER TABLE `eventocharlas`
  ADD PRIMARY KEY (`id`),
  ADD KEY `empresa_id` (`empresa_id`);

--
-- Indices de la tabla `eventoferiaempresas`
--
ALTER TABLE `eventoferiaempresas`
  ADD PRIMARY KEY (`id`),
  ADD KEY `empresa_id` (`empresa_id`);

--
-- Indices de la tabla `eventospeedmeeting`
--
ALTER TABLE `eventospeedmeeting`
  ADD PRIMARY KEY (`id`),
  ADD KEY `empresa_id` (`empresa_id`);

--
-- Indices de la tabla `presentacionproyectos`
--
ALTER TABLE `presentacionproyectos`
  ADD PRIMARY KEY (`id`),
  ADD KEY `empresa_id` (`empresa_id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `empresas`
--
ALTER TABLE `empresas`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21313;

--
-- AUTO_INCREMENT de la tabla `eventocharlas`
--
ALTER TABLE `eventocharlas`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `eventoferiaempresas`
--
ALTER TABLE `eventoferiaempresas`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `eventospeedmeeting`
--
ALTER TABLE `eventospeedmeeting`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `presentacionproyectos`
--
ALTER TABLE `presentacionproyectos`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `eventocharlas`
--
ALTER TABLE `eventocharlas`
  ADD CONSTRAINT `eventocharlas_ibfk_1` FOREIGN KEY (`empresa_id`) REFERENCES `empresas` (`id`);

--
-- Filtros para la tabla `eventoferiaempresas`
--
ALTER TABLE `eventoferiaempresas`
  ADD CONSTRAINT `eventoferiaempresas_ibfk_1` FOREIGN KEY (`empresa_id`) REFERENCES `empresas` (`id`);

--
-- Filtros para la tabla `eventospeedmeeting`
--
ALTER TABLE `eventospeedmeeting`
  ADD CONSTRAINT `eventospeedmeeting_ibfk_1` FOREIGN KEY (`empresa_id`) REFERENCES `empresas` (`id`);

--
-- Filtros para la tabla `presentacionproyectos`
--
ALTER TABLE `presentacionproyectos`
  ADD CONSTRAINT `presentacionproyectos_ibfk_1` FOREIGN KEY (`empresa_id`) REFERENCES `empresas` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
