/*
 Navicat MySQL Data Transfer

 Source Server         : localhost_3306
 Source Server Type    : MySQL
 Source Server Version : 80032 (8.0.32-0ubuntu0.20.04.2)
 Source Host           : localhost:3306
 Source Schema         : Mydb

 Target Server Type    : MySQL
 Target Server Version : 80032 (8.0.32-0ubuntu0.20.04.2)
 File Encoding         : 65001

 Date: 22/03/2023 11:59:57
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for tb_course
-- ----------------------------
DROP TABLE IF EXISTS `tb_course`;
CREATE TABLE `tb_course` (
  `couid` int NOT NULL COMMENT '课程编号',
  `cname` varchar(50) NOT NULL COMMENT '课程名称',
  `credit` tinyint NOT NULL COMMENT '学分',
  `teaid` int NOT NULL COMMENT '教师工号',
  PRIMARY KEY (`couid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Records of tb_course
-- ----------------------------
BEGIN;
INSERT INTO `tb_course` (`couid`, `cname`, `credit`, `teaid`) VALUES (1, 'python1', 2, 1);
INSERT INTO `tb_course` (`couid`, `cname`, `credit`, `teaid`) VALUES (2, 'python2', 2, 2);
INSERT INTO `tb_course` (`couid`, `cname`, `credit`, `teaid`) VALUES (3, 'python3', 2, 3);
INSERT INTO `tb_course` (`couid`, `cname`, `credit`, `teaid`) VALUES (4, 'java', 2, 1);
COMMIT;

-- ----------------------------
-- Table structure for tb_score
-- ----------------------------
DROP TABLE IF EXISTS `tb_score`;
CREATE TABLE `tb_score` (
  `scid` int NOT NULL AUTO_INCREMENT COMMENT '选课编号',
  `sid` int NOT NULL COMMENT '学号',
  `cid` int NOT NULL COMMENT '课程编号',
  `seldate` date DEFAULT '2021-02-14' COMMENT '选课时间日期',
  `mark` decimal(4,1) DEFAULT NULL COMMENT '考试成绩',
  PRIMARY KEY (`scid`),
  KEY `cid` (`cid`),
  KEY `sid` (`sid`) USING BTREE /*!80000 INVISIBLE */,
  CONSTRAINT `cid` FOREIGN KEY (`cid`) REFERENCES `tb_course` (`couid`),
  CONSTRAINT `sid` FOREIGN KEY (`sid`) REFERENCES `tb_student` (`stuid`)
) ENGINE=InnoDB AUTO_INCREMENT=1013 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Records of tb_score
-- ----------------------------
BEGIN;
INSERT INTO `tb_score` (`scid`, `sid`, `cid`, `seldate`, `mark`) VALUES (1001, 1, 1, '2021-02-14', 99.0);
INSERT INTO `tb_score` (`scid`, `sid`, `cid`, `seldate`, `mark`) VALUES (1002, 2, 1, '2021-02-14', 94.0);
INSERT INTO `tb_score` (`scid`, `sid`, `cid`, `seldate`, `mark`) VALUES (1003, 3, 1, '2021-02-14', 95.0);
INSERT INTO `tb_score` (`scid`, `sid`, `cid`, `seldate`, `mark`) VALUES (1004, 4, 1, '2021-02-14', 93.0);
INSERT INTO `tb_score` (`scid`, `sid`, `cid`, `seldate`, `mark`) VALUES (1005, 5, 2, '2021-02-14', 96.0);
INSERT INTO `tb_score` (`scid`, `sid`, `cid`, `seldate`, `mark`) VALUES (1006, 6, 2, '2021-02-14', 86.0);
INSERT INTO `tb_score` (`scid`, `sid`, `cid`, `seldate`, `mark`) VALUES (1007, 7, 2, '2021-02-14', 91.0);
INSERT INTO `tb_score` (`scid`, `sid`, `cid`, `seldate`, `mark`) VALUES (1008, 8, 2, '2021-02-14', 100.0);
INSERT INTO `tb_score` (`scid`, `sid`, `cid`, `seldate`, `mark`) VALUES (1009, 1, 4, '2021-02-14', 94.0);
INSERT INTO `tb_score` (`scid`, `sid`, `cid`, `seldate`, `mark`) VALUES (1010, 2, 4, '2021-02-14', 85.0);
INSERT INTO `tb_score` (`scid`, `sid`, `cid`, `seldate`, `mark`) VALUES (1011, 3, 4, '2021-02-14', 69.0);
INSERT INTO `tb_score` (`scid`, `sid`, `cid`, `seldate`, `mark`) VALUES (1012, 6, 4, '2021-02-14', 82.0);
COMMIT;

-- ----------------------------
-- Table structure for tb_student
-- ----------------------------
DROP TABLE IF EXISTS `tb_student`;
CREATE TABLE `tb_student` (
  `stuid` int NOT NULL COMMENT '学号',
  `sname` varchar(20) NOT NULL COMMENT '学生姓名',
  `gender` bit(1) DEFAULT b'1' COMMENT '性别',
  `birth` date NOT NULL DEFAULT '1998-05-17' COMMENT '出生日期',
  `addr` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT '上海' COMMENT '籍贯',
  `collid` int NOT NULL DEFAULT '1702' COMMENT '所属学院编号\n',
  PRIMARY KEY (`stuid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Records of tb_student
-- ----------------------------
BEGIN;
INSERT INTO `tb_student` (`stuid`, `sname`, `gender`, `birth`, `addr`, `collid`) VALUES (1, '小刘', b'1', '1978-03-06', '上海', 1701);
INSERT INTO `tb_student` (`stuid`, `sname`, `gender`, `birth`, `addr`, `collid`) VALUES (2, '不知火舞', b'0', '1998-05-30', '上海', 1702);
INSERT INTO `tb_student` (`stuid`, `sname`, `gender`, `birth`, `addr`, `collid`) VALUES (3, '妲己', b'0', '1998-09-18', '上海', 1702);
INSERT INTO `tb_student` (`stuid`, `sname`, `gender`, `birth`, `addr`, `collid`) VALUES (4, '许嫣然', b'0', '1997-05-17', '上海', 1702);
INSERT INTO `tb_student` (`stuid`, `sname`, `gender`, `birth`, `addr`, `collid`) VALUES (5, '唐嫣', b'0', '1999-12-19', '上海', 1702);
INSERT INTO `tb_student` (`stuid`, `sname`, `gender`, `birth`, `addr`, `collid`) VALUES (6, '火树', b'1', '1968-01-11', '上海', 1702);
INSERT INTO `tb_student` (`stuid`, `sname`, `gender`, `birth`, `addr`, `collid`) VALUES (7, '不二同学', b'0', '1966-09-12', '上海', 1702);
INSERT INTO `tb_student` (`stuid`, `sname`, `gender`, `birth`, `addr`, `collid`) VALUES (8, '黄子弘凡', b'1', '2000-03-17', '上海', 1702);
INSERT INTO `tb_student` (`stuid`, `sname`, `gender`, `birth`, `addr`, `collid`) VALUES (9, '石凯弟弟', b'1', '1980-01-01', '上海', 1702);
COMMIT;

SET FOREIGN_KEY_CHECKS = 1;
