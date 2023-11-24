CREATE DATABASE AgricultureDB;
USE AgricultureDB;
CREATE TABLE CROP (
    cropId INT PRIMARY KEY,
    cropName VARCHAR(255),
    cropType VARCHAR(255),
    maintenanceId INT
);
DESC CROP;
CREATE TABLE MAINTENANCE (
    maintenanceSerialNum INT PRIMARY KEY,
    plantingDate DATE,
    harvestDate DATE
);
DESC MAINTENANCE;
CREATE TABLE MAINTENANCE_FERTILISERS (
    maintenanceSerialNo INT ,
    fertiliserDate DATE, 
    PRIMARY KEY(maintenanceSerialNo, fertiliserDate)
);
DESC MAINTENANCE_FERTILISERS;
CREATE TABLE EQUIPMENT (
    equipmentId INT PRIMARY KEY,
    model VARCHAR(255),
    versionNum VARCHAR(255),
    equipmentCost DECIMAL(10, 2),
    deviceId INT
);
DESC EQUIPMENT;
CREATE TABLE SALES (
    salesId INT PRIMARY KEY,
    buyerId INT,
    pricePerTenKg DECIMAL(10, 2),
    quantity INT,
    cropId INT
);
DESC SALES;
CREATE TABLE LABOURER (
    workId INT,
    labourerId INT PRIMARY KEY,
    fname VARCHAR(255),
    lname VARCHAR(255),
    salaryPerWeek DECIMAL(10, 2),
    labourerContact VARCHAR(20)
);
DESC LABOURER;
DESC MAINTENANCE_FERTILISERS;
DESC CROP;
ALTER TABLE CROP ADD CONSTRAINT maintenanceId FOREIGN KEY (maintenanceId) REFERENCES MAINTENANCE(maintenanceSerialNum);
ALTER TABLE MAINTENANCE_FERTILISERS ADD CONSTRAINT maintenanceSerialNo FOREIGN KEY (maintenanceSerialNo) REFERENCES MAINTENANCE(maintenanceSerialNum);
ALTER TABLE EQUIPMENT ADD CONSTRAINT deviceId FOREIGN KEY (deviceId) REFERENCES CROP(cropId);
ALTER TABLE SALES ADD CONSTRAINT cropId FOREIGN KEY (cropId) REFERENCES CROP(cropId);

INSERT INTO CROP (cropId, cropName, cropType, maintenanceId) VALUES
(1, 'Wheat', 'Grain', 101),
(2, 'Rice', 'Grain', 102),
(3, 'Tomato', 'Vegetable', 103),
(4, 'Apple', 'Fruit', 104),
(5, 'Carrot', 'Vegetable', 105),
(6, 'Corn', 'Grain', 106),
(7, 'Potato', 'Vegetable', 107),
(8, 'Orange', 'Fruit', 108),
(9, 'Lettuce', 'Vegetable', 109),
(10, 'Barley', 'Grain', 110),
(11, 'Cucumber', 'Vegetable', 111),
(12, 'Banana', 'Fruit', 112),
(13, 'Oats', 'Grain', 113),
(14, 'Spinach', 'Vegetable', 114),
(15, 'Grapes', 'Fruit', 115),
(16, 'Soybeans', 'Grain', 116),
(17, 'Broccoli', 'Vegetable', 117),
(18, 'Peach', 'Fruit', 118),
(19, 'Rye', 'Grain', 119),
(20, 'Peas', 'Vegetable', 120);
SELECT * FROM CROP;

