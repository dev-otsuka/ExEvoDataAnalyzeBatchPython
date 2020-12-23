CREATE TABLE slot_summary_data(
    id INT(11) AUTO_INCREMENT NOT NULL, 
    store_id INT(11) NOT NULL ,
    slot_id INT(11) NOT NULL ,
    play_date datetime NOT NULL,
    total_play_count INT(11) NOT NULL,
    bic_bonus_count INT(11) NOT NULL,
    regular_bonus_count INT(11) NOT NULL,
    max_payout INT(11) NOT NULL,
    graph_transition TEXT,
    index index_store_id (store_id),
    index index_slot_id (slot_id),
    index index_play_date (play_date),
    PRIMARY KEY (id));