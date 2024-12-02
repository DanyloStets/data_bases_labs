use local_flixbus;
-- -----------------------------------------------------
-- --------------------- Task: Check Reviews ------------------------
-- -----------------------------------------------------

-- -----------------------------------------------------
-- --------------------- On create ---------------------
-- -----------------------------------------------------

DROP TRIGGER IF EXISTS check_driver_exists_on_create;
DELIMITER //

CREATE TRIGGER check_driver_exists_on_create
BEFORE INSERT ON reviews
FOR EACH ROW
BEGIN
    -- Check if driver_id exists
    IF NOT EXISTS (SELECT 1 FROM driver WHERE id = NEW.driver_id) THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Driver ID does not exist';
    END IF;
END;
//

DELIMITER ;

-- -----------------------------------------------------
-- --------------------- On Update ---------------------
-- -----------------------------------------------------

DROP TRIGGER IF EXISTS check_driver_exists_on_update;
DELIMITER //

CREATE TRIGGER check_driver_exists_on_update
BEFORE UPDATE ON reviews
FOR EACH ROW
BEGIN
    -- Check if driver_id exists
    IF NOT EXISTS (SELECT 1 FROM driver WHERE id = NEW.driver_id) THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Driver ID does not exist';
    END IF;
END;
//

DELIMITER ;


-- -----------------------------------------------------
-- --------------------- Task 2 ------------------------
-- -----------------------------------------------------


-- -----------------------------------------------------
-- --------------------- 1 -----------------------------
-- -----------------------------------------------------

DROP PROCEDURE IF EXISTS parametrized_insertion_tickets;

DELIMITER //

CREATE PROCEDURE parametrized_insertion_tickets(
    IN p_price INT,
    IN p_passenger_id INT,
    IN p_route_id INT
)
BEGIN
    INSERT INTO tickets(price, passenger_id, route_id)
    VALUES (p_price, p_passenger_id, p_route_id);
END //

DELIMITER ;


-- -----------------------------------------------------
-- --------------------- 2 -----------------------------
-- -----------------------------------------------------

DROP PROCEDURE IF EXISTS many_to_many_relation;
DELIMITER //

CREATE PROCEDURE many_to_many_relation(
    IN p_driver_name VARCHAR(100),
    IN p_driver_surname VARCHAR(100),
    IN p_route_id INT
)
BEGIN
    DECLARE p_driver_id INT;
    DECLARE p_route_exists INT;

    -- Знайти ID водія за ім'ям та прізвищем
    SELECT id INTO p_driver_id
    FROM driver
    WHERE name = p_driver_name AND surname = p_driver_surname;

    -- Якщо водія не знайдено, викликати помилку
    IF p_driver_id IS NULL THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Driver not found';
    END IF;

    -- Перевірити, чи існує такий маршрут
    SELECT COUNT(*) INTO p_route_exists
    FROM route
    WHERE id = p_route_id;

    -- Якщо маршрут не знайдено, викликати помилку
    IF p_route_exists = 0 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Route not found';
    END IF;

    -- Перевірити, чи зв’язок між водієм і маршрутом уже існує
    IF EXISTS (
        SELECT 1
        FROM driver_routes
        WHERE driver_id = p_driver_id AND route_id = p_route_id
    ) THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Driver already assigned to this route';
    END IF;

    -- Вставити запис у стикувальну таблицю
    INSERT INTO driver_routes (driver_id, route_id)
    VALUES (p_driver_id, p_route_id);

END;
//

DELIMITER ;


-- -----------------------------------------------------
-- --------------------- 3 -----------------------------
-- -----------------------------------------------------
DROP PROCEDURE IF EXISTS insert_multiple_drivers;

DELIMITER //

CREATE PROCEDURE insert_multiple_drivers()
BEGIN
    DECLARE i INT DEFAULT 1;

    WHILE i <= 10 DO
        INSERT INTO driver (name, surname, numbers, experience_years, company)
        VALUES (CONCAT('Noname', i), CONCAT('Noname', i), 123 + i, 5 + i, CONCAT('Company', i));

        SET i = i + 1;
    END WHILE;
END //

DELIMITER ;


-- -----------------------------------------------------
-- --------------------- 4 -----------------------------
-- -----------------------------------------------------

DROP PROCEDURE IF EXISTS get_info_about_route;
DROP PROCEDURE IF EXISTS info_about_route;

DELIMITER //

