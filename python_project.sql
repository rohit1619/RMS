-- phpMyAdmin SQL Dump
-- version 4.8.3
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Oct 04, 2020 at 05:41 AM
-- Server version: 10.1.36-MariaDB
-- PHP Version: 7.2.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `python_project`
--

-- --------------------------------------------------------

--
-- Table structure for table `register_data`
--

CREATE TABLE `register_data` (
  `id` int(11) NOT NULL,
  `f_name` varchar(110) NOT NULL,
  `l_name` varchar(110) NOT NULL,
  `phone` varchar(110) NOT NULL,
  `email` varchar(110) NOT NULL,
  `question` varchar(110) NOT NULL,
  `answer` varchar(110) NOT NULL,
  `password` varchar(110) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `register_data`
--

INSERT INTO `register_data` (`id`, `f_name`, `l_name`, `phone`, `email`, `question`, `answer`, `password`) VALUES
(1, 'rohit', 'mishra', '6207232847', 'rk730mishra@gmail.com', 'Your First Pet', 'matho', '123'),
(2, 'kumar', 'rohit', '8292049019', 'kumar1619ce@gmail.com', 'Your Favirate Book', 'zero to one', '321');

-- --------------------------------------------------------

--
-- Table structure for table `student_data`
--

CREATE TABLE `student_data` (
  `roll` varchar(110) NOT NULL,
  `name` varchar(110) NOT NULL,
  `email` varchar(110) NOT NULL,
  `gender` varchar(110) NOT NULL,
  `phone` varchar(110) NOT NULL,
  `dob` varchar(110) NOT NULL,
  `address` varchar(110) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `student_data`
--

INSERT INTO `student_data` (`roll`, `name`, `email`, `gender`, `phone`, `dob`, `address`) VALUES
('123', 'rohit', 'rk730mish@gmail.com', 'Male', '6207232847', '29/06/2000', 'gaya'),
('16701050003', 'Abhishek yadav', 'jai2help@gmai.com', 'Transgender', '123456', '14/01/2000', 'Ranchi'),
('16701050032', 'rohit kumar', 'rk730mishra@gmail.com', 'Male', '6207232847', '29/06/2000', 'gaya,bihar'),
('16707050027', 'Suman raj', 'sumanpatel@gmail.com', 'Male', '12345980', 'may 2000', 'hazaribag');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `register_data`
--
ALTER TABLE `register_data`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `student_data`
--
ALTER TABLE `student_data`
  ADD PRIMARY KEY (`roll`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `register_data`
--
ALTER TABLE `register_data`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