INSERT INTO MAINTENANCE (maintenanceSerialNum, plantingDate, harvestDate) VALUES
(101, '2023-01-01', '2023-03-15'),
(102, '2023-02-05', '2023-05-20'),
(103, '2023-03-10', '2023-06-25'),
(104, '2023-04-15', '2023-09-10'),
(105, '2023-05-20', '2023-11-30'),
(106, '2023-06-25', '2023-12-15'),
(107, '2023-07-30', '2024-02-01'),
(108, '2023-09-05', '2024-04-10'),
(109, '2023-10-10', '2024-07-15'),
(110, '2023-11-15', '2024-09-30'),
(111, '2023-12-20', '2025-01-10'),
(112, '2024-02-01', '2025-04-20'),
(113, '2024-03-10', '2025-07-05'),
(114, '2024-04-15', '2025-09-10'),
(115, '2024-05-20', '2025-11-30'),
(116, '2024-06-25', '2026-01-15'),
(117, '2024-07-30', '2026-02-28'),
(118, '2024-09-05', '2026-05-10'),
(119, '2024-10-10', '2026-08-15'),
(120, '2024-11-15', '2026-10-30');
SELECT * FROM MAINTENANCE;

INSERT INTO MAINTENANCE_FERTILISERS (maintenanceSerialNo, fertiliserDate) VALUES
(101, '2023-01-05'),
(102, '2023-02-10'),
(103, '2023-03-15'),
(104, '2023-04-20'),
(105, '2023-05-25'),
(106, '2023-06-30'),
(107, '2023-08-05'),
(108, '2023-09-10'),
(109, '2023-10-15'),
(110, '2023-11-20'),
(111, '2023-12-25'),
(112, '2024-02-05'),
(113, '2024-03-10'),
(114, '2024-04-15'),
(115, '2024-05-20'),
(116, '2024-06-25'),
(117, '2024-07-30'),
(118, '2024-09-05'),
(119, '2024-10-10'),
(120, '2024-11-15');
SELECT * FROM MAINTENANCE;


INSERT INTO EQUIPMENT (equipmentId, model, versionNum, equipmentCost, deviceId) VALUES
(101, 'Excavator', 'V1.0', 50000.00, 1),
(102, 'Tractor', 'V2.5', 75000.00, 2),
(103, 'Harvester', 'V3.2', 100000.00, 3),
(104, 'Plow', 'V1.5', 30000.00, 4),
(105, 'Seeder', 'V1.8', 25000.00, 5),
(106, 'Sprayer', 'V1.2', 35000.00, 6),
(107, 'Combine', 'V2.0', 120000.00, 7),
(108, 'Cultivator', 'V1.3', 28000.00, 8),
(109, 'Harrow', 'V1.1', 22000.00, 9),
(110, 'Transplanter', 'V1.6', 30000.00, 10),
(111, 'Mower', 'V1.4', 26000.00, 11),
(112, 'Digger', 'V1.7', 32000.00, 12),
(113, 'Seeder-Planter', 'V1.9', 27000.00, 13),
(114, 'Fertilizer Spreader', 'V2.2', 38000.00, 14),
(115, 'Baler', 'V2.3', 50000.00, 15),
(116, 'Irrigation System', 'V2.4', 80000.00, 16),
(117, 'Truck', 'V2.6', 90000.00, 17),
(118, 'Loader', 'V2.7', 65000.00, 18),
(119, 'Windrower', 'V2.8', 42000.00, 19),
(120, 'Tiller', 'V2.9', 32000.00, 20);
SELECT * FROM EQUIPMENT;


INSERT INTO SALES (salesId, buyerId, pricePerTenKg, quantity, cropId) VALUES
(201, 201, 15.50, 500, 1),
(202, 202, 20.25, 300, 2),
(203, 203, 12.75, 700, 3),
(204, 204, 18.00, 450, 4),
(205, 205, 14.80, 600, 5),
(206, 206, 16.20, 550, 6),
(207, 207, 19.75, 400, 7),
(208, 208, 14.00, 800, 8),
(209, 209, 17.50, 350, 9),
(210, 210, 22.80, 250, 10),
(211, 211, 13.50, 680, 11),
(212, 212, 20.00, 500, 12),
(213, 213, 15.30, 720, 13),
(214, 214, 18.50, 480, 14),
(215, 215, 16.75, 550, 15),
(216, 216, 14.20, 620, 16),
(217, 217, 21.00, 380, 17),
(218, 218, 17.80, 420, 18),
(219, 219, 19.25, 400, 19),
(220, 220, 15.90, 480, 20);
SELECT * FROM SALES;

