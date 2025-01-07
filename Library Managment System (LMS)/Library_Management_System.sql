-- Create Database
CREATE DATABASE LibraryManagement;

-- Use Database
USE LibraryManagement;

-- Create Books Table
CREATE TABLE Books (
    BookID INT AUTO_INCREMENT PRIMARY KEY,
    Title VARCHAR(100),
    Author VARCHAR(100),
    Publisher VARCHAR(100),
    Quantity INT
);

-- Insert Predefined Data into Books Table
INSERT INTO Books (Title, Author, Publisher, Quantity)
VALUES
('Python Basics', 'John Doe', 'TechPress', 10),
('Data Science Essentials', 'Jane Smith', 'DataPub', 8),
('Machine Learning', 'Alan Turing', 'MLPress', 5),
('Artificial Intelligence', 'Eliza Stark', 'AIWorld', 12);

-- Create Members Table
CREATE TABLE Members (
    MemberID INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(100),
    Email VARCHAR(100),
    PhoneNumber VARCHAR(15),
    MembershipDate DATE
);

-- Create Transactions Table
CREATE TABLE Transactions (
    TransactionID INT AUTO_INCREMENT PRIMARY KEY,
    BookID INT,
    MemberID INT,
    IssueDate DATE,
    DueDate DATE,
    ReturnDate DATE,
    Fine DECIMAL(10, 2),
    FOREIGN KEY (BookID) REFERENCES Books(BookID),
    FOREIGN KEY (MemberID) REFERENCES Members(MemberID)
);

-- Trigger to Update Book Quantity on Borrow
DELIMITER $$

CREATE TRIGGER DecreaseBookQuantity 
AFTER INSERT ON Transactions
FOR EACH ROW
BEGIN
    UPDATE Books
    SET Quantity = Quantity - 1
    WHERE BookID = NEW.BookID;
END$$

DELIMITER ;


-- Trigger to Update Book Quantity on Return
DELIMITER $$

CREATE TRIGGER IncreaseBookQuantity 
AFTER UPDATE ON Transactions
FOR EACH ROW
BEGIN
    IF NEW.ReturnDate IS NOT NULL THEN
        UPDATE Books
        SET Quantity = Quantity + 1
        WHERE BookID = NEW.BookID;
    END IF;
END$$

DELIMITER ;


select * from Transactions-- 
-- DELETE FROM Transactions WHERE TransactionID = 8;