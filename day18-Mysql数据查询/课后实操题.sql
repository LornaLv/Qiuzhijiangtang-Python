# 课后实操题
-- 1、查询所有80后学生的姓名、性别和出生日期（筛选）
SELECT sname AS 姓名,if (gender,'男','女') as 性别,birth as 出生日期 from tb_student where birth BETWEEN '1980-01-01' AND '1989-12-31';
SELECT sname AS 姓名,case gender when 1 then '男' else '女' END as 性别,birth as 出生日期 from tb_student where birth BETWEEN '1980-01-01' AND '1989-12-31';

-- 2、查询名字有4个中文字符的学生学号和姓名（运算+函数）
SELECT stuid AS 学号,sname AS 姓名 from tb_student where LENGTH(sname)=12;
SELECT stuid AS 学号,sname AS 姓名 from tb_student where sname like '____';

-- 3、查询名字中有“不”字或“嫣”字的学生的姓名（模糊）
SELECT * FROM tb_student where sname like '%不%' OR sname LIKE '%嫣%';

-- 4、查询学生选课的所有日期（去重）
SELECT DISTINCT seldate as 选课日期 from tb_score;

-- 5、查询男学生的姓名和生日，按年龄从大到小排序（排序）
SELECT sname as 姓名, SUBSTR(birth,6,5) AS 生日,('2023'-SUBSTR(birth,1,4)) AS 年龄 from tb_student where gender=1 ORDER BY birth ;

-- 6、查询每个学生的学号和平均成绩（分组和聚合函数）
SELECT sid as 学号,AVG(mark) as 平均成绩 from tb_score group by sid;

-- 7、查询选了两门以上的课程的学生的姓名（子查询/分组条件/集合运算）
SELECT sname as 姓名 FROM tb_student WHERE stuid IN(SELECT sid as 学号 from tb_score GROUP BY sid HAVING count(sid)=2);

-- 8、查询选课学生的姓名和平均成绩（子查询和连接查询）
SELECT tb_student.sname as 学生姓名,tb_score.sid as 学号,avg(mark) as 平均成绩 FROM tb_score INNER JOIN tb_student on tb_score.sid=tb_student.stuid  GROUP BY sid;

-- 9、查询每个学生的姓名和选课数量（左外连接和子查询）
SELECT tb_student.sname as 学生姓名,tb_score.sid as 学号,count(*) as 选课数量 FROM tb_score INNER JOIN tb_student on tb_score.sid=tb_student.stuid  GROUP BY sid;