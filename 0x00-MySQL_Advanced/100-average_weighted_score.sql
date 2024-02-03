-- Procedure to compute and store the average weighted score for a user
DELIMITER //
CREATE PROCEDURE ComputeAverageWeightedScoreForUser(IN user_id INT)
BEGIN
    DECLARE total_score FLOAT DEFAULT 0;
    DECLARE total_weight FLOAT DEFAULT 0;
    DECLARE avg_score FLOAT DEFAULT 0;

    -- Calculate the total weighted score
    SELECT SUM(c.score * p.weight) INTO total_score
    FROM corrections c
    JOIN projects p ON c.project_id = p.id
    WHERE c.user_id = user_id;

    -- Calculate the total weight
    SELECT SUM(weight) INTO total_weight
    FROM projects;

    -- Calculate the average weighted score
    IF total_weight > 0 THEN
        SET avg_score = total_score / total_weight;
    END IF;

    -- Update the user's average score in the users table
    UPDATE users
    SET average_score = avg_score
    WHERE id = user_id;
END //
DELIMITER ;

