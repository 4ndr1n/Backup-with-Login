create table Backup(
BackupID int not null primary key auto_increment,
filepath varchar(200),
filesize varchar(50),
copydate varchar(50)
);

create database Schulprojekt;
use Schulproket;

CREATE TABLE user (
ID int NOT NULL primary key auto_increment,
user varchar(30) NOT NULL,
pass varchar(30) NOT NULL
);

create table RegistrationPass(
ID int not null primary key auto_increment,
pass varchar(30)
);