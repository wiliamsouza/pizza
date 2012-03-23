/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;


--
-- Create schema pizza
--

CREATE DATABASE /*!32312 IF NOT EXISTS*/ pizza;
USE pizza;
CREATE TABLE `bebida` (
  `id` int(10) unsigned NOT NULL auto_increment,
  `nome` varchar(100) NOT NULL default '',
  `tipo` varchar(100) NOT NULL default '',
  `preco` decimal(5,2) unsigned NOT NULL default '0.00',
  PRIMARY KEY  (`id`)
) TYPE=MyISAM;
CREATE TABLE `conteudo` (
  `id` int(10) unsigned NOT NULL auto_increment,
  `pedido_id` int(10) unsigned NOT NULL default '0',
  `produtos_id` text NOT NULL,
  `tamanho_id` int(10) unsigned NOT NULL default '0',
  `quantidade` tinyint(2) unsigned NOT NULL default '0',
  `observacao` text NOT NULL,
  PRIMARY KEY  (`id`)
) TYPE=MyISAM;
CREATE TABLE `endereco` (
  `id` int(10) unsigned NOT NULL auto_increment,
  `pessoa_id` int(10) unsigned NOT NULL default '0',
  `cidade` varchar(30) NOT NULL default '',
  `cep` varchar(10) NOT NULL default '',
  `rua` varchar(100) NOT NULL default '',
  `numero` varchar(10) NOT NULL default '',
  `complemento` varchar(100) NOT NULL default '',
  `referencia` varchar(100) NOT NULL default '',
  `bairro` varchar(50) NOT NULL default '',
  `preco_entrega` decimal(5,2) unsigned NOT NULL default '0.00',
  PRIMARY KEY  (`id`)
) TYPE=MyISAM;
CREATE TABLE `entregador` (
  `id` int(10) unsigned NOT NULL auto_increment,
  `nome` varchar(100) NOT NULL default '',
  `residencial` varchar(12) NOT NULL default '',
  `celular` varchar(12) NOT NULL default '',
  PRIMARY KEY  (`id`)
) TYPE=MyISAM;
CREATE TABLE `lanche` (
  `id` int(10) unsigned NOT NULL auto_increment,
  `nome` varchar(100) NOT NULL default '',
  `sabor_id` int(10) unsigned NOT NULL default '0',
  `preco` decimal(5,2) unsigned NOT NULL default '0.00',
  PRIMARY KEY  (`id`)
) TYPE=MyISAM;
CREATE TABLE `massa` (
  `id` int(10) unsigned NOT NULL auto_increment,
  `nome` varchar(100) NOT NULL default '',
  `sabor_id` int(10) unsigned NOT NULL default '0',
  `preco` decimal(5,2) unsigned NOT NULL default '0.00',
  PRIMARY KEY  (`id`)
) TYPE=MyISAM;
CREATE TABLE `outro` (
  `id` int(10) unsigned NOT NULL auto_increment,
  `nome` varchar(100) NOT NULL default '',
  `tipo` varchar(100) NOT NULL default '',
  `preco` decimal(5,2) NOT NULL default '0.00',
  PRIMARY KEY  (`id`)
) TYPE=MyISAM;
CREATE TABLE `pedido` (
  `id` int(10) unsigned NOT NULL auto_increment,
  `pessoa_id` int(10) unsigned NOT NULL default '0',
  `data` varchar(10) NOT NULL default '',
  `estado` varchar(10) NOT NULL default '',
  `entregador_id` int(10) unsigned NOT NULL default '0',
  PRIMARY KEY  (`id`)
) TYPE=MyISAM;
CREATE TABLE `pessoa` (
  `id` int(10) unsigned NOT NULL auto_increment,
  `nome` varchar(100) NOT NULL default '',
  `residencial` varchar(12) NOT NULL default '',
  `celular` varchar(12) NOT NULL default '',
  `recado` varchar(12) NOT NULL default '',
  `nascimento` varchar(10) NOT NULL default '',
  `sexo` char(1) NOT NULL default '',
  `email` varchar(100) NOT NULL default '',
  `observacao` text NOT NULL,
  PRIMARY KEY  (`id`)
) TYPE=MyISAM;
CREATE TABLE `sabor` (
  `id` int(10) unsigned NOT NULL auto_increment,
  `nome` varchar(100) NOT NULL default '',
  `ingredientes` text NOT NULL,
  PRIMARY KEY  (`id`)
) TYPE=MyISAM;
CREATE TABLE `sobremesa` (
  `id` int(10) unsigned NOT NULL auto_increment,
  `nome` varchar(100) NOT NULL default '',
  `tipo` varchar(100) NOT NULL default '',
  `preco` decimal(5,2) unsigned NOT NULL default '0.00',
  PRIMARY KEY  (`id`)
) TYPE=MyISAM;
CREATE TABLE `tamanho` (
  `id` int(10) unsigned NOT NULL auto_increment,
  `tamanho` varchar(100) NOT NULL default '',
  PRIMARY KEY  (`id`)
) TYPE=MyISAM;
/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