INSERT INTO LABOURER (workId, labourerId, fname, lname, salaryPerWeek, labourerContact) VALUES
(1, 1001, 'Ravi', 'Kumar', 500.00, '+91 98765 43210'),
(2, 1002, 'Priya', 'Sharma', 600.00, '+91 87654 32109'),
(3, 1003, 'Amit', 'Patel', 550.00, '+91 76543 21098'),
(4, 1004, 'Neha', 'Singh', 650.00, '+91 65432 10987'),
(5, 1005, 'Deepak', 'Yadav', 700.00, '+91 54321 09876'),
(6, 1006, 'Anjali', 'Gupta', 480.00, '+91 43210 98765'),
(7, 1007, 'Rajesh', 'Verma', 550.00, '+91 32109 87654'),
(8, 1008, 'Sara', 'Malhotra', 620.00, '+91 21098 76543'),
(9, 1009, 'Vikram', 'Rajput', 520.00, '+91 10987 65432'),
(10, 1010, 'Meera', 'Saxena', 600.00, '+91 09876 54321'),
(11, 1011, 'Rahul', 'Joshi', 580.00, '+91 98765 43210'),
(12, 1012, 'Ananya', 'Bansal', 530.00, '+91 87654 32109'),
(13, 1013, 'Aryan', 'Mishra', 670.00, '+91 76543 21098'),
(14, 1014, 'Simran', 'Chauhan', 550.00, '+91 65432 10987'),
(15, 1015, 'Rohan', 'Agarwal', 720.00, '+91 54321 09876'),
(16, 1016, 'Nisha', 'Singhania', 480.00, '+91 43210 98765'),
(17, 1017, 'Rajat', 'Bhatia', 600.00, '+91 32109 87654'),
(18, 1018, 'Pooja', 'Shukla', 540.00, '+91 21098 76543'),
(19, 1019, 'Amitabh', 'Rastogi', 650.00, '+91 10987 65432'),
(20, 1020, 'Shalini', 'Yadav', 700.00, '+91 09876 54321');

SELECT * FROM LABOURER;
#################
SELECT * FROM MAINTENANCE;
SELECT * FROM MAINTENANCE_FERTILISERS;
#display all crops
SELECT * FROM CROP;
select * from sales;

#condition based search
SELECT * FROM CROP WHERE cropType = 'Fruit';

#nested query
SELECT * FROM MAINTENANCE WHERE maintenanceSerialNum IN (
    SELECT maintenanceId FROM CROP WHERE cropType = 'Vegetable'
);

#correlatd query
SELECT c.cropId, c.cropName, c.cropType, m.plantingDate, m.harvestDate
FROM CROP c
JOIN MAINTENANCE m ON c.maintenanceId = m.maintenanceSerialNum;

#aggregated query
SELECT SUM(e.equipmentCost) AS totalEquipmentCost
FROM EQUIPMENT e
JOIN CROP c ON e.deviceId = c.cropId;




DELETE FROM MAINTENANCE_FERTILISERS;
DELETE FROM EQUIPMENT;
DELETE FROM SALES;
DELETE FROM LABOURER;
DELETE FROM CROP;
DELETE FROM MAINTENANCE;

ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'QueSt20$6*ad#4';
FLUSH PRIVILEGES;

SHOW GRANTS FOR 'root'@'localhost';

SELECT user, host, plugin FROM mysql.user WHERE user = 'root';

GRANT SELECT, INSERT, UPDATE, DELETE ON agriculturedb.* TO 'root'@'localhost';
FLUSH PRIVILEGES;
DROP PROCEDURE IF EXISTS CalculateAllTotalSales;

DELIMITER //

