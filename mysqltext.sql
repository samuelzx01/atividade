create database loja;
use loja;
create table loja_produtos(
id int primary key auto_increment,
produto varchar(99),
preco varchar(99)


);

insert into loja_produtos(produto, preco) values
('Teclado', '99');

