CREATE TABLE `collections` (
  `userid` int(11) NOT NULL,
  `collectionid` smallint(6) NOT NULL,
  `name` varchar(32) NOT NULL,
  PRIMARY KEY  (`userid`,`collectionid`),
  KEY `nameindex` (`userid`,`name`)
) ENGINE=InnoDB;

CREATE TABLE `wbo` (
  `username` int(11) NOT NULL,
  `collection` smallint(6) NOT NULL default '0',
  `id` varbinary(64) NOT NULL default '',
  `parentid` varbinary(64) default NULL,
  `predecessorid` varbinary(64) default NULL,
  `sortindex` int(11) default NULL,
  `modified` bigint(20) default NULL,
  `payload` longtext,
  `payload_size` int(11) default NULL,
  PRIMARY KEY  (`username`,`collection`,`id`),
  KEY `parentindex` (`username`,`collection`,`parentid`),
  KEY `modified` (`username`,`collection`,`modified`),
  KEY `weightindex` (`username`,`collection`,`sortindex`),
  KEY `predecessorindex` (`username`,`collection`,`predecessorid`),
  KEY `size_index` (`username`,`payload_size`)
) ENGINE=InnoDB;
