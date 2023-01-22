DROP DATABASE IF EXISTS proyecto7;
CREATE DATABASE proyecto7 CHARACTER SET utf8mb4;
USE proyecto7;

CREATE TABLE player (
	player_id VARCHAR(25) UNIQUE PRIMARY KEY,
    player_name VARCHAR(40) NOT NULL,
    player_risck TINYINT NOT NULL,
    human TINYINT(1) NOT NULL
);

CREATE TABLE deck (
  deck_id CHAR(3) PRIMARY KEY,
  deck_name VARCHAR(25) NOT NULL
);

CREATE TABLE cardgame (
  cardgame_id INT,
  deck_id CHAR(3) NOT NULL,
  players TINYINT NOT NULL,
  rounds TINYINT NOT NULL,
  start_time DATETIME NULL,
  end_time DATETIME NULL,
  PRIMARY KEY (cardgame_id, deck_id),
  FOREIGN KEY (deck_id)
  REFERENCES deck(deck_id)
);

CREATE TABLE card (
  card_id CHAR(3),
  deck_id CHAR(3) NOT NULL,
  card_name VARCHAR(25) NULL,
  card_priority TINYINT NULL,
  card_value DECIMAL(3,1) NULL,
  card_real_value TINYINT NULL,
  PRIMARY KEY (card_id, deck_id),
  FOREIGN KEY (deck_id)
  REFERENCES deck (deck_id)
);

CREATE TABLE game (
  game_id VARCHAR(25),
  player_id VARCHAR(25) NOT NULL,
  cardgame_id INT NOT NULL,
  initial_card_id CHAR(3) NULL,
  start_points TINYINT NULL,
  end_points TINYINT NULL,
	PRIMARY KEY (game_id, player_id, cardgame_id),
    FOREIGN KEY (player_id)
    REFERENCES player (player_id),
    FOREIGN KEY (cardgame_id)
    REFERENCES cardgame (cardgame_id),
    FOREIGN KEY (initial_card_id)
    REFERENCES card (card_id)
);

CREATE TABLE round (
  round_num TINYINT AUTO_INCREMENT,
  game_id VARCHAR(25),
  player_id VARCHAR(25) NOT NULL,
  cardgame_id INT NOT NULL,
  start_round_points TINYINT NULL,
  end_round_points TINYINT NULL,
  is_bank TINYINT(1) NULL,
  bet_points TINYINT NULL,
  cards_value DECIMAL(4,1) NULL,
	PRIMARY KEY (round_num, game_id, player_id, cardgame_id),
    FOREIGN KEY (game_id)
    REFERENCES game (game_id),
    FOREIGN KEY (player_id)
    REFERENCES player (player_id),
    FOREIGN KEY (cardgame_id)
    REFERENCES cardgame (cardgame_id)
);