CREATE PROCEDURE CalculateTotalSales(IN p_cropId INT)
BEGIN
    DECLARE total_sales DECIMAL(10, 2);

    -- Calculate total sales
    SELECT IFNULL(SUM(pricePerTenKg * quantity), 0) INTO total_sales
    FROM SALES
    WHERE cropId = p_cropId;

    -- Update the totalSales column in the CROP table
    UPDATE CROP
    SET totalSales = total_sales
    WHERE cropId = p_cropId;

    -- Select the total sales for returning (optional)
    SELECT total_sales AS totalSales;
END //

DELIMITER ;




DELIMITER //

CREATE PROCEDURE UpdateMaintenance(
    IN p_maintenance_id INT,
    IN p_planting_date DATE,
    IN p_harvest_date DATE
)
BEGIN
    UPDATE MAINTENANCE
    SET plantingDate = p_planting_date, harvestDate = p_harvest_date
    WHERE maintenanceSerialNum = p_maintenance_id;
END //

DELIMITER ;

DELIMITER //

CREATE PROCEDURE CalculateDaysToHarvest(IN p_cropId INT)
BEGIN
    DECLARE planting_date DATE;
    DECLARE harvest_date DATE;
    DECLARE days_to_harvest INT;

    -- Get the planting date and harvesting date for the given crop
    SELECT plantingDate, harvestDate INTO planting_date, harvest_date
    FROM MAINTENANCE
    WHERE maintenanceSerialNum = (SELECT maintenanceId FROM CROP WHERE cropId = p_cropId);

    -- Calculate the number of days to harvest
    SET days_to_harvest = DATEDIFF(harvest_date, planting_date);

    -- Return the result
    SELECT days_to_harvest AS DaysToHarvest;
END //

DELIMITER ;



CREATE TABLE insert_to_crop_log (
    log_id INT PRIMARY KEY AUTO_INCREMENT,
    crop_id INT,
    crop_name VARCHAR(255),
    crop_type VARCHAR(255),
    maintenance_id INT,
    inserted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

SELECT * FROM insert_to_crop_log;

-- DELIMITER //
-- CREATE TRIGGER before_insert_crop
-- BEFORE INSERT ON CROP
-- FOR EACH ROW
-- BEGIN
--     -- Check if the maintenanceId being inserted exists in the MAINTENANCE table
--     DECLARE maintenance_exists INT;

--     SELECT COUNT(*) INTO maintenance_exists
--     FROM MAINTENANCE
--     WHERE maintenanceSerialNum = NEW.maintenanceId;

--     IF maintenance_exists = 0 THEN
--         SIGNAL SQLSTATE '45000'
--         SET MESSAGE_TEXT = 'Cannot insert crop. Associated maintenance record not found.';
--     END IF;

--     -- Your additional trigger logic goes here
--     -- For example, you can log the inserted data into another table
--     INSERT INTO insert_crop_log (cropId, cropName, cropType, maintenanceId, inserted_at)
--     VALUES (NEW.cropId, NEW.cropName, NEW.cropType, NEW.maintenanceId, NOW());
-- END;
-- //
-- DELIMITER ;


DROP PROCEDURE if exists CalculateTotalSales;
DROP table inserted_crop_log;




CREATE TABLE MAINTENANCE_LOG (
    logId INT PRIMARY KEY AUTO_INCREMENT,
    maintenanceSerialNum INT,
    logTimestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    operation VARCHAR(50)
);

SELECT * FROM MAINTENANCE_LOG;

DELIMITER //
CREATE TRIGGER maintenance_after_update
AFTER UPDATE
ON MAINTENANCE FOR EACH ROW
BEGIN
    INSERT INTO MAINTENANCE_LOG (maintenanceSerialNum, operation)
    VALUES (NEW.maintenanceSerialNum, 'UPDATE');
END;
//
DELIMITER ;


SELECT * FROM MAINTENANCE;
DELETE FROM CROP WHERE cropId = 30;
SELECT * FROM CROP;
SELECT * FROM SALES;

ALTER TABLE CROP DROP COLUMN totalSales;
ALTER TABLE CROP ADD COLUMN totalSales DECIMAL(10, 2);


SHOW TABLES;