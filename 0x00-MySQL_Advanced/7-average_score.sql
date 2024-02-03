-- 7-average_score.sql
DROP PROCEDURE IF EXIST ComputeAverageScoreForUser
DELIMITER //
CREATE PROCEDURE ComputeAverageScoreForUser(
    IN user_id INT
)
BEGIN
     UPDATE users
     SET average_score = (SELECT AVG(score) FROM corrections WHERE corrections.user_id = user_id)
     WHERE user_id = user_id;
END;//
DELIMITER ;