-- Збережена процедура для отримання інформації про 'distance' у таблиці 'route'
CREATE PROCEDURE get_info_about_route(in p_type text, out result float)
BEGIN
    DECLARE res float DEFAULT 0;

    CASE p_type
        WHEN 'MIN' THEN
            SET res = (SELECT MIN(r.distance) FROM route AS r);
        WHEN 'MAX' THEN
            SET res = (SELECT MAX(r.distance) FROM route AS r);
        WHEN 'SUM' THEN
            SET res = (SELECT SUM(r.distance) FROM route AS r);
        WHEN 'AVG' THEN
            SET res = (SELECT AVG(r.distance) FROM route AS r);
        ELSE
            SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Invalid operation type.';
    END CASE;

    SET result = res;
END //

DELIMITER ;

DELIMITER //

-- Збережена процедура для виклику першої процедури та повернення результату
CREATE PROCEDURE info_about_route(in p_type text)
BEGIN
    CALL get_info_about_route(p_type, @result);
    SELECT @result;
END //

DELIMITER ;



-- -----------------------------------------------------
-- --------------------- 5 -----------------------------
-- -----------------------------------------------------


drop procedure if exists create_dynamic_tables_from_drivers;
DELIMITER //

CREATE PROCEDURE create_dynamic_tables_from_drivers()
BEGIN
    DECLARE done INT DEFAULT 0;
    DECLARE driver_name VARCHAR(100);
    DECLARE driver_surname VARCHAR(100);
    DECLARE table_counter INT DEFAULT 0;
    DECLARE cur CURSOR FOR SELECT name, surname FROM driver;
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = 1;

    OPEN cur;

    driver_loop: LOOP
        FETCH cur INTO driver_name, driver_surname;
        IF done OR table_counter = 10 THEN
            LEAVE driver_loop;
        END IF;

        -- Generate a unique table name using driver name, surname, and timestamp
        SET driver_name = REPLACE(driver_name, ' ', '_');
        SET driver_surname = REPLACE(driver_surname, ' ', '_');
        SET @table_name = CONCAT(driver_name, '_', driver_surname, '_', UNIX_TIMESTAMP());

        -- Generate a random number of columns between 1 and 9
        SET @num_columns = FLOOR(1 + (RAND() * 9));

        -- Start building the SQL query for table creation
        SET @sql = CONCAT('CREATE TABLE ', @table_name, ' (id INT PRIMARY KEY AUTO_INCREMENT');

        -- Add random columns to the table
        SET @counter = 1;
        WHILE @counter <= @num_columns DO
            SET @sql = CONCAT(@sql, ', column_', @counter, ' VARCHAR(255)');
            SET @counter = @counter + 1;
        END WHILE;

        -- Close the table definition
        SET @sql = CONCAT(@sql, ');');

        -- Execute the dynamic SQL
        PREPARE stmt FROM @sql;
        EXECUTE stmt;
        DEALLOCATE PREPARE stmt;

        -- Increment the table counter
        SET table_counter = table_counter + 1;
    END LOOP;

    CLOSE cur;
END //

DELIMITER ;









-- --------------------------------------------------
-- --------------------- Task 3 ---------------------
-- --------------------------------------------------

DROP TRIGGER IF EXISTS prevent_modification_on_route;
DROP TRIGGER IF EXISTS prevent_delete_on_route;

-- --------------------------------------------------
-- --------------------- 1 --------------------------
-- --------------------------------------------------

DELIMITER //

CREATE TRIGGER prevent_modification_on_route
BEFORE UPDATE ON route
FOR EACH ROW
BEGIN
    SIGNAL SQLSTATE '45000'
    SET MESSAGE_TEXT = 'Modifications are not allowed on route table.';
END //

DELIMITER ;



-- --------------------------------------------------
-- --------------------- 2 --------------------------
-- --------------------------------------------------

DELIMITER //

CREATE TRIGGER prevent_delete_on_route
BEFORE DELETE ON route
FOR EACH ROW
BEGIN
    SIGNAL SQLSTATE '45000'
    SET MESSAGE_TEXT = 'Deletion is not allowed on route table.';
END //

DELIMITER ;


DROP TRIGGER IF EXISTS prevent_invalid_distance_insert;

-- --------------------------------------------------
-- --------------------- 3 --------------------------
-- --------------------------------------------------

DELIMITER //

CREATE TRIGGER prevent_invalid_distance_insert
BEFORE INSERT ON route
FOR EACH ROW
BEGIN
    IF NEW.distance <= 0 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Distance must be greater than zero.';
    END IF;
END //

DELIMITER ;
