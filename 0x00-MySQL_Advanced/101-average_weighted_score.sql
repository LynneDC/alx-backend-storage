-- Procedure to compute and store the average weighted score for all users
DELIMITER //
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
    DECLARE user_id INT;
    
    -- Loop through each user
    DECLARE user_cursor CURSOR FOR SELECT id FROM users;
    OPEN user_cursor;
    
    user_loop: LOOP
        FETCH user_cursor INTO user_id;
        IF user_id IS NULL THEN
            LEAVE user_loop;
        END IF;

        -- Call the procedure for individual user
        CALL ComputeAverageWeightedScoreForUser(user_id);
    END LOOP;

    CLOSE user_cursor;
END //
DELIMITER ;

