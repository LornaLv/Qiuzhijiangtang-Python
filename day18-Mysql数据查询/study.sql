/*
 Navicat MySQL Data Transfer

 Source Server         : localhost_3306
 Source Server Type    : MySQL
 Source Server Version : 80032 (8.0.32-0ubuntu0.20.04.2)
 Source Host           : localhost:3306
 Source Schema         : study

 Target Server Type    : MySQL
 Target Server Version : 80032 (8.0.32-0ubuntu0.20.04.2)
 File Encoding         : 65001

 Date: 21/03/2023 18:39:43
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for class
-- ----------------------------
DROP TABLE IF EXISTS `class`;
CREATE TABLE `class` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `delete` bit(1) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Records of class
-- ----------------------------
BEGIN;
INSERT INTO `class` (`id`, `name`, `delete`) VALUES (1, 'python1', NULL);
INSERT INTO `class` (`id`, `name`, `delete`) VALUES (2, 'python2', NULL);
INSERT INTO `class` (`id`, `name`, `delete`) VALUES (3, 'python3', NULL);
INSERT INTO `class` (`id`, `name`, `delete`) VALUES (4, 'python4', NULL);
COMMIT;

-- ----------------------------
-- Table structure for score
-- ----------------------------
DROP TABLE IF EXISTS `score`;
CREATE TABLE `score` (
  `id` int NOT NULL AUTO_INCREMENT,
  `stu_name` int DEFAULT NULL,
  `sub_name` int DEFAULT NULL,
  `score` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `sub_name` (`sub_name`),
  KEY `stu_name` (`stu_name`) USING BTREE /*!80000 INVISIBLE */,
  CONSTRAINT `stu_name` FOREIGN KEY (`stu_name`) REFERENCES `students` (`id`),
  CONSTRAINT `sub_name` FOREIGN KEY (`sub_name`) REFERENCES `subject` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=37 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Records of score
-- ----------------------------
BEGIN;
INSERT INTO `score` (`id`, `stu_name`, `sub_name`, `score`) VALUES (1, 1, 1, 90);
INSERT INTO `score` (`id`, `stu_name`, `sub_name`, `score`) VALUES (2, 1, 2, 89);
INSERT INTO `score` (`id`, `stu_name`, `sub_name`, `score`) VALUES (3, 1, 3, 85);
INSERT INTO `score` (`id`, `stu_name`, `sub_name`, `score`) VALUES (4, 2, 1, 86);
INSERT INTO `score` (`id`, `stu_name`, `sub_name`, `score`) VALUES (5, 2, 2, 84);
INSERT INTO `score` (`id`, `stu_name`, `sub_name`, `score`) VALUES (6, 2, 3, 89);
INSERT INTO `score` (`id`, `stu_name`, `sub_name`, `score`) VALUES (7, 3, 1, 58);
INSERT INTO `score` (`id`, `stu_name`, `sub_name`, `score`) VALUES (8, 3, 2, 94);
INSERT INTO `score` (`id`, `stu_name`, `sub_name`, `score`) VALUES (9, 3, 3, 67);
INSERT INTO `score` (`id`, `stu_name`, `sub_name`, `score`) VALUES (10, 4, 1, 79);
INSERT INTO `score` (`id`, `stu_name`, `sub_name`, `score`) VALUES (11, 4, 2, 89);
INSERT INTO `score` (`id`, `stu_name`, `sub_name`, `score`) VALUES (12, 4, 3, 81);
INSERT INTO `score` (`id`, `stu_name`, `sub_name`, `score`) VALUES (13, 5, 1, 94);
INSERT INTO `score` (`id`, `stu_name`, `sub_name`, `score`) VALUES (14, 5, 2, 98);
INSERT INTO `score` (`id`, `stu_name`, `sub_name`, `score`) VALUES (15, 5, 3, 79);
INSERT INTO `score` (`id`, `stu_name`, `sub_name`, `score`) VALUES (16, 6, 1, 83);
INSERT INTO `score` (`id`, `stu_name`, `sub_name`, `score`) VALUES (17, 6, 2, 98);
INSERT INTO `score` (`id`, `stu_name`, `sub_name`, `score`) VALUES (18, 6, 3, 69);
INSERT INTO `score` (`id`, `stu_name`, `sub_name`, `score`) VALUES (19, 7, 1, 67);
INSERT INTO `score` (`id`, `stu_name`, `sub_name`, `score`) VALUES (20, 7, 2, 85);
INSERT INTO `score` (`id`, `stu_name`, `sub_name`, `score`) VALUES (21, 7, 3, 84);
INSERT INTO `score` (`id`, `stu_name`, `sub_name`, `score`) VALUES (22, 8, 1, 82);
INSERT INTO `score` (`id`, `stu_name`, `sub_name`, `score`) VALUES (23, 8, 2, 89);
INSERT INTO `score` (`id`, `stu_name`, `sub_name`, `score`) VALUES (24, 8, 3, 79);
INSERT INTO `score` (`id`, `stu_name`, `sub_name`, `score`) VALUES (25, 9, 1, 75);
INSERT INTO `score` (`id`, `stu_name`, `sub_name`, `score`) VALUES (26, 9, 2, 98);
INSERT INTO `score` (`id`, `stu_name`, `sub_name`, `score`) VALUES (27, 9, 3, 95);
INSERT INTO `score` (`id`, `stu_name`, `sub_name`, `score`) VALUES (28, 10, 1, 86);
INSERT INTO `score` (`id`, `stu_name`, `sub_name`, `score`) VALUES (29, 10, 2, 79);
INSERT INTO `score` (`id`, `stu_name`, `sub_name`, `score`) VALUES (30, 10, 3, 71);
INSERT INTO `score` (`id`, `stu_name`, `sub_name`, `score`) VALUES (31, 11, 1, 73);
INSERT INTO `score` (`id`, `stu_name`, `sub_name`, `score`) VALUES (32, 11, 2, 89);
INSERT INTO `score` (`id`, `stu_name`, `sub_name`, `score`) VALUES (33, 11, 3, 59);
INSERT INTO `score` (`id`, `stu_name`, `sub_name`, `score`) VALUES (34, 12, 1, 86);
INSERT INTO `score` (`id`, `stu_name`, `sub_name`, `score`) VALUES (35, 12, 2, 99);
INSERT INTO `score` (`id`, `stu_name`, `sub_name`, `score`) VALUES (36, 12, 3, 67);
COMMIT;

