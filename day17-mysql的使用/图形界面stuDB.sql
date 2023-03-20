/*
 Navicat MySQL Data Transfer

 Source Server         : localhost_3306
 Source Server Type    : MySQL
 Source Server Version : 80032 (8.0.32-0ubuntu0.20.04.2)
 Source Host           : localhost:3306
 Source Schema         : stuDB

 Target Server Type    : MySQL
 Target Server Version : 80032 (8.0.32-0ubuntu0.20.04.2)
 File Encoding         : 65001

 Date: 20/03/2023 18:51:30
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for course
-- ----------------------------
DROP TABLE IF EXISTS `course`;
CREATE TABLE `course` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Records of course
-- ----------------------------
BEGIN;
COMMIT;

-- ----------------------------
-- Table structure for student
-- ----------------------------
DROP TABLE IF EXISTS `student`;
CREATE TABLE `student` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `gender` bit(1) DEFAULT NULL,
  `address` varchar(100) NOT NULL,
  `hobby` varchar(60) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Records of student
-- ----------------------------
BEGIN;
INSERT INTO `student` (`id`, `name`, `gender`, `address`, `hobby`) VALUES (2, 'lv', b'0', '海南', '篮球');
INSERT INTO `student` (`id`, `name`, `gender`, `address`, `hobby`) VALUES (3, '刘德华', b'0', '中国', '唱歌');
INSERT INTO `student` (`id`, `name`, `gender`, `address`, `hobby`) VALUES (4, '臧', b'0', '北京', '唱歌');
INSERT INTO `student` (`id`, `name`, `gender`, `address`, `hobby`) VALUES (5, '张', b'1', '青岛', '学习');
COMMIT;

SET FOREIGN_KEY_CHECKS = 1;
