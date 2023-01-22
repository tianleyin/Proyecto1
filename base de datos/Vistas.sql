CREATE VIEW ranking
AS
SELECT player_id, sum(end_points - start_points) as earn_points,
count(distinct (game_id)) as games_played,
format(sum((hour(end_time) - hour(start_time)) * 60 +
(minute(end_time) - minute(start_time)) +
(second(end_time) - second(start_time))/ 60),0) as minutes_played
FROM cardgame c, game g
WHERE c.cardgame_id = g.cardgame_id
group by player_id
;

CREATE VIEW high_bet
AS
SELECT game_id, player_id, max(bet_points) as high_bet
FROM round
where bet_points in (select max(bet_points) from round group by game_id)
group by game_id, player_id
;

CREATE VIEW low_bet
AS
SELECT game_id, player_id, min(bet_points) as low_bet
FROM round
where bet_points in (select min(bet_points) from round group by game_id)
group by game_id, player_id
;

CREATE VIEW winer_bot
AS
SELECT game_id, sum(end_points - start_points) as earn_points
FROM game, player
where game.player_id = player.player_id and human = false and start_points < end_points and end_points in (select max(end_points) from game group by game_id)
group by game_id
;

CREATE VIEW bank_round_winer
AS
SELECT game_id, count(round_num) as bank_round_winer
FROM round
where is_bank = true and start_round_points < end_round_points
group by game_id
;

CREATE VIEW player_bank
AS
SELECT game_id, count(distinct(player_id)) as user_bank
from round
where is_bank = true
group by game_id
;

CREATE VIEW average_bet
AS
SELECT game_id, format(avg(bet_points),2) as avarage_bet
FROM round
group by game_id
;

CREATE VIEW average_initial_bet
AS
SELECT game_id, format(avg(bet_points),2) as average_initial_bet
FROM round
WHERE round_num = 1
group by game_id
;

CREATE VIEW average_final_bet
AS
SELECT game_id, format(avg(bet_points),2) as average_final_bet
FROM round
WHERE round_num in (select max(round_num) from round group by game_id)
group by game_id, round_num
;