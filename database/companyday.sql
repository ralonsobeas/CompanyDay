-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 07-05-2022 a las 14:52:52
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
-- Estructura de tabla para la tabla `alembic_version`
--

CREATE TABLE `alembic_version` (
  `version_num` varchar(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `alembic_version`
--

INSERT INTO `alembic_version` (`version_num`) VALUES
('96fa5aa12d8e');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `empresas`
--

CREATE TABLE `empresas` (
  `validado` tinyint(1) DEFAULT NULL,
  `id` int(11) NOT NULL,
  `nombre` varchar(120) DEFAULT NULL,
  `password` varchar(256) DEFAULT NULL,
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
  `admin` tinyint(1) DEFAULT NULL,
  `confirmed` int(11) DEFAULT NULL,
  `userHash` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `empresas`
--

INSERT INTO `empresas` (`validado`, `id`, `nombre`, `password`, `personaContacto`, `email`, `telefono`, `direccion`, `poblacion`, `provincia`, `codigoPostal`, `pais`, `urlWeb`, `logo`, `consentimientoNombre`, `buscaCandidatos`, `admin`, `confirmed`, `userHash`) VALUES
(0, 0, 'admin', 'sha256$gu1vTdLYzQbhi9Yq$b16e4f324b1acccc612b271a7450d7f3b14fef31dea10a06f5773f98896b4b7e', NULL, 'admin', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 1, NULL, NULL),
(1, 1, 'BMW', 'sha256$AYQah9rrFOO3yvE4$2c3ad1c7cf4608558e2cbcedd87e30a5923f37ab503fb8e94d6b821668be42aa', 'Fernando Alonso', 'falonso@bmw.com', '900357902', 'Av. de Burgos, nº 118', 'Madrid', 'Madrid', '28050', 'España', 'https://www.bmw.es', '1.png', 1, 1, 0, 1, NULL),
(1, 2, 'Telefonica', 'sha256$AYQah9rrFOO3yvE4$2c3ad1c7cf4608558e2cbcedd87e30a5923f37ab503fb8e94d6b821668be42aa', 'Sandra López', 'slopez@telefonica.com', '936895350', 'Calle gran vía, 28', 'Madrid', 'Madrid', '28013', 'España', 'https://www.telefonica.es/es/', '2.png', 1, 1, 0, NULL, NULL),
(1, 3, 'CaixaBank', 'sha256$AYQah9rrFOO3yvE4$2c3ad1c7cf4608558e2cbcedd87e30a5923f37ab503fb8e94d6b821668be42aa', 'Carlos Martínez', 'cmartinez@caixabank.com', '902223223', 'Calle pintor Sorolla,2 - 4', 'Valencia', 'Valencia', '46002', 'España', 'https://www.caixabank.es', '3.png', 1, 1, 0, 1, NULL),
(1, 4, 'Santander', 'sha256$AYQah9rrFOO3yvE4$2c3ad1c7cf4608558e2cbcedd87e30a5923f37ab503fb8e94d6b821668be42aa', 'Mónica Soria', 'msoria@santander.com', '902112211', 'Av. de Cantabria s/n', 'Boadilla del Monte', 'Madrid', '28660', 'España', 'https://www.bancosantander.es/particulares', '4.png', 1, 1, 0, 1, NULL),
(1, 5, 'U-Tad', 'sha256$AYQah9rrFOO3yvE4$2c3ad1c7cf4608558e2cbcedd87e30a5923f37ab503fb8e94d6b821668be42aa', 'Marta Izquierdo', 'mizquiedo@u-tad.com', '900373379', 'Edificio Madrid, Complejo Europa Empresarial', 'Las Rozas', 'Madrid', '28290', 'España', 'https://u-tad.com/en/', '5.jpg', 1, 1, 0, 1, NULL),
(1, 6, 'El ranchito', 'sha256$AYQah9rrFOO3yvE4$2c3ad1c7cf4608558e2cbcedd87e30a5923f37ab503fb8e94d6b821668be42aa', 'Gonzalo Carrion', 'gcarrion@elranchito.es', '913103130', 'De La Coruña 29', 'Madrid', 'Madrid', '28020', 'España', 'https://www.elranchito.es/', '6.png', 1, 1, 0, 1, ''),
(1, 7, 'Ubisoft', 'sha256$AYQah9rrFOO3yvE4$2c3ad1c7cf4608558e2cbcedd87e30a5923f37ab503fb8e94d6b821668be42aa', 'Amaya Soria', 'asoria@ubisoft.es', '916404570', 'Calle Playa de Liencres 2 planta 1, puerta 2. Complejo Europa empresarial edif.Londres', 'Las Rozas', 'Madrid', '28290', 'España', 'https://www.ubisoft.com/es-es/', '7.png', 1, 1, 0, 1, NULL),
(1, 8, 'Black Forest Games', 'sha256$AYQah9rrFOO3yvE4$2c3ad1c7cf4608558e2cbcedd87e30a5923f37ab503fb8e94d6b821668be42aa', 'Sophia Bendowski', 'sbendowski@bfgames.com', ' 7813105791-0', 'Maria-und-Georg-Dietrich-Straße 2', 'Offenburg', 'Offenburg', '77652', 'Alemania', 'https://black-forest-games.com/', '8.png', 1, 1, 0, 1, NULL),
(1, 9, 'Skydance Animation', 'sha256$AYQah9rrFOO3yvE4$2c3ad1c7cf4608558e2cbcedd87e30a5923f37ab503fb8e94d6b821668be42aa', 'Sergio Rojas', 'srojas@skydance.com', '914230885', 'Ed. Bruselas, Complejo Europa Empresarial, C. Rozabella, 4', 'Las Rozas', 'Madrid', '28290', 'España', 'https://skydance.com/', '9.png', 1, 1, 0, 1, NULL),
(1, 10, 'Ánima Kitchent', 'sha256$AYQah9rrFOO3yvE4$2c3ad1c7cf4608558e2cbcedd87e30a5923f37ab503fb8e94d6b821668be42aa', 'Antonio López', 'alopez@anima.com', '916315084', 'Calle, P.º Imperial, 10-12, 2°B', 'Madrid', 'Madrid', '28005', 'España', 'https://www.animakitchent.com/', '10.png', 1, 1, 0, 1, NULL);

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
  `aprobada` tinyint(1) DEFAULT NULL,
  `autor` varchar(516) DEFAULT NULL,
  `empresa_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `eventocharlas`
--

INSERT INTO `eventocharlas` (`id`, `tema`, `presencialidad`, `titulo`, `fecha`, `aprobada`, `autor`, `empresa_id`) VALUES
(1, 'Inteligencia artificial para la conducción autónoma', 1, 'Conducción del futuro', '2022-11-13', 1, 'Eduardo Smith', 1),
(2, 'Información sobre el software Pegasus.', 1, '¿Es tu móvil seguro?', '2022-11-14', 1, 'José María Alonso Cebrián (Chema Alonso)', 2),
(3, 'Uso de modelos predictivos en la banca para bajar los índices de morosidad en el sector.', 1, 'Análisis de datos en el sector bancario', '2022-11-16', 1, 'Luis Esteban Grifoll', 3),
(4, '¿Qué perfiles buscan las empresas en el sector cinematográfico? Ayudaremos a los asistentes a encontrar los trabajos más adecuados para su perfil.', 0, 'Perfiles STEM en el mundo audiovisual', '2022-11-13', 1, 'Gonzalo Carrión', 6),
(5, 'Hablaremos sobre el futuro de los estudios universitarios en el sector. Comentaremos los próximos grados y másteres.', 1, 'U-Tad a la vanguardia de los estudios', '2022-11-17', 1, 'Alfonso Castro', 5),
(6, 'We will be talking about wich tools are used in Ubisoft.', 0, 'Snowdrop engine and other tools.', '2022-11-14', 1, 'Alissa Martin', 7),
(7, '¿Cómo se gestionan los flujos de trabajo en grandes compañías de animación? ¿Existen muchas dificultades entre departamentos de diferentes países?', NULL, 'Metodologías de trabajo en grandes proyectos', '2022-11-17', 1, 'Raúl Pérez', 9);

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
(1, '2022-11-14', 1, 1),
(2, '2022-11-14', 1, 2),
(3, '2022-11-14', 1, 3),
(4, '2022-11-14', 1, 4),
(5, '2022-11-14', 1, 5),
(6, '2022-11-14', 1, 6),
(7, '2022-11-14', 1, 7),
(8, '2022-11-14', 1, 8),
(9, '2022-11-14', 1, 9),
(10, '2022-11-14', 1, 10);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `eventospeedmeeting`
--

CREATE TABLE `eventospeedmeeting` (
  `id` int(11) NOT NULL,
  `presencialidad` tinyint(1) DEFAULT NULL,
  `fecha` date DEFAULT NULL,
  `horaInicio` time DEFAULT NULL,
  `horaFin` time DEFAULT NULL,
  `perfiles` varchar(4096) DEFAULT NULL,
  `pregunta` varchar(4096) DEFAULT NULL,
  `aprobada` tinyint(1) DEFAULT NULL,
  `empresa_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `eventospeedmeeting`
--

INSERT INTO `eventospeedmeeting` (`id`, `presencialidad`, `fecha`, `horaInicio`, `horaFin`, `perfiles`, `pregunta`, `aprobada`, `empresa_id`) VALUES
(1, 1, '2022-11-15', '13:00:00', '15:00:00', 'Ingenieros de software y diseñadores 3D', '¿Interesado en el mundo de la automoción?', 1, 1),
(2, 1, '2022-11-15', '14:30:00', '17:00:00', 'Big data, IA', '¿Te gusta el procesamiento de datos?', 1, 4),
(3, 1, '2022-11-15', '13:00:00', '16:00:00', 'VFX y pipeline designers', '¿Cinéfilo?', 1, 6),
(4, 1, '2022-11-16', '10:00:00', '13:00:00', 'Desarrolladores y diseñadores creativos.', '¿Deseando entrar en el mundo de los videojuegos?', 1, 8);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `personas`
--

CREATE TABLE `personas` (
  `id` int(11) NOT NULL,
  `nombre` varchar(500) DEFAULT NULL,
  `puesto` varchar(120) DEFAULT NULL,
  `comentario` varchar(500) DEFAULT NULL,
  `empresa_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `personas`
--

INSERT INTO `personas` (`id`, `nombre`, `puesto`, `comentario`, `empresa_id`) VALUES
(1, 'Rodrigo Alonso Solaguren-Beascoa', 'Director', NULL, 3),
(2, 'Manoel Alonso Gadi', 'Profesor', NULL, 5),
(3, 'Alfonso Castro', 'Coordinador ingeniería de software', NULL, 5),
(4, 'José Antonio Álvarez', 'Director', NULL, 4),
(5, 'Jaume Balagueró', 'Director VFX', NULL, 6),
(6, 'Manuel Terroba', 'CEO', NULL, 1),
(7, 'Gonzalo Sanjuan', 'Director de márketing', NULL, 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `presentacionproyectos`
--

CREATE TABLE `presentacionproyectos` (
  `validado` tinyint(1) DEFAULT NULL,
  `id` int(11) NOT NULL,
  `presencial` tinyint(1) DEFAULT NULL,
  `videojuegos` tinyint(1) DEFAULT NULL,
  `disenoDigital` tinyint(1) DEFAULT NULL,
  `cortosAnimacion` tinyint(1) DEFAULT NULL,
  `ingenieria` tinyint(1) DEFAULT NULL,
  `empresa_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `presentacionproyectos`
--

INSERT INTO `presentacionproyectos` (`validado`, `id`, `presencial`, `videojuegos`, `disenoDigital`, `cortosAnimacion`, `ingenieria`, `empresa_id`) VALUES
(1, 1, 1, 1, 0, 1, 0, 1);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `alembic_version`
--
ALTER TABLE `alembic_version`
  ADD PRIMARY KEY (`version_num`);

--
-- Indices de la tabla `empresas`
--
ALTER TABLE `empresas`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `nombre` (`nombre`),
  ADD UNIQUE KEY `email` (`email`);

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
-- Indices de la tabla `personas`
--
ALTER TABLE `personas`
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
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=123312516;

--
-- AUTO_INCREMENT de la tabla `eventocharlas`
--
ALTER TABLE `eventocharlas`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT de la tabla `eventoferiaempresas`
--
ALTER TABLE `eventoferiaempresas`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT de la tabla `eventospeedmeeting`
--
ALTER TABLE `eventospeedmeeting`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT de la tabla `personas`
--
ALTER TABLE `personas`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

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
-- Filtros para la tabla `personas`
--
ALTER TABLE `personas`
  ADD CONSTRAINT `personas_ibfk_1` FOREIGN KEY (`empresa_id`) REFERENCES `empresas` (`id`);

--
-- Filtros para la tabla `presentacionproyectos`
--
ALTER TABLE `presentacionproyectos`
  ADD CONSTRAINT `presentacionproyectos_ibfk_1` FOREIGN KEY (`empresa_id`) REFERENCES `empresas` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
