CREATE TABLE slot(
    id INT(11) AUTO_INCREMENT NOT NULL, 
    slot_id INT(11) NOT NULL,
    store_id INT(11) NOT NULL ,
    name VARCHAR(256) NOT NULL ,
    coin_lending_kind VARCHAR(256),
    index index_store_id (store_id),
    index index_slot_id (slot_id),
    PRIMARY KEY (id)) DEFAULT CHARSET=utf8mb4;