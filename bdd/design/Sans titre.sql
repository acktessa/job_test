CREATE TABLE `ADRESSE` (
  `adresse_id`,
  `numero`,
  `rue`,
  `info`,
  `ville`,
  `code_postal`,
  `commentaire`,
  `complement`,
  PRIMARY KEY(`adresse_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8;

CREATE TABLE `BIEN` (
  `bien_id`,
  `type`,
  `description`,
  `adresse_id`,
  ``,
  PRIMARY KEY(`bien_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8;

CREATE TABLE `LOCATION` (
  `bien_id`,
  `personne_id`,
  ``,
  PRIMARY KEY(`bien_id`, `personne_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8;

CREATE TABLE `PROPRIETE` (
  `bien_id`,
  `personne_id`,
  ``,
  PRIMARY KEY(`bien_id`, `personne_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8;

CREATE TABLE `INTERVENTION` (
  `bien_id`,
  `personne_id`,
  `motif`,
  `date_echeance`,
  `date_rdv`,
  `etat_avancement`,
  `commentaire`,
  PRIMARY KEY(`bien_id`, `personne_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8;

CREATE TABLE `PERSONNE` (
  `personne_id`,
  `nom`,
  `prenom`,
  PRIMARY KEY(`personne_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8;

ALTER TABLE `BIEN` ADD FOREIGN KEY (`adresse_id`) REFERENCES `ADRESSE` (`adresse_id`);
ALTER TABLE `LOCATION` ADD FOREIGN KEY (`bien_id`) REFERENCES `BIEN` (`bien_id`);
ALTER TABLE `LOCATION` ADD FOREIGN KEY (`personne_id`) REFERENCES `PERSONNE` (`personne_id`);
ALTER TABLE `PROPRIETE` ADD FOREIGN KEY (`bien_id`) REFERENCES `BIEN` (`bien_id`);
ALTER TABLE `PROPRIETE` ADD FOREIGN KEY (`personne_id`) REFERENCES `PERSONNE` (`personne_id`);
ALTER TABLE `INTERVENTION` ADD FOREIGN KEY (`bien_id`) REFERENCES `BIEN` (`bien_id`);
ALTER TABLE `INTERVENTION` ADD FOREIGN KEY (`personne_id`) REFERENCES `PERSONNE` (`personne_id`);