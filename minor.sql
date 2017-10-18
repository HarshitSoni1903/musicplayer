-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema songdb
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema songdb
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `songdb` DEFAULT CHARACTER SET utf8 ;
USE `songdb` ;

-- -----------------------------------------------------
-- Table `songdb`.`angrytable`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `songdb`.`angrytable` (
  `link` VARCHAR(200) NULL DEFAULT NULL,
  `Songname` VARCHAR(70) NULL DEFAULT NULL,
  `Artist` VARCHAR(20) NOT NULL,
  `Genre` VARCHAR(20) NOT NULL,
  `Album` VARCHAR(70) NULL DEFAULT NULL)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `songdb`.`disgusttable`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `songdb`.`disgusttable` (
  `link` VARCHAR(200) NULL DEFAULT NULL,
  `Songname` VARCHAR(70) NULL DEFAULT NULL,
  `Artist` VARCHAR(20) NOT NULL,
  `Genre` VARCHAR(20) NOT NULL,
  `Album` VARCHAR(70) NULL DEFAULT NULL)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `songdb`.`feartable`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `songdb`.`feartable` (
  `link` VARCHAR(200) NULL DEFAULT NULL,
  `Songname` VARCHAR(70) NULL DEFAULT NULL,
  `Artist` VARCHAR(20) NOT NULL,
  `Genre` VARCHAR(20) NOT NULL,
  `Album` VARCHAR(70) NULL DEFAULT NULL)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `songdb`.`happytable`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `songdb`.`happytable` (
  `link` VARCHAR(200) NULL DEFAULT NULL,
  `Songname` VARCHAR(70) NULL DEFAULT NULL,
  `Artist` VARCHAR(20) NOT NULL,
  `Genre` VARCHAR(20) NOT NULL,
  `Album` VARCHAR(70) NULL DEFAULT NULL)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `songdb`.`neutraltable`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `songdb`.`neutraltable` (
  `link` VARCHAR(200) NULL DEFAULT NULL,
  `Songname` VARCHAR(70) NULL DEFAULT NULL,
  `Artist` VARCHAR(20) NOT NULL,
  `Genre` VARCHAR(20) NOT NULL,
  `Album` VARCHAR(70) NULL DEFAULT NULL)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `songdb`.`sadtable`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `songdb`.`sadtable` (
  `link` VARCHAR(200) NULL DEFAULT NULL,
  `Songname` VARCHAR(70) NULL DEFAULT NULL,
  `Artist` VARCHAR(20) NOT NULL,
  `Genre` VARCHAR(20) NOT NULL,
  `Album` VARCHAR(70) NULL DEFAULT NULL)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `songdb`.`surprisetable`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `songdb`.`surprisetable` (
  `link` VARCHAR(200) NULL DEFAULT NULL,
  `Songname` VARCHAR(70) NULL DEFAULT NULL,
  `Artist` VARCHAR(20) NOT NULL,
  `Genre` VARCHAR(20) NOT NULL,
  `Album` VARCHAR(70) NULL DEFAULT NULL)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `songdb`.`userdata`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `songdb`.`userdata` (
  `userid` VARCHAR(20) NOT NULL,
  `username` VARCHAR(40) NOT NULL,
  PRIMARY KEY (`userid`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `songdb`.`usermood`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `songdb`.`usermood` (
  `userid` VARCHAR(20) NOT NULL,
  `period` INT(11) NOT NULL,
  `fear` FLOAT NULL DEFAULT NULL,
  `disgust` FLOAT NULL DEFAULT NULL,
  `anger` FLOAT NULL DEFAULT NULL,
  `neutral` FLOAT NULL DEFAULT NULL,
  `happiness` FLOAT NULL DEFAULT NULL,
  `sad` FLOAT NULL DEFAULT NULL,
  `surprise` FLOAT NULL DEFAULT NULL,
  `mood` VARCHAR(25) NULL DEFAULT NULL,
  INDEX `userid` (`userid` ASC),
  CONSTRAINT `usermood_ibfk_1`
    FOREIGN KEY (`userid`)
    REFERENCES `songdb`.`userdata` (`userid`)
    ON DELETE CASCADE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;