-- phpMyAdmin SQL Dump
-- version 3.5.5
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Jan 29, 2022 at 07:10 AM
-- Server version: 5.5.21-log
-- PHP Version: 5.3.20

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `mk_database`
--

-- --------------------------------------------------------

--
-- Table structure for table `mk_diary`
--

CREATE TABLE IF NOT EXISTS `mk_diary` (
  `ITEM_ID` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `ITEM` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `ITEM_DATE` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `ITEM_AMOUNT` int(11) NOT NULL,
  `5DX_BAAN` int(11) NOT NULL,
  `5DX_TIME` int(11) DEFAULT NULL,
  `5DX_DSVR` int(11) DEFAULT NULL,
  `5DX_ALIGN` float(6,2) DEFAULT NULL,
  `5DX_MAP` float(6,2) DEFAULT NULL,
  `5DX_AUTO_THICKNESS` float(6,2) DEFAULT NULL,
  `5DX_TEST` float(6,2) DEFAULT NULL,
  `5DX_BAAN1` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `VITROX_BAAN` int(11) NOT NULL,
  `VITROX_TIME` int(11) DEFAULT NULL,
  `VITROX_DSVR` int(11) DEFAULT NULL,
  `VITROX_TEST` float(6,2) DEFAULT NULL,
  `VITROX_BAAN1` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `5DXI_PROG` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `5DXI_LINECAPA` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `5DXI_EPI` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `5DXI_COMMENTS` text COLLATE utf8_unicode_ci,
  `HEXI` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `5DXII_PROG` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `5DXII_LINECAPA` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `5DXII_EPI` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `5DXII_COMMENTS` text COLLATE utf8_unicode_ci,
  `HEXII` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `VITROXI_PROG` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `VITROXI_LINECAPA` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `VITROXI_EPI` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `VITROXI_COMMENTS` text COLLATE utf8_unicode_ci,
  `VITROXII_PROG` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `VITROXII_LINECAPA` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `VITROXII_EPI` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `VITROXII_COMMENTS` text COLLATE utf8_unicode_ci,
  `VITROXII_TIME` int(11) DEFAULT NULL,
  `VITROXII_DSVR` int(11) DEFAULT NULL,
  `VITROXII_TEST` float(6,2) DEFAULT NULL,
  `VITROXII_BAAN1` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `VITROXII_BAAN` int(11) DEFAULT NULL,
  `VITROXIII_BAAN` int(11) DEFAULT NULL,
  `VITROXIII_TIME` int(11) DEFAULT NULL,
  `VITROXIII_DSVR` int(11) DEFAULT NULL,
  `VITROXIII_TEST` float(6,2) DEFAULT NULL,
  `VITROXIII_BAAN1` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `VITROXIII_PROG` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `VITROXIII_LINECAPA` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `VITROXIII_EPI` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `VITROXIII_COMMENTS` text COLLATE utf8_unicode_ci,
  
  
  `VITROXIV_BAAN` int(11) DEFAULT NULL,
  `VITROXIV_TIME` int(11) DEFAULT NULL,
  `VITROXIV_DSVR` int(11) DEFAULT NULL,
  `VITROXIV_TEST` float(6,2) DEFAULT NULL,
  `VITROXIV_BAAN1` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `VITROXIV_PROG` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `VITROXIV_LINECAPA` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `VITROXIV_EPI` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `VITROXIV_COMMENTS` text COLLATE utf8_unicode_ci,
  
  PRIMARY KEY (`ITEM_ID`)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci AUTO_INCREMENT=1078 ;


--
-- Table structure for table `mk_user`
--

CREATE TABLE IF NOT EXISTS `mk_user` (
  `USER_ID` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `USERNAME` varchar(20) COLLATE utf8_unicode_ci NOT NULL,
  `PASSWORD` char(40) COLLATE utf8_unicode_ci NOT NULL,
  `EMAIL_ADDR` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `IS_ACTIVE` tinyint(1) DEFAULT '0',
  PRIMARY KEY (`USER_ID`)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci AUTO_INCREMENT=2 ;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