-- ----------------------------
-- Table structure for students
-- ----------------------------
DROP TABLE IF EXISTS `students`;
CREATE TABLE `students` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `gender` bit(1) DEFAULT NULL,
  `hometown` varchar(20) DEFAULT '上海',
  `class_id` int DEFAULT NULL,
  `age` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `class_id` (`class_id`) USING BTREE,
  CONSTRAINT `class_id` FOREIGN KEY (`class_id`) REFERENCES `class` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Records of students
-- ----------------------------
BEGIN;
INSERT INTO `students` (`id`, `name`, `gender`, `hometown`, `class_id`, `age`) VALUES (1, '诸葛亮', b'1', '秦皇岛', 1, 19);
INSERT INTO `students` (`id`, `name`, `gender`, `hometown`, `class_id`, `age`) VALUES (2, '安琪拉', b'0', '秦皇岛', 1, 24);
INSERT INTO `students` (`id`, `name`, `gender`, `hometown`, `class_id`, `age`) VALUES (3, '白起', b'1', '青岛', 1, 19);
INSERT INTO `students` (`id`, `name`, `gender`, `hometown`, `class_id`, `age`) VALUES (4, '不知火舞', b'0', '长沙', 1, 20);
INSERT INTO `students` (`id`, `name`, `gender`, `hometown`, `class_id`, `age`) VALUES (5, '妲己', b'0', '长沙', 1, 19);
INSERT INTO `students` (`id`, `name`, `gender`, `hometown`, `class_id`, `age`) VALUES (6, '狄仁杰', b'1', '长沙', 2, 17);
INSERT INTO `students` (`id`, `name`, `gender`, `hometown`, `class_id`, `age`) VALUES (7, '小乔', b'0', '长沙', 2, 21);
INSERT INTO `students` (`id`, `name`, `gender`, `hometown`, `class_id`, `age`) VALUES (8, '芈月', b'0', '长沙', 2, 17);
INSERT INTO `students` (`id`, `name`, `gender`, `hometown`, `class_id`, `age`) VALUES (9, '李白', b'1', '上海', 2, 17);
INSERT INTO `students` (`id`, `name`, `gender`, `hometown`, `class_id`, `age`) VALUES (10, '吕布', b'1', '北京', 2, 23);
INSERT INTO `students` (`id`, `name`, `gender`, `hometown`, `class_id`, `age`) VALUES (11, '嬴政', b'1', '北京', 3, 18);
INSERT INTO `students` (`id`, `name`, `gender`, `hometown`, `class_id`, `age`) VALUES (12, '王昭君', b'0', '北京', 3, 22);
INSERT INTO `students` (`id`, `name`, `gender`, `hometown`, `class_id`, `age`) VALUES (13, '何炅', b'1', '', 3, 18);
INSERT INTO `students` (`id`, `name`, `gender`, `hometown`, `class_id`, `age`) VALUES (14, '赵信', b'1', '上海', NULL, 18);
COMMIT;

-- ----------------------------
-- Table structure for subject
-- ----------------------------
DROP TABLE IF EXISTS `subject`;
CREATE TABLE `subject` (
  `id` int NOT NULL AUTO_INCREMENT,
  `subject_name` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Records of subject
-- ----------------------------
BEGIN;
INSERT INTO `subject` (`id`, `subject_name`) VALUES (1, '数学');
INSERT INTO `subject` (`id`, `subject_name`) VALUES (2, '语文');
INSERT INTO `subject` (`id`, `subject_name`) VALUES (3, '英语');
COMMIT;

SET FOREIGN_KEY_CHECKS = 1;
